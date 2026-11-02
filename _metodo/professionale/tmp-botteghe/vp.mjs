import { createRequire } from 'module';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const [out, w, h, mode, ...urls] = process.argv.slice(2);
const browser = await chromium.launch({ args: ['--proxy-server=https=' + process.env.HTTPS_PROXY.replace('http://', '')] });
for (const [i,url] of urls.entries()) {
  const ctx = await browser.newContext({ viewport: { width: +w, height: +h }, isMobile: mode === 'mobile', hasTouch: mode === 'mobile' });
  const page = await ctx.newPage();
  try { await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 }); } catch(e) { console.log('timeout', url); }
  await page.waitForTimeout(1500);
  for (let k=0;k<2;k++){ for (const t of ['Accetta tutti','Accetta tutto','Accetta','Accept all','Accept All','Allow all','Accept','Alle akzeptieren','Akzeptieren','Tout accepter','Accepter','Sì, ho','Si, ho','Sì','SI','Yes','Ja','I am over 18','Enter','Entra','OK']) { const b = page.getByRole('button', { name: t, exact: false }).first(); try { if (await b.isVisible({timeout:300})) { await b.click({timeout:1000}); await page.waitForTimeout(700);} } catch(e){} } }
  await page.waitForTimeout(1500);
  const name = new URL(url).hostname.replace('www.','').split('.')[0];
  await page.screenshot({ path: `${out}/${name}.jpg`, type: 'jpeg', quality: 60 });
  console.log(name);
  await ctx.close();
}
await browser.close();
