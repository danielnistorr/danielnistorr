// Controllo automatico di un sito di prova, Elementor e fallback, a 390/768/1024/1440.
// uso: node controlla.mjs <porta> "<percorso:nome> <percorso:nome> ..."   es. node controlla.mjs 8902 "/:01-home /chi-siamo/:02-chi-siamo"
// Per ogni pagina e larghezza: scorrimento orizzontale, immagini rotte o non caricate, elementi che escono a destra,
// link interni che puntano a pagine inesistenti, testi con trattino lungo. Esce con codice 1 se trova problemi.
import { createRequire } from 'module';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const [porta, elenco] = process.argv.slice(2);
const coppie = elenco.trim().split(/\s+/).map(c => c.split(':'));
const browser = await chromium.launch();
const problemi = [];
const percorsi = new Set(coppie.map(c => c[0]));
for (const [pth, nome] of coppie) {
  for (const [tipo, url] of [['el', `http://127.0.0.1:${porta}${pth}`], ['ht', `http://127.0.0.1:${porta}/anteprima/${nome}.html`]]) {
    for (const w of [390, 768, 1024, 1440]) {
      const ctx = await browser.newContext({ viewport: { width: w, height: 900 }, isMobile: w < 1024, hasTouch: w < 1024 });
      const page = await ctx.newPage();
      const r = await page.goto(url, { waitUntil: 'networkidle', timeout: 90000 }).catch(e => null);
      if (!r || r.status() >= 400) { problemi.push(`${tipo} ${nome} @${w}: risposta ${r ? r.status() : 'nessuna'}`); await ctx.close(); continue; }
      await page.evaluate(() => document.querySelectorAll('img[loading=lazy]').forEach(i => { i.loading = 'eager'; }));
      await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } window.scrollTo(0, 0); });
      await page.waitForTimeout(800);
      const d = await page.evaluate((w) => {
        const out = [];
        const sw = document.documentElement.scrollWidth;
        if (sw > innerWidth) out.push(`scorrimento orizzontale ${sw} > ${innerWidth}`);
        for (const i of document.images) {
          if (i.offsetParent === null) continue;
          if (!i.complete || i.naturalWidth === 0) out.push(`immagine non caricata ${i.currentSrc || i.src}`);
          else if (/placeholder/.test(i.currentSrc)) out.push(`immagine segnaposto ${i.currentSrc}`);
          else {
            const r = i.getBoundingClientRect();
            const fit = getComputedStyle(i).objectFit;
            // ingrandita oltre la risoluzione nativa (con tolleranza del 10%) a densità 1
            if (fit !== 'contain' && r.width > i.naturalWidth * 1.1) out.push(`immagine ingrandita ${Math.round(r.width)}px da ${i.naturalWidth}px: ${i.currentSrc.split('/').pop()}`);
          }
        }
        for (const e of document.querySelectorAll('body *')) {
          const cs = getComputedStyle(e);
          if (cs.position === 'fixed' || e.closest('[style*="overflow"], .bv-track') ) continue;
          const r = e.getBoundingClientRect();
          if (r.width && r.right > innerWidth + 1 && !e.closest('details:not([open])')) {
            let p = e.parentElement, clip = false;
            while (p) { const o = getComputedStyle(p); if (/(hidden|clip|auto|scroll)/.test(o.overflowX)) { clip = true; break; } p = p.parentElement; }
            if (!clip) { out.push(`esce a destra: <${e.tagName.toLowerCase()} class="${(e.className && e.className.baseVal === undefined ? e.className : '').toString().slice(0, 60)}"> right=${Math.round(r.right)}`); }
          }
        }
        if (document.body.innerText.includes('—')) out.push('trattino lungo nel testo');
        const interni = [...document.querySelectorAll('a[href^="/"]')].map(a => a.getAttribute('href').split('#')[0]);
        return { out: [...new Set(out)].slice(0, 12), interni: [...new Set(interni)] };
      }, w);
      d.out.forEach(x => problemi.push(`${tipo} ${nome} @${w}: ${x}`));
      if (tipo === 'el' && w === 1440) d.interni.filter(h => h && !percorsi.has(h) && !/^\/(privacy|cookie)/.test(h) && !/^\/wp-/.test(h)).forEach(h => problemi.push(`${tipo} ${nome}: link interno a ${h} (pagina non nell'elenco)`));
      await ctx.close();
    }
  }
}
await browser.close();
console.log(problemi.length ? problemi.join('\n') : 'nessun problema: ' + coppie.length + ' pagine x 2 build x 4 larghezze');
process.exit(problemi.length ? 1 : 0);
