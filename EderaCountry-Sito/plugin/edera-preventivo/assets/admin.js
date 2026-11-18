/* Edera Preventivo, pagina del pannello: righe ripetibili (aggiungi, togli, sposta) e la prova del calcolatore
   con le regole salvate, fatta con lo stesso motore del sito (calcolo.js).
   Servizi e dotazioni (dalla 1.1.0): ogni voce mostra solo i campi del suo modo di prezzo e un riassunto che
   segue i campi; "Aggiungi le voci del listino" mette nel modulo, senza salvare, le voci del PDF che mancano. */
(function () {
  "use strict";
  var d = document;
  var tutti = function (s, b) { return Array.prototype.slice.call((b || d).querySelectorAll(s)); };
  var contatore = 1000;
  var C = window.EDERA_PREVENTIVO, E = window.EderaCalcolo;
  var TA = (C && C.testi) || {};
  var riempi = function (t, m) { return String(t || '').replace(/\{([a-z_]+)\}/g, function (x, k) { return Object.prototype.hasOwnProperty.call(m, k) ? m[k] : x; }); };
  var euro = function (n) { return E ? E.euro(n) : n + ' €'; };

  // servizi e dotazioni: i campi del modo scelto e il riassunto ("Sedie · 1 € a pezzo · max 65 · attivo"),
  // lo stesso testo di edera_preventivo_sommario()
  function campo(voce, k) {
    return tutti('[name$="[' + k + ']"]', voce).filter(function (el) { return !el.closest('.edp-fasce'); });
  }
  function valore(voce, k) { var el = campo(voce, k).filter(function (x) { return x.type !== 'hidden'; })[0]; return el ? (el.type === 'checkbox' ? el.checked : el.value) : ''; }
  function sommario(voce) {
    var nome = String(valore(voce, 'nome')).trim(), modo = valore(voce, 'modo');
    var p = euro(Number(String(valore(voce, 'prezzo')).replace(',', '.')) || 0);
    var parti = [nome || TA.senzaNome];
    parti.push(modo === 'incluso' ? TA.compreso : (modo === 'persona' ? E.testo('aPersona').replace('{prezzo}', p) : (modo === 'pezzo' ? riempi(TA.aPezzo, { prezzo: p }) : p)));
    var fasce = tutti('.edp-gruppo[data-tipo="fascia_voce"] > .edp-righe > .edp-riga', voce).length;
    if (modo !== 'incluso' && fasce) parti.push(fasce === 1 ? TA.fascia1 : riempi(TA.fasce, { n: fasce }));
    var max = Math.floor(Number(valore(voce, 'massimo')) || 0);
    if ((modo === 'pezzo' || modo === 'incluso') && max > 0) parti.push(riempi(TA.max, { n: max }));
    var spazi = tutti('input[type=checkbox][name$="[spazi][]"]:checked', voce).map(function (x) { return x.parentNode.textContent.trim(); });
    if (spazi.length) parti.push(riempi(TA.soloCon, { spazi: spazi.join(', ') }));
    parti.push(valore(voce, 'attivo') ? TA.attivo : TA.spento);
    return parti.join(' · ');
  }
  function aggiornaVoce(voce) {
    var m = voce.querySelector('[data-ruolo="modo"]'), q = voce.querySelector('[data-ruolo="quantita"]');
    if (!m) return;
    tutti('.edp-se', voce).forEach(function (el) {
      var modi = (el.getAttribute('data-modi') || '').split(' '), qq = el.getAttribute('data-quantita');
      el.hidden = modi.indexOf(m.value) < 0 || !!(qq && q && qq !== q.value);
    });
    var s = voce.querySelector(':scope > summary .edp-sommario');
    if (s && E) s.textContent = sommario(voce);
  }
  var cambia = function (e) { var v = e.target.closest && e.target.closest('details.edp-voce'); if (v) aggiornaVoce(v); };
  d.addEventListener('input', cambia);
  d.addEventListener('change', cambia);
  // un campo non valido (per esempio un prezzo negativo) dentro una voce chiusa o un gruppo di campi nascosto: il
  // browser non lo mostrerebbe e il salvataggio si fermerebbe senza dire niente. Si apre la voce e si mostra il campo.
  d.addEventListener('invalid', function (e) {
    for (var x = e.target.closest('details'); x; x = x.parentElement && x.parentElement.closest('details')) x.open = true;
    for (var y = e.target.closest('.edp-se[hidden]'); y; y = y.parentElement && y.parentElement.closest('.edp-se[hidden]')) y.hidden = false;
  }, true);

  // righe ripetibili
  d.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (!b) return;
    var riga = b.closest('.edp-riga');
    var voce = b.closest('details.edp-voce');
    if (b.classList.contains('edp-aggiungi')) {
      // il gruppo del bottone (le fasce sono un gruppo dentro la riga di uno spazio o di una voce): il suo modello e il suo elenco
      var gruppo = b.closest('.edp-gruppo');
      var modello = gruppo.querySelector(':scope > template.edp-modello');
      var elenco = gruppo.querySelector(':scope > .edp-righe');
      var segno = new RegExp(b.getAttribute('data-segno') || '__i__', 'g');
      var html = modello.innerHTML.replace(segno, String(contatore++));
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
    if (voce && voce.isConnected) aggiornaVoce(voce);   // una fascia aggiunta o tolta cambia il riassunto
  });

  // "Aggiungi le voci del listino": le voci del PDF che mancano (per nome), spente, nel modulo; si salva dopo
  var listino = d.getElementById('edp-listino');
  if (listino && C && C.listino) listino.addEventListener('click', function () {
    var gruppo = d.querySelector('#edp-servizi .edp-gruppo[data-tipo="servizio"]');
    var elenco = gruppo.querySelector(':scope > .edp-righe'), modello = gruppo.querySelector(':scope > template.edp-modello');
    var presenti = tutti(':scope > .edp-riga', elenco).map(function (r) { return String(valore(r, 'nome')).trim().toLowerCase(); });
    var aggiunte = 0, prima = null;
    C.listino.forEach(function (x) {
      if (presenti.indexOf(String(x.nome).trim().toLowerCase()) > -1) return;
      var t = d.createElement('div'); t.innerHTML = modello.innerHTML.replace(/__i__/g, String(contatore++));
      var riga = t.firstElementChild;
      elenco.appendChild(riga);
      Object.keys(x).forEach(function (k) {
        if (k === 'fasce' || k === 'spazi') return;
        campo(riga, k).forEach(function (el) {
          if (el.type === 'checkbox') el.checked = !!x[k];
          else if (el.type !== 'hidden') el.value = x[k];
        });
      });
      // gli spazi: per chiave, o per nome se la chiave e' diversa ("piscina")
      var caselle = tutti('input[type=checkbox][name$="[spazi][]"]', riga);
      (x.spazi || []).forEach(function (k) {
        var c = caselle.filter(function (el) { return el.value === k; })[0]
          || caselle.filter(function (el) { return el.parentNode.textContent.toLowerCase().indexOf(k) > -1; })[0];
        if (c) c.checked = true;
      });
      var v = riga.querySelector('details.edp-voce');
      if (v) { v.open = false; aggiornaVoce(v); }
      if (!prima) prima = riga;
      aggiunte++;
    });
    var esito = d.getElementById('edp-listino-esito');
    if (esito) esito.textContent = aggiunte ? (aggiunte === 1 ? TA.aggiunta : riempi(TA.aggiunte, { n: aggiunte })) : TA.nessuna;
    if (prima) prima.scrollIntoView({ block: 'nearest' });
  });

  // prova del calcolatore
  var box = d.getElementById('edp-prova-box');
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
  // servizi e dotazioni come nel calcolatore: dotazioni, poi servizi extra; le voci comprese vanno solo nella mail
  [['dotazione', TA.dotazioni], ['servizio', TA.servizi]].forEach(function (g) {
    var voci = R.servizi.map(function (x, i) {
      if (!x.attivo || x.modo === 'incluso' || (x.gruppo === 'dotazione') !== (g[0] === 'dotazione')) return '';
      var pezzi = x.modo === 'pezzo' || (x.fasce || []).some(function (f) { return f.modo === 'pezzo'; });
      var max = Math.floor(Number(x.massimo) || 0);
      return '<span class="edp-prova-voce" data-voce="' + i + '"><label><input type="checkbox" name="p-servizi" value="' + i + '"> ' + esc(x.nome) + '</label> <small>' + esc(E.prezzoTesto(x)) + '</small>'
        + (pezzi && x.quantita !== 'automatica' ? ' <input type="number" class="p-q" data-voce="' + i + '" min="1"' + (max ? ' max="' + max + '"' : '') + ' step="1" value="1" aria-label="' + esc(riempi(max ? E.testo('quantitaMax') : E.testo('quantita'), { massimo: max }) + ', ' + x.nome) + '">' : '')
        + (pezzi && x.quantita === 'automatica' ? ' <small class="p-auto" data-voce="' + i + '"></small>' : '') + '</span>';
    }).join('');
    if (voci) html += '<fieldset class="edp-prova-gruppo"><legend>' + esc(g[1]) + '</legend>' + voci + '</fieldset>';
  });
  html += '</div><div class="edp-prova-esito" aria-live="polite"><p class="edp-prova-totale" id="p-totale"></p><ul id="p-voci"></ul><p id="p-avvisi" class="edp-prova-avvisi"></p><pre id="p-mail"></pre></div>';
  box.innerHTML = html;

  function aggiorna() {
    var spazi = tutti('input[name="p-spazi"]:checked', box).map(function (x) { return x.value; });
    if (!spazi.length) { var p = box.querySelector('input[name="p-spazi"]'); if (p) { p.checked = true; spazi = [p.value]; } }
    // le voci legate a spazi non scelti si nascondono e perdono la spunta, come sul sito
    tutti('.edp-prova-voce', box).forEach(function (el) {
      var si = E.voceDisponibile(R.servizi[Number(el.getAttribute('data-voce'))], spazi);
      el.hidden = !si;
      if (!si) el.querySelector('input[type=checkbox]').checked = false;
    });
    tutti('.edp-prova-gruppo', box).forEach(function (el) { el.hidden = !el.querySelector('.edp-prova-voce:not([hidden])'); });
    var quantita = {};
    tutti('input.p-q', box).forEach(function (x) { quantita[x.getAttribute('data-voce')] = x.value; });
    var data = d.getElementById('p-data').value;
    var r = E.calcola(R, { spazi: spazi, ospiti: d.getElementById('p-ospiti').value, durata: d.getElementById('p-durata').value, data: data,
      servizi: tutti('input[name="p-servizi"]:checked', box).map(function (x) { return Number(x.value); }), quantita: quantita });
    tutti('.p-auto', box).forEach(function (el) {
      var i = Number(el.getAttribute('data-voce')), v = r.info[i];
      el.textContent = v && v.auto ? E.testoAuto(R.servizi[i], v, r.n) : '';
    });
    // come sul sito: senza importo (oltre la capienza) niente prezzi, solo il testo al posto del totale
    d.getElementById('p-totale').textContent = r.senzaImporto ? R.testi.da_valutare : E.euro(r.totale);
    d.getElementById('p-voci').innerHTML = (r.senzaImporto ? [] : r.voci.concat(r.righe)).map(function (v) { return '<li><span>' + esc(v.nome) + '</span><b>' + E.euro(v.valore) + '</b></li>'; }).join('')
      + '<li><span>Partecipanti</span><b>' + r.n + '</b></li><li><span>Durata</span><b>' + esc(r.durata === 'mezza' ? R.durate.mezza : R.durate.intera) + '</b></li>';
    var avvisi = E.note(R, r);
    if (!r.mezzaPossibile && d.getElementById('p-durata').value === 'mezza') avvisi.push(TA.mezzaNo);
    if (r.oltre) avvisi.push((r.modo === 'rigido' && r.limite === r.capienza ? 'Oltre la capienza' : 'Oltre il massimo assoluto') + ': contate ' + r.limite + ' persone.');
    if (r.sotto) avvisi.push('Sotto il minimo: contate ' + r.n + ' persone.');
    if (data && E.calendarioAttivo(R)) { var dd = E.disponibile(R, data); if (!dd.ok) avvisi.push('Data non disponibile sul sito (' + dd.motivo + (dd.nota ? ': ' + dd.nota : '') + ').'); }
    d.getElementById('p-avvisi').textContent = avvisi.join(' ');
    var m = E.mail(R, r, { data: data });
    d.getElementById('p-mail').textContent = 'Oggetto: ' + m.oggetto + '\n\n' + m.testo;
  }
  box.addEventListener('input', function (e) {
    // la quantita' non supera il massimo disponibile
    if (e.target.classList.contains('p-q') && e.target.max !== '' && Number(e.target.value) > Number(e.target.max)) e.target.value = e.target.max;
    aggiorna();
  });
  box.addEventListener('change', aggiorna);
  aggiorna();
})();
