# 01. Analisi del sito attuale (www.zoccaratoserramenti.it)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte o misurato, **[Probabile]** inferenza forte, **[Ipotesi]** da verificare con il cliente, **[DA CONFERMARE]** dato da chiedere al cliente prima di usarlo.

Prove: pagine scaricate in `_prova/crawl/pagine/`, misure Playwright in `_prova/attuale/misure-1440.json` e `misure-390.json`, prova del consenso in `_prova/attuale/consenso.json`, screenshot in `_prova/attuale/`, fonti esterne in `_prova/crawl/fonti/`, inventario delle foto in `_prova/inventario-immagini.json`.

## In breve

- Sito statico in HTML scritto a mano (nessun CMS), impaginato a 960 px, **senza meta viewport**: su telefono la pagina resta larga 980 px e viene rimpicciolita (scrollWidth 980 a 390 su tutte le 14 pagine), il menu scende a circa 6 px effettivi. [Certo]
- Fermo al 2015: **©2015 nel piè di pagina di tutte le 14 pagine**, mappa Google incorporata il 21 luglio 2015, grafica "ECOBONUS2015 65%", "esperienza quarantennale" (dal 1974 sono 52 anni), informativa privacy sul solo D.Lgs. 196/2003. [Certo]
- La home non ha testo: 5 foto a scorrimento automatico e 4 didascalie che puntano a "#". Il carattere previsto (Open Sans) non si carica mai perché è chiamato in http e il browser lo blocca. [Certo]
- Il patrimonio vero sono le foto dei lavori: **190 immagini**, quasi tutte 1000x750 o 750x1000, scattate con fotocamere compatte (i timbri data visibili sono del 2010 e del 2011). Circa **63 foto distinte reggono fino a 1000 px** (48 orizzontali, 1 quasi quadrata, 14 verticali); una sola foto regge una apertura a tutta larghezza (la slide home-02, 1680 px). 10 foto hanno il timbro data della fotocamera stampato sopra. [Certo]
- Identità esistente: logo blu "ZOCCARATO ...l'originale... serramenti ●●●● dal 1974" (solo JPG 320x76), blu **#006BAC** del sito e del logo, blu notte **#203870** nei punti e in "dal 1974", una fascia blu sotto le foto. I camion e i furgoni della flotta portano la stessa grafica: è il materiale più riconoscibile dell'azienda. [Certo]
- Storia raccontata dal sito: 1974 il fondatore apre una piccola officina del ferro, 1982 entrano i figli Sante e Maurizio e parte il serramento in alluminio, 1997 apre l'unità locale di Brebbia (VA). Lavori per privati e per la rete delle stazioni di servizio. [Certo, dal sito]
- Problemi di privacy misurati: banner Cookiebot con "Statistiche" e "Marketing" **già attivati**, mappa Google caricata prima del consenso e anche dopo "Rifiuta", Google Analytics che parte senza consenso sulla pagina della privacy. [Certo]
- Attenzione: **zoccaratoserramenti.com non è loro**. È di Zoccarato Giannino, Fagnano Olona (VA), P.IVA 00131820128, serramenti in PVC; anche la pagina facebook.com/ZoccaratoSerramenti risulta di quella impresa. [Certo per il dominio, Probabile per Facebook]

## Pagine esistenti

Nessuna sitemap (`/sitemap.xml` e `/robots.txt` rispondono 404). Pagine trovate seguendo menu e link interni: 14, più `/index.html` che duplica la home.

| N. | Pagina | URL | Contenuto | Foto in galleria |
|---|---|---|---|---|
| 01 | Home | `/` (doppione `/index.html`) | slider RoyalSlider di 5 foto 1680x850, nessun testo, piè di pagina | 0 |
| 02 | Chi siamo | `/chi-siamo.html` | storia 1974-1997, servizio effrazioni, invito Ecobonus 2015 | 8 + grafica Ecobonus |
| 03 | Privati: abitazioni civili | `/abitazioni.html` | paragrafo comune + galleria Highslide | 53 |
| 04 | Privati: pensiline | `/pensiline-privati.html` | paragrafo comune + galleria | 9 |
| 05 | Privati: porte interne | `/interni.html` | paragrafo comune + galleria | 9 |
| 06 | Privati: portoncini ingresso | `/ingresso.html` | paragrafo comune + galleria | 11 |
| 07 | Privati: scorrevoli | `/scorrevoli.html` | paragrafo comune + galleria | 22 |
| 08 | Privati: sistemi oscuranti | `/oscuranti.html` | paragrafo comune + galleria | 26 |
| 09 | Privati: speciali residenziali | `/speciali.html` | paragrafo comune + galleria | 11 |
| 10 | Industria: commerciali industriali | `/commerciali.html` | paragrafo comune + galleria (1 foto rotta) | 26 (25 esistenti) |
| 11 | Industria: monoblocchi prefabbricati | `/monoblocchi.html` | paragrafo comune + galleria | 3 |
| 12 | Industria: pensiline | `/pensiline-industria.html` | paragrafo comune + galleria | 3 |
| 13 | Dove siamo e contatti | `/dove-siamo-contatti.html` | indirizzi, telefono, fax, email, mappa Google; nessun modulo | 0 |
| 14 | Privacy e cookie | `/cookie-policy.htm` | informativa D.Lgs. 196/2003 + dichiarazione Cookiebot | 0 |

Menu: HOME, CHI SIAMO, LAVORAZIONI PER PRIVATI (7 voci), LAVORAZIONI PER L'INDUSTRIA (3 voci), DOVE SIAMO e CONTATTI. Le due voci con sottomenu non hanno una pagina (`href="#"`) e il sottomenu si apre solo al passaggio del mouse (jQuery `hover`). [Certo]

Screenshot del sito attuale: `_prova/attuale/NN-pagina-1440.png` (pagina intera a 1440), `NN-pagina-390.png` (pagina intera su telefono 390), `NN-pagina-390-schermo.png` (prima schermata su telefono), `00-banner-cookie-1440.png` e `00-banner-cookie-390.png` (banner Cookiebot), `13-contatti-dopo-rifiuto-1440.png`.

## Testi reali (verbatim, con i refusi originali)

Home (didascalie sulle slide, tutte con link a "#"):
1. Slide 1: nessuna didascalia; nella foto è stampato "serramenti ●●●● dal 1974".
2. "SERRAMENTI" / "SERRAMENTI INDUSTRIALI" / "ESTERNI e GIARDINI" / "L'ORIGINALE DAL 1974"

Chi siamo, titolo "Zoccarato Serramenti: dal 1974":
3. "Era l'anno 1974 quando il fondatore dell'azienda ZOCCARATO abbandonava la sua posizione di dipendente presso un'azienda locale per avviare una piccola realtà familiare specializzata sulla lavorazione del ferro (recinzioni, cancelli ecc.)."
4. "Nel 1982 inizia a svilupparsi la zona artigianale del paese ed entrano in azienda i suoi due figli maschi Sante e Maurizio e con loro inizia la produzione del serramento in alluminio. Con innumerevoli sforzi si costruisce il primo capannone ZOCCARATO che, dopo alcuni lavori di ampliamento nel corso dell'ultimo ventennio, è diventato l'attuale sede produttiva ed amministrativa della ZOCCARATO SERRAMENTI Snc pur iniziando ad acquisire clientela anche nella zona di Varese dove nel 1997 è stata aperta un'unità Locale."
5. "L'esperienza quarantennale della ZOCCARATO SERRAMENTI nel settore dei serramenti in alluminio ha portato l'azienda ad offrire un servizio mirato alla cura della qualità e al servizio personalizzato del cliente finale, dalla progettazione alla posa ed alla rifinitura, sempre ad opera del nostro personale specializzato e di maturata esperienza."
6. "Nell'ultimo decennio ha collaborato con le più note compagnie di distribuzione carburanti sempre avendo quell'anima "Artigianale", (che caratterizza l'azienda fin dalla nascita) verso il cliente privato o il professionista."
7. Titolo "I SERVIZI ZOCCARATO SERRAMENTI": "La ditta ZOCCARATO SERRAMENTI in caso di effrazioni e danni da furto assicura alla propria clientela un intervento in tempi rapidissimi e con l'assistenza di preventivazione per le compagnie assicurative."
8. "La ditta ZOCCARATO SERRAMENTI vi invita ad approfittare dei vantaggi della riqualificazione energetica, sostituendo i vostri serramenti." / "Scopri di più sul sito della Agenza delle Entrate, alla pagina dedicata."
9. Didascalie delle foto: "1974: Zoccarato, gli inizi" / "1982: Zoccarato e la zona industriale" / "oggi: Zoccarato, la Flotta Aziendale" (3 foto) / "per i propri clienti, intervento immediato in caso di effrazioni" (3 foto) / "Ecobonus 2015".

Pagine delle lavorazioni (10 pagine, stesso paragrafo):
10. Titoli: "Lavorazioni per Privati: ABITAZIONI", "...: PENSILINE", "...: PORTE INTERNE", "...: PORTONCINI INGRESSO", "...: INFISSI SCORREVOLI", "...: SISTEMI OSCURANTI", "...: SPECIALI RESIDENZIALI"; "Lavorazioni l'Industria: COMMERCIALI e INDUSTRIALI", "Lavorazioni l'Industria: MONOBLOCCHI PREFABBRICATI", "Lavorazioni l'Industria: PENSILINE COMMERCIALI".
11. Paragrafo comune: "L'esperienza quarantennale della ZOCCARATO SERRAMENTI nel settore dei serramenti in alluminio ha portato l'azienda ad offrire un servizio mirato alla cura della qualità e al servizio personalizzato del cliente finale, dalla progettazione alla posa ed alla rifinitura, sempre ad opera del nostro specializzato e di matura esperienza"
12. Didascalie ripetute su ogni foto: "Abitazioni Residenziali", "Pensiline Residenziali", "Porte interne", "Portoncini di Ingresso", "Infissi Scorrevoli", "Sistemi oscuranti", "Speciali Reesidenziali", "Commerciali e Industriali", "Monoblocchi prefabbricati", "Pensiline Commerciali".

Dove siamo e contatti, titolo "Zoccarato Serramenti: dove siamo":
13. "ZOCCARATO SERRAMENTI / via dell'industria, 18 - Borgoricco (PD) / Tel. 049 5798194 | Fax 049 9335588 / Unità locale: / Via Sandro Pertini, 1 / 21020 Brebbia (VA) / info@zoccaratoserramenti.it"

Piè di pagina (uguale su tutte le pagine):
14. "Zoccarato Serramenti Snc / via dell'industria, 18 - Borgoricco (PD) | Tel. 049 5798194 | Fax 049 9335588 | info@zoccaratoserramenti.it / ©2015 Zoccarato Serramenti Snc | P. IVA 01298510288 | privacy"

Privacy e cookie (estratti):
15. "INFORMATIVA SULLA PRIVACY E SUI WEB COOKIE ai sensi del D.Lgs. 196/2003 (Codice della privacy)." Il testo parla di "contratti di acquisto dei prodotti e/o servizi tramite il sito", di registrazione e account utente e di "numero di carta di credito/debito": nulla di questo esiste sul sito. Segue la dichiarazione Cookiebot "aggiornata l'ultima volta il 22/07/23" con 1 cookie necessario e 4 statistici (_ga, _ga_#, _gat, _gid).

Testi chiusi dentro le immagini (trascritti):
16. Logo: "ZOCCARATO ...l'originale... serramenti ●●●● dal 1974".
17. Fiancata del camion (`fascia-azienda`, `chi-siamo-laflotta`, slide home-01): "SERRAMENTI METALLICI ZOCCARATO ...l'originale BORGORICCO (PD) - BREBBIA (VA) Tel. 049 579 81 94 - zoccaratoserramenti@tiscali.it".
18. Slide home-01: "serramenti ●●●● dal 1974".
19. Grafica `ecobonus.jpg`: "ECOBONUS2015 65% detrazione fiscale" con la scala delle classi energetiche A-G.

Refusi e incoerenze da non riportare nel nuovo sito: "del nostro specializzato e di matura esperienza" (manca "personale", su 10 pagine; in Chi siamo è giusto: "del nostro personale specializzato e di maturata esperienza"); "Lavorazioni l'Industria" (manca "per"); "Speciali Reesidenziali"; menu "speciale residenziali" contro titolo "SPECIALI RESIDENZIALI"; "Agenza delle Entrate"; "unità Locale"; "quell'anima "Artigianale", (che...)"; "esperienza quarantennale" (scritto nel 2015: dal 1974 sono 52 anni); "via dell'industria" minuscolo. Il nome compare come "ZOCCARATO SERRAMENTI", "Zoccarato Serramenti Snc", "ZOCCARATO SERRAMENTI Snc", "Zoccarato Serramenti S.N.C." (Google): nel nuovo sito si usa **Zoccarato Serramenti** e, dove servono i dati legali, **Zoccarato Serramenti S.n.c. di Zoccarato Sante & Maurizio**.

Frasi forti da tenere (corrette): l'officina del ferro del 1974 e i "recinzioni, cancelli"; i figli Sante e Maurizio e il primo serramento in alluminio nel 1982; "dalla progettazione alla posa ed alla rifinitura, sempre ad opera del nostro personale"; l'anima "artigianale" verso il privato e il professionista; l'intervento rapido dopo un'effrazione con il preventivo per l'assicurazione; "l'originale dal 1974".

## Cosa fanno (servizi e prodotti)

Dal sito [Certo]:
- **Serramenti in alluminio** progettati, prodotti, posati e rifiniti con personale proprio, per privati e per aziende.
- **Per privati**: finestre e portefinestre per abitazioni civili (anche verande, bovindi, vetrate a tutta altezza, timpani vetrati), pensiline e pergole, porte interne, portoncini d'ingresso, scorrevoli (anche alzanti con veneziane nel vetro), sistemi oscuranti (persiane a battente, a libro e scorrevoli, scuri, avvolgibili), "speciali residenziali" (dalle foto: parapetti inox a cavi, cancelli in lamiera, coperture vetrate apribili, lucernari).
- **Per l'industria e il commercio**: serramenti per uffici, negozi e capannoni, vetrine, box e chioschi, **monoblocchi prefabbricati** (dalle foto: locali tecnici in pannelli), pensiline commerciali (dalle foto: pensiline ad arco di stazioni di servizio).
- **Stazioni di servizio**: "ha collaborato con le più note compagnie di distribuzione carburanti"; le foto mostrano punti vendita, chioschi e pensiline di distributori. Marchi delle compagnie non citati. [DA CONFERMARE quali si possono nominare]
- **Pronto intervento dopo effrazioni e furti**, con preventivo per le compagnie assicurative.
- **Sostituzione dei serramenti per la riqualificazione energetica** (il sito rimanda all'Ecobonus 2015).

Da fonti pubbliche:
- Oggetto sociale (Registro Imprese, riportato da Atoka e Coobiz): "la costruzione, l'installazione e la manutenzione di serramenti in ferro, alluminio e pvc, carpenteria metallica e leggera, nonche' il montaggio di motori per chiusure telecomandate". [Certo] Se oggi lavorano anche PVC e automazioni è [DA CONFERMARE].
- Lavori per enti pubblici in provincia di Varese: Comune di Laveno Mombello, "FORNITURA E POSA N. 2 PORTE UFFICI AMMINISTRATIVI VILLA FRUA", affidamento diretto del 28/12/2021, CIG Z463470591, 8.159 euro; Comune di Cocquio Trevisago, "FORNITURA E POSA DI INFISSI EDIFICIO DESTINATO A ASILO NIDO IN LOCALITÀ "TORRE"", aggiudicazione del 16/10/2023, CIG ZA83C2E5CA, 20.420 euro. [Certo] Usarli come referenze nel sito è [DA CONFERMARE].
- Zone servite: Padovano (sede di Borgoricco) e Varesotto (unità locale di Brebbia dal 1997). Le foto mostrano spesso case con vista lago: [Ipotesi] lavori nella zona del Lago Maggiore, da non scrivere senza conferma.
- Marchi di profili, vetri o accessori: **nessuno dichiarato** sul sito. Certificazioni: **nessuna dichiarata**. [Certo]
- Recensioni Google: 3,6 su 5 da 11 recensioni (6 da cinque stelle, 1 da quattro, 1 da tre, 3 da una; una negativa riguarda zanzariere). Non si usano nel sito senza permesso degli autori. [Certo]

## Immagini usate oggi

Tutte scaricate alla risoluzione massima pubblicata (le gallerie Highslide aprono il file grande; le miniature `-ico` 150x150 sono escluse). Nessun `srcset`, nessuna versione più grande sul server. Originali in `assets/originali/` con nomi parlanti e `manifest.json`; giudizio foto per foto in `_prova/inventario-immagini.json` (soggetto, qualità, larghezza massima, uso).

| Tipo | Quantità | Risoluzione | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Slide della home | 5 | 1680x850 | solo **home-02** (scorrevole effetto legno sotto portico) ha dettaglio vero a 1680; home-01, 03, 05 sono foto da 1000 px ingrandite (morbide a 100%, reggono circa 1200 px); home-04 regge circa 1400 | home-02 per l'apertura; le altre come foto a mezza pagina |
| Foto dei lavori, privati | 141 | 1000x750, 1000x600, 750x1000; alcune 563x750 e 450x750 | 54 buone, 49 discrete, 38 scarse; portoncini e porte interne sono le più deboli (piccole, sfocate, bianco su bianco) | gallerie per categoria, foto a mezza pagina fino a 1000 px, card |
| Foto dei lavori, industria | 31 | 1000x750, 750x1000 | 10 buone (uffici, vetrine, pensilina ad arco, monoblocchi), 19 discrete, 2 scarse; 1 file citato manca (`commerciali-25.jpg`, 404) | blocco "Aziende e stazioni di servizio" |
| Foto aziendali | 8 | 1000 px, una 400x400 | 2 foto storiche riscansionate (camion con struttura in ferro, sede vista dall'alto), 3 della flotta e della sede (camion con logo, furgoni in piazzale), 3 di effrazioni | pagina Azienda: storia, flotta, pronto intervento |
| Fasce di testata | 3 | 1680x188 | ritagli ingranditi, molto morbidi | non usare |
| Logo | 1 | JPG 320x76 su bianco | basta a 1x per 211 px, sgrana su retina; nessun vettoriale | **chiedere il logo vettoriale**; per la demo si ridisegna come testo |
| Grafica Ecobonus 2015 | 1 | 400x150 | contenuto scaduto | non usare |

Altri dati sulle foto [Certo]:
- 10 foto hanno il **timbro data o ora** della fotocamera in giallo o rosso (2010/06/07, 2010/08/06, 2011/03, 2011/05/18 19:35 e simili): vanno ritagliate o scartate.
- Doppioni: `abitazioni-19B` = `oscuranti-19B`; `speciali-27` = `speciali-105`. Le 5 slide della home vengono da foto delle gallerie.
- Foto distinte utilizzabili: **circa 63 buone fino a 1000 px di larghezza** (500 px css su schermi retina), 1 sola per l'apertura a tutta larghezza (1680 px). Nessuna foto supera i 1680 px.
- Le foto sono di cantiere, non da catalogo: luce diretta, ombre, cielo bruciato in alcune, persone e auto riflesse. Raccontano bene la varietà del lavoro; non reggono un'impaginazione a foto grandi e piene.
- Le miniature di Chi siamo sono **deformate**: file 150x150 mostrati a 180x150 (stirati del 20%); la grafica Ecobonus 400 px è mostrata a 430. (`misure-1440.json`, pagina 02)
- Sul sito non ci sono PDF, cataloghi, video o animazioni Flash; gli unici sfondi CSS sono le 3 fasce di testata.
- Nessuna foto pubblicata dall'azienda fuori dal sito: la scheda Google non è rivendicata (solo foto di recensori), la pagina Facebook trovata chiede il login, nessun Instagram (`assets/esterne/manifest.json`). La Wayback Machine non era raggiungibile da qui: da riprovare per cercare versioni precedenti al 2015.

## Problemi tecnici da segnalare al cliente

Misure prese il 6 ottobre 2026 con Playwright (Chromium), dalla rete del container. Ogni punto ha la prova indicata.

1. **Non si legge da telefono.** Nessun `<meta name="viewport">` su nessuna pagina: a 390 px di larghezza `document.documentElement.scrollWidth` vale **980** su tutte le 14 pagine; la pagina viene rimpicciolita al 40%, il menu (14,4 px su 980) diventa di circa 6 px effettivi, le voci sono bersagli di circa 17 px. Prova: `misure-390.json`, `NN-pagina-390-schermo.png`. [Certo]
2. **Contenuti fermi al 2015.** "©2015" nel piè di pagina di tutte le 14 pagine; mappa incorporata con timestamp `1437489980247` (21 luglio 2015); grafica "ECOBONUS2015 65%" e link alla pagina dell'Agenzia delle Entrate sulla "Detrazione riqualificazione energetica 55" che ora porta alla home del portale; "esperienza quarantennale"; sui camion fotografati l'email `zoccaratoserramenti@tiscali.it`. I file del server risultano caricati nel 2021 e nel 2022 (header Last-Modified), ma i contenuti sono quelli del 2015. [Certo]
3. **Privacy e cookie.** (a) Informativa "ai sensi del D.Lgs. 196/2003", nessun riferimento al Regolamento UE 2016/679 (GDPR), testo generico che parla di acquisti online, account e carte di credito che il sito non ha. (b) Banner Cookiebot con **"Statistiche" e "Marketing" già attivati** prima della scelta (`00-banner-cookie-1440.png`, `misure-1440.json` campo `banner`). (c) La dichiarazione cookie (aggiornata 22/07/23) elenca solo cookie necessari e statistici, non quelli di marketing che il banner propone. (d) Nella pagina contatti la **mappa Google si carica prima del consenso e resta caricata dopo "Rifiuta"** (richieste a google.com/maps, maps.googleapis.com, maps.gstatic.com; `consenso.json`). (e) La pagina della privacy non carica Cookiebot ma carica Google Analytics: aprendola, senza alcun consenso, partono `analytics.js` (UA-65264279-1) e `gtag/js?id=G-4MK7VR8NXT` e vengono scritti i cookie `_ga`, `_gid`, `_gat`, `_ga_4MK7VR8NXT` (`consenso.json`). [Certo]
4. **Peso e velocità.** Home: **4,9 MB in 32 richieste**, di cui 4,77 MB di immagini (5 slide da 795 KB a 1,19 MB, caricate tutte subito). Evento load 2,6 s a 1440 da rete veloce; con rete mobile lenta simulata (profilo Slow 4G: 1,6 Mbps, 150 ms) **load 25 s, LCP 22 s** (due prove: 25,5 e 25,0 s). Pagine galleria: 40-92 richieste, 1,0-1,9 MB. Prova: `misure-*.json`, `_prova/script/lento.cjs`. [Certo]
5. **Codice vecchio ed errori.** Due versioni di jQuery sulla stessa pagina (1.6.2 del 2011 e 2.1.3 del 2014), RoyalSlider 8.1, Highslide JS, script di un vecchio banner cookie ancora inclusi; errore JavaScript in console su 12 pagine su 14 (`$(...).royalSlider is not a function`) e su 3 pagine anche `Failed to execute 'insertBefore'` per il codice Analytics duplicato (ingresso, oscuranti, scorrevoli). [Certo]
6. **Carattere mai caricato.** Il foglio di Google Fonts per Open Sans è chiamato in `http://` su una pagina in https: il browser lo blocca (Mixed Content) su tutte le pagine e il sito si vede in un carattere di ripiego. [Certo]
7. **Link rotti o vuoti.** `images/commerciali-25.jpg` risponde 404 (la galleria Commerciali apre una foto che non c'è); 6 link "#" in home (2 voci di menu, 4 didascalie delle slide) e 2 su ogni altra pagina; link all'Agenzia delle Entrate che finisce sulla home del portale. Telefono non cliccabile (nessun link `tel:`). [Certo]
8. **Contatti.** Nessun modulo per chiedere un preventivo: solo telefono, fax ed email. Nessun orario. In un settore dove il sito serve soprattutto a raccogliere richieste di preventivo, è il punto che pesa di più. [Certo]
9. **Motori di ricerca e accessibilità.** Stesso titolo "ZOCCARATO SERRAMENTI" su tutte le 15 URL; nessuna meta description; nessun H1 (tranne la privacy); nessun attributo `lang`; le foto delle gallerie hanno tutte `alt="Highslide JS"`, le 5 slide della home non hanno alt; nessuna sitemap; il dominio senza www (`https://zoccaratoserramenti.it/`) risponde 200 con le stesse pagine invece di reindirizzare (contenuto doppio). [Certo]
10. **Dati societari.** Il piè di pagina ha sede e P.IVA (bene). Mancano la ragione sociale completa ("S.n.c. di Zoccarato Sante & Maurizio") e il numero di iscrizione al Registro delle Imprese (REA PD-239515), che l'art. 2250 c.c. chiede anche sul sito alle società iscritte al registro. [Probabile: da far confermare al commercialista]
11. **HTTPS**: funziona. Certificato Let's Encrypt valido fino al 23/11/2026 (rinnovo automatico, da crt.sh), http reindirizza a https con 301. Server nginx con pannello Plesk. Nessun CMS: ogni modifica richiede di correggere a mano l'HTML. [Certo]
12. **Testi chiusi in immagini**: "serramenti dal 1974" stampato sulla slide 1, tutta la grafica Ecobonus, il logo in JPG. [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Zoccarato Serramenti S.n.c. di Zoccarato Sante & Maurizio | aziende.it, Visurissima (Registro Imprese) |
| Forma | Società in nome collettivo, attiva | aziende.it |
| P.IVA e codice fiscale | 01298510288 | sito (piè di pagina), aziende.it |
| REA | PD-239515, CCIAA di Padova | aziende.it, Visurissima |
| Iscrizione | data iscrizione 22/10/1992, inizio attività 10/09/1992 (aziende.it indica 10/09/1992 come data di iscrizione) | Visurissima, aziende.it, Companyreports |
| Attività dal | 1974 (officina del ferro del fondatore); alluminio dal 1982 | sito, Chi siamo |
| ATECO | 25.12.1 (25.12.10), fabbricazione di porte, finestre e loro telai, imposte e cancelli metallici | aziende.it, Atoka |
| Codice SDI | J6URRTW | aziende.it, Visurissima |
| Sede | Via dell'Industria 18, 35010 Borgoricco (PD), zona artigianale (Atoka indica la frazione San Michele delle Badesse) | sito, Registro Imprese, Atoka |
| Unità locale | Via Sandro Pertini 1, 21020 Brebbia (VA), aperta nel 1997 | sito; Coobiz ("Altre sedi: Brebbia (Varese), Via Pertini 1") |
| Telefono | 049 5798194 | sito, Google, PagineBianche |
| Fax | 049 9335588 | sito |
| Email | info@zoccaratoserramenti.it | sito |
| PEC | **zoccaratoserramenti@pec.it** | Visurissima, "Fonte: Registro Imprese", dati al 06/10/2026. INI-PEC non raggiungibile da qui (richiesta respinta): **verificare su INI-PEC con la P.IVA prima dell'invio** |
| Soci | Sante e Maurizio Zoccarato (dalla ragione sociale e da Chi siamo) | Registro Imprese, sito |
| Fondatore | il padre di Sante e Maurizio; il sito non ne dice il nome | [DA CONFERMARE] |
| Dipendenti | 6 (anno 2024, aziende.it aggiornato al 5 luglio 2026); Atoka ne indica 8 | aziende.it, Atoka |
| Fatturato | non pubblicato (snc, nessun bilancio depositato) | Visurissima |
| Orari | non sul sito; Google (scheda non rivendicata) mostra solo "martedì 08:30-17" | [DA CONFERMARE] |
| Google | "Zoccarato Serramenti S.n.c.", categoria Fornitore di finestre, 3,6 stelle da 11 recensioni, scheda **non rivendicata**, accesso per sedia a rotelle segnalato | Google Maps, cid 838436468784443514 |
| Social | nessun profilo verificato; pagina Facebook "Zoccarato serramenti" (id 100066984705761) non consultabile senza login | [DA CONFERMARE] |
| Marchi trattati | nessuno dichiarato | sito |
| Certificazioni | nessuna dichiarata | sito |
| Colori | blu #006BAC (titoli e fascia del sito, logo #0068B0), blu notte #203870 (punti e "dal 1974"), rosso #C50004 solo al passaggio del mouse | CSS del sito, logo |
| Omonimi da non confondere | Zoccarato Giannino, Fagnano Olona (VA), P.IVA 00131820128, PVC, sito zoccaratoserramenti.com; "Zoccarato R." a Borgoricco nelle directory | Atoka, ricerca web |

Schede esterne con errori: Reteimprese indica il civico 28 invece di 18; PagineBianche e Google non sono rivendicate. [Certo]

Cosa manca e va chiesto al cliente: logo vettoriale; foto recenti (la flotta, la sede, l'officina, posa in cantiere, lavori dopo il 2015) e gli originali delle foto delle gallerie a piena risoluzione; orari; nome del fondatore; quali lavori per stazioni di servizio ed enti pubblici si possono citare; se lavorano anche PVC, zanzariere e automazioni; marchi dei profili usati; conferma della PEC.

## URL vecchi

Da reindirizzare con 301 alle pagine nuove (la destinazione si decide nella mappa pagine, 03). Vanno coperte anche le varianti `http://`, `https://zoccaratoserramenti.it/` senza www e `/index.html`.

| URL vecchio | Contenuto |
|---|---|
| `/` | Home |
| `/index.html` | Home (doppione) |
| `/chi-siamo.html` | Chi siamo |
| `/abitazioni.html` | Privati: abitazioni civili |
| `/pensiline-privati.html` | Privati: pensiline |
| `/interni.html` | Privati: porte interne |
| `/ingresso.html` | Privati: portoncini ingresso |
| `/scorrevoli.html` | Privati: scorrevoli |
| `/oscuranti.html` | Privati: sistemi oscuranti |
| `/speciali.html` | Privati: speciali residenziali |
| `/commerciali.html` | Industria: commerciali industriali |
| `/monoblocchi.html` | Industria: monoblocchi prefabbricati |
| `/pensiline-industria.html` | Industria: pensiline |
| `/dove-siamo-contatti.html` | Dove siamo e contatti |
| `/cookie-policy.htm` | Privacy e cookie |

Le immagini sono in `/images/` (190 file grandi più 180 miniature `-ico`); se Google le ha indicizzate conviene lasciare la cartella online per qualche mese o reindirizzarla alle gallerie. Elenco completo dei file in `_prova/crawl/lista-risorse.txt`.

## Fonti

- Sito: https://www.zoccaratoserramenti.it/ (crawl completo del 6/10/2026 in `_prova/crawl/`).
- Registro Imprese tramite: https://www.aziende.it/zoccarato-serramenti-snc-di-zoccarato-sante-maurizio ; https://www.visurissima.it/aziende/ZOCCARATO-SERRAMENTI-S.N.C.-DI-ZOCCARATO-SANTE--MAURIZIO_01298510288.html ; https://atoka.io/public/it/azienda/zoccarato-serramenti-snc-di-zoccarato-sante-maurizio/2833f8d2a931 ; https://www.companyreports.it/report-aziende/zoccarato-serramenti-snc-di-zoccarato-sante-maurizio-01298510288 ; https://www.coobiz.it/azienda/borgoricco-costruzione-installazione/co1906284
- Appalti: https://lavenomombello.trasparenza-valutazione-merito.it/web/trasparenza/pga-g/-/anac/display/215 ; https://cocquiotrevisago.trasparenza-valutazione-merito.it/web/trasparenza/pga-g/-/anac/display/156449
- Google Maps: https://www.google.com/maps?cid=838436468784443514 ; PagineBianche: https://www.paginebianche.it/borgoricco/zoccarato-serramenti.4490725
- Certificati: https://crt.sh/?q=zoccaratoserramenti.it
- Omonimo: https://atoka.io/public/it/azienda/zoccarato-giannino/1e9c2c7dbeef ; https://www.zoccaratoserramenti.com/
