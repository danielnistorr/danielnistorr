// 247LAB, filtro delle collezioni: bottoni veri (aria-pressed), tastiera e dito; senza JavaScript si vede tutto.
(function(){
  var cat=document.querySelector('[data-catalogo]');
  if(!cat)return;
  var barra=cat.querySelector('.filtri'),esito=cat.querySelector('.filtri-esito');
  var sezioni=[].slice.call(cat.querySelectorAll('[data-famiglia]'));
  var scelta={famiglia:'',finitura:''};
  var parola=function(n){return n===1?'modello':'modelli';};
  function applica(annuncia){
    var tot=0;
    sezioni.forEach(function(s){
      var vis=0,okF=!scelta.famiglia||s.getAttribute('data-famiglia')===scelta.famiglia;
      [].forEach.call(s.querySelectorAll('[data-finiture]'),function(v){
        var ok=okF&&(!scelta.finitura||('|'+v.getAttribute('data-finiture')+'|').indexOf('|'+scelta.finitura+'|')>-1);
        v.hidden=!ok;if(ok)vis++;
      });
      s.hidden=vis===0;tot+=vis;
    });
    [].forEach.call(barra.querySelectorAll('button[data-chiave]'),function(b){
      b.setAttribute('aria-pressed',scelta[b.getAttribute('data-chiave')]===b.getAttribute('data-valore')?'true':'false');
    });
    if(annuncia!==false)esito.textContent=tot+' '+parola(tot)+(tot===0?': prova un altro filtro.':'');
  }
  barra.hidden=false;
  barra.addEventListener('click',function(ev){
    var b=ev.target.closest('button[data-chiave]');if(!b)return;
    scelta[b.getAttribute('data-chiave')]=b.getAttribute('data-valore');
    applica();
    if(history.replaceState){history.replaceState(null,'',scelta.famiglia?'#'+scelta.famiglia:location.pathname+location.search);}
  });
  var h=decodeURIComponent(location.hash.slice(1));
  if(h&&sezioni.some(function(s){return s.getAttribute('data-famiglia')===h;})){
    scelta.famiglia=h;applica();
    var t=document.getElementById('catalogo');if(t)t.scrollIntoView();
  }else{applica(false);}
})();
