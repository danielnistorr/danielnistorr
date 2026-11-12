/* Edera Preventivo, pagina del pannello: righe ripetibili (aggiungi, togli, sposta) e la prova del calcolatore
   con le regole salvate, fatta con lo stesso motore del sito (calcolo.js). */
(function () {
  "use strict";
  var d = document;
  var tutti = function (s, b) { return Array.prototype.slice.call((b || d).querySelectorAll(s)); };
  var contatore = 1000;

  // righe ripetibili
  d.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (!b) return;
    var riga = b.closest('.edp-riga');
    if (b.classList.contains('edp-aggiungi')) {
      var tipo = b.getAttribute('data-tipo');
      var modello = d.querySelector('template.edp-modello[data-tipo="' + tipo + '"]');
      var elenco = d.querySelector('.edp-righe[data-tipo="' + tipo + '"]');
      var html = modello.innerHTML.replace(/__i__/g, String(contatore++));
      var t = d.createElement('div'); t.innerHTML = html;
      var nuova = t.firstElementChild;
      elenco.appendChild(nuova);
      var primo = nuova.querySelector('input:not([type=hidden]), select');
      if (primo) primo.focus();
    } else if (riga && b.classList.contains('edp-togli')) {
      var dopo = riga.nextElementSibling || riga.previousElementSibling;
      riga.remove();
      if (dopo) { var f = dopo.querySelector('.edp-togli'); if (f) f.focus(); }
    } else if (riga && b.classList.contains('edp-su') && riga.previousElementSibling) {
      riga.parentNode.insertBefore(riga, riga.previousElementSibling); b.focus();
    } else if (riga && b.classList.contains('edp-giu') && riga.nextElementSibling) {
      riga.parentNode.insertBefore(riga.nextElementSibling, riga); b.focus();
    }
  });

  // prova del calcolatore
  var box = d.getElementById('edp-prova-box');
  var C = window.EDERA_PREVENTIVO, E = window.EderaCalcolo;
  if (!box || !C || !E) return;
  var R = C.regole;
  var esc = function (t) { return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); };
  var html = '<div class="edp-prova-campi"><fieldset><legend>Spazi</legend>';
  R.spazi.filter(function (s) { return s.attivo; }).forEach(function (s) {
    html += '<label><input type="checkbox" name="p-spazi" value="' + esc(s.chiave) + '"' + (s.scelto ? ' checked' : '') + '> ' + esc(s.nome) + '</label>';
  });
  html += '</fieldset><label class="edp-campo"><span>Partecipanti (vuoto = esempio)</span><input type="number" id="p-ospiti" min="0" step="1"></label>';
  html += '<label class="edp-campo"><span>Durata</span><select id="p-durata"><option value="intera">' + esc(R.durate.intera) + '</option><option value="mezza">' + esc(R.durate.mezza) + '</option></select></label>';
  html += '<label class="edp-campo"><span>Data</span><input type="date" id="p-data"></label>';
  var servizi = R.servizi.map(function (x, i) { return x.attivo ? '<label><input type="checkbox" name="p-servizi" value="' + i + '"> ' + esc(x.nome) + '</label>' : ''; }).join('');
  if (servizi) html += '<fieldset><legend>Servizi aggiuntivi</legend>' + servizi + '</fieldset>';
  html += '</div><div class="edp-prova-esito" aria-live="polite"><p class="edp-prova-totale" id="p-totale"></p><ul id="p-voci"></ul><p id="p-avvisi" class="edp-prova-avvisi"></p><pre id="p-mail"></pre></div>';
  box.innerHTML = html;

  function aggiorna() {
    var spazi = tutti('input[name="p-spazi"]:checked', box).map(function (x) { return x.value; });
    if (!spazi.length) { var p = box.querySelector('input[name="p-spazi"]'); if (p) { p.checked = true; spazi = [p.value]; } }
    var data = d.getElementById('p-data').value;
    var r = E.calcola(R, { spazi: spazi, ospiti: d.getElementById('p-ospiti').value, durata: d.getElementById('p-durata').value, data: data,
      servizi: tutti('input[name="p-servizi"]:checked', box).map(function (x) { return Number(x.value); }) });
    d.getElementById('p-totale').textContent = E.euro(r.totale);
    d.getElementById('p-voci').innerHTML = r.voci.concat(r.righe).map(function (v) { return '<li><span>' + esc(v.nome) + '</span><b>' + E.euro(v.valore) + '</b></li>'; }).join('')
      + '<li><span>Partecipanti</span><b>' + r.n + '</b></li><li><span>Durata</span><b>' + esc(r.durata === 'mezza' ? R.durate.mezza : R.durate.intera) + '</b></li>';
    var avvisi = [];
    if (!r.mezzaPossibile && d.getElementById('p-durata').value === 'mezza') avvisi.push('La mezza giornata non vale per questi spazi: conta la giornata intera.');
    if (r.oltre) avvisi.push('Oltre la capienza: contate ' + r.massimo + ' persone.');
    if (r.sotto) avvisi.push('Sotto il minimo: contate ' + r.n + ' persone.');
    if (data && E.calendarioAttivo(R)) { var dd = E.disponibile(R, data); if (!dd.ok) avvisi.push('Data non disponibile sul sito (' + dd.motivo + (dd.nota ? ': ' + dd.nota : '') + ').'); }
    d.getElementById('p-avvisi').textContent = avvisi.join(' ');
    var m = E.mail(R, r, { data: data });
    d.getElementById('p-mail').textContent = 'Oggetto: ' + m.oggetto + '\n\n' + m.testo;
  }
  box.addEventListener('input', aggiorna);
  box.addEventListener('change', aggiorna);
  aggiorna();
})();
