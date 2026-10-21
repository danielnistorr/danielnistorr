// 247LAB, progetti: il filtro dell'archivio per tipo e per anni. Senza JavaScript si vedono tutti i progetti.
(function(){
  var f=document.querySelector('.progetti-filtro'),lista=document.getElementById('lista');
  if(!f||!lista)return;
  var voci=[].slice.call(lista.children),conta=document.getElementById('conta'),vuoto=document.getElementById('vuoto');
  var stato={tipo:'',periodo:''};
  function forme(){
    // le righe di due: 7 + 5 colonne, poi 5 + 7, contando solo i progetti visibili
    var n=0;
    voci.forEach(function(v){if(v.hidden)return;var riga=Math.floor(n/2)%2,largo=(n%2)===riga;
      v.classList.toggle('p-largo',largo);v.classList.toggle('p-stretto',!largo);n++;});
    return n;
  }
  function applica(){
    voci.forEach(function(v){
      var ok=(!stato.tipo||v.getAttribute('data-tipo')===stato.tipo)&&(!stato.periodo||(' '+v.getAttribute('data-periodi')+' ').indexOf(' '+stato.periodo+' ')>-1);
      v.hidden=!ok;
    });
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
    var b=e.target.closest('button');if(!b)return;
    if(b.hasAttribute('data-tipo'))scegli('tipo',b.getAttribute('data-tipo'));
    else if(b.hasAttribute('data-periodo'))scegli('periodo',b.getAttribute('data-periodo'));
  });
  var az=document.getElementById('azzera');
  if(az)az.addEventListener('click',function(){scegli('tipo','');scegli('periodo','');var t=f.querySelector('[data-tipo=""]');if(t)t.focus();});
  f.hidden=false;
})();
