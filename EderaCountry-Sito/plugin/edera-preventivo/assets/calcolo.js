/* Edera Preventivo: il motore dei conti, uguale per il sito e per la prova nel pannello.
   Riceve le regole (window.EDERA_PREVENTIVO.regole, dall'opzione del plugin) e le scelte di chi compila,
   e restituisce le voci della stima e il totale. Con le regole iniziali dà gli stessi numeri del calcolatore
   del sito originale.

   Ordine dei conti:
   1. ogni spazio scelto: prezzo fisso (giornata intera o mezza) oppure base + persone oltre le incluse;
      le persone contate non superano la capienza dello spazio. Con "oltre la capienza: si puo' superare, con
      la stima" le persone oltre la capienza degli spazi scelti si contano in piu' in ogni spazio a prezzo per
      persona, al suo prezzo; gli spazi a prezzo fisso restano al loro prezzo.
      Uno spazio con le fasce per numero di persone si calcola solo con le fasce: vale la fascia che contiene le
      persone contate per lo spazio (fisso per la fascia oppure a persona, con l'importo della mezza giornata se
      c'e'). Fuori da tutte le fasce vale il prezzo standard dello spazio, con una nota; oltre la capienza, con la
      stima, vale la fascia che contiene il numero o l'ultima senza limite superiore, altrimenti "da valutare";
   2. tariffe e supplementi del giorno scelto: sul primo spazio, su ogni spazio o sul totale;
   3. sconti (piu' spazi insieme, oltre N persone) sul prezzo degli spazi;
   4. servizi aggiuntivi spuntati, a prezzo fisso o a persona;
   5. spesa minima, poi arrotondamento del totale. */
(function (g) {
  "use strict";

  function c2(x) { return Math.round(x * 100) / 100; }
  function euro(n) {
    return new Intl.NumberFormat('it-IT', { style: 'currency', currency: 'EUR', maximumFractionDigits: 2, minimumFractionDigits: 0 }).format(n);
  }
  function dataDa(s) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s || '');
    return m ? new Date(+m[1], +m[2] - 1, +m[3]) : null;
  }
  function ymd(d) {
    var p = function (x) { return (x < 10 ? '0' : '') + x; };
    return d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate());
  }
  function giornoIso(d) { var x = d.getDay(); return x === 0 ? 7 : x; }
  function oggi() { var t = new Date(); return new Date(t.getFullYear(), t.getMonth(), t.getDate()); }

  function calendarioAttivo(R) {
    var c = R.calendario;
    return c.date_escluse.length > 0 || c.periodi_chiusi.length > 0 || c.giorni_chiusi.length > 0 || c.preavviso > 0 || c.finestra_mesi > 0;
  }
  // la prima e l'ultima data che si possono scegliere (null = nessun limite)
  function limiti(R, base) {
    var c = R.calendario, t = base || oggi(), min = null, max = null;
    if (calendarioAttivo(R)) { min = new Date(t); min.setDate(min.getDate() + (c.preavviso || 0)); }
    if (c.finestra_mesi > 0) { max = new Date(t); max.setMonth(max.getMonth() + c.finestra_mesi); }
    return { min: min, max: max };
  }
  // una data (AAAA-MM-GG) si puo' scegliere? { ok, motivo: preavviso | finestra | chiuso | esclusa | periodo }
  function disponibile(R, s, base) {
    if (!s) return { ok: true };
    var d = dataDa(s), c = R.calendario;
    if (!d) return { ok: false, motivo: 'formato' };
    var l = limiti(R, base);
    if (l.min && d < l.min) return { ok: false, motivo: 'preavviso' };
    if (l.max && d > l.max) return { ok: false, motivo: 'finestra' };
    if (c.giorni_chiusi.indexOf(giornoIso(d)) > -1) return { ok: false, motivo: 'chiuso' };
    var x = ymd(d), i;
    for (i = 0; i < c.date_escluse.length; i++) if (c.date_escluse[i].data === x) return { ok: false, motivo: 'esclusa', nota: c.date_escluse[i].nota };
    for (i = 0; i < c.periodi_chiusi.length; i++) {
      var p = c.periodi_chiusi[i];
      if (x >= p.dal && x <= p.al) return { ok: false, motivo: 'periodo', nota: p.nota };
    }
    return { ok: true };
  }

  function attivi(R) { return R.spazi.filter(function (s) { return s.attivo; }); }
  function mezzaPossibile(R, chiavi) {
    if (!R.durate.mezza_attiva) return false;
    var scelti = attivi(R).filter(function (s) { return chiavi.indexOf(s.chiave) > -1; });
    if (!scelti.length) return false;
    var con = scelti.filter(function (s) { return s.mezza; }).length;
    return R.durate.regola_mezza === 'tutti' ? con === scelti.length : con > 0;
  }
  function costo(s, n, durata, extra) {
    if (s.modo === 'fisso') return durata === 'mezza' && s.mezza ? Number(s.prezzo_mezza) : Number(s.prezzo_intera);
    return Number(s.base) + Math.max(0, Math.min(n, Number(s.persone) + extra) - Number(s.incluse)) * Number(s.a_persona);
  }
  // "Rustico", "Rustico e Piscina", "Rustico, Serra e Piscina"
  function elenco(nomi) { return nomi.length > 1 ? nomi.slice(0, -1).join(', ') + ' e ' + nomi[nomi.length - 1] : (nomi[0] || ''); }
  function riempi(t, m) { return String(t || '').replace(/\{([a-z_]+)\}/g, function (x, k) { return Object.prototype.hasOwnProperty.call(m, k) ? m[k] : x; }); }
  // le fasce per numero di persone: quella che contiene p, l'ultima senza limite superiore
  function haFasce(s) { return !!(s.fasce && s.fasce.length); }
  function fasciaPer(s, p) {
    for (var i = 0; i < s.fasce.length; i++) { var f = s.fasce[i]; if (p >= Number(f.da) && (!Number(f.a) || p <= Number(f.a))) return f; }
    return null;
  }
  function fasciaAperta(s) { var x = null; s.fasce.forEach(function (f) { if (!Number(f.a)) x = f; }); return x; }
  // il prezzo di uno spazio: { valore, nome (con la fascia applicata), fuori (nessuna fascia), valutare, p }
  function prezzoSpazio(R, s, n, durata, extra) {
    var p = Math.min(n, Number(s.persone) + extra), f = null, fuori = false, valutare = false;
    if (haFasce(s)) {
      f = fasciaPer(s, p);
      if (!f && p > Number(s.persone)) { f = fasciaAperta(s); valutare = !f; }   // oltre la capienza, con la stima
      else if (!f) fuori = true;
    }
    if (!f) return { valore: costo(s, n, durata, extra), nome: s.nome, fuori: fuori, valutare: valutare, p: p };
    var mezza = durata === 'mezza' && s.mezza && f.importo_mezza !== null && f.importo_mezza !== undefined && f.importo_mezza !== '';
    var importo = Number(mezza ? f.importo_mezza : f.importo), T = R.testi;
    var fascia = Number(f.a) ? riempi(T.fascia_limiti, { da: f.da, a: f.a }) : riempi(T.fascia_aperta, { da: f.da });
    var prezzo = riempi(f.modo === 'persona' ? T.fascia_persona : T.fascia_fissa, { importo: euro(importo) });
    return { valore: c2(f.modo === 'persona' ? importo * p : importo), nome: riempi(T.fascia_etichetta, { spazio: s.nome, fascia: fascia, prezzo: prezzo }),
      fascia: f, fuori: false, valutare: false, p: p };
  }
  // come si comporta il calcolatore oltre la capienza: rigido (com'era), stima, senza (importo)
  function modoOltre(R) { var m = R.generali.oltre_capienza; return m === 'stima' || m === 'senza' ? m : 'rigido'; }
  function quota(modo, valore, base) { return modo === 'percentuale' ? c2(base * Number(valore) / 100) : Number(valore); }
  function tariffaVale(t, d) {
    if (!t.attiva || !d) return false;
    if (t.tipo === 'mesi') return t.mesi.indexOf(d.getMonth() + 1) > -1;
    if (t.tipo === 'giorni') return t.giorni.indexOf(giornoIso(d)) > -1;
    if (t.tipo === 'periodo') { var x = ymd(d); return x >= t.dal && x <= t.al; }
    return false;
  }

  /* inp: { spazi: [chiavi], ospiti: testo del campo, durata: 'intera' | 'mezza', data: 'AAAA-MM-GG' | '', servizi: [indici] } */
  function calcola(R, inp) {
    var scelti = attivi(R).filter(function (s) { return inp.spazi.indexOf(s.chiave) > -1; });
    var capienza = scelti.reduce(function (a, s) { return a + Number(s.persone); }, 0);
    var modo = modoOltre(R), assoluto = Math.max(0, Number(R.generali.massimo_assoluto) || 0);
    // il numero piu' alto che si accetta (0 = nessun limite): con "rigido" la capienza, altrimenti il massimo assoluto
    var limite = modo === 'rigido' ? (assoluto > 0 ? Math.min(capienza, assoluto) : capienza) : assoluto;
    var minimo = Math.max(1, Number(R.sconti.minimo_persone) || 0);
    var n = Math.max(1, Number(inp.ospiti) || Number(R.generali.partecipanti_esempio));
    var oltre = false, sotto = false;
    if (limite > 0 && n > limite) { n = limite; oltre = true; }
    if (minimo > 1 && n < minimo) { n = limite > 0 ? Math.min(minimo, limite) : minimo; sotto = true; }
    var superata = modo !== 'rigido' && n > capienza;          // si supera la capienza e la richiesta parte lo stesso
    var extra = modo === 'stima' && superata ? n - capienza : 0;
    var mezza = mezzaPossibile(R, inp.spazi);
    var durata = inp.durata === 'mezza' && mezza ? 'mezza' : 'intera';
    var prezzi = scelti.map(function (s) { return prezzoSpazio(R, s, n, durata, extra); });
    var voci = prezzi.map(function (x) { return { nome: x.nome, valore: x.valore, tipo: 'spazio' }; });
    var valutare = prezzi.some(function (x) { return x.valutare; });
    var righe = [], d = dataDa(inp.data);
    // 2. tariffe sugli spazi, poi quelle sul totale
    R.tariffe.forEach(function (t) {
      if (!tariffaVale(t, d) || !voci.length) return;
      if (t.applica === 'primo_spazio') voci[0].valore = c2(voci[0].valore + quota(t.modo, t.valore, voci[0].valore));
      if (t.applica === 'ogni_spazio') voci.forEach(function (v) { v.valore = c2(v.valore + quota(t.modo, t.valore, v.valore)); });
    });
    var spazi = voci.reduce(function (a, v) { return a + v.valore; }, 0);
    R.tariffe.forEach(function (t) {
      if (tariffaVale(t, d) && voci.length && t.applica === 'totale') righe.push({ nome: t.nome, valore: quota(t.modo, t.valore, spazi), tipo: 'supplemento' });
    });
    var location = c2(spazi + righe.reduce(function (a, v) { return a + v.valore; }, 0));
    // 3. sconti
    var sc = R.sconti, sconto;
    if (sc.piu_spazi.attivo && scelti.length >= sc.piu_spazi.da && sc.piu_spazi.valore > 0) {
      sconto = Math.min(location, quota(sc.piu_spazi.modo, sc.piu_spazi.valore, location));
      righe.push({ nome: sc.piu_spazi.nome, valore: -sconto, tipo: 'sconto' });
    }
    if (sc.persone.attivo && n > sc.persone.oltre && sc.persone.valore > 0) {
      sconto = Math.min(location, quota(sc.persone.modo, sc.persone.valore, location));
      righe.push({ nome: sc.persone.nome, valore: -sconto, tipo: 'sconto' });
    }
    // 4. servizi aggiuntivi
    var servizi = [];
    R.servizi.forEach(function (x, i) {
      if (!x.attivo || inp.servizi.indexOf(i) < 0) return;
      servizi.push(x.nome);
      righe.push({ nome: x.nome, valore: c2(x.modo === 'persona' ? Number(x.prezzo) * n : Number(x.prezzo)), tipo: 'servizio' });
    });
    var totale = c2(spazi + righe.reduce(function (a, v) { return a + v.valore; }, 0));
    // 5. spesa minima e arrotondamento
    if (sc.spesa_minima > 0 && totale < sc.spesa_minima) {
      righe.push({ nome: g.EDERA_PREVENTIVO_TESTI ? g.EDERA_PREVENTIVO_TESTI.spesaMinima : 'Spesa minima', valore: c2(sc.spesa_minima - totale), tipo: 'minimo' });
      totale = Number(sc.spesa_minima);
    }
    var a = sc.arrotonda;
    if (a.modo !== 'nessuno' && a.passo > 0) {
      var f = a.modo === 'eccesso' ? Math.ceil : (a.modo === 'difetto' ? Math.floor : Math.round);
      var t = c2(f(c2(totale / a.passo)) * a.passo);
      if (t !== totale) { righe.push({ nome: g.EDERA_PREVENTIVO_TESTI ? g.EDERA_PREVENTIVO_TESTI.arrotondamento : 'Arrotondamento', valore: c2(t - totale), tipo: 'arrotondamento' }); totale = t; }
    }
    return { voci: voci, righe: righe, totale: totale, n: n, durata: durata, mezzaPossibile: mezza, minimo: minimo,
      capienza: capienza, limite: limite, massimo: capienza, modo: modo, oltre: oltre, sotto: sotto, superata: superata,
      senzaImporto: (modo === 'senza' && superata) || valutare,
      // con la stima, oltre la capienza: gli spazi a prezzo fisso (senza fascia) non contano le persone in piu'
      fissi: extra > 0 && !valutare ? scelti.filter(function (s, i) { return s.modo === 'fisso' && !prezzi[i].fascia; }).map(function (s) { return s.nome; }) : [],
      fuoriFascia: scelti.map(function (s, i) { return prezzi[i].fuori ? { nome: s.nome, p: prezzi[i].p } : null; }).filter(Boolean),
      etichette: voci.map(function (v) { return v.nome; }), spazi: scelti.map(function (s) { return s.nome; }), servizi: servizi };
  }

  // le note della stima, che vanno anche nella mail: oltre la capienza la riga "N persone, oltre la capienza..."
  // e, con la stima, quella sugli spazi a prezzo fisso, che non tengono conto delle persone in piu';
  // poi gli spazi con le fasce dove il numero non cade in nessuna fascia
  function note(R, r) {
    var out = [];
    if (r.superata) {
      out.push(riempi(R.testi.msg_oltre, { persone: String(r.n), capienza: String(r.capienza) }));
      if (r.fissi.length) out.push(riempi(R.testi.nota_fisso, { spazi: elenco(r.fissi) }));
    }
    if (!r.senzaImporto) r.fuoriFascia.forEach(function (x) { out.push(riempi(R.testi.msg_fuori_fascia, { spazio: x.nome, persone: String(x.p) })); });
    return out.filter(function (x) { return x.trim() !== ''; });
  }

  // il testo e l'oggetto della mail, dai modelli con i segnaposti {azienda} {email} {telefono} {tipo} {spazi}
  // {data} {persone} {capienza} {durata} {servizi} {servizi_riga} {note_riga} {totale} {dettaglio}
  function mail(R, r, campi) {
    var v = function (x, vuoto) { return (campi[x] || '').trim() || vuoto; };
    var etichetta = (r.durata === 'mezza' ? R.durate.mezza : R.durate.intera);
    // senza importo: solo i nomi (spazi senza fascia e prezzo, servizi), nessun euro
    var dettaglio = r.senzaImporto ? r.spazi.concat(r.servizi).join('\n')
      : r.voci.concat(r.righe).map(function (x) { return x.nome + ': ' + euro(x.valore); }).join('\n');
    var righe = note(R, r);
    var mappa = {
      azienda: v('azienda', 'da indicare'), email: v('email', 'da indicare'), telefono: v('telefono', 'da indicare'),
      tipo: v('tipo', 'da indicare'), spazi: (r.senzaImporto ? r.spazi : r.etichette).join(', '), data: v('data', 'da concordare'), persone: String(r.n),
      capienza: String(r.capienza), durata: etichetta.toLowerCase(), servizi: r.servizi.join(', '),
      servizi_riga: r.servizi.length ? 'Servizi aggiuntivi: ' + r.servizi.join(', ') + '\n' : '',
      note_riga: righe.length ? righe.join('\n') + '\n' : '',
      totale: r.senzaImporto ? R.testi.da_valutare : euro(r.totale), dettaglio: dettaglio
    };
    var corpo = R.testi.corpo;
    // le note (oltre la capienza, fuori fascia) ci sono sempre: dove il testo ha {note_riga}, altrimenti dopo la
    // riga dei partecipanti (o in fondo, se il testo non ha {persone})
    if (righe.length && corpo.indexOf('{note_riga}') < 0) {
      var i = corpo.indexOf('{persone}'), fine = i > -1 ? corpo.indexOf('\n', i) : -1;
      corpo = fine > -1 ? corpo.slice(0, fine + 1) + '{note_riga}' + corpo.slice(fine + 1) : corpo.replace(/\s+$/, '') + '\n\n' + righe.join('\n');
    }
    var oggetto = riempi(R.testi.oggetto, Object.assign({}, mappa, { azienda: v('azienda', 'evento aziendale') }));
    return { oggetto: oggetto, testo: riempi(corpo, mappa) };
  }

  g.EderaCalcolo = { calcola: calcola, mail: mail, note: note, riempi: riempi, euro: euro, disponibile: disponibile, limiti: limiti,
    calendarioAttivo: calendarioAttivo, mezzaPossibile: mezzaPossibile, dataDa: dataDa, ymd: ymd };
})(window);
