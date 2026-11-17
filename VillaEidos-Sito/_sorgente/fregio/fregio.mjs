// Villa Eidos: rende fregio.html in PNG al doppio della misura (Chromium di Playwright, con i caratteri del tema).
// uso: node fregio.mjs <cartella di uscita>   ->  fregio-largo.png (3200 x 1334), fregio-alto.png (1080 x 864)
// immagini.py li converte poi in WebP nelle misure del sito.
import { createRequire } from 'module';
import path from 'path';
import url from 'url';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const qui = path.dirname(url.fileURLToPath(import.meta.url));
const out = process.argv[2] || '.';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1700, height: 1300 }, deviceScaleFactor: 2 });
await p.goto(url.pathToFileURL(path.join(qui, 'fregio.html')).href);
await p.evaluate(() => document.fonts.ready);
for (const id of ['largo', 'alto']) {
  await p.locator('#' + id).screenshot({ path: path.join(out, `fregio-${id}.png`) });
}
await b.close();
console.log('fregio in', out);
