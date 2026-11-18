// Registra lo scorrimento di una pagina come lo farebbe una persona, per giudicare anche il movimento.
// uso: node registra.mjs <url> <cartella> [larghezza=1440] [altezza=900]
// esce: <cartella>/scorrimento-<larghezza>.mp4 (da guardare), fotogrammi-<larghezza>-NN.jpg (uno al secondo)
// e foglio-<larghezza>.jpg (tutti i fotogrammi in un foglio, per il giudice)
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
import { execFileSync } from 'child_process';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');

const [, , url, out, Wa = '1440', Ha = '900'] = process.argv;
const W = +Wa, H = +Ha, tel = W < 600;
fs.mkdirSync(out, { recursive: true });
const tmp = fs.mkdtempSync(path.join(out, 'video-'));
const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1, isMobile: tel, hasTouch: tel,
  recordVideo: { dir: tmp, size: { width: W, height: H } } });
const p = await ctx.newPage();
const errori = [];
p.on('pageerror', e => errori.push(e.message));
await p.goto(url, { waitUntil: 'networkidle', timeout: 90000 });
await p.waitForTimeout(2600);
await p.mouse.move(W / 2, H / 2);
let fatto = 0;
for (let giro = 0; giro < 400; giro++) {
  const { y, max } = await p.evaluate(() => ({ y: window.scrollY, max: document.documentElement.scrollHeight - window.innerHeight }));
  if (y >= max - 2) break;
  if (tel) await p.evaluate(() => window.scrollBy(0, 70)); else await p.mouse.wheel(0, 100);
  fatto += 100;
  await p.waitForTimeout(55);
  if (fatto % 1000 < 100) await p.waitForTimeout(700); // una pausa ogni tanto, come chi guarda
}
await p.waitForTimeout(1500);
const video = p.video();
await ctx.close();
await b.close();
const webm = await video.path();
const mp4 = path.join(out, `scorrimento-${W}.mp4`);
execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', webm, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '24', '-movflags', '+faststart', mp4]);
for (const f of fs.readdirSync(out)) if (f.startsWith(`fotogrammi-${W}-`)) fs.unlinkSync(path.join(out, f));
execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', mp4, '-vf', `fps=1,scale=${tel ? 260 : 480}:-1`, path.join(out, `fotogrammi-${W}-%02d.jpg`)]);
const fotogrammi = fs.readdirSync(out).filter(f => f.startsWith(`fotogrammi-${W}-`)).sort().map(f => path.join(out, f));
execFileSync('montage', [...fotogrammi, '-tile', tel ? '8x' : '5x', '-geometry', '+3+3', path.join(out, `foglio-${W}.jpg`)]);
fs.rmSync(tmp, { recursive: true, force: true });
console.log(JSON.stringify({ mp4, fotogrammi: fotogrammi.length, errori }));
