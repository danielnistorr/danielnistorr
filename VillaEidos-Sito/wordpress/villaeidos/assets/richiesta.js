/* Villa Eidos: modulo "Richiesta di disponibilita'" (parti/richiesta.html).
   Non manda niente al sito: "Prepara la mail" compone il testo e lo mostra; "Apri la mail" lo apre nel programma
   di posta di chi scrive (mailto), "Copia il testo" lo copia. L'indirizzo e' nell'attributo data-email del modulo (config/richiesta.php). */
(function(){
  "use strict";
  var f = document.getElementById('richiesta');
  if (!f) return;
  var C = window.VILLAEIDOS_RICHIESTA || {};
  var EMAIL = f.getAttribute('data-email');
  var $ = function(id){ return document.getElementById(id); };
  var v = function(id, vuoto){ var x = ($(id).value || '').trim(); return x || vuoto; };
  function data(s){ var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s || ''); return m ? m[3] + '/' + m[2] + '/' + m[1] : ''; }
  function tipo(){ var t = f.querySelector('input[name="tipo"]:checked'); return t ? t.value : ''; }

  function errore(el, msg){
    el.setCustomValidity(msg); el.reportValidity(); el.focus();
    setTimeout(function(){ el.setCustomValidity(''); }, 0);
  }

  f.addEventListener('submit', function(e){
    e.preventDefault();
    if (!v('r-nome', '')) return errore($('r-nome'), 'Indicare il nome.');
    if (!$('r-email').value.trim() || !$('r-email').checkValidity()) return errore($('r-email'), 'Indicare un indirizzo email valido.');
    if (!tipo()) return errore(f.querySelector('input[name="tipo"]'), 'Scegliere il tipo di spazio.');
    if (!$('r-privacy').checked) return errore($('r-privacy'), 'Serve la presa visione dell\'informativa privacy.');
    var testo = 'Richiesta di disponibilità, Villa Eidos\n\n' +
      'Azienda: ' + v('r-azienda', 'da indicare') + '\n' +
      'Nome: ' + v('r-nome', '') + '\n' +
      'Email: ' + v('r-email', '') + '\n' +
      'Telefono: ' + v('r-telefono', 'da indicare') + '\n' +
      'Spazio: ' + tipo() + '\n' +
      'Data indicativa: ' + (data($('r-data').value) || 'da concordare') + '\n' +
      'Numero di persone: ' + v('r-persone', 'da indicare') + '\n' +
      (v('r-messaggio', '') ? '\nMessaggio:\n' + v('r-messaggio', '') + '\n' : '');
    var oggetto = (C.oggetto || 'Richiesta di disponibilità') + ', ' + tipo() + (v('r-azienda', '') ? ', ' + v('r-azienda', '') : '');
    var href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(oggetto) + '&body=' + encodeURIComponent(testo);
    $('riepilogo-testo').textContent = testo;
    $('r-invia').href = href;
    $('riepilogo').hidden = false;
    $('r-esito').textContent = 'La mail parte dal proprio programma di posta. Se non si apre, copiare il testo e mandarlo a ' + EMAIL + '.';
    $('riepilogo').scrollIntoView({block: 'nearest'});
  });

  $('r-copia').addEventListener('click', function(){
    var t = $('riepilogo-testo').textContent;
    var ok = function(){ $('r-esito').textContent = 'Testo copiato: incollarlo in una mail a ' + EMAIL + '.'; };
    var no = function(){ $('r-esito').textContent = 'Copia non riuscita: selezionare il testo qui sopra.'; };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(ok, no); else no();
  });
})();
