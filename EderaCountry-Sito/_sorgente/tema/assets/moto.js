/* Edera Country House: traduce le classi dei movimenti (scritte in Elementor, Classi CSS) negli attributi
   del kit HE (he.js), prima che il kit parta. Vedi inc/movimento.php.
     moto-righe     -> data-he-split sul titolo (+ data-he-subito se e' nella prima schermata)
     moto-taglio    -> data-he-wipe="su" su una cornice intorno alla foto (la didascalia resta ferma)
     moto-testata   -> data-he-header sulla testata e data-he-chiara-dopo="#<questo contenitore>" */
(function(){
  "use strict";
  // con "riduci movimento" non si tocca niente: la pagina resta quella ferma (il kit non parte)
  if (!window.matchMedia || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var d = document;
  var tutti = function(s){ return Array.prototype.slice.call(d.querySelectorAll(s)); };

  // SplitText tratta lo spazio unificatore (&nbsp;) come uno spazio normale: le parole unite restano unite
  // in un <span> che non va a capo, cosi' le righe sono le stesse della pagina ferma
  function unisci(el){
    var w = d.createTreeWalker(el, NodeFilter.SHOW_TEXT), testi = [], n;
    while ((n = w.nextNode())) if (n.nodeValue.indexOf('\u00a0') > -1) testi.push(n);
    testi.forEach(function(t){
      var pezzi = t.nodeValue.split(/(\S+(?:\u00a0\S+)+)/), f = d.createDocumentFragment();
      pezzi.forEach(function(p, i){
        if (!p) return;
        if (i % 2) { var s = d.createElement('span'); s.className = 'he-unito'; s.textContent = p; f.appendChild(s); }
        else f.appendChild(d.createTextNode(p));
      });
      t.parentNode.replaceChild(f, t);
    });
  }

  // un titolo fatto di <span> che vanno a capo da soli (come "Gli eventi" / "che lasciano il segno.")
  // diventa testo con <br>: SplitText tiene gli a capo e il titolo resta sulle stesse righe della pagina ferma
  function righe(el){
    var figli = Array.prototype.slice.call(el.children);
    if (!figli.length || !figli.every(function(c){ return c.tagName === 'SPAN' && getComputedStyle(c).display === 'block'; })) return;
    var testi = figli.map(function(c){ return c.textContent; });
    el.textContent = '';
    testi.forEach(function(x, i){ if (i) el.appendChild(d.createElement('br')); el.appendChild(d.createTextNode(x + (i < testi.length - 1 ? ' ' : ''))); });
    el.classList.add('he-righe');
  }

  tutti('.moto-righe').forEach(function(el){
    var t = el.querySelector('.elementor-heading-title') || el;
    righe(t);
    if (getComputedStyle(t).whiteSpace !== 'nowrap') unisci(t); // sulle righe che non vanno a capo non serve
    t.setAttribute('data-he-split', '');
    if (t.getBoundingClientRect().top < window.innerHeight) t.setAttribute('data-he-subito', '');
  });

  tutti('.moto-taglio, .moto-taglio-sinistra, .moto-taglio-destra').forEach(function(el){
    var verso = el.classList.contains('moto-taglio-sinistra') ? 'sinistra' : (el.classList.contains('moto-taglio-destra') ? 'destra' : 'su');
    var foto = el.querySelector('picture') || el.querySelector('img');
    if (!foto) return;
    var cornice = d.createElement('span');
    cornice.className = 'he-taglio';
    foto.parentNode.insertBefore(cornice, foto);
    cornice.appendChild(foto);
    cornice.setAttribute('data-he-wipe', verso);
  });

  var dopo = d.querySelector('.moto-testata'), testa = d.querySelector('.testa');
  if (dopo && testa) {
    if (!dopo.id) dopo.id = 'edera-apertura';
    testa.setAttribute('data-he-header', '');
    testa.setAttribute('data-he-chiara-dopo', '#' + dopo.id);
  }
})();
