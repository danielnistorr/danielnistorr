/* La mazzetta di Paraga Pelli: lo stesso script della home statica (sito/index.html), adattato a WordPress.
   B (base delle immagini) e D (catalogo: 27 articoli, 403 colori) li scrive contenuti.py prima di questo file.
   Parte quando la pagina è pronta, perché i dorsi e i nomi degli usi stanno in widget più in basso. */
function pplAvvia(){
  var ap=document.getElementById('apertura'), mz=document.getElementById('ppl-mazzetta');
  if(!ap||!mz||mz.getAttribute('data-pronta'))return;
  mz.setAttribute('data-pronta','1');
  var A=D.articoli, perNome={};
  A.forEach(function(a,i){perNome[a.a]=i});
  var root=document.documentElement;
  var nome=document.getElementById('ppl-nome'), cod=document.getElementById('ppl-codice'), riga=document.getElementById('ppl-nome-linea');
  var img=document.getElementById('ppl-campione'), cn=document.getElementById('ppl-c-nome'), cc=document.getElementById('ppl-c-cod'), sch=document.getElementById('ppl-scheda');
  var lento=window.matchMedia('(prefers-reduced-motion: reduce)');

  function lin(v){v/=255;return v<=.04045?v/12.92:Math.pow((v+.055)/1.055,2.4)}
  function lum(h){return .2126*lin(parseInt(h.substr(1,2),16))+.7152*lin(parseInt(h.substr(3,2),16))+.0722*lin(parseInt(h.substr(5,2),16))}
  function chiaro(h,k){var L=lum(h)*(k||1);return (L+.05)/(.0106+.05) > (.889+.05)/(L+.05)}  /* inchiostro o carta: vince il contrasto maggiore */
  /* sopra il drappo il testo sta anche nelle pieghe in ombra: la scelta si fa su un tono scurito del 35% */
  function chiaroDrappo(h){return chiaro(h,.65)}
  function scansione(c){return B+c.i}
  function scansione2(c){return B+'c2'+c.i.slice(1)}

  /* etichetta corta sulla linguetta e codice grande: il numero, se c'è e non si ripete; altrimenti il nome del colore */
  A.forEach(function(a){
    var corti=a.c.map(function(c){var m=c.l.match(/(\d+(?:-\d+)?)$/);return m?m[1]:c.l});
    a.c.forEach(function(c,i){var k=corti[i];c.k=(corti.indexOf(k)!==corti.lastIndexOf(k))?c.l:k});
  });

  var art=-1, col=-1, bott=[];
  function righeScheda(a){
    var r=[['Materiale',a.mat]];
    if(a.sp)r.push(['Spessore',a.sp]);
    if(a.dis)r.push(['Disegno',a.dis]);
    if(a.uso)r.push(['Uso',a.uso]);
    r.push(['Colori',a.c.length+' a campione']);
    return r.map(function(x){return '<dt>'+x[0]+'</dt><dd>'+x[1].replace(/(\d) mm/,'$1&nbsp;mm')+'</dd>'}).join('');
  }
  function riempiScheda(a){sch.innerHTML=righeScheda(a)}
  function misuraScheda(){
    var p=sch.cloneNode(false);p.removeAttribute('id');p.setAttribute('aria-hidden','true');
    p.style.cssText='position:absolute;visibility:hidden;left:0;top:0;min-height:0;width:'+sch.clientWidth+'px';
    sch.parentNode.appendChild(p);var hmax=0;
    A.forEach(function(a){p.innerHTML=righeScheda(a);hmax=Math.max(hmax,p.offsetHeight)});
    p.remove();sch.style.minHeight=hmax+'px';
  }
  function adatta(){
    /* nome e codice devono stare nella riga: se no il codice si stringe, poi anche il nome */
    root.style.setProperty('--k-c',1);root.style.setProperty('--k-n',1);
    var w=riga.clientWidth-parseFloat(getComputedStyle(riga).paddingLeft)*2, col1=getComputedStyle(riga).flexDirection==='column';
    var wn=nome.getBoundingClientRect().width, wc=cod.getBoundingClientRect().width, g=col1?0:24;
    if(col1){
      if(wc>w)root.style.setProperty('--k-c',(w/wc).toFixed(3));
      if(wn>w)root.style.setProperty('--k-n',(w/wn).toFixed(3));
    }else if(wn+wc+g>w){
      var kc=Math.max(.42,(w-wn-g)/wc);root.style.setProperty('--k-c',kc.toFixed(3));
      if(wn+wc*kc+g>w)root.style.setProperty('--k-n',((w-wc*kc-g)/wn).toFixed(3));
    }
  }
  function apriArticolo(i,ci){
    var a=A[i];art=i;
    mz.innerHTML='';bott=[];col=-1;
    mz.style.setProperty('--n',a.c.length);
    mz.setAttribute('aria-label','Colori di '+a.n);
    a.c.forEach(function(c,j){
      var b=document.createElement('button');
      b.type='button';b.className='ppl-linguetta '+(chiaro(c.h)?'su-chiaro':'su-scuro');
      b.setAttribute('role','radio');b.setAttribute('aria-checked','false');b.setAttribute('aria-label',c.t);
      b.style.backgroundImage='url('+scansione(c)+')';b.style.backgroundColor=c.h;
      var et=document.createElement('span');et.className=c.k.length>4&&!/^\d+$/.test(c.k)?'et lunga':'et';et.textContent=c.k;b.appendChild(et);b.tabIndex=-1;
      b.addEventListener('click',function(){scegli(j,false)});
      mz.appendChild(b);bott.push(b);
    });
    nome.textContent=a.n;cn.textContent=a.n;riempiScheda(a);
    document.querySelectorAll('.ppl-dorso').forEach(function(d,k){d.setAttribute('aria-checked',k===i?'true':'false');d.tabIndex=k===i?0:-1});
    scegli(ci||0,false);
  }
  function scegli(j,fuoco){
    var a=A[art];
    if(j<0)j=a.c.length-1; if(j>=a.c.length)j=0;
    if(col>=0&&bott[col]){bott[col].setAttribute('aria-checked','false');bott[col].tabIndex=-1}
    col=j;var c=a.c[j],b=bott[j];
    b.setAttribute('aria-checked','true');b.tabIndex=0;if(fuoco)b.focus({preventScroll:true});
    /* tono sotto il drappo e opacità della mappa: tarati in finale_drappo.py perché la zona centrale del drappo
       abbia il colore della scansione (delta E medio sotto 2) */
    var base=c.b||c.h, ch=chiaroDrappo(base);
    root.style.setProperty('--tono',c.h);
    root.style.setProperty('--base',base);
    root.style.setProperty('--drappo-op',c.o||1);
    root.style.setProperty('--su-tono',ch?'#1A1817':'#F6F3EE');
    root.style.setProperty('--su-tono-2',ch?'rgba(26,24,23,.72)':'rgba(246,243,238,.8)');
    document.body.classList.toggle('ppl-tema-chiaro',ch);
    cod.textContent=c.k;cc.textContent=c.l;
    img.srcset=scansione(c)+' 350w, '+scansione2(c)+' 640w';img.src=scansione(c);img.alt='Scansione del campione '+c.t;
    adatta();
    if(mz.scrollWidth>mz.clientWidth+2){mz.scrollLeft=Math.max(0,b.offsetLeft-(mz.clientWidth-b.offsetWidth)/2)}
  }
  mz.addEventListener('keydown',function(e){
    var k=e.key,n=null;
    if(k==='ArrowRight'||k==='ArrowDown')n=col+1;else if(k==='ArrowLeft'||k==='ArrowUp')n=col-1;else if(k==='Home')n=0;else if(k==='End')n=A[art].c.length-1;
    if(n!==null){e.preventDefault();scegli(n,true)}
  });

  /* i dorsi: un tocco apre la cartella di quell'articolo in cima alla pagina */
  var ds=document.getElementById('ppl-dorsi');
  function vaiSu(){ap.scrollIntoView({behavior:lento.matches?'auto':'smooth',block:'start'});if(bott[col])bott[col].focus({preventScroll:true})}
  if(ds){
    A.forEach(function(a,i){
      var b=document.createElement('button');b.type='button';b.className='ppl-dorso '+(a.dc?'chiaro':'scuro');
      b.setAttribute('role','radio');b.setAttribute('aria-checked','false');b.tabIndex=-1;
      b.style.backgroundImage='url('+B+a.dorso+')';
      b.setAttribute('aria-label',a.n+', '+a.c.length+' colori');
      b.innerHTML='<span class="nd">'+a.n+'</span><span class="cc">'+a.c.length+'</span>';
      b.addEventListener('click',function(){apriArticolo(i,a.dk);vaiSu()});
      ds.appendChild(b);
    });
    ds.addEventListener('keydown',function(e){
      var k=e.key,n=null;
      if(k==='ArrowRight'||k==='ArrowDown')n=art+1;else if(k==='ArrowLeft'||k==='ArrowUp')n=art-1;else if(k==='Home')n=0;else if(k==='End')n=A.length-1;
      if(n===null)return;e.preventDefault();n=(n+A.length)%A.length;
      var d=ds.children;d[art].tabIndex=-1;apriArticolo(n,A[n].dk);d[n].focus();
    });
  }

  /* gli usi: i nomi degli articoli aprono la cartella */
  document.querySelectorAll('.ppl-nomi').forEach(function(ul){
    ul.getAttribute('data-art').split(' ').forEach(function(x){
      var i=perNome[x],li=document.createElement('li'),b=document.createElement('button');
      if(i===undefined)return;
      b.type='button';b.textContent=A[i].n;b.setAttribute('aria-label','Apri la cartella '+A[i].n);
      b.addEventListener('click',function(){apriArticolo(i,A[i].dk);vaiSu()});
      li.appendChild(b);ul.appendChild(li);
    });
  });

  apriArticolo(perNome.BOTTICELLI,A[perNome.BOTTICELLI].dk);
  misuraScheda();
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){misuraScheda();adatta()});
  window.addEventListener('resize',function(){misuraScheda();adatta()});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',pplAvvia);else pplAvvia();
