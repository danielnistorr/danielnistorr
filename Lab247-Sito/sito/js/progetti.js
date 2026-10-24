// 247LAB, progetti: il filtro dell'archivio per tipo e per anni. Senza JavaScript si vedono tutti i progetti.
(function(){
  var f=document.querySelector('.progetti-filtro'),lista=document.getElementById('lista');
  if(!f||!lista)return;
  var voci=[].slice.call(lista.children),conta=document.getElementById('conta'),vuoto=document.getElementById('vuoto');
  var stato={tipo:'',periodo:''};
  function forme(){
    // i primi due visibili in grande (7 + 5 colonne), poi tre per riga
    var n=0;
    voci.forEach(function(v){if(v.hidden)return;
      v.classList.toggle('p-largo',n===0);v.classList.toggle('p-stretto',n===1);v.classList.toggle('p-terzo',n>1);n++;});
    return n;
  }
  function passa(v,tipo,periodo){
    return (!tipo||v.getAttribute('data-tipo')===tipo)&&(!periodo||(' '+v.getAttribute('data-periodi')+' ').indexOf(' '+periodo+' ')>-1);
  }
  // i numeri accanto alle voci seguono l'altro filtro; le voci che darebbero 0 progetti si spengono
  function numeri(){
    f.querySelectorAll('button[data-tipo],button[data-periodo]').forEach(function(b){
      var t=b.hasAttribute('data-tipo'),val=b.getAttribute(t?'data-tipo':'data-periodo');
      var n=voci.filter(function(v){return t?passa(v,val,stato.periodo):passa(v,stato.tipo,val);}).length;
      var sp=b.querySelector('.n');if(sp)sp.textContent=n;
      if(val&&n===0)b.setAttribute('aria-disabled','true');else b.removeAttribute('aria-disabled');
    });
  }
  function applica(){
    voci.forEach(function(v){v.hidden=!passa(v,stato.tipo,stato.periodo);});
    numeri();
    var n=forme();
    conta.textContent=n;
    conta.parentNode.lastChild.textContent=n===1?' progetto':' progetti';
    vuoto.hidden=n>0;
  }
  function scegli(gruppo,valore){
    stato[gruppo]=valore;
    f.querySelectorAll('[data-'+gruppo+']').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-'+gruppo)===valore?'true':'false');});
    applica();
  }
  f.addEventListener('click',function(e){
    var b=e.target.closest('button');if(!b||b.getAttribute('aria-disabled')==='true')return;
    if(b.hasAttribute('data-tipo'))scegli('tipo',b.getAttribute('data-tipo'));
    else if(b.hasAttribute('data-periodo'))scegli('periodo',b.getAttribute('data-periodo'));
  });
  var az=document.getElementById('azzera');
  if(az)az.addEventListener('click',function(){scegli('tipo','');scegli('periodo','');var t=f.querySelector('[data-tipo=""]');if(t)t.focus();});
  numeri();
  f.hidden=false;
})();
