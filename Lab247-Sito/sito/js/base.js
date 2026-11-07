// 247LAB, JavaScript comune a tutte le pagine (preso dalla home): menu del telefono e newsletter del piede.
(function(){
  // menu sul telefono: pannello a tutto schermo, Esc lo chiude e il fuoco torna sul bottone
  var t=document.getElementById('testata');
  if(t){
    var b=t.querySelector('.apri-menu'),l=b.querySelector('span'),h=document.documentElement;
    var chiudi=function(){t.classList.remove('aperta');h.classList.remove('menu-aperto');b.setAttribute('aria-expanded','false');l.textContent='Menu';};
    b.addEventListener('click',function(){var a=t.classList.toggle('aperta');h.classList.toggle('menu-aperto',a);b.setAttribute('aria-expanded',a?'true':'false');l.textContent=a?'Chiudi':'Menu';});
    t.querySelectorAll('.menu a').forEach(function(a){a.addEventListener('click',chiudi);});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&t.classList.contains('aperta')){chiudi();b.focus();}});
    matchMedia('(min-width:901px)').addEventListener('change',function(m){if(m.matches)chiudi();});
  }
  // newsletter: non e' ancora collegata a un servizio (vedi LEGGIMI), quindi non promette un'iscrizione
  var f=document.getElementById('newsletter'),e=document.getElementById('nl-esito');
  if(f&&e){
    f.addEventListener('submit',function(ev){ev.preventDefault();
      if(!f.email.value||!f.email.checkValidity()){e.textContent='Scrivi un indirizzo email valido.';f.email.focus();return;}
      if(!f.consenso.checked){e.textContent='Serve il consenso per iscriverti.';return;}
      e.innerHTML='L\'iscrizione apre a breve: intanto scrivici a <a href="mailto:info@247lab.it?subject=Newsletter">info@247lab.it</a>.';
    });
  }
})();
