// 247LAB, foto ingrandibili (schede prodotto e progetti). Ogni foto e' un link al suo file piu' grande: senza
// JavaScript si apre il file; con JavaScript si apre qui sopra, sul nero, con le frecce per le altre foto del gruppo.
// Esc o "Chiudi" chiudono e il fuoco torna alla foto da cui si e' partiti. Nessuna animazione.
(function(){
  var link=[].slice.call(document.querySelectorAll('a.ingrandisci'));
  if(!link.length||typeof HTMLDialogElement!=='function')return;
  var d=document.createElement('dialog');
  d.className='lente';d.setAttribute('aria-label','Foto ingrandita');
  d.innerHTML='<img alt=""><p class="lente-riga"><span class="lente-conta num" aria-live="polite"></span>'
    +'<button type="button" class="lente-prec">Precedente</button><button type="button" class="lente-succ">Successiva</button>'
    +'<button type="button" class="lente-chiudi">Chiudi</button></p>';
  document.body.appendChild(d);
  var im=d.querySelector('img'),conta=d.querySelector('.lente-conta'),gruppo=[],i=0,da=null;
  function mostra(n){
    i=(n+gruppo.length)%gruppo.length;var a=gruppo[i],x=a.querySelector('img');
    im.src=a.getAttribute('href');im.alt=x?x.alt:'';
    conta.textContent=gruppo.length>1?(i+1)+' di '+gruppo.length:'';
    d.querySelector('.lente-prec').hidden=d.querySelector('.lente-succ').hidden=gruppo.length<2;
  }
  link.forEach(function(a){
    a.addEventListener('click',function(e){
      if(e.metaKey||e.ctrlKey||e.shiftKey)return;
      e.preventDefault();da=a;
      var g=a.getAttribute('data-gruppo');
      gruppo=link.filter(function(b){return b.getAttribute('data-gruppo')===g&&b.offsetParent!==null;});
      if(gruppo.indexOf(a)<0)gruppo=[a];
      mostra(gruppo.indexOf(a));d.showModal();d.querySelector('.lente-chiudi').focus();
    });
  });
  d.querySelector('.lente-prec').addEventListener('click',function(){mostra(i-1);});
  d.querySelector('.lente-succ').addEventListener('click',function(){mostra(i+1);});
  d.querySelector('.lente-chiudi').addEventListener('click',function(){d.close();});
  d.addEventListener('keydown',function(e){
    if(e.key==='ArrowRight'&&gruppo.length>1){e.preventDefault();mostra(i+1);}
    if(e.key==='ArrowLeft'&&gruppo.length>1){e.preventDefault();mostra(i-1);}
  });
  d.addEventListener('click',function(e){if(e.target===d||e.target===im)d.close();});
  d.addEventListener('close',function(){im.removeAttribute('src');if(da)da.focus();});
})();
