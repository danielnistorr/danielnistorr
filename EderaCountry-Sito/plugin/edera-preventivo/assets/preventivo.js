/* Edera Preventivo: il calcolatore sul sito (shortcode [edera_preventivo]).
   Lo stesso comportamento del calcolatore originale; i conti li fa assets/calcolo.js con le regole del pannello
   (window.EDERA_PREVENTIVO). La richiesta resta una mail precompilata: il sito non riceve e non salva dati.
   Se il calendario ha regole, il campo "Data dell'evento" usa flatpickr (in locale, licenza MIT) e non lascia
   scegliere i giorni esclusi, chiusi, troppo vicini o troppo lontani. */
(function(){
  var C = window.EDERA_PREVENTIVO, E = window.EderaCalcolo;
  if (!C || !E || !document.getElementById('calcolo')) return;
  var R = C.regole, T = C.testi, euro = E.euro, EMAIL = R.testi.email;
  var $ = function(id){ return document.getElementById(id); };
  var ospiti = $('ospiti');
  var tutti = function(s){ return Array.prototype.slice.call(document.querySelectorAll(s)); };
  var scelti = function(){ return tutti('input[name="spazi"]:checked').map(function(e){ return e.value; }); };
  var servizi = function(){ return tutti('input[name="servizi"]:checked').map(function(e){ return Number(e.value); }); };
  var durataIntera = document.querySelector('input[name="durata"][value="1.5"]');
  var durataMezza = document.querySelector('input[name="durata"][value="1"]');
  var campoData = $('data'), calendario = null, notaData = $('data-nota');

  function aggiornaDurata(){
    var mezza = E.mezzaPossibile(R, scelti());
    durataMezza.disabled = !mezza;
    if (!mezza) durataIntera.checked = true;
    $('durata-nota').textContent = mezza ? R.durate.nota_mezza_si : R.durate.nota_mezza_no;
  }
  function durata(){ return (document.querySelector('input[name="durata"]:checked') || durataIntera).value === '1' ? 'mezza' : 'intera'; }
  function calcola(){
    var r = E.calcola(R, { spazi: scelti(), ospiti: ospiti.value, durata: durata(), data: campoData.value, servizi: servizi() });
    ospiti.max = r.massimo;
    if (r.minimo > 1) ospiti.min = r.minimo;
    var nota = r.minimo > 1 ? T.daA.replace('{min}', r.minimo).replace('{max}', r.massimo) : 'Con gli spazi scelti, fino a ' + r.massimo + ' persone.';
    if (ospiti.value !== '' && r.oltre && R.testi.msg_capienza) nota = R.testi.msg_capienza.replace(/\{max\}/g, r.massimo);
    $('ospiti-nota').textContent = nota;
    if (ospiti.value !== '' && (r.oltre || r.sotto)) ospiti.value = r.n;
    var esc = function(t){ return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
    var riga = function(v){ return '<li><span>' + esc(v.nome) + '</span><b>' + euro(v.valore) + '</b></li>'; };
    var html = r.voci.map(riga).join('') + r.righe.map(riga).join('');
    html += '<li><span>Partecipanti' + (ospiti.value === '' ? ' (esempio)' : '') + '</span><b>' + r.n + '</b></li>';
    html += '<li><span>Durata</span><b>' + esc(r.durata === 'mezza' ? R.durate.mezza : R.durate.intera) + '</b></li>';
    $('totale').textContent = euro(r.totale);
    $('voci-stima').innerHTML = html;
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
  ospiti.addEventListener('input', calcola);
  campoData.addEventListener('change', function(){ controllaData(); calcola(); });

  // calendario: flatpickr, con i giorni non disponibili spenti
  if (E.calendarioAttivo(R) && window.flatpickr) {
    var l = E.limiti(R);
    calendario = window.flatpickr(campoData, {
      locale: window.flatpickr.l10ns && window.flatpickr.l10ns.it ? 'it' : 'default',
      dateFormat: 'Y-m-d', altInput: true, altFormat: 'j F Y', altInputClass: 'edp-data',
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
