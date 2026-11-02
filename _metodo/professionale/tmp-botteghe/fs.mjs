import { createRequire } from 'module';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const browser = await chromium.launch({ args: ['--proxy-server=https=' + process.env.HTTPS_PROXY.replace('http://', '')] });
for (const url of process.argv.slice(2)) {
  const page = await (await browser.newContext({ viewport:{width:1440,height:900} })).newPage();
  try { await page.goto(url, { waitUntil: 'networkidle', timeout: 50000 }); } catch(e) {}
  await page.waitForTimeout(1500);
  const r = await page.evaluate(() => { const m={}; for (const e of document.querySelectorAll('h1,h2,h3,h4,p,a,li,span,td')) { const r=e.getBoundingClientRect(); if(!r.width||!e.textContent.trim()) continue; if ([...e.children].some(c=>c.textContent.trim()===e.textContent.trim())) continue; const s=getComputedStyle(e); const k=`${s.fontFamily.split(',')[0]} ${Math.round(parseFloat(s.fontSize))}px w${s.fontWeight} ${s.textTransform==='uppercase'?'MAIUSC':''} lh${Math.round(parseFloat(s.lineHeight)||0)}`; (m[k]=m[k]||[]).push(e.textContent.trim().slice(0,25)); } return Object.entries(m).map(([k,v])=>`${v.length}x ${k} :: ${v.slice(0,3).join(' | ')}`).sort((a,b)=>parseInt(b)-parseInt(a)).slice(0,16); });
  console.log('=====',url); console.log(r.join('\n'));
}
await browser.close();
