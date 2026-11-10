/* Edera Country House: planimetria (shortcode [edera_planimetria], inc/planimetria.php).
   - Pallini: un clic o un tocco apre la scheda breve (nome, capienza, azioni); Esc o un clic fuori la chiude.
   - "Scegli nel preventivo": spunta lo spazio nel calcolatore con la sua casella e il suo evento "change"
     (i conti li fa solo il calcolatore), poi il link porta al preventivo.
   - "Vedi le foto": galleria a schermo intero. Le foto si caricano solo all'apertura. Focus chiuso nella
     finestra, Esc, frecce, scorrimento col dito, pagina sotto ferma (anche lo scorrimento morbido, se c'e'),
     focus restituito a chi l'ha aperta.
   Nessuna animazione: le cose compaiono e spariscono di colpo. */
(function(){
  "use strict";
  var d = document;
  var tutti = function(s, b){ return Array.prototype.slice.call((b || d).querySelectorAll(s)); };

  tutti('[data-planimetria]').forEach(function(box){
    var aperta = null; // il pallino con la scheda aperta

    function chiudiScheda(rimettiFocus){
      if (!aperta) return;
      var p = aperta; aperta = null;
      p.setAttribute('aria-expanded', 'false');
      d.getElementById(p.getAttribute('aria-controls')).hidden = true;
      if (rimettiFocus) p.focus();
    }
    function apriScheda(p){
      chiudiScheda(false);
      aperta = p;
      p.setAttribute('aria-expanded', 'true');
      d.getElementById(p.getAttribute('aria-controls')).hidden = false;
    }
    tutti('.pl-punto', box).forEach(function(p){
      p.addEventListener('click', function(e){
        e.stopPropagation();
        if (aperta === p) chiudiScheda(false); else apriScheda(p);
      });
    });
    tutti('.pl-scheda', box).forEach(function(s){ s.addEventListener('click', function(e){ e.stopPropagation(); }); });
    d.addEventListener('click', function(){ chiudiScheda(false); });
    d.addEventListener('keydown', function(e){
      if (e.key === 'Escape' && aperta && !galleriaAperta()) chiudiScheda(true);
    });

    // "Scegli nel preventivo": solo se nella pagina c'e' il calcolatore con quello spazio
    tutti('.pl-scegli', box).forEach(function(a){
      var casella = d.getElementById('s-' + a.getAttribute('data-spazio'));
      if (!casella || !d.getElementById('calcolo')) { a.hidden = true; return; }
      a.addEventListener('click', function(){
        if (!casella.checked) {
          casella.checked = true;
          casella.dispatchEvent(new Event('change', { bubbles: true }));
        }
        chiudiScheda(false);
      });
    });

    // ------------------------------------------------------------- galleria
    var g = box.querySelector('.pl-galleria');
    if (!g) return;
    var foto = g.querySelector('.pl-g-foto'), didascalia = g.querySelector('.pl-g-didascalia');
    var conta = g.querySelector('.pl-g-conta'), mini = tutti('.pl-mini', g);
    var chiudi = g.querySelector('.pl-chiudi'), corrente = 0, daChi = null, caricate = false;
    function galleriaAperta(){ return !g.hidden; }

    function mostra(i){
      corrente = (i + mini.length) % mini.length;
      var m = mini[corrente];
      if (m.getAttribute('data-srcset')) foto.setAttribute('srcset', m.getAttribute('data-srcset')); else foto.removeAttribute('srcset');
      foto.src = m.getAttribute('data-src');
      foto.alt = m.getAttribute('data-didascalia');
      didascalia.textContent = m.getAttribute('data-didascalia');
      conta.textContent = (corrente + 1) + ' / ' + mini.length;
      mini.forEach(function(b, j){ b.setAttribute('aria-current', j === corrente ? 'true' : 'false'); });
    }
    function apri(chi){
      daChi = chi || d.activeElement;
      chiudiScheda(false);
      if (!caricate) {
        mini.forEach(function(b){ var im = b.querySelector('img'); im.src = im.getAttribute('data-src'); });
        caricate = true;
      }
      mostra(0);
      g.hidden = false;
      d.documentElement.classList.add('pl-bloccato');
      if (window.heLenis && window.heLenis.stop) window.heLenis.stop();
      chiudi.focus();
    }
    function esci(){
      g.hidden = true;
      d.documentElement.classList.remove('pl-bloccato');
      if (window.heLenis && window.heLenis.start) window.heLenis.start();
      if (daChi && daChi.focus) daChi.focus();
    }
    tutti('.pl-apri-foto', box).forEach(function(b){
      b.hidden = false;
      b.addEventListener('click', function(e){
        e.stopPropagation();
        // dalla scheda il focus torna al pallino, che resta sulla mappa
        var p = b.closest('.pl-pallino');
        apri(p ? p.querySelector('.pl-punto') : b);
      });
    });
    chiudi.addEventListener('click', esci);
    g.querySelector('.pl-prec').addEventListener('click', function(){ mostra(corrente - 1); });
    g.querySelector('.pl-succ').addEventListener('click', function(){ mostra(corrente + 1); });
    mini.forEach(function(b, j){ b.addEventListener('click', function(){ mostra(j); }); });
    g.addEventListener('click', function(e){ if (e.target === g) esci(); });
    g.addEventListener('keydown', function(e){
      if (e.key === 'Escape') { e.preventDefault(); esci(); return; }
      if (e.key === 'ArrowRight') { e.preventDefault(); mostra(corrente + 1); return; }
      if (e.key === 'ArrowLeft') { e.preventDefault(); mostra(corrente - 1); return; }
      if (e.key === 'Tab') {
        var f = tutti('button', g).filter(function(x){ return x.offsetParent !== null; });
        var primo = f[0], ultimo = f[f.length - 1];
        if (e.shiftKey && d.activeElement === primo) { e.preventDefault(); ultimo.focus(); }
        else if (!e.shiftKey && d.activeElement === ultimo) { e.preventDefault(); primo.focus(); }
        else if (f.indexOf(d.activeElement) < 0) { e.preventDefault(); primo.focus(); }
      }
    });
    // scorrimento col dito
    var x0 = null, y0 = null;
    var palco = g.querySelector('.pl-g-palco');
    palco.addEventListener('touchstart', function(e){ var t = e.changedTouches[0]; x0 = t.clientX; y0 = t.clientY; }, { passive: true });
    palco.addEventListener('touchend', function(e){
      if (x0 === null) return;
      var t = e.changedTouches[0], dx = t.clientX - x0, dy = t.clientY - y0;
      x0 = null;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) mostra(corrente + (dx < 0 ? 1 : -1));
    }, { passive: true });
  });
})();
