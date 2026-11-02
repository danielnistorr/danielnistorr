import { createRequire } from 'module';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const browser = await chromium.launch({ args: ['--proxy-server=https=' + process.env.HTTPS_PROXY.replace('http://', '')] });
for (const url of process.argv.slice(2)) {
  for (const [w,h,m] of [[1440,900,false],[390,844,true]]) {
  const ctx = await browser.newContext({ viewport:{width:w,height:h}, isMobile:m, hasTouch:m });
  const page = await ctx.newPage();
  try { await page.goto(url, { waitUntil: 'networkidle', timeout: 50000 }); } catch(e) {}
  await page.waitForTimeout(2000);
  const r = await page.evaluate(() => {
    const vis = e => { const r=e.getBoundingClientRect(); return r.width>0 && r.height>0; };
    const hdr = document.querySelector('header') || document.querySelector('[class*=header]');
    const hr = hdr ? hdr.getBoundingClientRect() : null;
    const hs = hdr ? getComputedStyle(hdr) : null;
    const btns = [...document.querySelectorAll('a,button')].filter(vis).filter(e => { const s=getComputedStyle(e); return (s.borderStyle!=='none' && parseFloat(s.borderWidth)>0) || (s.backgroundColor!=='rgba(0, 0, 0, 0)' && s.backgroundColor!=='transparent'); }).slice(0,40).map(e => { const s=getComputedStyle(e), r=e.getBoundingClientRect(); return `"${e.textContent.trim().replace(/\s+/g,' ').slice(0,22)}" ${Math.round(r.width)}x${Math.round(r.height)} pad ${s.padding} rad ${s.borderRadius} bd ${s.borderWidth} ${s.borderColor} bg ${s.backgroundColor} col ${s.color} fs ${s.fontSize}`; }).filter((v,i,a)=>a.indexOf(v)===i).slice(0,8);
    const lefts = [...document.querySelectorAll('h2,h3,p')].filter(vis).map(e=>Math.round(e.getBoundingClientRect().left+scrollX));
    const cnt = {}; lefts.forEach(l=>cnt[l]=(cnt[l]||0)+1);
    const secs = [...document.querySelectorAll('main > *, section, .wp-block-group, [class*=section]')].filter(vis).slice(0,30).map(e=>{const s=getComputedStyle(e);return Math.round(e.getBoundingClientRect().height)+'h pt'+s.paddingTop+' pb'+s.paddingBottom+' bg'+s.backgroundColor}).filter((v,i,a)=>a.indexOf(v)===i).slice(0,14);
    const tel=[...document.querySelectorAll('a[href^="tel:"]')].map(a=>a.textContent.trim().slice(0,25)+'@'+Math.round(a.getBoundingClientRect().top)+(vis(a)?'':'(nascosto)'));
    const sticky=[...document.querySelectorAll('body *')].filter(e=>['fixed','sticky'].includes(getComputedStyle(e).position)&&vis(e)).map(e=>(e.tagName+'.'+String(e.className).slice(0,30))+' '+Math.round(e.getBoundingClientRect().height)+'h').slice(0,6);
    return {header: hr? `${Math.round(hr.height)}h pos ${hs.position} bg ${hs.backgroundColor}`:'-', btns, lefts:Object.entries(cnt).sort((a,b)=>b[1]-a[1]).slice(0,5), secs, tel, sticky};
  });
  console.log('=====', url, w); console.log(JSON.stringify(r,null,1));
  await ctx.close(); }
}
await browser.close();
