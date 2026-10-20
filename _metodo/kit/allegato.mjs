// uso: node allegato.mjs <spec.json> <cartella-uscita> [--mittente "Nome Cognome · telefono · email"]
// Crea il PDF da allegare alla mail: A4 orizzontale, tre pagine.
//   1. la prima schermata della home a tutta pagina, con nome e frase sotto
//   2. due schermate da telefono e tre punti "cosa cambia"
//   3. due sezioni della home da computer e il prossimo passo
// Le immagini si scattano adesso dalla pagina statica (<cartella>/sito/index.html) a densità 2 e 3,
// così il PDF resta nitido anche stampato. Accanto al PDF scrive pagine-<n>.png per guardarlo.
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
import { execFileSync } from 'child_process';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');

const argv = process.argv.slice(2);
const specPath = argv[0], outDir = argv[1] && path.resolve(argv[1]);
const mi = argv.indexOf('--mittente');
const mittente = mi > -1 ? argv[mi + 1] : '';
if (!specPath || !outDir) { console.error('uso: node allegato.mjs <spec.json> <cartella-uscita> [--mittente "..."]'); process.exit(1); }
const S = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const REPO = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const sito = path.join(REPO, S.cartella, 'sito', 'index.html');
if (!fs.existsSync(sito)) { console.error('manca ' + sito); process.exit(1); }
const work = path.join(outDir, '_lavoro');
fs.mkdirSync(work, { recursive: true });

const browser = await chromium.launch();

async function apri(ctxOpts) {
  const ctx = await browser.newContext(ctxOpts);
  const page = await ctx.newPage();
  await page.goto('file://' + sito, { waitUntil: 'load', timeout: 90000 });
  await page.evaluate(() => document.querySelectorAll('img[loading=lazy],iframe[loading=lazy]').forEach(e => { e.loading = 'eager'; }));
  await page.evaluate(async () => {
    for (let y = 0; y < document.documentElement.scrollHeight; y += 500) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); }
    window.scrollTo(0, 0);
  });
  await page.waitForFunction(() => [...document.images].filter(i => i.offsetParent !== null).every(i => i.complete && i.naturalWidth > 0), null, { timeout: 20000 }).catch(() => console.log('avviso: immagini non tutte caricate'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  return { ctx, page };
}

// computer: prima schermata e sezioni
{
  const { ctx, page } = await apri({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
  await page.screenshot({ path: path.join(work, 'copertina.jpg'), type: 'jpeg', quality: 80 });
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  for (const [i, s] of S.sezioni.entries()) {
    const y0 = Math.max(0, s.y0), y1 = Math.min(H, s.y1);
    await page.screenshot({ path: path.join(work, `sezione-${i + 1}.jpg`), type: 'jpeg', quality: 78, fullPage: true, clip: { x: 0, y: y0, width: 1440, height: y1 - y0 } });
  }
  await ctx.close();
}
// telefono: prima schermata e una seconda più in basso
{
  const { ctx, page } = await apri({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true });
  await page.screenshot({ path: path.join(work, 'telefono-1.jpg'), type: 'jpeg', quality: 80 });
  await page.evaluate(y => window.scrollTo(0, y), S.telefono2_y);
  await page.waitForTimeout(600);
  await page.screenshot({ path: path.join(work, 'telefono-2.jpg'), type: 'jpeg', quality: 80 });
  await ctx.close();
}

const esc = t => String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const font = path.join(REPO, '3Esse-Sito/assets/fonts/switzer');
// sezioni: altezza in mm a 180 mm di larghezza; se insieme superano lo spazio, si stringono
const altezze = S.sezioni.map(s => (Math.min(s.y1, 1e9) - s.y0) * 180 / 1440);
const spazio = 210 - 32 - S.sezioni.length * 9;
const scala = Math.min(1, spazio / altezze.reduce((a, b) => a + b, 0));
const larg = (180 * scala).toFixed(1);

const html = `<!doctype html><html lang="it"><head><meta charset="utf-8"><title>${esc(S.azienda)}: la nuova home</title>
<style>
@font-face{font-family:Sw;src:url("file://${font}/switzer-300.woff2") format("woff2");font-weight:300}
@font-face{font-family:Sw;src:url("file://${font}/switzer-400.woff2") format("woff2");font-weight:400}
@font-face{font-family:Sw;src:url("file://${font}/switzer-500.woff2") format("woff2");font-weight:500}
@page{size:297mm 210mm;margin:0}
:root{--fondo:#f3f1ec;--ink:#151515;--muto:#67645e;--filo:#d6d2c8}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--fondo);color:var(--ink);font-family:Sw,sans-serif;text-rendering:geometricPrecision;font-kerning:normal;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.p{width:297mm;height:210mm;position:relative;overflow:hidden;page-break-after:always;background:var(--fondo)}
.p:last-child{page-break-after:auto}
.n{position:absolute;right:16mm;bottom:9mm;font-size:7.5pt;color:var(--muto);letter-spacing:.02em}
/* 1 */
.cop img{display:block;width:297mm;height:185.625mm;object-fit:cover;object-position:top}
.cop .strip{position:absolute;left:16mm;right:16mm;bottom:0;height:24.375mm;display:flex;align-items:center;justify-content:space-between;gap:20mm}
.cop .chi{font-size:14pt;font-weight:500;letter-spacing:-.01em;line-height:1.15;white-space:nowrap}
.cop .chi span{display:block;font-size:8.5pt;font-weight:400;color:var(--muto);letter-spacing:0;margin-top:1.2mm}
.cop .frase{font-size:10pt;line-height:1.4;max-width:150mm;text-align:right;color:var(--ink)}
/* 2 */
.tel{display:flex;gap:16mm;padding:16mm 16mm 0}
.tel .fon{display:flex;gap:7mm;flex:none}
.tel .fon img{display:block;height:162mm;width:auto;border-radius:5.5mm;border:.3mm solid var(--filo)}
.tel .testo{flex:1;padding-top:2mm}
h2{font-size:22pt;font-weight:400;letter-spacing:-.015em;line-height:1.1;margin-bottom:9mm}
.punto{border-top:.25mm solid var(--filo);padding:4.2mm 0 5.5mm}
.punto b{display:block;font-size:11.5pt;font-weight:500;line-height:1.25;margin-bottom:1.6mm}
.punto p{font-size:9.5pt;line-height:1.45;color:var(--muto)}
/* 3 */
.sez{display:flex;gap:14mm;padding:16mm 16mm 0}
.sez .col{flex:none;width:${larg}mm;display:flex;flex-direction:column;gap:4mm}
.sez figure img{display:block;width:100%;height:auto;border:.25mm solid var(--filo)}
.sez figcaption{font-size:8pt;color:var(--muto);margin-top:1.8mm;line-height:1.35}
.sez .testo{flex:1;display:flex;flex-direction:column;padding-top:2mm;min-height:170mm}
.sez .testo p{font-size:10.5pt;line-height:1.5}
.sez .piccolo{margin-top:auto;font-size:7.8pt;line-height:1.45;color:var(--muto);border-top:.25mm solid var(--filo);padding-top:3.5mm}
.sez .mitt{margin-top:3mm;font-size:8.5pt;color:var(--ink)}
</style></head><body>
<section class="p cop">
  <img src="file://${work}/copertina.jpg" alt="">
  <div class="strip">
    <div class="chi">${esc(S.azienda)}<span>La nuova home, proposta di ${esc(S.data)}</span></div>
    <div class="frase">${esc(S.sottotitolo)}</div>
  </div>
</section>
<section class="p">
  <div class="tel">
    <div class="fon"><img src="file://${work}/telefono-1.jpg" alt=""><img src="file://${work}/telefono-2.jpg" alt=""></div>
    <div class="testo">
      <h2>${esc(S.titolo_punti || 'Cosa cambia')}</h2>
      ${S.punti.map(p => `<div class="punto"><b>${esc(p.titolo)}</b><p>${esc(p.testo)}</p></div>`).join('')}
    </div>
  </div>
  <div class="n">2 / 3</div>
</section>
<section class="p">
  <div class="sez">
    <div class="col">${S.sezioni.map((s, i) => `<figure><img src="file://${work}/sezione-${i + 1}.jpg" alt=""><figcaption>${esc(s.didascalia)}</figcaption></figure>`).join('')}</div>
    <div class="testo">
      <h2>Il prossimo passo</h2>
      <p>${esc(S.prossimo_passo)}</p>
      <div class="piccolo">${esc(S.nota || 'Testi, numeri e foto vengono dal vostro sito di oggi e si confermano insieme prima di andare online.')}${S.foto_indicative ? ' Le foto con la scritta "Foto indicativa" sono provvisorie e si sostituiscono con foto vostre.' : ''}</div>
      ${mittente ? `<div class="mitt">${esc(mittente)}</div>` : ''}
    </div>
  </div>
  <div class="n">3 / 3</div>
</section>
</body></html>`;
const htmlPath = path.join(work, 'allegato.html');
fs.writeFileSync(htmlPath, html);
{
  const ctx = await browser.newContext();
  const page = await ctx.newPage();
  await page.goto('file://' + htmlPath, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const pdf = path.join(outDir, S.file);
  await page.pdf({ path: pdf, width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  await ctx.close();
  const kb = Math.round(fs.statSync(pdf).size / 1024);
  const pagine = execFileSync('pdfinfo', [pdf]).toString().match(/Pages:\s+(\d+)/)[1];
  execFileSync('pdftoppm', ['-r', '70', '-png', pdf, path.join(outDir, 'pagina')]);
  console.log(`${pdf}  ${kb} KB  ${pagine} pagine  sezioni a ${larg} mm`);
}
await browser.close();
