// Misura i segnali "IA" di una pagina (vedi segnali-ia.md, paragrafo 7).
// uso: node misura-segnali.cjs <cartella-uscita> <nome> <url o file:///...> [larghezza]
// scrive <nome>-<larghezza>-info.json, <nome>-<larghezza>-top.png e <nome>-<larghezza>.png (pagina intera)
// Soglie consigliate (home a 1440): area immagini >= 35 %, mono <= 5 %, etichette maiuscole sopra i titoli <= 1,
// frecce testuali <= 2, titoli col punto <= 1, misure H2 distinte >= 3, filetti < 30.
const { createRequire } = require('module');
const r = createRequire('/opt/node-tools/node_modules/');
const { chromium } = r('playwright');
const fs = require('fs');
const [,, OUT, NAME, URL, W] = process.argv;
const width = parseInt(W || '1440');
(async () => {
  const opts = {};
  if (process.env.HTTPS_PROXY) opts.args = ['--proxy-server=' + process.env.HTTPS_PROXY.replace('http://','')];
  const browser = await chromium.launch(opts);
  const ctx = await browser.newContext({ viewport: { width, height: 900 }, ignoreHTTPSErrors: false, locale: 'it-IT',
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36' });
  const page = await ctx.newPage();
  try { await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 45000 }); } catch (e) { console.log('goto', e.message.slice(0,120)); }
  await page.waitForTimeout(3500);
  // prova a chiudere i banner cookie
  for (const t of ['Accetta tutti','Accetta','Accept all','Accept All','Alle akzeptieren','Akzeptieren','Accept','OK','Accetto','Acepto','Aceptar todas','Aceptar','Tout accepter','Ich stimme zu','Zustimmen','Agree']) {
    try { const b = page.getByRole('button', { name: t, exact: true }); if (await b.count()) { await b.first().click({ timeout: 1500 }); await page.waitForTimeout(800); break; } } catch (e) {}
  }
  await page.screenshot({ path: `${OUT}/${NAME}-${width}-top.png` });
  // scorre per caricare le immagini e far partire le animazioni
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(H, 16000); y += 600) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(250); }
  await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(1200);
  const m = await page.evaluate(() => {
    const vis = el => { const s = getComputedStyle(el); if (s.visibility === 'hidden' || s.display === 'none' || parseFloat(s.opacity) === 0) return false; const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
    const fam = s => s.fontFamily.split(',')[0].replace(/["']/g,'').trim();
    const isMono = f => /mono|code|courier|consol|menlo/i.test(f);
    const leaves = [];
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n; const seen = new Set();
    while ((n = walker.nextNode())) {
      const t = n.textContent.replace(/\s+/g,' ').trim(); if (!t) continue;
      const el = n.parentElement; if (!el || ['SCRIPT','STYLE','NOSCRIPT'].includes(el.tagName)) continue;
      if (!vis(el)) continue;
      if (!seen.has(el)) { seen.add(el); leaves.push(el); }
    }
    const byFam = {}; let tot = 0, mono = 0; const labels = []; let arrows = 0; const styles = {};
    for (const el of leaves) {
      const s = getComputedStyle(el); const f = fam(s);
      const t = Array.from(el.childNodes).filter(c => c.nodeType === 3).map(c => c.textContent).join(' ').replace(/\s+/g,' ').trim();
      const L = t.length; tot += L; byFam[f] = (byFam[f]||0) + L; if (isMono(f)) mono += L;
      arrows += (t.match(/[→↗›»]/g) || []).length;
      const fs_ = parseFloat(s.fontSize); const ls = s.letterSpacing === 'normal' ? 0 : parseFloat(s.letterSpacing) / fs_;
      const upper = s.textTransform === 'uppercase' || (t.length > 3 && t === t.toUpperCase() && /[A-ZÀ-Ý]/.test(t));
      if (upper && fs_ <= 14.5 && L > 2 && L < 70) labels.push({ t: t.slice(0,60), f, fs: fs_, ls: +ls.toFixed(3), mono: isMono(f) });
      const key = `${f}|${s.fontWeight}|${Math.round(fs_)}|${s.fontStyle}|${s.textTransform}`; styles[key] = (styles[key]||0) + L;
    }
    const heads = Array.from(document.querySelectorAll('h1,h2,h3')).filter(vis).map(h => {
      const s = getComputedStyle(h); const t = h.innerText.replace(/\s+/g,' ').trim();
      return { tag: h.tagName, t: t.slice(0,90), f: fam(s), fs: parseFloat(s.fontSize), w: s.fontWeight, it: s.fontStyle === 'italic' || !!h.querySelector('em,i'), up: s.textTransform === 'uppercase', dot: /\.$/.test(t), lines: Math.round(h.getBoundingClientRect().height / (parseFloat(s.lineHeight) || parseFloat(s.fontSize)*1.2)) };
    });
    const numbered = leaves.filter(el => /^(0\d|\d{1,2}\s?\/\s?\d{1,2}|N°\s?\d+)[\s.·\u2014\u2013-]*$/.test(el.textContent.trim()) || /^0\d\s?[·./\u2014\u2013-]\s/.test(el.textContent.trim())).length;
    // filetti: bordi superiori o inferiori sottili e larghi
    let hair = 0; for (const el of document.querySelectorAll('body *')) { const s = getComputedStyle(el); const r = el.getBoundingClientRect(); if (r.width < 200) continue; for (const side of ['Top','Bottom']) { const w = parseFloat(s['border'+side+'Width']); if (w > 0 && w <= 2 && s['border'+side+'Style'] !== 'none') hair++; } }
    // corsivo nei titoli e testo
    const ital = leaves.filter(el => getComputedStyle(el).fontStyle === 'italic').length;
    // area coperta da immagini (griglia a celle da 20 px)
    const PH = document.documentElement.scrollHeight, PW = document.documentElement.clientWidth, cell = 20, cols = Math.ceil(PW / cell), rows = Math.ceil(PH / cell), g = new Uint8Array(cols * rows);
    const mark = r => { const x0 = Math.max(0, Math.floor(r.left / cell)), x1 = Math.min(cols, Math.ceil(r.right / cell)), y0 = Math.max(0, Math.floor((r.top + scrollY) / cell)), y1 = Math.min(rows, Math.ceil((r.bottom + scrollY) / cell)); for (let y = y0; y < y1; y++) for (let x = x0; x < x1; x++) g[y * cols + x] = 1; };
    for (const el of document.querySelectorAll('img,video,picture,canvas,iframe')) { const r = el.getBoundingClientRect(); if (r.width > 120 && r.height > 120) mark(r); }
    for (const el of document.querySelectorAll('body *')) { const s = getComputedStyle(el); if (s.backgroundImage && s.backgroundImage.includes('url(')) { const r = el.getBoundingClientRect(); if (r.width > 120 && r.height > 120) mark(r); } }
    let cov = 0; for (const v of g) cov += v; const imgPct = +(cov / g.length * 100).toFixed(1);
    const h2sizes = [...new Set(heads.filter(h => h.tag === 'H2').map(h => Math.round(h.fs)))];
    const famSorted = Object.entries(byFam).sort((a,b) => b[1]-a[1]).map(([k,v]) => [k, +(v/tot*100).toFixed(1)]);
    const stSorted = Object.entries(styles).sort((a,b) => b[1]-a[1]).slice(0,12).map(([k,v]) => [k, +(v/tot*100).toFixed(1)]);
    return { imgPct, h2sizes, url: location.href, title: document.title, height: document.documentElement.scrollHeight, chars: tot, families: famSorted, monoPct: +(mono/tot*100).toFixed(1), labelsN: labels.length, labelsMono: labels.filter(l=>l.mono).length, labels: labels.slice(0,25), arrows, heads: heads.slice(0,30), headsDot: heads.filter(h=>h.dot).length, headsN: heads.length, headsItalic: heads.filter(h=>h.it).length, headsUpper: heads.filter(h=>h.up).length, numbered, hairlines: hair, italicLeaves: ital, topStyles: stSorted };
  });
  fs.writeFileSync(`${OUT}/${NAME}-${width}-info.json`, JSON.stringify(m, null, 1));
  const full = Math.min(H, 14000);
  await page.setViewportSize({ width, height: 900 });
  try { await page.screenshot({ path: `${OUT}/${NAME}-${width}.png`, fullPage: true, timeout: 60000 }); } catch (e) { console.log('shot', e.message.slice(0,100)); }
  console.log(NAME, 'ok', m.height, 'img%', m.imgPct, 'H2', JSON.stringify(m.h2sizes), 'fam', JSON.stringify(m.families.slice(0,4)), 'mono%', m.monoPct, 'labels', m.labelsN, 'arrows', m.arrows, 'headsDot', m.headsDot + '/' + m.headsN);
  await browser.close();
})();
