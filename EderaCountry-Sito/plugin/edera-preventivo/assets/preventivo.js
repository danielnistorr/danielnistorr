/* Edera Preventivo: il calcolatore sul sito (shortcode [edera_preventivo]).
   Lo stesso comportamento del calcolatore originale; i conti li fa assets/calcolo.js con le regole del pannello
   (window.EDERA_PREVENTIVO). La richiesta resta una mail precompilata: il sito non riceve e non salva dati.
   Se il calendario ha regole, il campo "Data dell'evento" usa flatpickr (in locale, licenza MIT) e non lascia
   scegliere i giorni esclusi, chiusi, troppo vicini o troppo lontani.
   Servizi e dotazioni (dalla 1.1.0): una voce legata a certi spazi compare solo con uno di quegli spazi (tolto lo
   spazio, si nasconde e si toglie la spunta); la quantita' scritta da chi compila non supera il massimo; quella
   automatica si legge sotto il nome ("65 sedie per 65 persone"). */
(function(){
  var C = window.EDERA_PREVENTIVO, E = window.EderaCalcolo;
  if (!C || !E || !document.getElementById('calcolo')) return;
  var R = C.regole, T = C.testi, euro = E.euro, EMAIL = R.testi.email;
  var $ = function(id){ return document.getElementById(id); };
  var ospiti = $('ospiti');
  var tutti = function(s){ return Array.prototype.slice.call(document.querySelectorAll(s)); };
  var scelti = function(){ return tutti('input[name="spazi"]:checked').map(function(e){ return e.value; }); };
  var servizi = function(){ return tutti('input[name="servizi"]:checked').filter(function(e){ var c = e.closest('[data-voce]'); return !c || !c.hidden; }).map(function(e){ return Number(e.value); }); };
  var quantita = function(){ var q = {}; tutti('input.edp-q').forEach(function(e){ q[e.getAttribute('data-voce')] = e.value; }); return q; };
  var durataIntera = document.querySelector('input[name="durata"][value="1.5"]');
  var durataMezza = document.querySelector('input[name="durata"][value="1"]');
  var campoData = $('data'), calendario = null, notaData = $('data-nota'), noteStima = $('stima-note');

  function aggiornaDurata(){
    var mezza = E.mezzaPossibile(R, scelti());
    durataMezza.disabled = !mezza;
    if (!mezza) durataIntera.checked = true;
    $('durata-nota').textContent = mezza ? R.durate.nota_mezza_si : R.durate.nota_mezza_no;
  }
  function durata(){ return (document.querySelector('input[name="durata"]:checked') || durataIntera).value === '1' ? 'mezza' : 'intera'; }
  // le voci dei servizi e dotazioni che ci sono con gli spazi scelti; un gruppo senza voci si nasconde
  function aggiornaVoci(){
    var chiavi = scelti();
    tutti('.edp-servizi [data-voce]:not(.edp-auto):not(.edp-q)').forEach(function(el){
      var x = R.servizi[Number(el.getAttribute('data-voce'))], si = !!x && E.voceDisponibile(x, chiavi);
      el.hidden = !si;
      var c = el.querySelector('input[name="servizi"]');
      if (!si && c) c.checked = false;
    });
    tutti('.edp-compresi').forEach(function(el){ el.hidden = !el.querySelector('li:not([hidden])'); });
    tutti('.edp-servizi').forEach(function(el){ el.hidden = !el.querySelector('.spazio[data-voce]:not([hidden]), li[data-voce]:not([hidden])'); });
  }
  function calcola(){
    aggiornaVoci();
    var r = E.calcola(R, { spazi: scelti(), ospiti: ospiti.value, durata: durata(), data: campoData.value, servizi: servizi(), quantita: quantita() });
    // quantita' automatica: "65 sedie per 65 persone"
    tutti('.edp-auto[data-voce]').forEach(function(el){
      var i = Number(el.getAttribute('data-voce')), v = r.info[i];
      el.textContent = v && v.auto ? E.testoAuto(R.servizi[i], v, r.n) : '';
    });
    // con "rigido" il massimo e' la capienza; se si puo' superare, solo l'eventuale massimo assoluto
    if (r.limite > 0) ospiti.max = r.limite; else ospiti.removeAttribute('max');
    if (r.minimo > 1) ospiti.min = r.minimo;
    var nota = r.modo !== 'rigido' ? E.riempi(R.testi.nota_capienza, { capienza: r.capienza })
      : (r.minimo > 1 ? T.daA.replace('{min}', r.minimo).replace('{max}', r.limite) : 'Con gli spazi scelti, fino a ' + r.limite + ' persone.');
    if (ospiti.value !== '' && r.oltre && R.testi.msg_capienza) nota = R.testi.msg_capienza.replace(/\{max\}/g, r.limite);
    $('ospiti-nota').textContent = nota;
    if (ospiti.value !== '' && (r.oltre || r.sotto)) ospiti.value = r.n;
    var esc = function(t){ return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
    var riga = function(v){ return '<li><span>' + esc(v.nome) + '</span><b>' + euro(v.valore) + '</b></li>'; };
    // senza importo (oltre la capienza): niente prezzi, solo partecipanti e durata
    var html = r.senzaImporto ? '' : r.voci.map(riga).join('') + r.righe.map(riga).join('');
    html += '<li><span>Partecipanti' + (ospiti.value === '' ? ' (esempio)' : '') + '</span><b>' + r.n + '</b></li>';
    html += '<li><span>Durata</span><b>' + esc(r.durata === 'mezza' ? R.durate.mezza : R.durate.intera) + '</b></li>';
    $('totale').textContent = r.senzaImporto ? R.testi.da_valutare : euro(r.totale);
    $('totale').classList.toggle('edp-da-valutare', r.senzaImporto);
    $('voci-stima').innerHTML = html;
    // le note della stima: oltre la capienza, spazi a prezzo fisso, numeri fuori dalle fasce
    if (noteStima) {
      var note = E.note(R, r);
      noteStima.innerHTML = note.map(function(x){ return '<p>' + esc(x) + '</p>'; }).join('');
      noteStima.hidden = !note.length;
    }
    return r;
  }
  function controllaData(){
    if (!E.calendarioAttivo(R) || !notaData) return true;
    var d = E.disponibile(R, campoData.value);
    notaData.textContent = d.ok ? '' : R.testi.msg_data;
    notaData.hidden = d.ok;
    return d.ok;
  }

  tutti('input[name="spazi"]').forEach(function(el){
    el.addEventListener('change', function(){ if (!scelti().length) el.checked = true; aggiornaDurata(); calcola(); });
  });
  tutti('input[name="durata"]').forEach(function(el){ el.addEventListener('change', calcola); });
  tutti('input[name="servizi"]').forEach(function(el){ el.addEventListener('change', calcola); });
  // la quantita' scritta: fino al massimo disponibile (si corregge subito), almeno 1 (quando si lascia il campo)
  tutti('input.edp-q').forEach(function(el){
    el.addEventListener('input', function(){ if (el.max !== '' && Number(el.value) > Number(el.max)) el.value = el.max; calcola(); });
    el.addEventListener('change', function(){ if (!(Math.floor(Number(el.value)) >= 1)) el.value = 1; else el.value = Math.floor(Number(el.value)); calcola(); });
  });
  ospiti.addEventListener('input', calcola);
  campoData.addEventListener('change', function(){ controllaData(); calcola(); });

  // calendario: flatpickr, con i giorni non disponibili spenti
  if (E.calendarioAttivo(R) && window.flatpickr) {
    var l = E.limiti(R);
    // italiano con i mesi in minuscolo, come si scrivono ("8 dicembre 2026")
    var it = window.flatpickr.l10ns && window.flatpickr.l10ns.it ? Object.assign({}, window.flatpickr.l10ns.it) : null;
    if (it) {
      var minuscolo = function(x){ return x.toLowerCase(); };
      it.months = { shorthand: it.months.shorthand.map(minuscolo), longhand: it.months.longhand.map(minuscolo) };
    }
    calendario = window.flatpickr(campoData, {
      locale: it || 'default',
      dateFormat: 'Y-m-d', altInput: true, altFormat: 'j F Y', ariaDateFormat: 'j F Y', altInputClass: 'edp-data',
      disableMobile: true, animate: false, minDate: l.min, maxDate: l.max,
      disable: [function(d){ return !E.disponibile(R, E.ymd(d)).ok; }],
      onChange: function(){ controllaData(); calcola(); }
    });
    if (calendario.altInput) {
      calendario.altInput.placeholder = T.scegliData;
      calendario.altInput.setAttribute('aria-describedby', 'data-nota');
    }
  }

  $('prepara').addEventListener('click', function(){
    var errore = null;
    if (ospiti.value === '' || !ospiti.checkValidity()) errore = ospiti;
    else if (!controllaData()) errore = calendario && calendario.altInput ? calendario.altInput : campoData;
    else if (!$('privacy').checked) errore = $('privacy');
    if (errore) {
      errore.setCustomValidity(errore === ospiti ? 'Indica il numero di partecipanti.' : (errore === $('privacy') ? 'Serve il consenso per inviare la richiesta.' : R.testi.msg_data));
      errore.reportValidity(); errore.focus();
      setTimeout(function(){ errore.setCustomValidity(''); }, 0);
      return;
    }
    var d = calcola();
    var m = E.mail(R, d, {
      azienda: $('azienda').value, email: $('email').value, telefono: $('telefono').value, tipo: $('tipo').value,
      data: calendario && calendario.altInput ? calendario.altInput.value : campoData.value
    });
    $('riepilogo-testo').textContent = m.testo;
    $('invia').href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(m.oggetto) + '&body=' + encodeURIComponent(m.testo);
    $('riepilogo').classList.add('visibile');
    $('esito').textContent = 'La richiesta parte dal tuo programma di posta, verso ' + EMAIL + '.';
    $('riepilogo').scrollIntoView({block: 'nearest'});
  });
  $('copia').addEventListener('click', function(){
    var t = $('riepilogo-testo').textContent;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(t).then(function(){ $('esito').textContent = 'Riepilogo copiato: incollalo in una mail a ' + EMAIL + '.'; }, function(){ $('esito').textContent = 'Copia non riuscita: seleziona il testo qui sopra.'; });
    } else { $('esito').textContent = 'Seleziona il testo qui sopra e copialo.'; }
  });

  aggiornaDurata(); calcola();
})();
