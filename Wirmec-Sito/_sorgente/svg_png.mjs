// Rende le mappe SVG (vettoriali, scritte già in tracciati) in PNG al doppio della misura, con fondo trasparente:
// Elementor non importa gli SVG senza "upload non filtrati", un PNG entra nella libreria media come le foto.
// Uso: node svg_png.mjs <in.svg> <out.png> <scala>      (lanciato da prepara_immagini.py)
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire(process.env.NODE_TOOLS || '/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const [inp, out, scala = '2'] = process.argv.slice(2);
const svg = fs.readFileSync(inp, 'utf8');
const vb = svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
const w = Math.round(+vb[1]), h = Math.round(+vb[2]);
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: +scala });
await p.setContent(`<html><body style="margin:0;background:transparent"><img id="i" style="width:${w}px;height:${h}px;display:block" src="data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}"></body></html>`);
await p.waitForTimeout(300);
await (await p.$('#i')).screenshot({ path: out, omitBackground: true });
await b.close();
