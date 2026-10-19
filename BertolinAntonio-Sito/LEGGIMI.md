# Antonio Bertolin Srl: proposta di nuova home

Questa è una proposta non richiesta, solo per la homepage. Nessuno ha contattato l'azienda: niente è stato inviato né pubblicato.

La versione finale è costruita sulla bozza B, "Il telaio", che ha scelto il committente, ed è stata rifinita dopo il giudizio cieco senza toccare idea e prima schermata (dettagli in `screenshot/home/NOTA.md`). La versione finale precedente era costruita sulla bozza A ed è stata sostituita; i suoi script sono in `_prova/script/finale-su-a-scartata/`.

## Dove sono le cose

| Cosa | Dove |
|---|---|
| La pagina | `sito/index.html`, con `sito/img/` (JPEG in più larghezze) e `sito/fonts/` (Mona Sans e la sua licenza). Si apre direttamente con file:/// |
| Gli screenshot | `screenshot/home/home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg` |
| La nota di progetto | `screenshot/home/NOTA.md` |
| Lo script che rifà tutto | `bash _prova/script/build_finale.sh` (immagini, logo, caratteri, pagina, controlli, screenshot, segnali, controlli finali) |
| La sorgente della pagina | `_prova/script/pagina-finale.html` |
| Lo script delle immagini | `_prova/script/finale_img.py` |
| Lo script del logo SVG | `_prova/script/logo_svg.py` (scrive `sito/img/logo.svg`, che la build mette in linea nella pagina) |
| Lo script degli screenshot e delle prove | `_prova/script/finale_shoot.mjs` |
| I controlli a 320, 768, 1024 e 1920, il filtro e i segnali | `_prova/controlli/`; i controlli finali (scorrimento da 320 a 2560, collegamenti, allineamenti, DPR 2, tastiera e dito) sono in `_prova/controlli/verifica.txt`, fatti da `_prova/script/verifica_finale.mjs` |
| Analisi, fonti e bozze | `01-analisi.md`; le bozze in `_prova/home/a` e `_prova/home/b` |

## Dati da confermare con l'azienda prima di pubblicare

Tutto ciò che è dubbio è rimasto fuori dalla pagina. Restano aperti questi punti.

1. **Consegne in 12 ore**. Sul sito di oggi c'è "Rapide consegne in 12 ore". Non è in pagina. Va chiesto per quali trattamenti e quantità, e da quando si contano le ore. Se viene confermato, diventa una riga piccola nei contatti, per esempio "Consegne in 12 ore, per [trattamenti]".
2. **Certificazione UNI EN ISO 9001:2015**. I PDF online (IMQ/CSQ n. 0316.2019, IQNet IT-118612) scadono il 2 marzo 2025, quindi la certificazione non è in pagina. Se è stata rinnovata, servono il numero e le date nuove. A quel punto va messa vicino ai contatti.
3. **Spessori**. In pagina ci sono 0-400 nm sul titanio e 5-20 micron sull'alluminio, come li scrive il sito. Vanno ricontrollati, e sul sito c'è anche la dicitura "nano micron", da correggere.
4. **Type II**. Il sito dice "supera i 20 µm" e cita MIL-A-8625 Tipo III e AMS 2488D, ma la MIL-A-8625 è una norma per l'alluminio. In pagina ci sono solo "grigio scuro", "antigrippante e lubrificante" e i settori.
5. **Colori dell'alluminio**. Il sito dice naturale, nero, rosso, blu e oro. I tubi in foto mostrano anche azzurro, champagne e rame, che nelle legende stanno sotto Blu, Oro e Rosso. Va confermato quali colori fanno oggi e come li chiamano. Va confermata anche la gamma del titanio: in pagina oro, blu, rosa e verde, quelli dei pezzi in foto.
6. **Misure del pezzo**. La frase "le misure del pezzo non cambiano in modo sostanziale" viene dal sito ("non modificando sostanzialmente le dimensioni"). Va confermata la formula.
7. **Il telaio**. Le boccole in foto sono di alluminio? E il telaio è nel reparto di Tombelle? Didascalia e distinta non lo dicono finché non lo confermano. Va chiesto anche se "barra del telaio" e "boccola tornita" sono i nomi che usano loro, perché ora stanno nella distinta sotto i palloncini 1 e 2.
8. **Lavorazioni e logo**. L'officina fa ancora particolari meccanici su specifica del cliente? In pagina sono raccontati come storia ("ha cominciato... poi"). La parola "MECCANICHE" del logo resta?
9. **Anni**. Manca l'anno di nascita dell'officina ("da quarant'anni" in un testo del 2019 o successivo) e quello della srl. In pagina non ci sono.
10. **Settori e clienti**. Sono ancora tutti attuali: medicale, dentale, aeronautico, navale, automotive, moto, bici, moda e arredamento? Si possono nominare dei clienti?
11. **Minuteria medicale**. Si può mostrare in foto? I pezzi sono probabilmente di clienti.
12. **Preventivo**. In pagina si chiede di mandare disegno, materiale e quantità a info@bertolinantonio.it. Va bene così, o serve un indirizzo diverso o un modulo?
13. **Dati per il piede**. Mancano PEC, REA e capitale sociale. Va chiesto anche se il fax 049 9834008 è ancora attivo: non l'ho messo.
14. **Sedi**. In pagina la sede legale è in Via Ugo Foscolo 9, Padova (dal certificato ISO) e lo stabilimento a Tombelle. Va confermato che sia ancora così. Il link "Indicazioni stradali" cerca "Viale Serenissima 15, 30030 Tombelle di Vigonovo VE" su Google Maps: va controllato che il segnaposto cada sull'ingresso giusto, o va sostituito con il link della loro scheda.
15. **Privacy**. Il link porta alla pagina privacy del sito di oggi. Il nuovo sito ne avrà bisogno di una aggiornata.
16. **News**. Quelle del 2019 si tolgono? Ci sono novità vere, come impianti nuovi o fiere? Una data vera in home, oltre al 2018, aiuterebbe.

## Foto da rifare dal vero

Tutte le foto in pagina sono dell'azienda e vengono dal sito di oggi. Reggono una proposta, non il sito vero. Basta mezza giornata in reparto e mezza di still life.

1. **Il telaio carico prima del bagno**: è l'apertura e ha la priorità.
   - Luce: luce naturale di reparto, più un pannello bianco grande a sinistra, e il fondo (parete o telo) chiaro e uniforme.
   - Fuoco: diaframma chiuso (f/11-f/16) e cavalletto, così anche le file in fondo restano leggibili. Oggi la metà destra è sfocata: in pagina c'è solo la parte sinistra della foto, a 1:1, larga 1440 px. Non è ingrandita: oltre i 1440 px la fascia resta larga 1440 e centrata, e sugli schermi ad alta densità ha un punto vero per punto CSS.
   - Tagli: uno orizzontale molto largo, almeno 2880 px nitidi da bordo a bordo per la fascia 1440 x 700 a densità 2 (meglio 4000), e uno verticale 4:5 per il telefono, con la barra del telaio a un quarto da sinistra. Con la foto nuova si può tornare a una fascia larga fino a 1920 e oltre.
   - Palloncini: se cambia l'inquadratura, vanno rimessi sulla barra e su una boccola (`--x`, `--y` in pagina, in percentuale della foto).
   - Fondo: chiaro e pulito già in ripresa. Oggi le bande della compressione JPEG del sito sono state lisciate al computer.
   - In più: le mani con i guanti che appendono i pezzi.
2. **I tubi di alluminio**.
   - Fondo: bianco o grigio chiarissimo senza giunte.
   - Luce: morbida dall'alto, la stessa altezza di camera per tutti.
   - I tubi: puliti, senza polvere né graffi (oggi sono ripuliti al computer solo in parte), un tubo per colore dichiarato.
   - Senza la base con la scritta rossa, oppure con una base neutra.
3. **La minuteria medicale**.
   - Un pezzo per colore, da solo e a fuoco pieno, sullo stesso fondo.
   - In più una composizione ordinata su una griglia, non sparsa, larga almeno 2100 px nitidi sul gruppo dei pezzi. Oggi il gruppo è largo 1100 px e in pagina sta a circa 1:1: sugli schermi ad alta densità è al limite.
   - Va fatta solo con il permesso del cliente.
4. **La scala dei 21 tondini di titanio**. Non è in questa pagina, ma è il soggetto più forte che hanno.
   - Macro su un fondo neutro chiaro, con la barra orizzontale e la camera in asse.
   - Luce morbida, con un riflesso solo e uguale su ogni tondino.
   - Pulire prima la barra e l'incisione.
5. **Lo stabilimento**. L'aerea va bene. Servirebbe anche una foto a terra dell'ingresso, per chi arriva.

## Licenze

- **Mona Sans** (GitHub, distribuito da Google Fonts): SIL Open Font License 1.1, testo in `sito/fonts/OFL-Mona-Sans.txt`.
  - È libera anche per uso commerciale e si può servire dal proprio server.
  - "Mona" è un nome riservato: i file non vanno modificati e poi ripubblicati con quel nome.
- **Foto**: sono tutte di Antonio Bertolin Srl (`assets/originali/`).
  - Va chiesto chi le ha scattate, e se ci sono gli originali a piena risoluzione dei file `DSC_`.
  - Le foto Unsplash e Pexels in `assets/esterne/` (licenze in `assets/CREDITI.md`) non sono usate nella versione finale.
  - Non ci sono immagini generate dall'IA.
- **Marchi IQNET e IMQ**: non sono in pagina. Se la certificazione è rinnovata, vanno usati secondo le regole degli enti.

## Logo

In testata e nel piede c'è il loro logo ridisegnato in SVG dal PNG del sito (`logo-footer-bertolin.png`, 274 x 102 px), con `_prova/script/logo_svg.py`. Lo script ingrandisce il PNG 8 volte e ne ricava i contorni. È un solo `<symbol>` in linea nella pagina: grafite in testata, bianco nel piede. Sugli schermi ad alta densità ora è netto, ma il tratteggio dell'arco e le lettere sono una ricostruzione e non il disegno originale. Serve il vettoriale (SVG, AI o PDF) da mettere al suo posto.

## Note sui controlli

- I segnali da IA (`_prova/controlli/segnali/`) danno 0 soglie bloccanti e 0 da guardare. L'area foto è al 35,2 %, appena sopra la soglia: se si toglie o rimpicciolisce una foto, va ricontrollata.
- `scrollWidth` è uguale a `innerWidth` da 320 a 2560 px. Il filtro funziona con tastiera e dito, e tel, mailto e mappe sono corretti (`_prova/controlli/verifica.txt`).
- Con le foto rifatte dal vero conviene allargare il telaio e la minuteria, invece di aggiungere altre immagini.
