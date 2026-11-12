/* Edera Country House: calcolatore "Preventivo flash".
   E' lo script del sito originale; i numeri (prezzi, capienze, stagione) arrivano da config/preventivo.php
   del tema attraverso window.EDERA_PREVENTIVO, invece di essere scritti qui dentro. */
(function(){
  var C = window.EDERA_PREVENTIVO;
  if (!C || !document.getElementById('calcolo')) return;
  var euro = function(n){ return new Intl.NumberFormat('it-IT',{style:'currency',currency:'EUR',maximumFractionDigits:2,minimumFractionDigits:0}).format(n); };
  var NOMI = {}, LIMITI = {};
  Object.keys(C.spazi).forEach(function(k){ NOMI[k] = C.spazi[k].nome; LIMITI[k] = Number(C.spazi[k].persone); });
  var EMAIL = C.email;
  var $ = function(id){ return document.getElementById(id); };
  var ospiti = $('ospiti');
  var scelti = function(){ return Array.prototype.slice.call(document.querySelectorAll('input[name="spazi"]:checked')).map(function(e){ return e.value; }); };
  var durataIntera = document.querySelector('input[name="durata"][value="1.5"]');
  var durataMezza = document.querySelector('input[name="durata"][value="1"]');

  // la mezza giornata solo se fra gli spazi scelti ce n'e' uno con il prezzo a mezza giornata (la piscina)
  function aggiornaDurata(){
    var mezza = scelti().some(function(x){ return C.spazi[x].mezza !== undefined; });
    durataMezza.disabled = !mezza;
    if (!mezza) durataIntera.checked = true;
    $('durata-nota').textContent = mezza ? C.notaSi : C.notaNo;
  }
  function costo(spazio, n, durata){
    var s = C.spazi[spazio];
    if (!s) return 0;
    if (s.intera !== undefined) return durata === 1 && s.mezza !== undefined ? Number(s.mezza) : Number(s.intera);
    return Number(s.base) + Math.max(0, Math.min(n, Number(s.persone)) - Number(s.incluse)) * Number(s.a_persona);
  }
  // tariffa stagionale: i mesi di config/preventivo.php (oggi dal 1/10 al 31/3)
  function stagionale(data){
    var mese = Number(data.slice(5, 7));
    return C.stagione.mesi.map(Number).indexOf(mese) > -1;
  }
  function calcola(){
    var spazi = scelti();
    var massimo = spazi.reduce(function(s, x){ return s + LIMITI[x]; }, 0);
    ospiti.max = massimo;
    $('ospiti-nota').textContent = 'Con gli spazi scelti, fino a ' + massimo + ' persone.';
    var n = Math.max(1, Number(ospiti.value) || Number(C.esempio));
    if (n > massimo) { n = massimo; if (ospiti.value !== '') ospiti.value = n; }
    var durata = Number((document.querySelector('input[name="durata"]:checked') || durataIntera).value);
    var voci = spazi.map(function(x){ return {nome: NOMI[x], valore: costo(x, n, durata)}; });
    if (stagionale($('data').value)) voci[0].valore += Number(C.stagione.supplemento);
    var totale = voci.reduce(function(s, v){ return s + v.valore; }, 0);
    $('totale').textContent = euro(totale);
    var html = voci.map(function(v){ return '<li><span>' + v.nome + '</span><b>' + euro(v.valore) + '</b></li>'; }).join('');
    html += '<li><span>Partecipanti' + (ospiti.value === '' ? ' (esempio)' : '') + '</span><b>' + n + '</b></li>';
    html += '<li><span>Durata</span><b>' + (durata === 1 ? 'Mezza giornata' : 'Giornata intera') + '</b></li>';
    $('voci-stima').innerHTML = html;
    return {spazi: spazi, n: n, durata: durata, totale: totale};
  }
  document.querySelectorAll('input[name="spazi"]').forEach(function(el){
    el.addEventListener('change', function(){ if (!scelti().length) el.checked = true; aggiornaDurata(); calcola(); });
  });
  document.querySelectorAll('input[name="durata"]').forEach(function(el){ el.addEventListener('change', calcola); });
  ospiti.addEventListener('input', calcola);
  $('data').addEventListener('change', calcola);

  $('prepara').addEventListener('click', function(){
    var errore = null;
    if (ospiti.value === '' || !ospiti.checkValidity()) errore = ospiti;
    else if (!$('privacy').checked) errore = $('privacy');
    if (errore) {
      errore.setCustomValidity(errore === ospiti ? 'Indica il numero di partecipanti.' : 'Serve il consenso per inviare la richiesta.');
      errore.reportValidity(); errore.focus();
      setTimeout(function(){ errore.setCustomValidity(''); }, 0);
      return;
    }
    var d = calcola();
    var v = function(id, vuoto){ return $(id).value.trim() || vuoto; };
    var testo = 'Richiesta di preventivo, Edera Country House\n\n' +
      'Azienda: ' + v('azienda', 'da indicare') + '\n' +
      'Email: ' + v('email', 'da indicare') + '\n' +
      'Telefono: ' + v('telefono', 'da indicare') + '\n' +
      'Tipologia di evento: ' + v('tipo', 'da indicare') + '\n' +
      'Spazi: ' + d.spazi.map(function(x){ return NOMI[x]; }).join(', ') + '\n' +
      'Data: ' + v('data', 'da concordare') + '\n' +
      'Partecipanti: ' + d.n + '\n' +
      'Durata: ' + (d.durata === 1 ? 'mezza giornata' : 'giornata intera') + '\n' +
      'Stima location: ' + euro(d.totale) + '\n\n' +
      'Importo indicativo, da confermare con la struttura.';
    $('riepilogo-testo').textContent = testo;
    $('invia').href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Richiesta di preventivo, ' + v('azienda', 'evento aziendale')) + '&body=' + encodeURIComponent(testo);
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
