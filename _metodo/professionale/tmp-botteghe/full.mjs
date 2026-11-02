import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const [url, name] = process.argv.slice(2);
const OUT='/home/user/danielnistorr/_metodo/professionale/riferimenti/botteghe-'+name;
const TMP='/home/user/danielnistorr/_metodo/professionale/tmp-botteghe/'+name;
const browser = await chromium.launch({ args: ['--proxy-server=https=' + process.env.HTTPS_PROXY.replace('http://', '')] });
async function consent(page){ for (let k=0;k<2;k++){ for (const t of ['Accetta tutti','Accetta tutto','Accetta','Accept all','Accept All','Allow all','Accept','Alle akzeptieren','Akzeptieren','Tout accepter','Accepter','Continue','Yes','Ja','Sì','Chiudi']) { const b = page.getByRole('button', { name: t, exact: false }).first(); try { if (await b.isVisible({timeout:250})) { await b.click({timeout:1000}); await page.waitForTimeout(600);} } catch(e){} } } }
async function open(w,h,mobile){
  const ctx = await browser.newContext({ viewport:{width:w,height:h}, isMobile:mobile, hasTouch:mobile, deviceScaleFactor:1, locale:'it-IT' });
  const page = await ctx.newPage();
  try { await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 }); } catch(e) { console.log('timeout'); }
  await page.waitForTimeout(1500); await consent(page); await page.waitForTimeout(4000);
  await page.keyboard.press('Escape').catch(()=>{});
  for (const sel of ['[aria-label*=lose i]','.pum-close','.popmake-close','button.close','.modal-close','[class*=popup] [class*=close]','[class*=modal] [class*=close]']) { try { const b=page.locator(sel).first(); if (await b.isVisible({timeout:300})) { await b.click({timeout:1000}); await page.waitForTimeout(500);} } catch(e){} }
  await page.waitForTimeout(2500);
  await page.evaluate(()=>window.scrollTo(0,0)); await page.waitForTimeout(800);
  return [ctx,page];
}
// 1440 first screen + full
let [ctx,page]=await open(1440,900,false);
await page.screenshot({ path: OUT+'-1440.jpg', type:'jpeg', quality:70 });
await page.evaluate(() => document.querySelectorAll('img[loading=lazy],iframe[loading=lazy]').forEach(f => { f.loading = 'eager'; }));
await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 400) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 250)); } window.scrollTo(0, 0); });
await page.waitForTimeout(2500);
await page.keyboard.press('Escape').catch(()=>{});
if (!process.env.NOHIDE) await page.evaluate(() => { for (const e of document.querySelectorAll('body *')) { const s=getComputedStyle(e); if ((s.position==='fixed') ) { const r=e.getBoundingClientRect(); if (r.height > innerHeight*0.3 && r.top > 5) e.style.display='none'; if (/pum|popup|modal|newsletter/i.test(e.className+e.id) && r.height>200) e.style.display='none'; } } document.documentElement.style.overflow='auto'; document.body.style.overflow='auto'; });
await page.waitForTimeout(800);
const info = await page.evaluate(() => {
  const cs = e => getComputedStyle(e);
  const vis = e => { const r=e.getBoundingClientRect(); return r.width>0 && r.height>0 && cs(e).visibility!=='hidden'; };
  const sample = sel => [...document.querySelectorAll(sel)].filter(vis).slice(0,4).map(e => { const s=cs(e); return `${sel}: "${e.textContent.trim().replace(/\s+/g,' ').slice(0,50)}" | ${s.fontFamily.slice(0,60)} | ${s.fontSize}/${s.lineHeight} w${s.fontWeight} ls${s.letterSpacing} tt${s.textTransform} col${s.color}`; });
  const out = [];
  for (const sel of ['h1','h2','h3','h4','p','nav a','header a','button','a[class*=btn],a[class*=button],.button,.btn','footer p, footer a','li']) out.push(...sample(sel));
  const links = [...document.querySelectorAll('a[href^="tel:"],a[href^="mailto:"],a[href*="wa.me"],a[href*="maps"],a[href*="whatsapp"]')].map(a=>a.href+' ['+a.textContent.trim().slice(0,30)+'] y='+Math.round(a.getBoundingClientRect().top+scrollY));
  const forms = [...document.querySelectorAll('form')].map(f=>'form y='+Math.round(f.getBoundingClientRect().top+scrollY)+' fields='+f.querySelectorAll('input,textarea,select').length);
  const iframes = [...document.querySelectorAll('iframe')].map(f=>f.src.slice(0,80));
  const heads = [...document.querySelectorAll('h1,h2,h3')].filter(vis).map(h=>h.tagName+'@'+Math.round(h.getBoundingClientRect().top+scrollY)+': '+h.textContent.trim().replace(/\s+/g,' ').slice(0,70));
  const fonts = [...new Set([...document.querySelectorAll('body *')].slice(0,3000).map(e=>cs(e).fontFamily))].slice(0,12);
  const ff=[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight+' '+f.style); 
  const body=cs(document.body);
  return {H:document.documentElement.scrollHeight, bodybg:body.backgroundColor, bodycolor:body.color, fonts, loaded:[...new Set(ff)], out, links, forms, iframes, heads, gen:[...document.querySelectorAll('meta[name=generator]')].map(m=>m.content), credits:[...document.querySelectorAll('a')].filter(a=>/credit|design|agency|studio|made by|sito|realizzato|website by/i.test(a.textContent)).map(a=>a.textContent.trim().slice(0,40)+' -> '+a.href).slice(0,8)};
});
fs.writeFileSync(TMP+'-info.json', JSON.stringify(info,null,1));
const H=Math.min(info.H,9000);
await page.screenshot({ path: OUT+'-1440-intera.jpg', type:'jpeg', quality:70, fullPage:true, clip:{x:0,y:0,width:1440,height:H} });
await ctx.close();
// mobile
[ctx,page]=await open(390,844,true);
await page.screenshot({ path: OUT+'-390.jpg', type:'jpeg', quality:70 });
await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 400) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 200)); } window.scrollTo(0, 0); });
const mH=Math.min(await page.evaluate(()=>document.documentElement.scrollHeight),9000);
const mob = await page.evaluate(() => ({ sw:document.documentElement.scrollWidth, tel:[...document.querySelectorAll('a[href^="tel:"]')].filter(a=>a.getBoundingClientRect().width>0).map(a=>a.textContent.trim().slice(0,30)+' y='+Math.round(a.getBoundingClientRect().top+scrollY)), h1:[...document.querySelectorAll('h1,h2')].slice(0,4).map(h=>h.textContent.trim().slice(0,40)+' '+getComputedStyle(h).fontSize) }));
fs.writeFileSync(TMP+'-mob.json', JSON.stringify(mob,null,1));
await page.waitForTimeout(1500);
await page.screenshot({ path: TMP+'-390-intera.jpg', type:'jpeg', quality:65, fullPage:true, clip:{x:0,y:0,width:390,height:mH} });
await ctx.close(); await browser.close();
console.log(name, 'H', info.H, 'mH', mH);
