const {createRequire}=require('module');const r=createRequire('/opt/node-tools/node_modules/');const {chromium}=r('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const errs=[];p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});p.on('requestfailed',q=>errs.push('fallita '+q.url()));
await p.goto('file://'+process.argv[2],{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
const h=await p.evaluate(()=>{const f=document.querySelector('.foglio');return [f.scrollHeight,f.clientHeight,document.body.scrollWidth]});console.log('altezza contenuto/foglio, larghezza:',h.join(' '));
await p.pdf({path:process.argv[3],format:'A4',printBackground:true,preferCSSPageSize:true,margin:{top:0,right:0,bottom:0,left:0}});console.log(errs.length?errs.join('\n'):'nessun errore');await b.close();})();
