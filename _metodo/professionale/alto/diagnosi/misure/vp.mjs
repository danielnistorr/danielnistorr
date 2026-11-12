import { createRequire } from 'module';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
import fs from 'fs';
const names = process.argv[2].split(',');
const R='/home/user/danielnistorr';
const fn = ({VW,VH}) => {
  const top = e => { const r=e.getBoundingClientRect(); const pts=[[r.left+r.width/2,r.top+r.height/2],[r.left+3,r.top+3],[r.left+Math.min(r.width-2,20),r.top+r.height/2]]; for(const [x,y] of pts){ if(x<0||y<0||x>=VW||y>=VH) continue; const h=document.elementFromPoint(x,y); if(h&&(h===e||e.contains(h)||h.contains(e))) return true;} return false; };
  const all=[...document.querySelectorAll('body *')];
  const clk=all.filter(e=>e.matches('a[href],button,input:not([type=hidden]),select,textarea,summary')&&e.getBoundingClientRect().width>2&&top(e));
  // unique by href/position
  const isBtn = e => { const s=getComputedStyle(e); const bg=s.backgroundColor; const hasBg=bg&&bg!=='rgba(0, 0, 0, 0)'&&bg!=='transparent'; const hasB=parseFloat(s.borderTopWidth)>0&&parseFloat(s.borderLeftWidth)>0&&parseFloat(s.borderBottomWidth)>0; const r=e.getBoundingClientRect(); return e.matches('a[href],button')&&(hasBg||hasB)&&r.height>=28&&r.height<=80&&r.width>40&&r.width<700; };
  let chars=0, nodes=0; const tw=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
  let n; while(n=tw.nextNode()){ const t=n.textContent.trim(); if(!t) continue; const e=n.parentElement; const s=getComputedStyle(e); if(s.visibility==='hidden'||parseFloat(s.opacity)<0.1) continue; const rg=document.createRange(); rg.selectNodeContents(n); const rs=[...rg.getClientRects()]; let ok=false; for(const r of rs){ if(r.width<1||r.bottom<=0||r.top>=VH||r.right<=0||r.left>=VW) continue; const x=Math.min(VW-1,Math.max(0,r.left+r.width/2)), y=Math.min(VH-1,Math.max(0,r.top+r.height/2)); const h=document.elementFromPoint(x,y); if(h&&(h===e||e.contains(h)||h.contains(e))){ok=true;break;} } if(ok){chars+=t.length;nodes++;} }
  // image coverage by sampling
  let img=0,tot=0; const isImg=h=>{ for(let k=0;h&&k<4;k++,h=h.parentElement){ if(h.matches('img,video,picture,canvas,svg image')) return true; const s=getComputedStyle(h); if(s.backgroundImage&&s.backgroundImage.includes('url(')) return true; } return false; };
  for(let y=5;y<VH;y+=VH/30) for(let x=5;x<VW;x+=VW/40){ tot++; const h=document.elementFromPoint(x,y); if(h&&isImg(h)) img++; }
  // biggest visible img natural res
  const imgs=[...document.querySelectorAll('img')].map(e=>{const r=e.getBoundingClientRect(); const ix=Math.max(0,Math.min(r.right,VW)-Math.max(r.left,0)), iy=Math.max(0,Math.min(r.bottom,VH)-Math.max(r.top,0)); return {src:(e.currentSrc||e.src).split('/').pop().slice(0,50),a:ix*iy,nw:e.naturalWidth,nh:e.naturalHeight,rw:Math.round(r.width),rh:Math.round(r.height)};}).filter(i=>i.a>0).sort((a,b)=>b.a-a.a);
  return {clk:clk.length, btn:clk.filter(isBtn).length, chars, nodes, img:+(img/tot).toFixed(2), big:imgs[0]||null};
};
const browser=await chromium.launch();
const out={};
for(const n of names){
  const key=n.split('=')[0]; out[key]={};
  for(const [VW,VH] of [[1440,900],[390,844]]){
    const ctx=await browser.newContext({viewport:{width:VW,height:VH},locale:'it-IT'}); const p=await ctx.newPage();
    try{ const live=n.includes('='); const url=live?n.split('=')[1]:'file://'+R+'/'+n+'-Sito/sito/index.html'; await p.goto(url,{waitUntil:'load',timeout:45000}); await p.waitForTimeout(live?3500:300);
      if(live){ for(const re of [/^(alle )?(akzeptieren|accept( all)?|tout accepter|accepter|accetta( tutti)?|agree|ok|got it|alle akzeptieren|zustimmen|allow all|i agree|einverstanden)/i]){ const b=p.locator('button, a, [role=button]').filter({hasText:re}); const c=await b.count(); for(let i=0;i<Math.min(c,3);i++){ try{ if(await b.nth(i).isVisible()){ await b.nth(i).click({timeout:2000}); await p.waitForTimeout(800);} }catch(e){} } } }
      await p.evaluate(()=>window.scrollTo(0,0)); await p.waitForTimeout(300);
      out[key][VW]=await p.evaluate(fn,{VW,VH});
      if(live) await p.screenshot({path:`${process.argv[4]}/${key}-${VW}.jpg`,type:'jpeg',quality:60});
    }catch(e){out[key][VW]={err:String(e).slice(0,200)}}
    await ctx.close();
  }
}
await browser.close();
fs.writeFileSync(process.argv[3],JSON.stringify(out));
