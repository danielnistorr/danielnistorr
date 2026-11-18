/* Edera Country House: menu del telefono, barra fissa del telefono, anno nel piede e link alle foto dei pallini.
   Lo stesso codice del sito originale (la parte del calcolatore e' in preventivo.js). */
(function(){
  var $ = function(id){ return document.getElementById(id); };

  // menu sul telefono
  var pannello = $('pannello'), apri = document.querySelector('.testa .apri-menu');
  if (pannello && apri) {
    var chiudi = pannello.querySelector('.chiudi');
    var stato = function(aperto){
      pannello.classList.toggle('aperto', aperto); apri.setAttribute('aria-expanded', aperto ? 'true' : 'false');
      document.body.style.overflow = aperto ? 'hidden' : '';
      (aperto ? chiudi : apri).focus();
    };
    apri.addEventListener('click', function(){ stato(true); });
    chiudi.addEventListener('click', function(){ stato(false); });
    pannello.querySelectorAll('nav a').forEach(function(a){ a.addEventListener('click', function(){ stato(false); }); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && pannello.classList.contains('aperto')) stato(false); });
  }

  // barra fissa sul telefono: compare dopo l'apertura, si toglie sul preventivo e sui contatti (senza animazioni)
  var barra = $('barra'), visti = {};
  var guarda = [document.querySelector('.apertura'), $('preventivo'), $('contatti')].filter(Boolean);
  if (barra && 'IntersectionObserver' in window) {
    var oss = new IntersectionObserver(function(voci){
      voci.forEach(function(v){ visti[v.target.id === 'preventivo' || v.target.id === 'contatti' ? v.target.id : 'apertura'] = v.isIntersecting; });
      barra.classList.toggle('su', !visti.apertura && !visti.preventivo && !visti.contatti);
    }, {threshold: 0});
    guarda.forEach(function(el){ oss.observe(el); });
  }
  if ($('anno')) $('anno').textContent = new Date().getFullYear();

  // planimetria: un link "#foto-<nome>" (per esempio sul pallino della Serra) apre il lightbox di Elementor
  // sulla galleria che in Avanzato > ID CSS ha "foto-<nome>", anche se la galleria e' nascosta su tutti i
  // dispositivi. Se la galleria non c'e', il link non fa niente. Nell'editor di Elementor il clic serve solo a
  // scegliere il pallino da modificare: la pagina non salta alla galleria.
  document.addEventListener('click', function(e){
    var a = e.target && e.target.closest ? e.target.closest('a[href^="#foto-"]') : null;
    if (!a) return;
    e.preventDefault();
    if (document.body.classList.contains('elementor-editor-active')) return;
    e.stopPropagation();
    var box = document.getElementById(a.getAttribute('href').slice(1));
    var prima = box && box.querySelector('a[data-elementor-open-lightbox]');
    if (prima) prima.click();
  }, true);
})();
