/* Villa Eidos: testata che si compatta scorrendo, menu del telefono e anno nel piede. */
(function(){
  "use strict";
  // testata: sotto i primi 24 px di scorrimento si compatta (classe "compatta"; la transizione c'e' solo con ve-moto)
  var testa = document.getElementById('testa');
  if (testa) {
    var compatta = function(){ testa.classList.toggle('compatta', (window.scrollY || window.pageYOffset) > 24); };
    window.addEventListener('scroll', compatta, {passive: true});
    compatta();
  }
  var menu = document.getElementById('menu'), apri = document.querySelector('.testa .apri-menu');
  if (menu && apri) {
    var chiudi = menu.querySelector('.chiudi-menu');
    var stato = function(aperto){
      menu.classList.toggle('aperto', aperto);
      apri.setAttribute('aria-expanded', aperto ? 'true' : 'false');
      document.documentElement.style.overflow = aperto ? 'hidden' : '';
      (aperto ? chiudi : apri).focus();
    };
    apri.addEventListener('click', function(){ stato(true); });
    chiudi.addEventListener('click', function(){ stato(false); });
    Array.prototype.forEach.call(menu.querySelectorAll('nav a'), function(a){ a.addEventListener('click', function(){ stato(false); }); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && menu.classList.contains('aperto')) stato(false); });
  }
  Array.prototype.forEach.call(document.querySelectorAll('.piede .anno'), function(el){ el.textContent = new Date().getFullYear(); });
})();
