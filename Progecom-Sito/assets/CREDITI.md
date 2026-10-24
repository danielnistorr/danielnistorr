# Crediti delle immagini: Progecom

## Immagini dell'azienda (`assets/originali/`)

Tutto viene da https://www.progecom-poggese.com (scaricato il 24/10/2026 dal CDN di Wix, file originali ridotti a 2400 px di lato massimo; i PNG trasparenti più pesanti sono stati convertiti in WebP). Inventario, misure originali, pagine di provenienza e voti in `_prova/inventario-immagini.json`.

Attenzione ai diritti, perché sul sito c'è molto materiale non di Progecom:
- le schede e la copertina dei crogioli sono del produttore MGI (Masc Global Industries);
- le foto dei forni della pagina `fergal` sono di Fergal S.r.l.;
- le quattro foto grandi della pagina Rappresentanze (stabilimento, lingotti con etichetta, balle di rottame, campione al quantometro) sono di STEMIN S.p.A.;
- il banner della home (colata in acciaieria con operai) è una foto di repertorio di origine ignota;
- le 16 icone arancioni delle famiglie di prodotto hanno lo stile di un generatore di immagini: non usarle.

Loghi: `logo-simbolo-738.png` (miglior qualità trovata, 738x752, PNG trasparente), `logo-simbolo-fascia-oro-738.png` (variante), `logo-favicon-originale.png` (100x102). Nessun SVG nel codice e nessun PDF con il logo. La scritta "PROGECOM" del sito è testo in un font caricato su Wix, non un file.

Video non scaricati (regola di disco): elenco nell'inventario.

## Segnaposto di repertorio (`assets/esterne/`)

Licenza verificata il 24/10/2026 sulla pagina di ogni foto. Unsplash: "Free to use under the Unsplash License" (https://unsplash.com/license), nessuna è Unsplash+. Pexels: "Free" con la Pexels License (https://www.pexels.com/license/). Le pagine Pexels riportano i dati di scatto (fotocamera reale); nessuna è generata dall'IA. Nessuna compare nei CREDITI delle altre home della campagna (controllati il 24/10/2026). Sono segnaposto per la proposta: le foto vere vanno fatte da Progecom (vedi `01-analisi.md`).

| File | Soggetto | Autore | Pagina della foto | Licenza |
|---|---|---|---|---|
| unsplash-jaeger-Y58_gFwZyPk.jpg (2400x1600) | blocco di metallo grezzo a due cubi su fondo bianco, luce morbida | Laura Jaeger (@lvjart) | https://unsplash.com/photos/Y58_gFwZyPk | Unsplash License |
| unsplash-diecastingmould-D60xwIqu-jA.jpg (2400x1600) | carter in alluminio pressofuso su fondo bianco (dominante fredda) | Diecasting Mould (@diecastingmould) | https://unsplash.com/photos/D60xwIqu-jA | Unsplash License |
| unsplash-escalante-oFe9f0VHEEc.jpg (2400x1350) | mucchio di getti in alluminio (pistoni grezzi) | Salvador Escalante (@salvador_86) | https://unsplash.com/photos/oFe9f0VHEEc | Unsplash License |
| unsplash-grieveson-hJqaSkr796w.jpg (1800x2400) | siviera che versa metallo nelle lingottiere, luce di capannone | Joseph Grieveson (@joseph_grieveson) | https://unsplash.com/photos/hJqaSkr796w | Unsplash License |
| pexels-szemerey-6804260.jpg (2400x1600) | colata da siviera, getto incandescente su fondo scuro | Bence Szemerey | https://www.pexels.com/photo/melted-steel-in-a-cast-iron-container-6804260/ | Pexels License |
| pexels-arapoglu-7451186.jpg (1600x2400) | bocca di forno incandescente sulla sabbia | Ali Arapoğlu (@baybiyik) | https://www.pexels.com/photo/close-up-of-flame-in-a-furnace-7451186/ | Pexels License |
| pexels-singha-19781878.jpg (1600x2400) | crogiolo con metallo che fonde sotto la fiamma, su blocco refrattario | Panta Singha | https://www.pexels.com/photo/close-up-of-flame-in-a-crucible-19781878/ | Pexels License |
| pexels-finalchoice-33444783.jpg (2400x1600) | metallo chiaro versato da un crogiolo sulla sabbia, vista dall'alto | Finalchoice | https://www.pexels.com/photo/molten-metal-poured-from-crucible-in-foundry-33444783/ | Pexels License |

Note d'uso:
- Jaeger: il titolo dice solo "metal" e la serie è "Form and structure studies 2024": è un blocco di metallo, non un lingotto di Progecom. Usarlo come materia, mai con la didascalia di una lega precisa.
- Diecasting Mould è l'account di un fornitore di pressofusi: nessun marchio è visibile nell'inquadratura.
- Escalante: su un getto si legge una sigla di stampo piccola e sfocata, nessun marchio commerciale.
- Grieveson: il file è morbido al 100% (compressione visibile); va bene a mezza pagina, non a tutto schermo.

## Uso nella home finale (`sito/`)

Repertorio usato: Diecasting Mould (apertura, carter isolato sul fondo della pagina), Grieveson (tappa Trasporto), Escalante (chiusura). Dal sito Progecom: forno a crogiolo `617993_63c4b918…`, degasaggio `617993_22fb7a2c…`, rete `617993_3b181aec…`, pistone `617993_dc2abcaa…`, valigetta `4a6a7c_da1722af…`, bocca di forno `4a6a7c_804c276f…`, lingotti STEMIN `4a6a7c_dc8cdae2…` (foto di STEMIN S.p.A., consenso da chiedere), logo `logo-simbolo-738.png`. Trattamenti in `_prova/script/finale_img.py`; nessuna foto nuova scaricata.
