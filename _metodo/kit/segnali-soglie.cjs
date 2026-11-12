// Controlla le soglie del paragrafo f di _metodo/CARATTERI-E-SEGNALI-IA.md (paragrafo 7 di ricerca-caratteri/segnali-ia.md).
// uso: node segnali-soglie.cjs <cartella-uscita> <nome> <url o file:///...> [larghezza]
// Legge <nome>-<larghezza>-info.json scritto prima da misura-segnali.cjs (stessa cartella, stesso nome), misura sulla
// pagina i controlli che misura-segnali.cjs non fa e stampa una riga per soglia:
//   OK              la soglia passa;
//   DA CORREGGERE   soglia bloccante non passata (separa i nostri siti dai riferimenti misurati il 6/10/2026);
//   DA GUARDARE     soglia indicativa non passata: anche siti veri la superano; si tiene con una ragione scritta nel LEGGIMI.
// Scrive <nome>-<larghezza>-soglie.json. Esce con 0 se nessuna soglia bloccante fallisce, 1 se almeno una fallisce,
// 2 se la misura manca o la pagina non si è aperta.
const { createRequire } = require('module');
const r = createRequire('/opt/node-tools/node_modules/');
const { chromium } = r('playwright');
const fs = require('fs');
const path = require('path');
const [,, OUT, NAME, URL, W] = process.argv;
const width = parseInt(W || '1440');

// nome di famiglia ripulito: senza pesi, stili, suffissi web, prefissi e codici di next/font
const PAROLE_VIA = new Set(['fallback', 'variable', 'vf', 'web', 'webfont', 'pro', 'std', 'lt', 'regular', 'roman', 'book', 'light', 'thin',
  'hairline', 'extralight', 'ultralight', 'medium', 'semibold', 'demibold', 'bold', 'extrabold', 'ultrabold', 'black', 'heavy', 'italic', 'oblique', 'it']);
const pulisci = f => String(f).toLowerCase().replace(/^_+/, '').replace(/[-_]+/g, ' ').replace(/\s[0-9a-f]{5,8}$/, '')
  .split(/\s+/).filter(p => p && !PAROLE_VIA.has(p) && !/^w\d+$/.test(p) && !/^\d+[a-z]*$/.test(p)).join(' ');
const PREFISSI = new Set(['pp', 'ff', 'gt', 'abc', 'itc', 'tt', 'nb', 'libre', 'noto', 'ibm', 'neue', 'ms', 'sf', 'adobe', 'dm', 'big', 'source', 'instrument', 'space', 'roboto', 'fira', 'pt']);
const gruppo = f => { const p = pulisci(f).split(' '); return PREFISSI.has(p[0]) && p[1] ? p[0] + ' ' + p[1] : p[0]; };

// caratteri da non usare come voce principale (CARATTERI-E-SEGNALI-IA.md, paragrafo b)
const LISTA = new Set(['Inter', 'Inter Tight', 'Roboto', 'Roboto Slab', 'Open Sans', 'Lato', 'Arial', 'Helvetica', 'Poppins', 'Montserrat',
  'Geist', 'Geist Mono', 'Manrope', 'Cardo', 'Figtree', 'Space Grotesk', 'Space Mono', 'Instrument Serif', 'Instrument Sans', 'Syne',
  'Fraunces', 'IBM Plex Sans', 'IBM Plex Sans Condensed', 'IBM Plex Serif', 'IBM Plex Mono', 'JetBrains Mono', 'Fira Code',
  'Bricolage Grotesque', 'Newsreader', 'Playfair Display', 'Playfair', 'Crimson Pro', 'Crimson Text', 'Source Sans 3', 'Source Sans Pro',
  'DM Sans', 'DM Serif Display', 'DM Serif Text', 'DM Mono', 'Plus Jakarta Sans', 'Outfit', 'Sora', 'Unbounded', 'Cormorant', 'Cormorant Garamond',
  'Satoshi', 'Clash Display', 'Cabinet Grotesk', 'Public Sans', 'Work Sans', 'EB Garamond', 'Lora', 'Merriweather', 'Nunito Sans', 'Raleway',
  'Noto Sans', 'Noto Serif', 'Oxanium', 'Be Vietnam Pro', 'Epilogue', 'Lexend', 'Spline Sans'].map(pulisci));

const BANNER = '[id*="cookie" i],[class*="cookie" i],[id*="consent" i],[class*="consent" i],[id*="gdpr" i],[class*="gdpr" i],' +
  '[id*="iubenda" i],[class*="iubenda" i],[id*="cmplz" i],[class*="cmplz" i],[id*="borlabs" i],[class*="borlabs" i],#onetrust-banner-sdk,#CybotCookiebotDialog';

(async () => {
  const infoPath = path.join(OUT, `${NAME}-${width}-info.json`);
  if (!fs.existsSync(infoPath)) { console.error('manca ' + infoPath + ': lanciare prima misura-segnali.cjs'); process.exit(2); }
  const info = JSON.parse(fs.readFileSync(infoPath, 'utf8'));
  if (info.errore) { console.error('misura non riuscita: ' + info.errore); process.exit(2); }
  const opts = {};
  if (process.env.HTTPS_PROXY) opts.args = ['--proxy-server=' + process.env.HTTPS_PROXY.replace('http://', '')];
  const browser = await chromium.launch(opts);
  const ctx = await browser.newContext({ viewport: { width, height: 900 }, locale: 'it-IT' });
  const page = await ctx.newPage();
  try { await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 45000 }); } catch (e) { console.error('la pagina non si apre: ' + e.message.split('\n')[0]); await browser.close(); process.exit(2); }
  await page.waitForTimeout(3000);
  const voci = ['Accetta tutti', 'Accetta', 'Accept all', 'Accept All', 'Alle akzeptieren', 'Accept', 'OK', 'Ok', 'Accetto', 'Allow all', 'Chiudi'];
  let chiuso = false;
  for (const ruolo of ['button', 'link']) {
    for (const t of voci) { try { const b = page.getByRole(ruolo, { name: t, exact: true }); if (await b.count()) { await b.first().click({ timeout: 1500 }); await page.waitForTimeout(600); chiuso = true; break; } } catch (e) {} }
    if (chiuso) break;
  }
  if (!chiuso) for (const t of voci) { try { const b = page.locator(BANNER).locator(`text="${t}"`); if (await b.count()) { await b.first().click({ timeout: 1500 }); await page.waitForTimeout(600); break; } } catch (e) {} }
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(H, 16000); y += 700) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(150); }
  await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(800);

  const x = await page.evaluate((BANNER) => {
    const vw = document.documentElement.clientWidth, PH = document.documentElement.scrollHeight;
    const visto = new Map();
    const vis = el => {
      if (visto.has(el)) return visto.get(el);
      let ok = true;
      for (let a = el; a && a.nodeType === 1; a = a.parentElement) { const s = getComputedStyle(a); if (s.display === 'none' || s.visibility === 'hidden' || parseFloat(s.opacity) === 0) { ok = false; break; } }
      if (ok) { const r = el.getBoundingClientRect(); ok = r.width > 0 && r.height > 0 && r.right > 0 && r.left < vw; }
      visto.set(el, ok); return ok;
    };
    const inBanner = el => { const b = el.closest(BANNER); return !!b && b !== document.body && b !== document.documentElement && b.getBoundingClientRect().height < PH * 0.6; };
    const abs = el => { const r = el.getBoundingClientRect(); return { top: r.top + scrollY, bottom: r.bottom + scrollY, left: r.left, right: r.right, w: r.width, h: r.height }; };
    const txt = el => (el.innerText || '').replace(/\s+/g, ' ').trim();
    const isUpper = (el, t) => getComputedStyle(el).textTransform === 'uppercase' || (t.length > 3 && t === t.toUpperCase() && /[A-ZÀ-Ý]/.test(t));
    const heads = [...document.querySelectorAll('h1,h2,h3')].filter(h => vis(h) && !inBanner(h));
    const tutti = [...document.querySelectorAll('body *')];
    // 4. etichette maiuscole subito sopra un titolo: fuori da menu, testata, piede, link e bottoni, e senza link dentro;
    //    non contano quelle con cifre (date, codici, orari); i luoghi si guardano a occhio
    const smalls = tutti.filter(el => {
      if (el.children.length > 2 || !vis(el) || inBanner(el)) return false; const t = txt(el); if (!t || t.length > 70 || t.length < 3) return false;
      const fs = parseFloat(getComputedStyle(el).fontSize);
      return fs <= 15.5 && isUpper(el, t) && !el.closest('nav,header,footer,button,a') && !el.querySelector('a,button');
    });
    const eyebrows = [];
    for (const h of heads) {
      const hr = abs(h);
      const cand = smalls.filter(el => { const r = abs(el); return r.bottom <= hr.top + 4 && hr.top - r.bottom < 100 && r.left < hr.right && r.right > hr.left; });
      const best = cand.sort((a, b) => abs(b).bottom - abs(a).bottom)[0];
      if (best && !/\d/.test(txt(best))) eyebrows.push(txt(best).slice(0, 50) + ' > ' + txt(h).slice(0, 40));
    }
    // 5. titoli in due frasi
    const twoSent = heads.filter(h => /[a-zà-ÿ0-9][.!?]\s+[A-ZÀ-Ý0-9]/.test(txt(h))).map(h => txt(h).slice(0, 80));
    // 7. fasce di fondo a tutta larghezza (colore pieno quasi opaco; foto e velature non contano)
    const alfa = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return 1; const p = m[1].split(',').map(s => parseFloat(s)); return p.length > 3 ? p[3] : 1; };
    const full = [...document.querySelectorAll('body, body *')].filter(el => { const r = el.getBoundingClientRect(); return r.width >= vw * 0.95 && r.height > 40 && vis(el) && !inBanner(el); });
    const bgOf = el => { const s = getComputedStyle(el); if (s.backgroundImage && s.backgroundImage !== 'none' && s.backgroundImage.includes('url(')) return 'foto'; const c = s.backgroundColor; if (!c || c === 'transparent' || alfa(c) < 0.9) return null; return c; };
    const layers = full.map(el => ({ r: abs(el), bg: bgOf(el) })).filter(o => o.bg);
    let base = getComputedStyle(document.body).backgroundColor; if (!base || alfa(base) < 0.9) base = getComputedStyle(document.documentElement).backgroundColor;
    if (!base || alfa(base) < 0.9) base = 'rgb(255, 255, 255)';
    const runs = []; const step = 10;
    for (let y = 0; y < PH; y += step) {
      let c = base; for (const o of layers) if (o.r.top <= y && o.r.bottom > y) c = o.bg;
      if (runs.length && runs[runs.length - 1].c === c) runs[runs.length - 1].h += step; else runs.push({ c, h: step });
    }
    const bands = runs.filter(r => r.c !== 'foto' && r.h > 200);
    const fasce = []; for (const b of bands) { if (!fasce.length || fasce[fasce.length - 1].c !== b.c) fasce.push(b); }
    // 8. titolo a sinistra e paragrafo a destra
    const ps = [...document.querySelectorAll('p')].filter(p => vis(p) && txt(p).length >= 80);
    const splitHeads = [];
    for (const h of [...document.querySelectorAll('h2')].filter(vis)) {
      const hr = abs(h); if (hr.w > vw * 0.62) continue;
      if (ps.some(p => { const r = abs(p); return r.left >= hr.right - 8 && r.left > hr.left + 200 && r.top < hr.bottom + 40 && r.bottom > hr.top - 10; })) splitHeads.push(txt(h).slice(0, 60));
    }
    // 11. numero grande con etichetta
    const bigNums = tutti.filter(el => {
      if (el.children.length || !vis(el)) return false; const t = txt(el); const fs = parseFloat(getComputedStyle(el).fontSize);
      return fs >= 40 && /^[+~≈]?\s?[\d.,]+\s?(%|\+|mc|mq|m²|m³|kg|t|kn|km|mm|anni)?$/i.test(t);
    }).map(el => txt(el));
    // 13. tabelle visibili con più di 4 righe di dati
    const tabs = [...document.querySelectorAll('table')].filter(vis).map(t => t.querySelectorAll('tbody tr').length || Math.max(0, t.querySelectorAll('tr').length - 1)).filter(n => n > 4);
    // 14. didascalie con la fonte delle foto
    const capSel = 'figcaption, [class*="caption"], [class*="didascal"], small';
    const fonteRe = /(foto|immagine|servizio fotografico)[^.]{0,40}(brochure|scheda|booking|catalogo|sito|pdf)|\b(fonte|credits?)\s*:/i;
    const caps = [...new Set([...document.querySelectorAll(capSel), ...[...document.querySelectorAll('p,span,div')].filter(el => !el.children.length)]
      .filter(el => vis(el) && !inBanner(el)).map(txt).filter(t => t.length < 200 && fonteRe.test(t)))].map(t => t.slice(0, 70));
    // 15. contenuto datato: si leggono i nodi di testo (anche nei paragrafi con link), fuori dal piede, dai banner,
    //     dalle righe legali e dai riferimenti normativi (D.M., D.Lgs., Regolamento UE, UNI EN ...)
    const legale = /©|p\.\s?iva|copyright|privacy|cookie|D\.\s?M\.|D\.\s?Lgs|D\.\s?P\.\s?R|Regolamento|Reg\.\s?\(?(UE|CE)|GDPR|Direttiva|\blegge\b|\bL\.\s?n?\.?\s?\d|UNI\s?EN|\bEN\s?\d{3}|ISO\s?\d/i;
    const mesi = '(gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre)';
    const dateRe = new RegExp('\\b\\d{1,2}[./]\\d{1,2}[./](\\d{2}|\\d{4})\\b|\\b\\d{1,2}\\s+' + mesi + '(\\s+\\d{4})?\\b|\\b' + mesi + '\\s+(19|20)\\d{2}\\b|\\b(18[5-9]\\d|19\\d\\d|20[0-3]\\d)\\b', 'gi');
    const datati = [];
    const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let nd;
    while ((nd = tw.nextNode())) {
      const el = nd.parentElement; if (!el || ['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(el.tagName)) continue;
      const t = nd.textContent.replace(/\s+/g, ' ').trim(); if (!t || legale.test(t)) continue;
      if (el.closest('footer') || inBanner(el) || !vis(el)) continue;
      // via i numeri di telefono (+39 049 ..., 049 718 464) prima di cercare gli anni
      const tt = t.replace(/(\+|\btel\.?|\btelefono)\s*[\d\s./-]{6,}/gi, ' ').replace(/\b\d{2,4}(\s\d{2,4}){2,}\b/g, ' ');
      for (const m of tt.matchAll(dateRe)) { const i = m.index; datati.push(m[0] + ' ("' + tt.slice(Math.max(0, i - 25), i + m[0].length + 10) + '")'); }
    }
    // 16. divieti controllabili dalla pagina
    const div = [], note = [];
    if ((document.body.innerText || '').includes(String.fromCharCode(0x2014))) div.push('trattino lungo nel testo');
    const emojiRe = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/u; if (heads.some(h => emojiRe.test(txt(h)))) div.push('emoji in un titolo');
    // tinta e saturazione dei colori di un gradiente: viola-blu = tinta 220-320 con saturazione sopra 0,3
    const colori = g => (g.match(/rgba?\([^)]+\)/g) || []).map(c => { const p = c.match(/[\d.]+/g).map(Number); const [R, G, B] = p.map(v => v / 255); const mx = Math.max(R, G, B), mn = Math.min(R, G, B), l = (mx + mn) / 2, d = mx - mn; let h = 0; if (d) { h = mx === R ? ((G - B) / d) % 6 : mx === G ? (B - R) / d + 2 : (R - G) / d + 4; h = (h * 60 + 360) % 360; } const s = d ? d / (1 - Math.abs(2 * l - 1)) : 0; return { h, s, l, a: p.length > 3 ? p[3] : 1 }; });
    let gradTxt = 0, gradViola = 0, gradAltri = 0, glass = 0, leftBorder = 0, lucide = 0, fade = 0;
    // animazioni d'ingresso: classi note, attributi data-aos/data-sal e @keyframes che partono da opacità 0
    const kfDaZero = new Set(); let fogliNonLetti = 0;
    const regole = [];
    const raccogli = rules => { for (const ru of rules || []) { if (ru.cssRules && !ru.selectorText && ru.type !== 7) raccogli(ru.cssRules); else regole.push(ru); } };
    for (const sh of document.styleSheets) { let rr; try { rr = sh.cssRules; } catch (e) { fogliNonLetti++; continue; } raccogli(rr); }
    for (const ru of regole) {
      if (ru.type === 7 && ru.cssRules) { for (const k of ru.cssRules) { if (/(^|,\s*)(from|0%)/.test(k.keyText) && k.style.opacity !== '' && parseFloat(k.style.opacity) === 0) kfDaZero.add(ru.name); } }
    }
    for (const el of tutti) {
      if (!vis(el) || inBanner(el)) continue;
      const s = getComputedStyle(el);
      if (/gradient/.test(s.backgroundImage)) {
        if (/text/.test(s.webkitBackgroundClip || s.backgroundClip || '')) gradTxt++;
        else if (colori(s.backgroundImage).some(c => c.a > 0.2 && c.s > 0.3 && c.l > 0.12 && c.l < 0.88 && c.h >= 220 && c.h <= 320)) gradViola++;
        else gradAltri++;
      }
      if ((s.backdropFilter && s.backdropFilter !== 'none') || (s.webkitBackdropFilter && s.webkitBackdropFilter !== 'none')) glass++;
      const bl = parseFloat(s.borderLeftWidth), bo = parseFloat(s.borderTopWidth) + parseFloat(s.borderRightWidth) + parseFloat(s.borderBottomWidth);
      if (bl >= 2 && bo === 0 && s.borderLeftStyle !== 'none' && !['INPUT', 'SELECT', 'TEXTAREA'].includes(el.tagName) && el.getBoundingClientRect().height > 60 && el.getBoundingClientRect().width > 160) leftBorder++;
      if (el.tagName === 'svg' && /lucide/.test(el.getAttribute('class') || '')) lucide++;
      const cls = typeof el.className === 'string' ? el.className : '';
      if (/\b(elementor-invisible|animated|fadeIn\w*|fade-?in\w*|fade-?up|aos-init|aos-animate|wow|reveal|scroll-reveal|sal-animate|in-view|inview)\b/i.test(cls) || el.hasAttribute('data-aos') || el.hasAttribute('data-sal')) fade++;
      else if (s.animationName && s.animationName !== 'none' && s.animationName.split(',').some(n => kfDaZero.has(n.trim()))) fade++;
    }
    if (gradTxt) div.push(gradTxt + ' testi in gradiente');
    if (gradViola) div.push(gradViola + ' gradienti viola-blu');
    if (gradAltri) note.push(gradAltri + ' altri gradienti (velature, sfumature: guardare)');
    if (glass) div.push(glass + ' elementi con backdrop-filter (vetro)');
    if (leftBorder) div.push(leftBorder + ' blocchi con bordo solo a sinistra');
    if (lucide) div.push(lucide + ' icone Lucide');
    if (fade) div.push(fade + ' elementi con animazione di ingresso');
    // hover che sbiadisce: regole :hover con opacità sotto 1 che toccano un link o un bottone visibile
    const hoverOp = [];
    for (const ru of regole) {
      if (!ru.selectorText || !/:hover/.test(ru.selectorText) || !ru.style || ru.style.opacity === "" || !(parseFloat(ru.style.opacity) > 0 && parseFloat(ru.style.opacity) < 1)) continue;
      for (const sel of ru.selectorText.split(',')) {
        if (!/:hover/.test(sel)) continue;
        let bersagli = []; try { bersagli = [...document.querySelectorAll(sel.replace(/:hover/g, '').trim() || '*')]; } catch (e) { continue; }
        if (bersagli.some(el => vis(el) && !inBanner(el) && (el.closest('a,button,[role="button"],input[type="submit"]') || el.querySelector('a,button')))) { hoverOp.push(sel.trim().slice(0, 60)); break; }
      }
    }
    if (hoverOp.length) div.push(hoverOp.length + ' regole :hover con opacità sotto 1 su link o bottoni (' + hoverOp.slice(0, 3).join(' | ') + ')');
    if (fogliNonLetti) note.push(fogliNonLetti + ' fogli di stile di altri domini non letti (hover e animazioni lì dentro non sono controllati)');
    let corpo = ''; for (const el of tutti) { if (el.children.length || el.closest('footer') || !vis(el) || inBanner(el)) continue; corpo += ' ' + txt(el); }
    const buzz = (corpo.match(/\b(eccellenz\w*|passion[ei]\w*|a 360|leader\b|know-how|mission\b|innovazion\w*|all['’]avanguardia|a tutto tondo|unico nel suo genere|soluzion[ei]\b|è importante sottolineare)/gi) || []);
    if (buzz.length) div.push('parole da brochure: ' + [...new Set(buzz.map(b => b.toLowerCase().replace('’', "'")))].join(', '));
    const nonSolo = (corpo.match(/non solo [^.]{1,60}? ma\b/gi) || []).length;
    // 18. titoli neri: sopra 40 px, peso 700 o più, spaziatura da -0,01em in su
    const neri = heads.map(h => { const s = getComputedStyle(h); const fs = parseFloat(s.fontSize); const ls = s.letterSpacing === 'normal' ? 0 : parseFloat(s.letterSpacing) / fs; return { t: txt(h).slice(0, 40), fs, w: parseInt(s.fontWeight), ls }; })
      .filter(h => h.fs > 40 && h.w >= 700 && h.ls > -0.01).map(h => `${h.t} (${Math.round(h.fs)} px, ${h.w})`);
    return { eyebrows, twoSent, fasce: fasce.map(f => ({ c: f.c, h: f.h })), splitHeads, bigNums, tabs, caps, datati: [...new Set(datati)].slice(0, 8), div, note, nonSolo, neri };
  }, BANNER);
  await browser.close();

  const fams = (info.families || []).filter(([, p]) => p >= 2);
  const gruppi = {}; for (const [f, p] of fams) { const k = gruppo(f); gruppi[k] = (gruppi[k] || 0) + p; }
  const nGruppi = Object.keys(gruppi).length;
  const principale = (info.families || [])[0] ? info.families[0][0] : '';
  const famTitoli = [...new Set((info.heads || []).map(h => h.f))];
  const forti = (info.families || []).filter(([, p]) => p >= 10).map(([f]) => f);
  const inLista = [...new Set([principale, ...famTitoli, ...forti].filter(f => LISTA.has(pulisci(f))))];
  const r2 = (v) => String(v).replace('.', ',');
  const righe = [];
  const add = (n, nome, ok, valore, bloccante = true) => righe.push({ n, nome, ok, valore, bloccante });
  add(1, 'Area coperta da foto (almeno 35 %)', info.imgPct >= 35, r2(info.imgPct) + ' %' + (info.iframe ? ` (più ${info.iframe} iframe, mappe o video, non contati)` : ''));
  add(2, 'Nessun carattere delle liste b come testo principale, titoli o 10 % del testo', inLista.length === 0, inLista.length ? 'nelle liste: ' + inLista.join(', ') : 'nessuno');
  add(3, 'Monospazio (0 % in un sito che non vende software)', info.monoPct === 0, r2(info.monoPct) + ' % del testo');
  add(4, 'Etichette maiuscole sopra i titoli (al massimo 1; date, codici e luoghi non contano)', x.eyebrows.length <= 1, x.eyebrows.length + (x.eyebrows.length ? ': ' + x.eyebrows.slice(0, 4).join(' | ') : ''));
  add(5, 'Titoli col punto (al massimo 1), titoli in due frasi e "non solo X ma Y" (nessuno)', info.headsDot <= 1 && x.twoSent.length === 0 && x.nonSolo === 0,
    `${info.headsDot} titoli col punto su ${info.headsN}; ${x.twoSent.length} in due frasi${x.twoSent.length ? ' (' + x.twoSent.slice(0, 2).join(' | ') + ')' : ''}; ${x.nonSolo} "non solo ... ma"`);
  add(6, 'Misure diverse degli H2 (almeno 3)', (info.h2sizes || []).length >= 3, (info.h2sizes || []).length + ' (' + (info.h2sizes || []).join(', ') + ' px)', false);
  add(7, 'Fasce di fondo a tutta larghezza (al massimo 4)', x.fasce.length <= 4, x.fasce.length + ' fasce di colore pieno più alte di 200 px' + (x.fasce.length ? ' (' + x.fasce.map(f => f.h).join(', ') + ' px)' : ''), false);
  add(8, 'Titolo a sinistra e paragrafo a destra (al massimo 1 sezione)', x.splitHeads.length <= 1, x.splitHeads.length + (x.splitHeads.length ? ': ' + x.splitHeads.slice(0, 3).join(' | ') : ''), false);
  add(9, 'Filetti larghi più di 200 px (meno di 30)', info.hairlines < 30, String(info.hairlines));
  add(10, 'Frecce scritte nei link (al massimo 2)', info.arrows <= 2, String(info.arrows) + (info.arrows ? ': ' + (info.frecce || []).slice(0, 5).join(' | ') : ''));
  add(11, 'Numero grande con etichetta (al massimo 1)', x.bigNums.length <= 1, x.bigNums.length + (x.bigNums.length ? ': ' + x.bigNums.slice(0, 5).join(', ') : ''), false);
  add(12, 'Numerazioni 01, 02 (solo per una procedura in ordine)', info.numbered <= 2, info.numbered + ' voci numerate' + (info.numbered > 2 ? ' (se sono i passi di una procedura vera, si tengono)' : ''), false);
  add(13, 'Tabelle in home (nessuna oltre le 4 righe di dati)', x.tabs.length === 0, x.tabs.length ? x.tabs.length + ' tabelle, righe di dati: ' + x.tabs.join(', ') : 'nessuna oltre le 4 righe');
  add(14, 'Didascalie (luogo e anno, mai la fonte delle foto)', x.caps.length === 0, x.caps.length ? x.caps.slice(0, 3).join(' | ') : 'nessuna didascalia con la fonte');
  add(15, 'Contenuto datato o con nome (almeno un elemento)', x.datati.length >= 1, x.datati.length ? 'date trovate: ' + x.datati.slice(0, 4).join(', ') : 'nessuna data fuori dal piede, dai banner e dalle norme (i nomi di persona non si misurano: guardare)', false);
  add(16, 'Divieti del committente controllabili dalla pagina', x.div.length === 0, x.div.length ? x.div.join('; ') : 'nessuno trovato (corsivo serif, tre box con icona e badge: guardare lo screenshot)');
  add(17, 'Famiglie (una o una superfamiglia; una seconda solo con un compito fisso)', nGruppi <= 2, fams.map(([f, p]) => `${f} ${r2(p)} %`).join(', ') + ` (${nGruppi} gruppi)`, false);
  add(18, 'Titoli neri (sopra 40 px in 700-900 con spaziatura da -0,01em in su)', x.neri.length === 0, x.neri.length ? x.neri.slice(0, 3).join(' | ') : 'nessuno', false);
  let bloccate = 0, daGuardare = 0;
  console.log(`Soglie del paragrafo f (CARATTERI-E-SEGNALI-IA.md), ${NAME} a ${width} px, ${info.height} px di pagina`);
  for (const r of righe) {
    const stato = r.ok ? 'OK            ' : (r.bloccante ? 'DA CORREGGERE ' : 'DA GUARDARE   ');
    if (!r.ok) { if (r.bloccante) bloccate++; else daGuardare++; }
    console.log(`${String(r.n).padStart(2)}. ${stato} ${r.nome}: ${r.valore}`);
  }
  for (const n of x.note) console.log('    nota: ' + n);
  console.log(`${bloccate} soglie bloccanti su ${righe.filter(r => r.bloccante).length} da correggere, ${daGuardare} su ${righe.filter(r => !r.bloccante).length} da guardare`);
  fs.writeFileSync(path.join(OUT, `${NAME}-${width}-soglie.json`), JSON.stringify({ url: URL, righe, extra: x }, null, 1));
  process.exit(bloccate ? 1 : 0);
})();
