/* Script della home statica (sito/index.html), uguale tranne i selettori con il prefisso hbr-:
   righello d'apertura, banco di misura, taratura dello schermo. Nessuna libreria. */
(function(){
  var root=document.documentElement;
  var k=1;
  try{var s=localStorage.getItem('hambro-k');if(s){k=parseFloat(s)||1}}catch(e){}
  if(!(k>=0.5&&k<=1.8))k=1;
  root.style.setProperty('--k',k);
  var kIn=document.querySelector('[data-k]');if(kIn)kIn.value=k;
  function fmt(v){return String(v).replace('.',',');}

  /* righello in millimetri, in scala reale (taratura inclusa).
     In cuoio le misure a catalogo: 2-4 (lacci, tondini, cordoncino) come una sola quota, poi 16, 20, 25, 30, 40, 50, 60.
     Due righe di numeri: dove un numero non sta nella riga bassa sale in quella alta e la sua tacca si allunga in verticale. */
  var CAT=[2,3,3.5,4,16,20,25,30,40,50,60];
  var INK='#1B1714',CU='#7B4524';
  function largo(t){var w=0;for(var i=0;i<t.length;i++){var c=t[i];w+=(c===','?3.6:(c==='-'?5:7.6));}return w;}
  function disegna(){
    var el=document.querySelector('[data-righello]');if(!el)return;
    var w=el.clientWidth,h=el.clientHeight;if(!w||!h)return;
    var compatto=h<60;
    var px=96/25.4*k;
    var rif=document.querySelector('.hbr-apertura h1');
    var start=Math.round(rif?rif.getBoundingClientRect().left:20);
    var fine=Math.min(100,Math.floor((w-start-(compatto?48:44))/px));
    if(!compatto&&w<=900)fine=Math.min(fine,60);   /* tablet stretto: il righello si ferma prima del ramo della fibbia */
    var Lc=compatto?11:16, L10=compatto?8:11, L5=compatto?6:8, L1=compatto?3:5;
    var y0=compatto?h-Lc-5:h-Lc-7, y1=y0-(compatto?16:18);
    var o='<svg xmlns="http://www.w3.org/2000/svg" width="'+w+'" height="'+h+'" viewBox="0 0 '+w+' '+h+'">';
    o+='<defs><linearGradient id="sf" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="'+INK+'" stop-opacity=".55"/><stop offset="1" stop-color="'+INK+'" stop-opacity="0"/></linearGradient></defs>';
    var xEnd=start+fine*px;
    o+='<rect x="'+start+'" y="'+(h-1)+'" width="'+(fine*px).toFixed(1)+'" height="1" fill="'+INK+'" fill-opacity=".55"/>';
    if(!compatto){o+='<rect x="'+xEnd.toFixed(1)+'" y="'+(h-1)+'" width="'+Math.max(0,Math.min(280,w-xEnd)).toFixed(1)+'" height="1" fill="url(#sf)"/>';}
    for(var i=0;i<=fine;i++){
      if(CAT.indexOf(i)>-1)continue;
      var x=start+i*px;
      var L=i%10===0?L10:(i%5===0?L5:L1);
      o+='<rect x="'+(x-0.5).toFixed(2)+'" y="'+(h-L)+'" width="1" height="'+L+'" fill="'+INK+'" fill-opacity=".4"/>';
    }
    CAT.forEach(function(v){
      if(v>fine)return;
      o+='<rect x="'+(start+v*px-0.5).toFixed(2)+'" y="'+(h-Lc)+'" width="1" height="'+Lc+'" fill="'+CU+'"/>';
    });
    /* la quota 2-4: un filo cuoio sopra le tacche 2, 3, 3,5 e 4 */
    o+='<rect x="'+(start+2*px-0.5).toFixed(2)+'" y="'+(h-Lc)+'" width="'+(2*px+1).toFixed(2)+'" height="1" fill="'+CU+'"/>';
    var et=[{x:start+2*px,t:'2-4',c:1,sx:1}];
    [16,20,25,30,40,50,60].forEach(function(v){if(v<=fine)et.push({x:start+v*px,t:String(v),c:1});});
    for(var d=70;d<=fine;d+=10)et.push({x:start+d*px,t:String(d),c:0});
    var fr=[-1e9,-1e9],gap=5,dest=-1e9;
    et.forEach(function(e){
      var lw=largo(e.t), l=e.sx?e.x-1:e.x-lw/2, r=l+lw, q=-1;
      if(l>=fr[0]+gap)q=0;else if(l>=fr[1]+gap)q=1;
      if(q<0)return;
      fr[q]=r;dest=Math.max(dest,r);
      var y=q?y1:y0;
      o+='<text x="'+l.toFixed(1)+'" y="'+y+'" class="hbr-rt'+(e.c?' c':'')+'" fill="'+(e.c?CU:INK)+'" fill-opacity="'+(e.c?1:.6)+'">'+e.t+'</text>';
      if(q){o+='<rect x="'+(e.x-0.5).toFixed(2)+'" y="'+(y1+4)+'" width="1" height="'+(h-Lc-(y1+4))+'" fill="'+CU+'"/>';}
    });
    o+='<text x="'+(dest+8).toFixed(1)+'" y="'+y0+'" class="hbr-rt" fill="'+INK+'" fill-opacity=".6">mm</text>';
    o+='</svg>';
    el.innerHTML=o;
  }
  disegna();
  var rt;window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(disegna,60);});
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(disegna);

  /* banco di misura */
  var banco=document.querySelector('.hbr-banco');
  var str=document.querySelector('[data-striscia]');
  var val=document.querySelector('[data-valore]');
  var cosa=document.querySelector('[data-cosa]');
  var rng=document.querySelector('[data-range]');
  var reg=document.querySelector('[data-regolo]');
  var tac=document.querySelector('[data-tacche]');
  var mn=document.querySelector('[data-misure-nastro]');
  var col=document.querySelector('[data-colori]');
  var vivo=[];for(var m=2;m<=60;m++)vivo.push(m);
  /* taglio vivo: ogni millimetro da 2 a 60 (frecce 1 mm, pagina su e giu' 10 mm); tubolare: le misure a catalogo */
  var MIS={vivo:vivo,tubo:[2,3,4,16]};
  var TAC={vivo:[2,10,20,30,40,50,60],tubo:[2,3,4,16]};
  var memo={vivo:30,tubo:4};
  var testi={vivo:'Striscia in pelle a taglio vivo, da mm2 a mm60',tubo:'Laccio tubolare in pelle: mm2, 3, 4 e 16',nastro:'Nastro in cotone o poliestere per tracolle e cinture'};
  var mat='vivo';
  function imposta(n){
    banco.style.setProperty('--n',n);
    val.textContent=fmt(n);
    str.setAttribute('aria-label',testi[mat]+': '+fmt(n)+' millimetri');
    rng.setAttribute('aria-valuetext',fmt(n)+' millimetri');
  }
  function vicina(v){var l=MIS[mat],b=l[0];l.forEach(function(x){if(Math.abs(x-v)<Math.abs(b-v))b=x;});return b;}
  function tacche(){
    var l=MIS[mat],t=TAC[mat],mi=l[0],ma=l[l.length-1],o='';
    t.forEach(function(v){o+='<i style="left:'+((v-mi)/(ma-mi)*100).toFixed(3)+'%"></i>';});
    tac.innerHTML=o;
    rng.min=mi;rng.max=ma;
    document.querySelector('[data-min]').textContent=fmt(mi);
    document.querySelector('[data-max]').textContent=fmt(ma);
  }
  function scegli(v){memo[mat]=v;rng.value=v;imposta(v);}
  rng.addEventListener('input',function(){scegli(vicina(parseFloat(rng.value)));});
  rng.addEventListener('keydown',function(e){
    var l=MIS[mat],i=l.indexOf(memo[mat]),j=i,salto=mat==='vivo'?10:1;
    if(e.key==='ArrowRight'||e.key==='ArrowUp')j=Math.min(l.length-1,i+1);
    else if(e.key==='ArrowLeft'||e.key==='ArrowDown')j=Math.max(0,i-1);
    else if(e.key==='PageUp')j=Math.min(l.length-1,i+salto);
    else if(e.key==='PageDown')j=Math.max(0,i-salto);
    else if(e.key==='Home')j=0;else if(e.key==='End')j=l.length-1;else return;
    e.preventDefault();scegli(l[j]);
  });
  document.querySelectorAll('input[name=mat]').forEach(function(r){
    r.addEventListener('change',function(){
      mat=r.value;
      str.className='hbr-striscia '+mat;
      cosa.textContent=testi[mat];
      var nastro=mat==='nastro';
      reg.hidden=nastro;mn.hidden=!nastro;col.hidden=!nastro;
      if(nastro){imposta(parseInt(document.querySelector('input[name=mn]:checked').value,10));}
      else{tacche();scegli(memo[mat]);}
    });
  });
  document.querySelectorAll('input[name=mn]').forEach(function(r){r.addEventListener('change',function(){imposta(parseInt(r.value,10));});});
  document.querySelectorAll('input[name=col]').forEach(function(r){r.addEventListener('change',function(){str.style.setProperty('--c',r.value);});});
  tacche();scegli(30);
  if(kIn){kIn.addEventListener('input',function(){
    k=parseFloat(kIn.value)||1;root.style.setProperty('--k',k);disegna();
    try{localStorage.setItem('hambro-k',String(k))}catch(e){}
  });}
})();
