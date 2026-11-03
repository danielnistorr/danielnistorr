# Progecom di Poggese Mauro: proposta di nuova home

Proposta non richiesta, solo la home. Nessun contatto con l'azienda, niente pubblicato.

## Dove sono le cose

- `sito/index.html`: la home, livello professionale del 3/11/2026 (statica, si apre con file:///), con `sito/img/` (solo le immagini usate, JPEG e WebP in più larghezze) e `sito/fonts/` (Archivo e Tinos, con le licenze).
- `screenshot/home/`: screenshot a 1440 e 390, prima schermata e pagina intera, chiusura e piede a 1440. La `NOTA.md` spiega le scelte e l'esito delle 15 regole, una per una.
- `_prova/script/build_finale.sh`: rifà immagini, pagina, screenshot e controlli. Gli script sono:
  - `pro_img.py`, le immagini (solo foto loro, stesso trattamento);
  - `pagina-pro.html`, il sorgente della pagina;
  - `pro_shoot.mjs`, gli screenshot e le prove di scorrimento e sovrapposizione da 320 a 1920;
  - `pro_controlli.mjs`, i controlli delle 15 regole e dei compiti della scheda d'uso (esito in `_prova/pro_controlli.json`).
- `_prova/versione-1-originale/`: la home precedente (pistone quotato, sei tappe) com'era, con i suoi screenshot e la sua nota. I vecchi script (`finale_img.py`, `pistone_img.py`, `pagina.html`, `shoot_finale.mjs`, `prova_finale.mjs`) rifanno quella.
- `_prova/uso/SCHEDA.md`: chi apre il sito e cosa ci viene a fare. `01-analisi.md`: fatti con fonti.

## Il modulo di richiesta va collegato a un servizio

Il modulo in fondo alla home (nome, azienda, email, telefono, tipo di richiesta, prodotto o norma, misura, lega e quantità, messaggio) oggi **non invia nulla**: compone un'email per commerciale@progecom-poggese.it con l'oggetto e i campi già scritti, e chi la manda deve allegare a mano disegno o foto. Anche i bottoni "Scrivi", "Fissa la manutenzione per email", "Manda la foto del pezzo", "Chiedi di questo" e "Proponi il tuo forno" sono `mailto:` con oggetto e traccia.
Per il sito vero il modulo va collegato a un servizio di invio che accetti allegati (PDF, DXF, STEP, JPG, almeno 20 MB), con una casella di controllo per la privacy e un filtro antispam senza riquadri da risolvere; la conferma va mandata anche a chi scrive. Quale casella riceve cosa (commerciale@ per offerte e ordini, info@ per il resto) va confermato con il titolare.

## Cosa chiedere all'azienda

1. **Orari e reperibilità.** Non sono pubblicati: la pagina non mostra orari né "aperto ora". Se Mauro Poggese vuole, si aggiungono gli orari del telefono o la frase "sempre al cellulare" nel piede.
2. **Il nome accanto al telefono.** In pagina il cellulare è "il cellulare di Mauro Poggese" (dalla ragione sociale): va bene per lui?
3. **Clienti, settori e lavori.** Il sito dice solo "importanti aziende leader". Per le regole 10 e 11 servono 3-6 clienti o settori da nominare (anche solo "pressofusione per l'automotive, Brescia") e 3 interventi con luogo, anno e due dati (per esempio una pulizia del forno nel week-end: forno, capacità, ore).
4. **Certificazioni, associazioni, marchi trattati.** Nessuna nelle fonti. Se ci sono (iscrizioni, associazioni di fonderia, marchi rappresentati oltre a STEMIN, MGI per i crogioli, Fergal per i forni), vanno in una fascia con la didascalia.
5. **Recensioni.** Non esistono online (nessuna scheda Google trovata). Se qualche cliente accetta, due righe con nome, azienda e comune.
6. **Le voci senza dati.** Per Refrattari e isolanti, Bruciatori preriscaldo stampi, Automazioni lubrificazione e Leghe di zinco la home rimanda alla scheda: servono 2-3 dati veri ciascuna (materiali, modelli, norme).
7. **Il video del magazzino.** L'apertura usa l'anteprima del loro video YouTube `BqKKjrjrDq0`: va bene usarla? Meglio il file originale o qualche foto vera del magazzino (vedi sotto). Anche il link al video, in apertura e in Chi siamo, va confermato: è il canale personale.

## Dati da confermare con il titolare

- **Usato.** Le quattro voci in home (Marconi a torre 2000 kg, € 70.000 su circa 250.000 del nuovo; Fergal fusione e attesa, € 78.000 con garanzia; forno rovesciabile 300-350 kg, € 20.000 su circa 38.000; siviera 250-300 kg, € 3.500 su circa 12.000) sono quelle pubblicate oggi: prezzi e disponibilità vanno confermati. Il costo del nuovo del Fergal non è indicato.
- **"Dal 1990"** è l'anno dell'attività ("PROGECOM, nasce nel 1990"); l'impresa individuale attuale ha un'altra data di iscrizione (P.IVA dell'ufficio di Padova, piede "© 2019").
- **"Magazzino a Mestrino"** e **"Pronti a magazzino"** per i crogioli vengono dalla scheda d'uso (video del magazzino crogioli): confermare che il magazzino è a Mestrino e quali voci sono sempre disponibili.
- **REA e PEC.** Il REA (PD 436591) risulta solo da un estratto di ricerca; la PEC non è stata trovata. Sono fuori dal piede finché non sono verificati.
- **Telefono.** C'è solo il cellulare +39 348 6046875. Nessun numero fisso.
- **Leghe di alluminio.** Le sigle (EN AB 46000, 46100, 47100, 47000, 46400; Al-Si, Al-Cu, Al-Mg) vengono dalla pagina Leghe di alluminio, che descrive lo stabilimento di un produttore: chiarire di chi sono (STEMIN o altri).
- **Famiglie di prodotto.** Quali delle 16 sono ancora vive e se la manutenzione dei forni nel week-end è ancora offerta. "Forni a gas ed elettrici" riassume i forni della pagina usato.
- **Frasi accorciate.** "Ordini evasi in tempi molto brevi, su tutto il territorio nazionale" accorcia "assolvere ed evadere in tempi molto brevi gli ordini dei ns. clienti su tutto il territorio nazionale"; "Il magazzino lo teniamo noi" riassume "sollevandoli dall'oneroso costo di gestione del magazzino"; nella frase sul week-end "ed il consumi" è diventato "e i consumi".
- **Logotipo.** La scritta PROGECOM è composta in Tinos 700, un serif bold vicino a quello di oggi: va confermata con il titolare, insieme al logo vettoriale.

## Pagine del sito nuovo a cui puntano i link

Sezioni della home: `#prodotti`, `#forni`, `#servizio`, `#usato`, `#chi`, `#richiesta`.

| Pagina | Percorso |
|---|---|
| Home | `/` |
| Chi siamo | `/chi-siamo/` |
| Rappresentanze, STEMIN | `/rappresentanze/stemin/` |
| Cerco, vendo, usato | `/usato/` |
| Prodotti (indice) | `/prodotti/` |
| Forni fusione e attesa | `/prodotti/forni-fusione-attesa/` |
| Crogioli | `/prodotti/crogioli/` |
| Refrattari e isolanti | `/prodotti/refrattari/` |
| Ricambistica forni | `/prodotti/ricambistica-forni/` |
| Bruciatori preriscaldo stampi | `/prodotti/bruciatori/` |
| Leghe di alluminio | `/prodotti/leghe-di-alluminio/` |
| Leghe di zinco | `/prodotti/leghe-di-zinco/` |
| Madrileghe | `/prodotti/madrileghe/` |
| Degasaggio | `/prodotti/degasaggio/` |
| Prodotti per scorifica e affinazione | `/prodotti/scorifica-affinazione/` |
| Filtrazione alluminio e metalli | `/prodotti/filtrazione/` |
| Trasporto metallo liquido | `/prodotti/trasporto-metallo-liquido/` |
| Pistoni iniezione presse | `/prodotti/pistoni-iniezione/` |
| Automazioni lubrificazione | `/prodotti/automazioni-lubrificazione/` |
| Distaccanti e vernici isolanti | `/prodotti/distaccanti/` |
| Strumenti di controllo | `/prodotti/strumenti-di-controllo/` |
| Privacy | `/privacy/` |
| Cookie | `/cookie/` |
| Versione inglese | `/en/` |

Telefono con `tel:`, email con `mailto:` (sempre con oggetto), indirizzo con il link a Google Maps ("Vai alla mappa").

## Newsletter e social

- **Newsletter: no.** News è "coming soon", non ci sono cataloghi propri né fiere e i clienti sono solo fonderie. L'unico contenuto che cambia è l'usato, che si serve meglio con la pagina Usato e il telefono.
- **Seguici: no.** Non esistono social aziendali. C'è solo il canale YouTube personale di Mauro Poggese (https://www.youtube.com/@MauroPoggese-n6f, video del magazzino e degli strumenti), da aggiungere al piede solo se lui vuole.

## Foto da rifare dal vero

In pagina ci sono solo immagini loro, ma nessuna è una foto professionale: il magazzino è un fotogramma di video, le quattro foto dei gruppi sono scatti al telefono con luci diverse. Basta mezza giornata nel magazzino di Mestrino, più un'ora in una fonderia cliente. Un solo fotografo, una sola luce, due formati (4:3 per i gruppi, 3:2 o 16:9 per l'apertura).

1. **Apertura: il magazzino crogioli.** Al posto del fotogramma. Corridoio fra gli scaffali di tre quarti, luce del capannone più un pannello morbido da sinistra, cavalletto, 24-35 mm a f/8, file da almeno 6000 px, orizzontale. Meglio con Mauro Poggese che legge l'etichetta di un crogiolo o carica un bancale, senza guardare l'obiettivo: è l'unica persona dell'azienda e la regola 3 chiede persone o sede.
2. **Fusione e forni.** Una bocca di forno durante la pulizia del week-end in una fonderia cliente, con il tecnico al lavoro (volto non in primo piano), al posto della bocca rossa della pagina usato (diritti incerti).
3. **Trattamento del metallo.** Una bobina di rete filtrante loro e il rotore in grafite, still life su carta grigio chiaro, luce laterale morbida da sinistra, 90-100 mm a f/8-11: al posto della macro della rete, forse del produttore.
4. **Pressofusione.** I pistoni e la fascia in rame della foto di oggi, sullo stesso fondo e con la stessa luce dello still life.
5. **Leghe e controllo.** La valigetta per macrografia e qualche strumento (pirometro, termocoppia) sullo stesso fondo; un lingotto in mano, se STEMIN è d'accordo.
6. **Servizio.** Il furgone o un bancale in partenza dal magazzino: darebbe una foto vera a "consegne in tutta Italia".

## Licenze

- **Caratteri.** Archivo, Google Fonts, SIL Open Font License 1.1; Tinos 700, Google Fonts, Apache License 2.0. Uso commerciale libero, file serviti dalla pagina, licenze in `sito/fonts/`.
- **Foto.** Nessuna foto di repertorio in pagina (tolte Diecasting Mould e Grieveson, che restano solo in `assets/esterne/` e in `assets/CREDITI.md`). Le foto dal sito di Progecom hanno diritti da confermare: la bocca di forno viene dalla pagina dell'usato e forse è del venditore; la rete filtrante forse è del produttore; il magazzino è l'anteprima del loro video. Elenco in `assets/CREDITI.md`.

## Logo

- Il simbolo con la fascia oro è il loro PNG (`logo-simbolo-fascia-oro-738.png`), non ricolorato, esportato in WebP a 48, 96, 144 e 192 px. Non esistono un vettoriale né un PDF.
- Da chiedere: il logo vettoriale o almeno un PNG grande, e il carattere della scritta PROGECOM. Il simbolo, a linee semplici, si può ricostruire in SVG fedele confrontandolo sovrapposto al PNG.
