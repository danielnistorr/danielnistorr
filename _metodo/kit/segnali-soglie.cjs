// Controlla le soglie del paragrafo 7 di ricerca-caratteri/segnali-ia.md su una pagina.
// uso: node segnali-soglie.cjs <cartella-uscita> <nome> <url o file:///...> [larghezza]
// Legge <nome>-<larghezza>-info.json scritto prima da misura-segnali.cjs (stessa cartella, stesso nome),
// misura sulla pagina i controlli che misura-segnali.cjs non fa, stampa una riga per soglia
// ("OK" o "DA CORREGGERE" con il valore misurato), scrive <nome>-<larghezza>-soglie.json ed esce con 1 se una soglia non passa.
const { createRequire } = require('module');
const r = createRequire('/opt/node-tools/node_modules/');
const { chromium } = r('playwright');
const fs = require('fs');
const path = require('path');
const [,, OUT, NAME, URL, W] = process.argv;
const width = parseInt(W || '1440');

// caratteri da non usare come voce principale (CARATTERI-E-SEGNALI-IA.md, paragrafo b)
const LISTA = ['Inter', 'Inter Tight', 'Roboto', 'Roboto Slab', 'Open Sans', 'Lato', 'Arial', 'Poppins',
  'Montserrat', 'Geist', 'Geist Mono', 'Manrope', 'Cardo', 'Space Grotesk', 'Space Mono', 'Instrument Serif', 'Instrument Sans',
  'Syne', 'Fraunces', 'IBM Plex Sans', 'IBM Plex Sans Condensed', 'IBM Plex Serif', 'IBM Plex Mono', 'JetBrains Mono', 'Fira Code',
  'Bricolage Grotesque', 'Newsreader', 'Playfair Display', 'Playfair', 'Crimson Pro', 'Crimson Text', 'Source Sans 3', 'Source Sans Pro',
  'DM Sans', 'DM Serif Display', 'DM Mono', 'Plus Jakarta Sans', 'Outfit', 'Sora', 'Unbounded', 'Cormorant', 'Cormorant Garamond',
  'Satoshi', 'Clash Display', 'Cabinet Grotesk'].map(s => s.toLowerCase());

(async () => {
  const infoPath = path.join(OUT, `${NAME}-${width}-info.json`);
  if (!fs.existsSync(infoPath)) { console.error('manca ' + infoPath + ': lanciare prima misura-segnali.cjs'); process.exit(2); }
  const info = JSON.parse(fs.readFileSync(infoPath, 'utf8'));
  const opts = {};
  if (process.env.HTTPS_PROXY) opts.args = ['--proxy-server=' + process.env.HTTPS_PROXY.replace('http://', '')];
  const browser = await chromium.launch(opts);
  const ctx = await browser.newContext({ viewport: { width, height: 900 }, locale: 'it-IT' });
  const page = await ctx.newPage();
  try { await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 45000 }); } catch (e) { console.log('goto', e.message.slice(0, 120)); }
  await page.waitForTimeout(3000);
  for (const t of ['Accetta tutti', 'Accetta', 'Accept all', 'Accept', 'OK', 'Accetto']) {
    try { const b = page.getByRole('button', { name: t, exact: true }); if (await b.count()) { await b.first().click({ timeout: 1500 }); await page.waitForTimeout(600); break; } } catch (e) {}
  }
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(H, 16000); y += 700) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(150); }
  await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(800);

  const x = await page.evaluate(() => {
    const vis = el => { const s = getComputedStyle(el); if (s.visibility === 'hidden' || s.display === 'none' || parseFloat(s.opacity) === 0) return false; const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
    const abs = el => { const r = el.getBoundingClientRect(); return { top: r.top + scrollY, bottom: r.bottom + scrollY, left: r.left, right: r.right, w: r.width, h: r.height }; };
    const txt = el => (el.innerText || '').replace(/\s+/g, ' ').trim();
    const isUpper = (el, t) => getComputedStyle(el).textTransform === 'uppercase' || (t.length > 3 && t === t.toUpperCase() && /[A-ZÀ-Ý]/.test(t));
    const heads = [...document.querySelectorAll('h1,h2,h3')].filter(vis);
    // 4. etichette maiuscole subito sopra un titolo (non contano quelle con cifre: date, codici, orari)
    const smalls = [...document.querySelectorAll('body *')].filter(el => {
      if (!vis(el) || el.children.length > 2) return false; const t = txt(el); if (!t || t.length > 70 || t.length < 3) return false;
      const fs = parseFloat(getComputedStyle(el).fontSize); return fs <= 15.5 && isUpper(el, t) && !el.closest('nav,header,footer,button,a');
    });
    const eyebrows = [];
    for (const h of heads) {
      const hr = abs(h);
      const cand = smalls.filter(el => { const r = abs(el); return r.bottom <= hr.top + 4 && hr.top - r.bottom < 100 && r.left < hr.right && r.right > hr.left; });
      const best = cand.sort((a, b) => abs(b).bottom - abs(a).bottom)[0];
      if (best && !/\d/.test(txt(best))) eyebrows.push(txt(best).slice(0, 50) + ' > ' + txt(h).slice(0, 40));
    }
    // 4b. pill o badge arrotondato sopra l'H1
    // 5. titoli in due frasi
    const twoSent = heads.filter(h => /[a-zà-ÿ0-9][.!?]\s+[A-ZÀ-Ý0-9]/.test(txt(h))).map(h => txt(h).slice(0, 80));
    // 7. fasce di fondo a tutta larghezza (solo colore pieno; le foto a tutta larghezza non contano)
    const vw = document.documentElement.clientWidth, PH = document.documentElement.scrollHeight;
    const full = [...document.querySelectorAll('body, body *')].filter(el => { const r = el.getBoundingClientRect(); return r.width >= vw * 0.95 && r.height > 40 && vis(el); });
    const bgOf = el => { const s = getComputedStyle(el); if (s.backgroundImage && s.backgroundImage !== 'none' && s.backgroundImage.includes('url(')) return 'foto'; const c = s.backgroundColor; if (!c || c === 'transparent' || /rgba\(.*,\s*0\)$/.test(c)) return null; return c; };
    const layers = full.map(el => ({ r: abs(el), bg: bgOf(el) })).filter(o => o.bg);
    let base = getComputedStyle(document.body).backgroundColor; if (!base || /rgba\(.*,\s*0\)$/.test(base) || base === 'transparent') base = getComputedStyle(document.documentElement).backgroundColor;
    if (!base || /rgba\(.*,\s*0\)$/.test(base) || base === 'transparent') base = 'rgb(255, 255, 255)';
    const runs = []; const step = 10;
    for (let y = 0; y < PH; y += step) {
      let c = base; for (const o of layers) if (o.r.top <= y && o.r.bottom > y) c = o.bg; // l'ultimo nel DOM vince (il più interno)
      if (runs.length && runs[runs.length - 1].c === c) runs[runs.length - 1].h += step; else runs.push({ c, h: step });
    }
    const bands = runs.filter(r => r.c !== 'foto' && r.h > 200);
    // fasce consecutive dello stesso colore separate da una foto contano una volta sola
    const fasce = []; for (const b of bands) { if (!fasce.length || fasce[fasce.length - 1].c !== b.c) fasce.push(b); }
    // 8. titolo a sinistra e paragrafo a destra
    const ps = [...document.querySelectorAll('p')].filter(p => vis(p) && txt(p).length >= 80);
    const splitHeads = [];
    for (const h of [...document.querySelectorAll('h2')].filter(vis)) {
      const hr = abs(h); if (hr.w > vw * 0.62) continue;
      if (ps.some(p => { const r = abs(p); return r.left >= hr.right - 8 && r.left > hr.left + 200 && r.top < hr.bottom + 40 && r.bottom > hr.top - 10; })) splitHeads.push(txt(h).slice(0, 60));
    }
    // 11. numero grande con etichetta
    const bigNums = [...document.querySelectorAll('body *')].filter(el => {
      if (!vis(el) || el.children.length) return false; const t = txt(el); const fs = parseFloat(getComputedStyle(el).fontSize);
      return fs >= 40 && /^[+~≈]?\s?[\d.,]+\s?(%|\+|mc|mq|m²|kg|t|kn|km|mm|anni)?$/i.test(t);
    }).map(el => txt(el));
    // 13. tabelle in home con più di 4 righe
    const tabs = [...document.querySelectorAll('table')].filter(vis).map(t => t.querySelectorAll('tbody tr, tr').length).filter(n => n > 5); // > 4 righe di dati più l'intestazione
    // 14. didascalie con la fonte delle foto
    const capSel = 'figcaption, [class*="caption"], [class*="didascal"], small';
    const fonteRe = /(foto|immagine|servizio fotografico)[^.]{0,40}(brochure|scheda|booking|catalogo|sito|pdf)|\b(fonte|credits?)\s*:/i;
    const caps = [...new Set([...document.querySelectorAll(capSel), ...[...document.querySelectorAll('p,span,div')].filter(el => !el.children.length)]
      .filter(vis).map(txt).filter(t => t.length < 200 && fonteRe.test(t)))].map(t => t.slice(0, 70));
    // 15. contenuto datato o con nome (fuori dal piede e dalle righe legali)
    let corpo = ''; for (const el of document.querySelectorAll('body *')) { if (!vis(el) || el.closest('footer') || el.children.length) continue; const t = txt(el); if (/©|p\.\s?iva|copyright/i.test(t)) continue; corpo += ' ' + t; }
    const mesi = '(gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre)';
    const dateRe = new RegExp('\\b\\d{1,2}[./]\\d{1,2}[./](\\d{2}|\\d{4})\\b|\\b\\d{1,2}\\s+' + mesi + '(\\s+\\d{4})?\\b|\\b' + mesi + '\\s+(19|20)\\d{2}\\b|\\b(19[5-9]\\d|20[0-3]\\d)\\b', 'gi');
    const datati = [...new Set((corpo.match(dateRe) || []).map(s => s.trim()))].slice(0, 8);
    // 16. divieti controllabili dalla pagina
    const div = [];
    const all = [...document.querySelectorAll('body *')].filter(vis);
    if ((document.body.innerText || '').includes('—')) div.push('trattino lungo nel testo');
    const emojiRe = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/u; if (heads.some(h => emojiRe.test(txt(h)))) div.push('emoji in un titolo');
    let grad = 0, gradTxt = 0, glass = 0, leftBorder = 0, lucide = 0, fade = 0;
    for (const el of all) {
      const s = getComputedStyle(el);
      if (/gradient/.test(s.backgroundImage)) { grad++; if (/text/.test(s.webkitBackgroundClip || s.backgroundClip || '')) gradTxt++; }
      if ((s.backdropFilter && s.backdropFilter !== 'none') || (s.webkitBackdropFilter && s.webkitBackdropFilter !== 'none')) glass++;
      const bl = parseFloat(s.borderLeftWidth), bo = parseFloat(s.borderTopWidth) + parseFloat(s.borderRightWidth) + parseFloat(s.borderBottomWidth);
      if (bl >= 2 && bo === 0 && s.borderLeftStyle !== 'none' && el.getBoundingClientRect().height > 60 && el.getBoundingClientRect().width > 160) leftBorder++;
      if (el.tagName === 'svg' && /lucide/.test(el.getAttribute('class') || '')) lucide++;
      if (/\b(elementor-invisible|animated|fadeIn\w*|aos-init|wow|reveal)\b/.test(el.className && el.className.baseVal === undefined ? el.className : '')) fade++;
    }
    if (gradTxt) div.push(gradTxt + ' testi in gradiente');
    if (grad) div.push(grad + ' fondi in gradiente (controllare: vietato quello viola-blu)');
    if (glass) div.push(glass + ' elementi con backdrop-filter (vetro)');
    if (leftBorder) div.push(leftBorder + ' blocchi con bordo solo a sinistra');
    if (lucide) div.push(lucide + ' icone Lucide');
    if (fade) div.push(fade + ' elementi con animazione di ingresso');
    // hover che cambia opacità: regole :hover con opacity nei fogli leggibili
    let hoverOp = 0; for (const sh of document.styleSheets) { let rules; try { rules = sh.cssRules; } catch (e) { continue; } for (const ru of rules || []) { if (ru.selectorText && /:hover/.test(ru.selectorText) && /(^|;)\s*opacity\s*:/.test(ru.style ? ru.style.cssText : '')) hoverOp++; } }
    if (hoverOp) div.push(hoverOp + ' regole :hover con opacity (bottoni che sbiadiscono)');
    const buzz = (corpo.match(/\b(eccellenz\w*|passion[ei]\w*|a 360|leader\b|know-how|mission\b|innovazion\w*|all'avanguardia|a tutto tondo|unico nel suo genere)/gi) || []);
    if (buzz.length) div.push('parole da brochure: ' + [...new Set(buzz.map(b => b.toLowerCase()))].join(', '));
    const nonSolo = (corpo.match(/non solo [^.]{1,60}? ma\b/gi) || []).length;
    return { eyebrows, twoSent, fasce: fasce.map(f => ({ c: f.c, h: f.h })), splitHeads, bigNums, tabs, caps, datati, div, nonSolo };
  });
  await browser.close();

  // famiglie raggruppate per superfamiglia (prima parola del nome)
  const fams = (info.families || []).filter(([, p]) => p >= 2);
  const gruppi = {}; for (const [f, p] of fams) { const k = f.split(/\s+/)[0].toLowerCase(); gruppi[k] = (gruppi[k] || 0) + p; }
  const nGruppi = Object.keys(gruppi).length;
  const principale = (info.families || [])[0] ? info.families[0][0] : '';
  const famTitoli = [...new Set((info.heads || []).map(h => h.f))];
  const forti = (info.families || []).filter(([, p]) => p >= 10).map(([f]) => f); // una voce che copre almeno il 10 % del testo
  const inLista = [principale, ...famTitoli, ...forti].filter(f => LISTA.includes(String(f).toLowerCase()));
  const r2 = (v) => String(v).replace('.', ',');
  const righe = [];
  const add = (n, nome, ok, valore) => righe.push({ n, nome, ok, valore });
  add(1, 'Area coperta da foto (almeno 35 %)', info.imgPct >= 35, r2(info.imgPct) + ' %');
  add(2, 'Caratteri (una famiglia o superfamiglia, un secondo solo per una funzione, nessuno delle liste)', nGruppi <= 2 && inLista.length === 0,
    fams.map(([f, p]) => `${f} ${r2(p)} %`).join(', ') + (inLista.length ? `; nelle liste: ${[...new Set(inLista)].join(', ')}` : ''));
  add(3, 'Monospazio (0 % in un sito che non vende software)', info.monoPct === 0, r2(info.monoPct) + ' % del testo');
  add(4, 'Etichette maiuscole sopra i titoli (al massimo 1, salvo date o luoghi)', x.eyebrows.length <= 1, x.eyebrows.length + (x.eyebrows.length ? ': ' + x.eyebrows.slice(0, 4).join(' | ') : ''));
  add(5, 'Titoli col punto (al massimo 1), titoli in due frasi e "non solo X ma Y" (nessuno)', info.headsDot <= 1 && x.twoSent.length === 0 && x.nonSolo === 0,
    `${info.headsDot} titoli col punto su ${info.headsN}; ${x.twoSent.length} in due frasi${x.twoSent.length ? ' (' + x.twoSent.slice(0, 2).join(' | ') + ')' : ''}; ${x.nonSolo} "non solo ... ma"`);
  add(6, 'Misure diverse degli H2 (almeno 3)', (info.h2sizes || []).length >= 3, (info.h2sizes || []).length + ' (' + (info.h2sizes || []).join(', ') + ' px)');
  add(7, 'Fasce di fondo a tutta larghezza (al massimo 4)', x.fasce.length <= 4, x.fasce.length + ' fasce di colore pieno più alte di 200 px' + (x.fasce.length ? ' (' + x.fasce.map(f => f.h).join(', ') + ' px)' : ''));
  add(8, 'Titolo a sinistra e paragrafo a destra (al massimo 1 sezione)', x.splitHeads.length <= 1, x.splitHeads.length + (x.splitHeads.length ? ': ' + x.splitHeads.slice(0, 3).join(' | ') : ''));
  add(9, 'Filetti larghi più di 200 px (meno di 30)', info.hairlines < 30, String(info.hairlines));
  add(10, 'Frecce scritte nei link (al massimo 2)', info.arrows <= 2, String(info.arrows));
  add(11, 'Numero grande con etichetta (al massimo 1)', x.bigNums.length <= 1, x.bigNums.length + (x.bigNums.length ? ': ' + x.bigNums.slice(0, 5).join(', ') : ''));
  add(12, 'Numerazioni 01, 02 (solo per una procedura in ordine)', info.numbered <= 2, info.numbered + ' voci numerate' + (info.numbered > 2 ? ' (se sono i passi di una procedura vera, si tengono)' : ''));
  add(13, 'Tabelle in home (nessuna oltre le 4 righe)', x.tabs.length === 0, x.tabs.length ? x.tabs.length + ' tabelle, righe: ' + x.tabs.join(', ') : 'nessuna oltre le 4 righe');
  add(14, 'Didascalie (luogo e anno, mai la fonte delle foto)', x.caps.length === 0, x.caps.length ? x.caps.slice(0, 3).join(' | ') : 'nessuna didascalia con la fonte');
  add(15, 'Contenuto datato o con nome (almeno un elemento)', x.datati.length >= 1, x.datati.length ? 'date trovate: ' + x.datati.join(', ') : 'nessuna data fuori dal piede (i nomi di persona non si misurano: guardare)');
  add(16, 'Divieti del committente controllabili dalla pagina', x.div.length === 0, x.div.length ? x.div.join('; ') : 'nessuno trovato (corsivo serif, tre box con icona e badge: guardare lo screenshot)');
  let falliti = 0;
  console.log(`Soglie del paragrafo 7 (segnali-ia.md), ${NAME} a ${width} px, ${info.height} px di pagina`);
  for (const r of righe) { if (!r.ok) falliti++; console.log(`${String(r.n).padStart(2)}. ${r.ok ? 'OK            ' : 'DA CORREGGERE '} ${r.nome}: ${r.valore}`); }
  console.log(falliti ? `${falliti} soglie su ${righe.length} da correggere` : `tutte le ${righe.length} soglie passano`);
  fs.writeFileSync(path.join(OUT, `${NAME}-${width}-soglie.json`), JSON.stringify({ url: URL, righe, extra: x }, null, 1));
  process.exit(falliti ? 1 : 0);
})();
