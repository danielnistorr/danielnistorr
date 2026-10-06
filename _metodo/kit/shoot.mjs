// uso: node shoot.mjs <url> <out.png> <width> <height> [mobile]
import { createRequire } from 'module';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const [url, out, w = '1440', h = '900', mode] = process.argv.slice(2);
const browser = await chromium.launch({ args: ['--proxy-server=https=' + (process.env.HTTPS_PROXY || 'http://127.0.0.1:39747').replace('http://', '')] });
const ctx = await browser.newContext({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1, isMobile: mode === 'mobile', hasTouch: mode === 'mobile' });
const page = await ctx.newPage();
await page.goto(url, { waitUntil: 'networkidle', timeout: 90000 });
// forza il caricamento delle immagini lazy scorrendo la pagina
await page.evaluate(() => document.querySelectorAll('iframe[loading=lazy],img[loading=lazy]').forEach(f => { f.loading = 'eager'; }));
await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 450) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 220)); } window.scrollTo(0, 0); });
await page.waitForFunction(() => [...document.images].filter(i => i.offsetParent !== null).every(i => i.complete && i.naturalWidth > 0), null, { timeout: 30000 }).catch(() => console.log('immagini non tutte caricate'));
const nIframe = await page.locator('iframe, .bv-track').count();
if (nIframe) {
  // anche la striscia scorrevole: la cattura "a pagina intera" di Chrome la fa scattare di una scheda
  // gli iframe di altri domini (Google Maps) escono bianchi nello screenshot a pagina intera:
  // allungo la finestra fino all'altezza della pagina, aspetto il rendering e fotografo la finestra
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  await page.setViewportSize({ width: +w, height: Math.min(H, 16000) });
  await page.waitForTimeout(5000);
  await page.screenshot({ path: out, fullPage: false });
} else {
  await page.waitForTimeout(600);
  await page.screenshot({ path: out, fullPage: true });
}
const dims = await page.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.scrollHeight, window.innerWidth]);
console.log(out, dims.join('x'), dims[0] > dims[2] ? 'OVERFLOW-X' : '');
await browser.close();
