// Misura i segnali "IA" di una pagina (vedi segnali-ia.md, paragrafo 7, e CARATTERI-E-SEGNALI-IA.md, paragrafo f).
// uso: node misura-segnali.cjs <cartella-uscita> <nome> <url o file:///...> [larghezza]
// scrive <nome>-<larghezza>-info.json, <nome>-<larghezza>-top.png e <nome>-<larghezza>.png (pagina intera)
// Esce con 2 (e scrive "errore" nel json) se la pagina non si apre, risponde con un errore o non ha testo.
// Soglie (home a 1440): area foto >= 35 %, mono 0 %, etichette maiuscole sopra i titoli <= 1, frecce <= 2,
// titoli col punto <= 1, filetti < 30. Le controlla segnali-soglie.cjs.
//
// Versione 2 (revisione del 6/10/2026), diversa dalla copia in ricerca-caratteri/ usata per le misure della ricerca:
// - testo, etichette, filetti e foto contano solo se visibili (anche gli antenati) e dentro la finestra in orizzontale:
//   i pannelli fuori schermo (menu, accesso) non contano;
// - il testo dei banner dei cookie non entra nelle quote dei caratteri; il banner si chiude anche con link o testo "OK";
// - i campi dei moduli (input, select, textarea, button) non contano come filetti;
// - frecce: le virgolette « » e le briciole di pane non contano; » e › contano solo dentro un link o un bottone;
// - area foto: niente iframe (mappe), niente immagini trasparenti o nascoste;
// - per i titoli si registra anche la spaziatura (per la soglia sul peso).
const { createRequire } = require('module');
const r = createRequire('/opt/node-tools/node_modules/');
const { chromium } = r('playwright');
const fs = require('fs');
const [,, OUT, NAME, URL, W] = process.argv;
const width = parseInt(W || '1440');
const BANNER = '[id*="cookie" i],[class*="cookie" i],[id*="consent" i],[class*="consent" i],[id*="gdpr" i],[class*="gdpr" i],' +
  '[id*="iubenda" i],[class*="iubenda" i],[id*="cmplz" i],[class*="cmplz" i],[id*="borlabs" i],[class*="borlabs" i],#onetrust-banner-sdk,#CybotCookiebotDialog';
const fallisci = (msg) => {
  fs.writeFileSync(`${OUT}/${NAME}-${width}-info.json`, JSON.stringify({ errore: msg, url: URL }, null, 1));
  console.log(NAME, 'ERRORE', msg);
  process.exit(2);
};
(async () => {
  const opts = {};
  if (process.env.HTTPS_PROXY) opts.args = ['--proxy-server=' + process.env.HTTPS_PROXY.replace('http://', '')];
  const browser = await chromium.launch(opts);
  const ctx = await browser.newContext({ viewport: { width, height: 900 }, ignoreHTTPSErrors: false, locale: 'it-IT',
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36' });
  const page = await ctx.newPage();
  let resp = null;
  try { resp = await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 45000 }); } catch (e) { await browser.close(); fallisci('la pagina non si apre: ' + e.message.split('\n')[0].slice(0, 120)); }
  if (resp && resp.status() >= 400) { await browser.close(); fallisci('la pagina risponde ' + resp.status()); }
  if (/^chrome-error:/.test(page.url())) { await browser.close(); fallisci('pagina di errore del browser'); }
  await page.waitForTimeout(3500);
  // prova a chiudere i banner dei cookie: bottoni, link, poi qualunque elemento con quel testo dentro un banner
  const voci = ['Accetta tutti', 'Accetta', 'Accept all', 'Accept All', 'Alle akzeptieren', 'Akzeptieren', 'Accept', 'OK', 'Ok', 'Accetto',
    'Acepto', 'Aceptar todas', 'Aceptar', 'Tout accepter', 'Ich stimme zu', 'Zustimmen', 'Agree', 'Allow all', 'Chiudi'];
  let chiuso = false;
  for (const ruolo of ['button', 'link']) {
    for (const t of voci) {
      try { const b = page.getByRole(ruolo, { name: t, exact: true }); if (await b.count()) { await b.first().click({ timeout: 1500 }); await page.waitForTimeout(800); chiuso = true; break; } } catch (e) {}
    }
    if (chiuso) break;
  }
  if (!chiuso) {
    for (const t of voci) {
      try { const b = page.locator(BANNER).locator(`text="${t}"`); if (await b.count()) { await b.first().click({ timeout: 1500 }); await page.waitForTimeout(800); break; } } catch (e) {}
    }
  }
  await page.screenshot({ path: `${OUT}/${NAME}-${width}-top.png` });
  // scorre per caricare le immagini e far partire le animazioni
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(H, 16000); y += 600) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(250); }
  await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(1200);
  const m = await page.evaluate((BANNER) => {
    const vw = document.documentElement.clientWidth;
    const PH = document.documentElement.scrollHeight;
    // visibile: né l'elemento né un antenato nascosto o trasparente, e dentro la finestra in orizzontale
    const visto = new Map();
    const visCatena = el => {
      if (visto.has(el)) return visto.get(el);
      let ok = true;
      for (let a = el; a && a.nodeType === 1; a = a.parentElement) {
        const s = getComputedStyle(a);
        if (s.display === 'none' || s.visibility === 'hidden' || parseFloat(s.opacity) === 0) { ok = false; break; }
      }
      if (ok) { const r = el.getBoundingClientRect(); ok = r.width > 0 && r.height > 0 && r.right > 0 && r.left < vw; }
      visto.set(el, ok); return ok;
    };
    const inBanner = el => { const b = el.closest(BANNER); return !!b && b !== document.body && b !== document.documentElement && b.getBoundingClientRect().height < PH * 0.6; };
    const fam = s => s.fontFamily.split(',')[0].replace(/["']/g, '').trim();
    const isMono = f => /mono|code|courier|consol|menlo/i.test(f);
    const leaves = [];
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n; const seen = new Set();
    while ((n = walker.nextNode())) {
      const t = n.textContent.replace(/\s+/g, ' ').trim(); if (!t) continue;
      const el = n.parentElement; if (!el || ['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(el.tagName)) continue;
      if (!visCatena(el) || inBanner(el)) continue;
      if (!seen.has(el)) { seen.add(el); leaves.push(el); }
    }
    const byFam = {}; let tot = 0, mono = 0; const labels = []; let arrows = 0; const frecce = []; const styles = {};
    for (const el of leaves) {
      const s = getComputedStyle(el); const f = fam(s);
      const t = Array.from(el.childNodes).filter(c => c.nodeType === 3).map(c => c.textContent).join(' ').replace(/\s+/g, ' ').trim();
      const L = t.length; tot += L; byFam[f] = (byFam[f] || 0) + L; if (isMono(f)) mono += L;
      // frecce: sempre → ↗ ↘ ⟶ ➔ ➜ ⇢; » e › solo dentro un link o un bottone, mai nelle virgolette «» né nelle briciole di pane
      let k = (t.match(/[→↗↘⟶➔➜⇢]/g) || []).length;
      if (!el.closest('[class*="breadcrumb" i],[aria-label*="bread" i],[id*="breadcrumb" i]') && el.closest('a,button,[role="button"]') && !t.includes('«')) k += (t.match(/[›»]/g) || []).length;
      if (k) { arrows += k; frecce.push(t.slice(0, 40)); }
      const fs_ = parseFloat(s.fontSize); const ls = s.letterSpacing === 'normal' ? 0 : parseFloat(s.letterSpacing) / fs_;
      const upper = s.textTransform === 'uppercase' || (t.length > 3 && t === t.toUpperCase() && /[A-ZÀ-Ý]/.test(t));
      if (upper && fs_ <= 14.5 && L > 2 && L < 70) labels.push({ t: t.slice(0, 60), f, fs: fs_, ls: +ls.toFixed(3), mono: isMono(f) });
      const key = `${f}|${s.fontWeight}|${Math.round(fs_)}|${s.fontStyle}|${s.textTransform}`; styles[key] = (styles[key] || 0) + L;
    }
    const heads = Array.from(document.querySelectorAll('h1,h2,h3')).filter(h => visCatena(h) && !inBanner(h)).map(h => {
      const s = getComputedStyle(h); const t = h.innerText.replace(/\s+/g, ' ').trim(); const fs_ = parseFloat(s.fontSize);
      return { tag: h.tagName, t: t.slice(0, 90), f: fam(s), fs: fs_, w: s.fontWeight, ls: s.letterSpacing === 'normal' ? 0 : +(parseFloat(s.letterSpacing) / fs_).toFixed(3),
        it: s.fontStyle === 'italic' || !!h.querySelector('em,i'), up: s.textTransform === 'uppercase', dot: /\.$/.test(t),
        lines: Math.round(h.getBoundingClientRect().height / (parseFloat(s.lineHeight) || fs_ * 1.2)) };
    });
    const numbered = leaves.filter(el => /^(0\d|\d{1,2}\s?\/\s?\d{1,2}|N°\s?\d+)[\s.·\u2014\u2013-]*$/.test(el.textContent.trim()) || /^0\d\s?[·./\u2014\u2013-]\s/.test(el.textContent.trim())).length;
    // filetti: bordi superiori o inferiori sottili su elementi larghi, visibili, nella finestra, fuori dai campi dei moduli
    let hair = 0;
    for (const el of document.querySelectorAll('body *')) {
      if (['INPUT', 'SELECT', 'TEXTAREA', 'BUTTON', 'OPTION'].includes(el.tagName)) continue;
      const s = getComputedStyle(el); const r = el.getBoundingClientRect(); if (r.width < 200) continue;
      let lati = 0; for (const side of ['Top', 'Bottom']) { const w = parseFloat(s['border' + side + 'Width']); if (w > 0 && w <= 2 && s['border' + side + 'Style'] !== 'none') lati++; }
      if (lati && visCatena(el) && !inBanner(el)) hair += lati;
    }
    const ital = leaves.filter(el => getComputedStyle(el).fontStyle === 'italic').length;
    // area coperta da immagini (griglia a celle da 20 px): img, video, canvas e sfondi con immagine; niente iframe
    const PW = vw, cell = 20, cols = Math.ceil(PW / cell), rows = Math.ceil(PH / cell), g = new Uint8Array(cols * rows);
    const mark = r => { const x0 = Math.max(0, Math.floor(r.left / cell)), x1 = Math.min(cols, Math.ceil(r.right / cell)), y0 = Math.max(0, Math.floor((r.top + scrollY) / cell)), y1 = Math.min(rows, Math.ceil((r.bottom + scrollY) / cell)); for (let y = y0; y < y1; y++) for (let x = x0; x < x1; x++) g[y * cols + x] = 1; };
    let mappe = 0;
    for (const el of document.querySelectorAll('iframe')) { const r = el.getBoundingClientRect(); if (r.width > 120 && r.height > 120 && visCatena(el)) mappe++; }
    for (const el of document.querySelectorAll('img,video,canvas')) { const r = el.getBoundingClientRect(); if (r.width > 120 && r.height > 120 && visCatena(el) && !inBanner(el)) mark(r); }
    for (const el of document.querySelectorAll('body *')) { const s = getComputedStyle(el); if (s.backgroundImage && s.backgroundImage.includes('url(')) { const r = el.getBoundingClientRect(); if (r.width > 120 && r.height > 120 && visCatena(el)) mark(r); } }
    let cov = 0; for (const v of g) cov += v; const imgPct = +(cov / g.length * 100).toFixed(1);
    const h2sizes = [...new Set(heads.filter(h => h.tag === 'H2').map(h => Math.round(h.fs)))];
    const famSorted = Object.entries(byFam).sort((a, b) => b[1] - a[1]).map(([k, v]) => [k, +(v / tot * 100).toFixed(1)]);
    const stSorted = Object.entries(styles).sort((a, b) => b[1] - a[1]).slice(0, 12).map(([k, v]) => [k, +(v / tot * 100).toFixed(1)]);
    return { imgPct, iframe: mappe, h2sizes, url: location.href, title: document.title, height: PH, chars: tot, families: famSorted,
      monoPct: tot ? +(mono / tot * 100).toFixed(1) : null, labelsN: labels.length, labelsMono: labels.filter(l => l.mono).length, labels: labels.slice(0, 25),
      arrows, frecce: frecce.slice(0, 15), heads: heads.slice(0, 40), headsDot: heads.filter(h => h.dot).length, headsN: heads.length,
      headsItalic: heads.filter(h => h.it).length, headsUpper: heads.filter(h => h.up).length, numbered, hairlines: hair, italicLeaves: ital, topStyles: stSorted };
  }, BANNER);
  if (!m.chars) { await browser.close(); fallisci('nessun testo visibile nella pagina'); }
  fs.writeFileSync(`${OUT}/${NAME}-${width}-info.json`, JSON.stringify(m, null, 1));
  await page.setViewportSize({ width, height: 900 });
  try { await page.screenshot({ path: `${OUT}/${NAME}-${width}.png`, fullPage: true, timeout: 60000 }); } catch (e) { console.log('shot', e.message.slice(0, 100)); }
  console.log(NAME, 'ok', m.height, 'img%', m.imgPct, 'H2', JSON.stringify(m.h2sizes), 'fam', JSON.stringify(m.families.slice(0, 4)), 'mono%', m.monoPct, 'labels', m.labelsN, 'arrows', m.arrows, 'headsDot', m.headsDot + '/' + m.headsN, 'filetti', m.hairlines);
  await browser.close();
})();
