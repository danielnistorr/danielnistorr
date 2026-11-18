import { createRequire } from 'module';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const OUT='/home/user/danielnistorr/RecinzioniFormentin-Sito/_prova/pro-controllo/';
const url='file:///home/user/danielnistorr/RecinzioniFormentin-Sito/sito/index.html?ora=2026-11-02T10:00';
const browser = await chromium.launch({ args: ['--proxy-server=https=' + (process.env.HTTPS_PROXY || 'http://127.0.0.1:39747').replace('http://', '')] });
const res={};
for (const [w,h,mob] of [[1440,900,false],[390,844,true]]) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1, isMobile: mob, hasTouch: mob });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.querySelectorAll('img[loading=lazy]').forEach(f => { f.loading = 'eager'; }));
  await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 450) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } window.scrollTo(0, 0); });
  await page.waitForTimeout(500);
  await page.screenshot({ path: OUT+`prima-${w}.jpg`, type:'jpeg', quality:80 });
  await page.screenshot({ path: OUT+`intera-${w}.jpg`, type:'jpeg', quality:75, fullPage:true });
  const r = await page.evaluate(() => {
    const vis = e => { const s=getComputedStyle(e); return s.display!=='none' && s.visibility!=='hidden' && e.getClientRects().length; };
    const sizes={}, fams={}, weights={};
    const small=[];
    document.querySelectorAll('body *').forEach(e => {
      if(!vis(e)) return;
      const hasText=[...e.childNodes].some(n=>n.nodeType===3 && n.textContent.trim());
      if(!hasText) return;
      const s=getComputedStyle(e);
      sizes[s.fontSize]=(sizes[s.fontSize]||0)+1; fams[s.fontFamily]=(fams[s.fontFamily]||0)+1; weights[s.fontWeight]=(weights[s.fontWeight]||0)+1;
      if(parseFloat(s.fontSize)<14) small.push(e.tagName+'.'+e.className+':'+e.textContent.trim().slice(0,30));
    });
    const r = sel => { const e=document.querySelector(sel); if(!e) return null; const b=e.getBoundingClientRect(); const s=getComputedStyle(e); return {x:Math.round(b.x),y:Math.round(b.y),w:Math.round(b.width),h:Math.round(b.height),fs:s.fontSize,lh:s.lineHeight,br:s.borderRadius,bg:s.backgroundColor}; };
    const btns=[...document.querySelectorAll('.btn')].filter(vis).map(b=>{const bb=b.getBoundingClientRect();const s=getComputedStyle(b);return [b.textContent.trim().slice(0,28),Math.round(bb.height),s.fontSize,s.borderRadius,s.backgroundColor,Math.round(bb.width)];});
    const secs=[...document.querySelectorAll('main > *, footer')].map(e=>{const s=getComputedStyle(e);const b=e.getBoundingClientRect();return [e.id||e.className,s.backgroundColor,s.paddingTop,s.paddingBottom,Math.round(b.y+scrollY),Math.round(b.height)];});
    const imgs=[...document.images].filter(vis).map(i=>{const b=i.getBoundingClientRect();return [i.getAttribute('src'),Math.round(b.width),Math.round(b.height),i.naturalWidth];});
    return {sizes,fams,weights,small,
      tel:document.querySelectorAll('a[href^="tel:"]').length,
      mailto:document.querySelectorAll('a[href^="mailto:"]').length,
      iframes:document.querySelectorAll('iframe').length,
      h1:r('h1'), testata:r('.testata'), ttel:r('#t-tel'), body:getComputedStyle(document.body).fontSize,
      lead:r('.ap-lead'), h2:r('.h2'), wrap:(()=>{const e=document.querySelector('.wrap');const s=getComputedStyle(e);return [s.paddingLeft,s.maxWidth, Math.round(e.getBoundingClientRect().x)]})(),
      btns, secs, imgs, sh:document.documentElement.scrollHeight, sw:document.documentElement.scrollWidth,
      passiP:r('.passi p'), schedaP:r('.scheda p'), lavH3:r('.lavori h3'), piedeLi:r('.piede li'), legale:r('.legale'),
      grande:r('.grande'), numeri:r('.numeri b')};
  });
  // scroll 50%
  await page.evaluate(()=>window.scrollTo(0, document.documentElement.scrollHeight*0.5-innerHeight/2));
  await page.waitForTimeout(400);
  r.tel50 = await page.evaluate(()=>{const e=document.getElementById('t-tel');const b=e.getBoundingClientRect();const el=document.elementFromPoint(b.x+b.width/2,b.y+b.height/2);return {y:Math.round(b.y),w:Math.round(b.width),h:Math.round(b.height),top:el&&el.closest('#t-tel')?true:false,text:e.textContent.trim()};});
  await page.screenshot({ path: OUT+`scorri50-${w}.jpg`, type:'jpeg', quality:80 });
  res[w]=r;
  await ctx.close();
}
console.log(JSON.stringify(res,null,1));
await browser.close();
