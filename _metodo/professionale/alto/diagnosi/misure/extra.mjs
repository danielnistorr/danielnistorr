import { createRequire } from 'module';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const names=process.argv[2].split(',');
const b=await chromium.launch(); const out={};
for(const n of names){ const p=await b.newPage({viewport:{width:1440,height:900}});
 await p.goto('file:///home/user/danielnistorr/'+n+'-Sito/sito/index.html'); await p.waitForTimeout(300);
 out[n]=await p.evaluate(()=>{
  const h1=document.querySelector('h1'); const hr=h1.getBoundingClientRect();
  const imgs=[...document.querySelectorAll('img')].map(e=>e.getBoundingClientRect()).filter(r=>r.top<900&&r.width*r.height>60000).sort((a,b)=>b.width*b.height-a.width*a.height);
  const im=imgs[0];
  let layout='altro';
  if(im){ if(im.left>=hr.right-40 && im.width<1000) layout='titolo sx, foto dx'; else if(im.width>=1300) layout= im.top>hr.bottom?'titolo sopra, foto larga sotto':'foto a tutta larghezza'; else if(im.right<=hr.left+40) layout='foto sx, titolo dx'; }
  else layout='senza foto in apertura';
  // eyebrow before h2
  const up=e=>{const s=getComputedStyle(e);return s.textTransform==='uppercase'&&parseFloat(s.letterSpacing)>0.3&&parseFloat(s.fontSize)<17;};
  const h2=[...document.querySelectorAll('h2')]; let eb=0;
  for(const h of h2){ let p=h.previousElementSibling; if(!p&&h.parentElement) p=h.parentElement.previousElementSibling; if(p&&up(p)) eb++; }
  const h1eb=(()=>{let p=h1.previousElementSibling; if(!p) p=h1.parentElement.previousElementSibling; return !!(p&&up(p));})();
  // row of >=3 items in first screen below h1
  const cands=[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect(); return r.top>hr.bottom&&r.top<900&&r.width>120&&r.width<480&&r.height>30&&e.innerText&&e.innerText.trim().length>3;});
  const byTop={}; for(const e of cands){const r=e.getBoundingClientRect(); const k=Math.round(r.top/6); (byTop[k]=byTop[k]||[]).push(r);} 
  let row=0; for(const k in byTop){ const rs=byTop[k]; const lefts=new Set(rs.map(r=>Math.round(r.left/20))); if(lefts.size>=3){ const span=Math.max(...rs.map(r=>r.right))-Math.min(...rs.map(r=>r.left)); if(span>600) row=Math.max(row,lefts.size);} }
  const secs=[...document.querySelectorAll('section')]; const bgs=secs.map(s=>getComputedStyle(s).backgroundColor);
  const pads=secs.map(s=>parseFloat(getComputedStyle(s).paddingTop));
  const hdr=document.querySelector('header'); 
  return {layout, h2:h2.length, h2eb:eb, h1eb, row, secs:secs.length, bgs:[...new Set(bgs)].length, pads:[...new Set(pads)].join('/'), hdrH: hdr?Math.round(hdr.getBoundingClientRect().height):null, hdrFixed: hdr?getComputedStyle(hdr).position:null};
 }); await p.close(); }
await b.close(); console.log(JSON.stringify(out));
