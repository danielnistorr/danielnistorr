# 01. Analisi del sito attuale (www.conceriaeuropa.it)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte o misurato, **[Probabile]** inferenza forte, **[DA CONFERMARE]** dato da verificare con il cliente (finisce nel LEGGIMI).
Le misure di rete sono prese con Playwright (Chromium) attraverso il proxy di questo ambiente: i tempi assoluti sono indicativi, i rapporti e i pesi no.
Nei testi verbatim i trattini medi dell'originale sono resi con il trattino semplice.

## In breve

- Sito PHP fatto a mano da Net Evolution, una sola pagina (`index.php`) con riquadri che caricano frammenti via jQuery (`it/contenuti.php`, `it/semianilina.php`...), in tre lingue (`?it`, `?en`, `?de`; senza parametro esce l'inglese) più un sottosito cinese/inglese separato su WordPress 3.9 del 2014 (`products.conceriaeuropa.it`). Impianto del 2012 circa (jQuery 1.8.3, uno snapshot Wayback del 20/01/2012), ritoccato nel tempo: foto chi siamo 2022, CSS 2024, loghi certificazioni e politica integrata gennaio 2025, dichiarazione di accessibilità luglio 2026. [Certo]
- Non è responsive: manca il meta viewport. A 390 px il telefono impagina a 980 px, il corpo è largo 1126 px e la pagina viene rimpicciolita al 35%: il piè di pagina da 10 px diventa 3,5 px, il testo "chi siamo" da 15 px diventa 5,2 px. Ruotando il telefono la pagina si ricarica **in inglese**. Su un portatile 1366x768 il piè di pagina con P.IVA e privacy finisce fuori schermo e non si può scorrere. [Certo]
- Il pulsante **"Scopri" del POR FESR** in italiano apre una mappa stradale con la sola parola **"prova"**; in tedesco risponde "File not found."; solo l'inglese ha la descrizione del progetto (scritta in italiano). [Certo]
- La galleria **"Fasi di lavorazione"** (28 foto vere del reparto) non si vede: il foglio di stile della galleria non è collegato e le foto finiscono sotto lo sfondo. [Certo]
- Prima del consenso il sito imposta i cookie Google Analytics `_ga` (13 mesi), `_gid`, `_gat` con il vecchio tag Universal Analytics `UA-42251414-20`, che Google ha spento nel 2023; la privacy policy del sito dice che non si usano cookie di tracciamento e indica come titolare "Conceria Europa s.a.s.". [Certo]
- Certificazioni ferme: il link "CERTIFICATO QUALITA' pdf" apre un attestato del 2013 intestato alla vecchia s.a.s., il logo apre un certificato ISO 9001:2008 **scaduto il 12/12/2014**, il badge Leather Working Group pubblicato riporta "Expiry date: 13 May 2026". [Certo per quanto pubblicato; stato attuale DA CONFERMARE]
- L'azienda stessa, nella dichiarazione di accessibilità del 01/07/2026 linkata in home, dichiara il sito "Parzialmente conforme" ed elenca 5 criteri non rispettati (testi alternativi, struttura, contrasto, scorrimento in due direzioni, lingua). Il nuovo sito li risolve tutti. [Certo]
- Materiale fotografico vero e abbondante: 10 sfondi di pelle a 2200x918, 28 foto delle fasi di lavorazione (1096x476, con testo stampato sopra), 8 foto del laboratorio (345-369 px), 22 foto prodotto (760x476, con nome stampato) e, nel sottosito, **79 foto senza scritte** (36 a 1400x700, una a 1920x1275, le altre a 800 px), tra cui la facciata della sede con la grande "e" azzurra. Mancano foto grandi di persone, sede e reparti senza testo sopra. [Certo]
- Identità: marchio "e" + "ConceriaEuropa" (grigio nella testata del sito, azzurro nell'insegna luminosa, sulla facciata e nel logo del sottosito). Nessun vettoriale disponibile. [Certo]

## Pagine esistenti

Il sito è una sola pagina con riquadri cliccabili; ogni "pagina" qui sotto è uno stato di `index.php` o un frammento caricato dentro di essa. Nessuna ha un URL proprio visibile al visitatore.

| Pagina | Come si raggiunge | Frammento | Stato |
|---|---|---|---|
| Home | `/`, `/index.php` (inglese), `/index.php?it`, `?en`, `?de` | `index.php` | mosaico di 5 riquadri immagine con testo dentro, menu verticale in PNG, 3 sfondi di pelle a rotazione |
| Conceria Europa (chi siamo) | riquadro "Europa" | `it/contenuti.php?lingua=it&pagina=0` | testo in un riquadro con scorrimento interno, 4 miniature da 145 px |
| Arredamento - Automotive | riquadro "arredamento automotive" | `contenuti.php` pagina 1 (`autom_arred.php`) | 3 riquadri a rotazione: arredamento, automotive, pelli speciali |
| Arredamento | riquadro "arredamento" | `it/arredamento_cat.php` | semianilina, pienofiore, fiore corretto |
| Automotive | riquadro "automotive" | `it/automotive_cat.php` | selleria, volanti, kit tagliati |
| Pelli speciali | riquadro "pelli speciali" | `it/pellispeciali.php` | ignifugo, aviation |
| 8 schede prodotto | dentro le categorie | `it/semianilina.php`, `pienofiore.php`, `smerigliato_stampati.php`, `selleria.php`, `volanti.php`, `kit_tagliati.php`, `ignifugo.php`, `avion.php` | 1-3 foto 760x476 a rotazione + 1-2 righe di testo |
| Metamorfosi della pelle | voce di fisarmonica | `contenuti.php` pagina 2 | 6 foto a rotazione: pelle grezza, rinverdita, wet blue, tinta, crust, rifinita |
| Fasi di lavorazione della pelle | riquadro "fasi di lavorazione pelli" | `contenuti.php` pagina 3 | galleria prettyPhoto di 28 foto: **non visibile** (vedi problemi) |
| Controllo qualità | riquadro "controllo qualità" | `contenuti.php` pagina 4 | 8 foto del laboratorio, 1 frase, link al certificato |
| Contatti | linguetta "contatti" | `it/contatti.php` (finestra modale 1080x640) | indirizzo, 5 email per ufficio, dati societari, mappa disegnata |
| Certificati | linguetta "certificati" | `it/certificati.php` (modale) | 8 loghi (uno ripetuto due volte) |
| POR FESR | bollino "Scopri" nella testata | `it/por.php` (modale) | italiano: "prova"; inglese: descrizione; tedesco: 404 |
| Privacy | linguetta "privacy policy" | `it/cookie.php` (modale) | testo della privacy del 2018 + link al PDF |
| Privacy e Cookie Policy | piè di pagina | iubenda (esterno) | ok |
| Policy Aziendale | pulsante in testata | `pdf/politica_sistema_integrato_rev.05.pdf` | PDF A3 del 10/09/2024 |
| Accessibilità | pulsante in testata | app.allystudio.it (esterno) | dichiarazione del 01/07/2026 |
| zh | link in testata | `http://products.conceriaeuropa.it/` | sottosito WordPress 2014, cinese e inglese, 15 pagine per lingua |

Screenshot di ogni stato a 1440 e 390 (più le versioni rimpicciolite "come sul telefono") in `_prova/attuale/`: `it-1440-NN-*.png`, `it-390-NN-*.png`, `it-390-NN-*-telefono.png`, `en-1440-*.png`, `zh-1440-home.png`, `zh-390-home.png`.

## Testi reali (verbatim, con i refusi originali)

### Chi siamo (it/contenuti.php)
1. "Conceria Europa: da oltre 40 anni al servizio della pelle."
2. "Fondata nel 1969 dai fratelli FAGGIANA l'azienda ha saputo crescere e consolidarsi nel tempo senza però dimenticare quell'attenzione ai dettagli che ha permesso il raggiungimento di elevati standard qualitativi nella produzione di pelli per arredamento e carrozzeria auto."
3. "La conceria Europa è una delle poche realtà del comprensorio che possono vantare ancora un ciclo di lavorazione completo (dalla pelle grezza al prodotto finito), garantendo un controllo sull'intero processo che, unito alla professionalità dei lavoratori ed ai moderni macchinari, permette di soddisfare qualsiasi esigenza del Cliente."
4. "La Conceria Europa è dotata dal 1999 di un Sistema di Gestione per la Qualità certificato UNI EN ISO 9001"

Inglese (stessa sezione): "Europa Tannery has over 40 years experience in leather production. In 1969 the Faggiani brothers founded the tannery [...]" / "Conceria Europa works exclusively from raw material to the finished product. This means that all of their upholstery and automotive leathers undergo the complete production cycle in house." / "Since 1999 Europa follows all guidelines of the ISO9001 UNI EN Quality Control System for their production. In 2002, their ISO 9001 Quality System certificate was renewed ."
Tedesco: "Die Lederfabrick Europa ist eine der wenigen Gerbereien im Raum Arzignano,die noch einen vollstaendigen Produktionszyklus betreiben.( von der Rohware bis zum Fertigleder )".

### Schede prodotto (it/*.php)
5. SEMIANILINA: "Pelle con una rifinizione leggera che lascia il fiore molto naturale e nello stesso tempo garantisce un buon comportamento all'uso." (con spazi multipli nell'originale)
6. PIENOFIORE: "Pelle pieno fiore, con grana naturale, caratterizzata da una mano particolarmente morbida. La rifinizione non influisce sull'aspetto naturale della pelle ma agisce come protezione d'uso e ne garantisce una buona resistenza all'usura e nel tempo."
7. SMERIGLIATO STAMPATI (nel riquadro immagine si chiama "fiore corretto"): "La correzione del fiore attenua alcuni difetti naturali della pelle e una rifinizione adeguata ne esalta il colore, l'aspetto, la mano e le proprietà d'uso."
8. SELLERIA: "Pelle destinata al rivestimento di pannelli e sedili auto. Ottime resistenze all'usura e solidità alla luce, sviluppata per soddisfare lo specifico capitolato del Cliente."
9. VOLANTI: "Pelle destinata al rivestimento di volanti. Ottime resistenze all'usura e solidità alla luce sviluppata per soddisfare lo specifico capitolato del Cliente."
10. KIT TAGLIATI: "Kit per il rivestimento di volanti tagliati su disegno del Cliente, pronti per la sellatura."
11. IGNIFUGO e AVIATION (stesso testo nelle due schede): "Pelli con trattamento di ignifugazione su capitolato del Cliente, destinate all'arredamento, interni auto e aerei. (esempio di capitolato: F.A.R. B, F.A.R. A, Classe 1IM e Crib5)"

### Controllo qualità
12. "La Conceria Europa possiede un laboratorio interno per l'esecuzione di prove fisiche sulla pelle, sia durante le fasi produttive che sul prodotto finito pronto per la consegna." Link: "CERTIFICATO QUALITA' pdf".

### Fasi di lavorazione (testo stampato dentro le 28 foto, trascritto)
13. magazzino grezzo (2 foto, solo titolo)
14. dissalatura: "Tramite sbattitura è rimosso il sale usato per la conservazione delle pelli."
15. rinverdimento calcinaio: "Le pelli sono reidratate e depilate, pronte per la successiva fase."
16. scarnatura: "Fase meccaniche che permette la rimozione dei residui rimasti dal lato carne. Segue la rifilatura manuale."
17. spaccatura: "Fase meccanica che permette di separate la parte superiore della pelle (lato fiore) da quello inferiore (crosta)"
18. concia, DECALCINAZIONE MACERAZIONE: "Neutralizzazione ed eliminazione dei prodotti alcalini di calcinaio seguito da un trattamento enzimatico per la pulizia della membrana del fiore." PICKEL: "Il pickel completa la de-calcinazione della pelle e la prepara con una adeguata acidificazione per la concia al cromo." CONCIA: "La concia trasforma il materiale organico ( collageno ) del quale è costituito la pelle in cuio. Con la concia riceve termo stabilità,resistenza contro attacco batterico e reatività chimica per tintura ed ingrasso a sec. dell'articolo da produrre."
19. pressatura: "Fase meccanica che consente di rimuovere gran parte dell'acqua contenuta nella pelle"
20. tintura: "Fase cruciale che conferisce alla pelle le caratteristiche del prodotto finito."
21. miscela: "Attraverso apposite cabine di spruzzatura si conferisce l'aspetto finale alla pelle" (copiato dalla rifinizione)
22. rifinizione: "Attraverso apposite cabine di spruzzatura si conferisce l'aspetto finale alla pelle"
23. bottalatura: "Le pelli inserite in bottali a temperatura ed umidità controllate acquisiscono morbidezza"
24. stampatura: "Tramite un cilindro a caldo viene impressa una grana alla pelle."
25. controllo qualità: "Le pelli sono sottoposte a test fisici secondo norme internazionali e/o capitolati dei clienti"

### Altri testi dentro immagini (trascritti)
- Menu laterale (PNG verticali 20x96, 20x130, 17x150): "home", "contatti", "privacy policy", "certificati", "www.netevolution.it".
- Riquadri home (JPG): "arredamento automotive", "controllo qualità", "fasi di lavorazione pelli"; in inglese "upholstery leather", "quality control", "phases of leather production".
- Categorie: "arredamento", "automotive", "pelli speciali", "semianilina", "pienofiore", "fiore corretto", "selleria", "volanti", "kit tagliati", "ignifugo", "aviation"; ogni foto ha anche il logo "e ConceriaEuropa" stampato.
- Metamorfosi: "pelle grezza", "pelle rinverdita", "wet blue", "pelle tinta", "crust", "pelle rifinita".
- Testata: "ConceriaEuropa", bollino "SCOPRI / POR 2014-2020 FESR / REGIONE DEL VENETO".

### Contatti (it/contatti.php)
26. "Montebello Vic. 36054 Vicenza Italy / Via Lungochiampo 129 / tel: +39 0444 44 01 53 (2 linee r.a) / fax: +39 0444 64 88 79 / Accoglienza: info@conceriaeuropa.it / Ufficio Amministrativo: amministrazione@conceriaeuropa.it / Ufficio Commerciale: faggiana.luigi@conceriaeuropa.it / Ufficio Ambiente: qualitaambiente@conceriaeuropa.it / Tesoreria e Finanza: rezzante.paolo@conceriaeuropa.it / C.f. e P.iva IT 00166680249 / Numero REA: VI - 0107752 / Capitale sociale 500.000 euro / GOOGLE MAP"
27. Piè di pagina: "CONCERIA EUROPA SRL - Montebello Vic. (VI) - Via Lungochiampo 129 - tel. +39 0444 44 01 53 - info@conceriaeuropa.it - P.iva IT 00166680249 - VI - 0107752 - Privacy Policy Cookie Policy"

### POR FESR
28. Italiano (`it/por.php`), testo completo sopra una mappa stradale: "prova"
29. Inglese (`en/por.php`), in italiano: "Innovazione tecnologica e ammodernamento aziendale / Descrizione progetto e finalità: Innovazione nella fase di scarnatura delle pelli. / Sostegno Finanziario deliberato: € 149.190,00 / Intervento realizzato avvalendosi del finanziamento POR / Obiettivo "Investimenti in favore della crescita e dell'occupazione" parte FESR Fondo Europeo di Sviluppo Regionale 2014-2020 / Asse 3 Competitività dei sistemi produttivi / Azione 3.1.1 sub A Bando per l'erogazione di contributi alle imprese del settore manifatturiero e dell'artigianato di servizi - Sportello B." Banner: "Un moltiplicatore di opportunità. Da non lasciarsi sfuggire."

### Politica integrata (PDF Rev. 05, 10/09/2024), frasi utili
30. "La CONCERIA EUROPA SRL riconosce, nella soddisfazione di tutti i requisiti dei suoi clienti a livello di qualità, utilità, affidabilità e tempestività nella fornitura dei propri prodotti, nella gestione dell'ambiente, della sicurezza e salute sul luogo di lavoro (SSL) e della responsabilità sociale una delle più importanti priorità aziendali [...]"
31. "Rispettare la legislazione globale, tutti i requisiti imposti dal REACH ai materiali acquistati per essere trasformati dalla conceria, eliminando le sostanze pericolose elencate nello ZDHC MRSL dall'uso e dallo scarico dalla nostra struttura;"
32. "Ad utilizzare sostanze chimiche più sicure e sostenibili nei nostri processi di produzione per garantire la protezione dei dipendenti, delle comunità, dell'ambiente e della salute dei consumatori"

### Privacy (it/cookie.php, PDF 29/10/2018)
33. "Il "titolare" del loro trattamento è Conceria Europa s.a.s. - 36054 Montebello Vicentino - Via Lungochiampo, 129 - P.Iva 00166680249 [...] Tel 0444 440153"
34. "[...] né vengono utilizzati c.d. cookies di profilazione e/o per il tracciamento degli utenti." (sezione COOKIES)
35. Responsabile del trattamento: "Net Evolution s.r.l. - fornitore dei servizi di sviluppo e manutenzione della piattaforma web".

### Testo nascosto (11 H1 con `display:none`, uguali in tutte le lingue)
"aviation leather tannery", "flameproof leather tannery", "automotive leather tannery", "contract leather tannery", "hospitality leather tannery", "upholstery leather tannery", "specialty leather tannery", "technical leather tannery", "steering wheel leather tannery", "car seats leather tannery", "wholesale leather supplier".

### Refusi e contraddizioni da non riportare
- "Fase meccaniche", "separate la parte", "da quello inferiore", "in cuio", "reatività", "termo stabilità,resistenza", "a sec. dell'articolo", "Classe 1IM" (è "Classe 1 IM"), "La conceria Europa" minuscolo; in inglese "Faggiani brothers", "naturai look", "controis", "garantees"; in tedesco "Qaulitaetsstandard", "Lederfabrick", "Umwandlund", "erhalteadie".
- "da oltre 40 anni": dal 1969 sono 57. "In 2002, their ISO 9001 Quality System certificate was renewed": fermo al 2002.
- La scheda "miscela" ha il testo della rifinizione; ignifugo e aviation hanno lo stesso testo; "fiore corretto" (immagine) e "SMERIGLIATO STAMPATI" (titolo) sono la stessa scheda.
- Capitale sociale **500.000 euro** su `it/contatti.php`, **78.000 euro** nel piè di pagina del sottosito. [DA CONFERMARE con visura]
- Forma giuridica: "SRL" nel piè di pagina e nella politica 2024; "s.a.s." nella privacy, nei certificati ICEC 2011-2014 e nella scheda Google. Nel nuovo sito: **Conceria Europa S.r.l.**
- I pulsanti "Policy Aziendale" e "Accessibilità" restano in italiano anche nelle pagine inglese e tedesca.

## Cosa fanno e cosa vendono

- **Conceria a ciclo completo**, dalla pelle grezza salata al finito, nello stesso stabilimento di Montebello Vicentino (distretto di Arzignano, valle del Chiampo). Concia al cromo. Campo del certificato ICEC: "Produzione a ciclo completo di pelli per carrozzeria, arredamento ed avio". [Certo]
- Fasi documentate in foto: magazzino grezzo, dissalatura, rinverdimento e calcinaio, scarnatura (nuova linea finanziata dal POR FESR, macchina Costruzioni Meccaniche Persico), spaccatura, decalcinazione e macerazione, pickel, concia, pressatura, tintura, preparazione miscele, rifinizione a spruzzo, bottalatura, stampatura della grana, controllo qualità. [Certo]
- **Arredamento**: semianilina, pieno fiore, fiore corretto smerigliato e stampato. [Certo]
- **Automotive**: pelle per selleria (sedili, pannelli porta, braccioli), pelle per volanti, **kit tagliati** su disegno del cliente pronti per la sellatura (foto del taglio automatico con pressa). [Certo]
- **Pelli speciali**: ignifughe su capitolato (F.A.R. B, F.A.R. A, Classe 1 IM, Crib 5) per arredamento, interni auto e **aerei**. [Certo]
- **Laboratorio interno** per prove fisiche in produzione e sul finito (foto di dinamometro, flessometri, camera climatica, microscopio), certificato ICEC TS 406. [Certo]
- Mercati: sito in italiano, inglese, tedesco e cinese, H1 nascosti in inglese: clienti esteri [Probabile]. Nessun cliente, marchio servito, numero di pelli o capacità produttiva pubblicati. [DA CONFERMARE]
- Nessun prezzo, nessun catalogo PDF, nessun modulo di contatto, nessun orario.

## Immagini usate oggi

Inventario completo con dimensioni, soggetto, qualità, larghezza massima e uso: `_prova/inventario-immagini.json` (176 voci). File con nomi parlanti in `assets/originali/` (36 MB): prefisso `sito-` dal sito principale, `zh-` dal sottosito.

| Gruppo | Quanti | Dimensioni | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Sfondi di pelle drappeggiata (gialla, kaki, testa di moro, antracite, cuoio, turchese, rossa, arancio, tortora, blu) | 10 | 2200x918 | buoni, nitidi; oggi deformati (vedi problemi) | aperture a tutta larghezza fino a 1440 (su retina rendono come 1100), fasce colore |
| Fasi di lavorazione (reparti veri, operai, bottali, macchine) | 28 | 1096x476 | discreti; titolo e descrizione stampati in alto | il materiale più autentico: ritaglio pulito 1096x336 sotto il testo (per la concia solo il terzo sinistro 340x476); chiedere gli originali |
| Metamorfosi della pelle | 6 | 1096x476 | buoni; scritta in basso a destra | sequenza dei sei stati, ritaglio 1096x360 |
| Laboratorio | 8 | 345-369 px | piccoli ma nitidi | griglia a riquadri piccoli, max 360 px |
| Chi siamo (due ritratti di anziani, probabilmente i fondatori; sede; parete interna) | 4 | 145 px | insufficienti | solo riferimento: chiedere gli originali [DA CONFERMARE chi sono] |
| Insegna luminosa "e Europa" | 1 | 293x483 | piccola | dettaglio verticale max 293 px |
| Schede prodotto (pelli, sedili, volanti, taglio kit, divani) | 22 | 760x476 | discrete; nome e logo stampati | sostituite dalle stesse foto pulite del sottosito |
| Sottosito, foto senza scritte | 79 | 36 a 1400x700, 1 a 1920x1275, 40 a 800x512-531, 2 verticali 800x1205 | buone, scatti 2012-2014 | pelli, volanti, sedili, kit tagliati, wet blue, campionario colori, **facciata della sede con la "e" azzurra (1400x700)**; 6 foto di divani e letti finiti: diritti da verificare [DA CONFERMARE] |
| Loghi certificazioni ICEC e LWG | 7 | 479-1487 px | buoni | fascia certificazioni |
| Logo | 2 | JPG 680x156 (grigio, con bollino POR), PNG 514x169 (azzurro) | non vettoriali | serve il vettoriale [DA CONFERMARE] |
| Progetto POR (collage scarnatrice Persico, banner FESR) | 2 | 580x478, 1085x106 | collage piccolo | pagina del progetto finanziato |

Ricerca fuori dal sito (Google, LinkedIn, Instagram, Facebook, portali, LWG): nessuna foto pubblicata dall'azienda; dettagli in `assets/esterne/manifest.json`. La scheda Google non è rivendicata e non ha foto del proprietario.

## Problemi tecnici da segnalare al cliente

Ogni punto con la misura e la prova (file in `_prova/attuale/`, script in `_prova/script/`).

1. **Telefono: il sito non si adatta.** Nessun `<meta name="viewport">`. A 390 px: layout 980 px, `document.body.scrollWidth` 1126, la pagina viene ridotta al 35% (390/1126). Piè di pagina 10 px che diventa 3,5 px, testo chi siamo 15 px che diventa 5,2 px. Le finestre di contatti, certificati, POR e privacy (larghe 1080 px) escono dal bordo sinistro e tagliano il testo ("ceria Europa - Privacy policy"). Prove: `it-390-01-home-telefono.png`, `it-390-11-contatti-telefono.png`, `it-390-14-privacy-cookie-telefono.png`, `misure-it-390.json`. [Certo]
2. **Ruotando il telefono la pagina torna in inglese.** Un gestore `resize` ricarica `index.php`, che senza parametro è inglese. Misura: da `index.php?it` (lingua `it`) a `index.php` (lingua `en`) dopo la rotazione 390x844 → 844x390. Lo stesso succede su computer ridimensionando la finestra. Prova: `it-390-ruotato-844.png`, `script/ruota.mjs`. [Certo]
3. **Portatile 1366x768: dati societari irraggiungibili.** Con `screen.width > 1100` lo script mette `overflow:hidden` sul body; con 650 px utili il piè di pagina (P.IVA, telefono, privacy) sta tra y 642 e 668 e la pagina non scorre (`scrollHeight` 650). Prova: `it-1366x650-portatile-home.png`. [Certo]
4. **POR FESR.** Italiano: la finestra mostra solo "prova" sopra una mappa (`it-1440-13-por-fesr.png`); tedesco: `de/por.php` risponde 404 "File not found."; inglese: descrizione del progetto (`en-1440-13-por-fesr.png`). Il progetto "Innovazione nella fase di scarnatura pelli" è nell'elenco pubblico OpenCoesione (114.000 euro di finanziamento pubblico secondo aziende.it; il sito dice "Sostegno Finanziario deliberato: € 149.190,00"). Le regole di comunicazione dei fondi FESR 2014-2020 chiedono al beneficiario una breve descrizione dell'operazione sul proprio sito [Probabile, da citare con cautela]. [Certo per quanto mostrato]
5. **Galleria "Fasi di lavorazione" invisibile.** Il clic apre prettyPhoto (`#fullResImage` = `1_grezzo.jpg`, 1096 px), ma `css/prettyPhoto.css` (presente sul server, 19,9 KB) non è collegato in `index.php`: i contenitori `.pp_pic_holder` e `.pp_overlay` restano `position:static` sotto `#container` (z-index 5) e `#div-sfondo` (z-index 2). Il visitatore vede solo una foto di sfondo. Prove: `it-1440-09-fasi-lavorazione.png`, `script/fasi.mjs`. [Certo]
6. **Errori in console.** `_gaq is not defined` a ogni clic sulle voci della fisarmonica (il codice chiama `_gaq.push` ma la pagina carica `analytics.js`); "Mixed Content" per `http://platform.twitter.com/widgets.js` e un iframe `http://www.facebook.com/plugins/` richiesti dalla galleria; errore CORS su `idb.iubenda.com`. Prova: `misure-it-1440.json` (campo `cons`). [Certo]
7. **Cookie prima del consenso.** Con il banner iubenda ancora aperto: cookie `_ga` (scadenza 10/11/2027), `_gid`, `_gat` su `.conceriaeuropa.it` e invio a `UA-42251414-20` (Universal Analytics, non elabora più dati dal luglio 2023). `ga('set','anonymizeIp',true)` è chiamato dopo `ga('send','pageview')`, quindi la prima visita non è anonimizzata. Il tag GA4 `G-0HENKRDYQH` invece rispetta il consenso (`gcs=G100`). La privacy del sito (2018) dice che non si usano cookie di tracciamento e nomina "Conceria Europa s.a.s.". Prova: `cookie-prima-del-consenso.json`, `script/cookie.mjs`. [Certo]
8. **Certificazioni pubblicate ferme o scadute.** "CERTIFICATO QUALITA' pdf" = attestato ICEC del 22/10/2013 intestato alla s.a.s.; il logo accanto apre `pdf/certificato-Page0001.jpg`, certificato CERT-058-1999-QMS-ICEC, ISO 9001:2008, **scadenza 12.12.2014**; il badge LWG `CON143.png` (caricato il 21/01/2025) riporta "Expiry date: 13 May 2026"; nella griglia dei certificati il logo tracciabilità compare due volte. Stato attuale delle certificazioni [DA CONFERMARE]. [Certo per quanto pubblicato]
9. **Testi chiusi nelle immagini.** Menu laterale in PNG verticali (20x96 px); i 3 riquadri della home sono JPG con il testo dentro; 22 foto prodotto hanno nome e logo stampati; le 28 foto delle fasi contengono circa 230 parole di spiegazione che Google e i lettori di schermo non leggono. Le 8 immagini della home non hanno `alt` (8 su 8). [Certo]
10. **Immagini deformate o ingrandite.** Gli sfondi 2200x918 (rapporto 2,40) sono stirati al 100% della finestra: a 1440x900 vengono schiacciati in orizzontale del 33% (rapporto 1,60); sul telefono sono mostrati 980x2120, cioè stirati in verticale 5,2 volte e ingranditi 2,3 volte in altezza. `controllo_qualita/c_2.jpg` 369x226 mostrata 351x247 (deformata del 13%); `pelli_speciali/avion_1.jpg` 532x426 ingrandita al 112% (595x476); i riquadri categoria 481 px mostrati a 500 (104%). Le miniature chi siamo sono a 145 px. Su schermi retina tutte le foto prodotto (760 px mostrate a 725) hanno metà della definizione necessaria. Prova: `misure-it-1440.json`, `misure-it-390.json`. [Certo]
11. **Contrasto e accessibilità.** Testo bianco sul riquadro grigio di chi siamo: contrasto 2,1-2,7:1 (minimo WCAG AA 4,5:1), misurato sui pixel di `it-1440-02-chi-siamo.png`. La dichiarazione di accessibilità del 01/07/2026 (A11y Studio, linkata in testata) indica "Parzialmente conforme" e i criteri 1.1.1, 1.3.1, 1.4.3, 1.4.10, 3.1.1 non rispettati, motivando con "onere sproporzionato". [Certo]
12. **Ricerca su Google.** Titolo "Conceria Europa" uguale in tutte le lingue e in tutti gli stati; nessuna meta description; nessun attributo `lang`; 11 H1 nascosti con `display:none` pieni di parole chiave (Google lo tratta come testo nascosto); un solo indirizzo per tutto il sito: schede prodotto e contatti non hanno URL propri; i frammenti `/it/*.php` aperti direttamente escono senza stile e con 3 immagini rotte (percorsi relativi) (`it-1440-frammento-semianilina-aperto-da-solo.png`); `robots.txt` e `sitemap.xml` assenti (404); `https://conceriaeuropa.it/` risponde 200 senza reindirizzare al www. [Certo]
13. **Tecnologia.** HTML 4.01 Transitional, impaginazione con 2 tabelle e posizioni assolute in pixel, jQuery 1.8.3 (2012) non minificato da 260 KB, jQuery UI 1.8.16 (2011), meta `charset=ISO-8859-1` mentre il server dichiara UTF-8, `X-Powered-By: PHP/7.4.33` (versione senza aggiornamenti di sicurezza dal 28/11/2022). HTTPS corretto: certificato Let's Encrypt valido fino al 22/11/2026, `http` → `https` con 301. [Certo]
14. **Peso e tempi (home italiana).** 38 richieste, 2,2-2,4 MB, di cui 1,6 MB di script (gtag 524 KB, iubenda 441 KB, jQuery 260 KB, jQuery UI 206 KB). Evento load a 1440: 6,9 / 10,1 / 13,4 s (mediana 10,1 s), DOMContentLoaded 3,3-5,5 s; a 390: 3,9 / 7,9 / 8,8 s (mediana 7,9 s). Prova: `peso-it-1440.json`, `peso-it-390.json`. [Certo, tempi indicativi per il proxy]
15. **Link rotti.** Internamente solo `de/por.php` (404). Tutti i link esterni rispondono 200 (Net Evolution, iubenda, A11y Studio, Google Maps, PDF). Il link "zh" porta a un sito solo `http`. Nessun anno di copyright nel piè di pagina. [Certo]
16. **Sottosito `products.conceriaeuropa.it`.** WordPress 3.9.40 (2014), PHP 5.6.40 (fine supporto 31/12/2018), WPML 3.1.5, Visual Composer, Revolution Slider 4.1.4 (le versioni precedenti alla 4.2 hanno una vulnerabilità nota e molto sfruttata di download di file: non verificata, da segnalare al fornitore), tema ht-increate; risponde solo in `http`, in `https` presenta il certificato predefinito di Plesk autofirmato e **scaduto l'11/12/2025**; la pagina `/author/admin/` rende pubblico il nome utente "admin"; capitale sociale 78.000 euro; tag `UA-42251414-30`. È responsive (viewport presente). Prove: `zh-1440-home.png`, `zh-390-home.png`, `crawl/zh/`. [Certo]
17. **Presenza esterna.** Scheda Google "Conceria Europa Sas Di Faggiana Agostino e Renato e C." con il pulsante "Rivendica questa attività" (non gestita), nessuna foto del proprietario; LinkedIn con 3 follower e nessuna descrizione. [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | CONCERIA EUROPA S.R.L. (in passato Conceria Europa S.a.s. di Faggiana Agostino e Renato & C.; data della trasformazione [DA CONFERMARE]) | piè di pagina del sito, politica 2024; aziende.it, companyreports.it; certificato ICEC 2011-2014 |
| P.IVA e C.F. | 00166680249 | sito (piè di pagina, contatti); aziende.it |
| REA | VI-107752 (sul sito "VI - 0107752") | sito; companyreports.it |
| Sede | Via Lungochiampo 129, 36054 Montebello Vicentino (VI) | sito; Google ("Via Lungo Chiampo, 129"), coordinate 45.4728581, 11.3833278 |
| Telefono | +39 0444 44 01 53 (2 linee r.a.); PagineBianche indica anche 0444 440385 [DA CONFERMARE] | it/contatti.php; paginebianche.it |
| Fax | +39 0444 64 88 79 | it/contatti.php |
| Email | info@ (accoglienza), amministrazione@, faggiana.luigi@ (commerciale), qualitaambiente@ (ambiente), rezzante.paolo@ (tesoreria e finanza), tutte @conceriaeuropa.it | it/contatti.php |
| PEC | **non trovata**: non è sul sito né su aziende.it, PagineBianche, companyreports.it; INI-PEC rifiuta le richieste automatiche ("Request Rejected"). [DA CONFERMARE su inipec.gov.it con la P.IVA] | |
| Capitale sociale | 500.000 euro (sito principale) / 78.000 euro (sottosito) [DA CONFERMARE con visura] | it/contatti.php; products.conceriaeuropa.it |
| Costituzione | iscritta il 25/07/1969; "Fondata nel 1969 dai fratelli FAGGIANA" | aziende.it; sito |
| Attività | ATECO 15.11, preparazione e concia del cuoio | aziende.it |
| Fatturato 2024 | 15.592.742 euro, utile 454.382 euro, costo del personale 2.482.291 euro | aziende.it, companyreports.it |
| Dipendenti | 20-49 | aziende.it |
| Orari | non pubblicati [DA CONFERMARE] | |
| Persone citate | Luigi Faggiana (commerciale), Paolo Rezzante (tesoreria), "Faggiana F." (referente accessibilità), Simone Faggiana (dipendente su LinkedIn) | sito; dichiarazione di accessibilità; LinkedIn |
| Certificazioni dichiarate (loghi nella scheda Certificati, gennaio 2025) | ICEC ISO 9001:2015, ICEC ISO 14001:2015, ICEC ISO 45001, ICEC Traceability, ICEC TS 406 laboratorio certificato, ICEC Sustainability Certification, Leather Working Group "Leather Manufacturer SILVER" CON143 (badge con scadenza 13/05/2026). Numeri e scadenze attuali [DA CONFERMARE] | it/certificati.php |
| Qualità dal 1999 | certificato CERT-058-1999-QMS-ICEC, primo rilascio 28.12.1999 | pdf/certificato-Page0001.jpg |
| Sistema integrato | Politica integrata Qualità Ambiente Sicurezza e Responsabilità sociale, Rev. 05 del 10/09/2024; cita REACH e ZDHC MRSL | pdf/politica_sistema_integrato_rev.05.pdf |
| Progetto finanziato | POR FESR Veneto 2014-2020, Asse 3, Azione 3.1.1 sub A, Sportello B: "Innovazione nella fase di scarnatura delle pelli"; sostegno deliberato 149.190,00 euro (sito); 114.000 euro di finanziamento pubblico (OpenCoesione via aziende.it) | en/por.php; aziende.it |
| Fornitori | sito: Net Evolution s.r.l.; privacy: Larese & Associati S.r.l.; cookie: iubenda; accessibilità: A11y Studio | sito |
| Lingue del sito | italiano, inglese, tedesco, cinese (sottosito) | sito |

## URL vecchi

Elenco completo (116 URL) in `_prova/url-vecchi.txt`, da usare per `plugin/redirect-301.csv`. Riassunto:

Sito principale (`https://www.conceriaeuropa.it`, anche senza www):
- `/`, `/index.php`, `/index.php?it`, `/index.php?en`, `/index.php?de`
- per ognuna delle tre cartelle lingua `/it/`, `/en/`, `/de/`: `contenuti.php?lingua=XX&pagina=0` ... `pagina=4`, `autom_arred.php`, `arredamento_cat.php`, `automotive_cat.php`, `pellispeciali.php`, `semianilina.php`, `pienofiore.php`, `smerigliato_stampati.php`, `selleria.php`, `volanti.php`, `kit_tagliati.php`, `ignifugo.php`, `avion.php`, `contatti.php`, `certificati.php`, `por.php` (non esiste in `/de/`), `cookie.php`
- documenti: `/pdf/politica_sistema_integrato_rev.05.pdf`, `/pdf/certificato_icec.pdf`, `/pdf/certificato-Page0001.jpg`, `/pdf/conceria-europa-privacy-policy-sito.pdf`

Sottosito (`http://www.products.conceriaeuropa.it`, anche senza www), pagine inglesi con `?lang=en`:
- `/`, `/europa-tannery/`, `/upholstery-leather/`, `/semianiline-leather/`, `/fullgrain-leather/`, `/corrected-grain-and-embossed-leather/`, `/automotive-car-upholstery-leather/`, `/car-leather-upholstery/`, `/steering-wheel-leather/`, `/cut-leather-kit/`, `/special-leather/`, `/avion-leather/`, `/fireproof/`, `/contact-conceria-europa/`, `/privacy-policy/`
- cinesi (anche con `?lang=zh-hans`): `/conceria-europa-欧洲皮革公司/`, `/家具/`, `/半苯胺/`, `/全粒面/`, `/磨砂印花/`, `/汽车/`, `/volanti-2/`, `/selleria-2/`, `/切片套装/`, `/特殊皮革-2/`, `/avion-2/`, `/防火皮/`, `/联系方式/`, `/portfolio/volanti-3/`, `/author/admin/`, `/?attachment_id=189`

## Cosa manca e cosa chiedere

- PEC (INI-PEC), capitale sociale corretto, data di passaggio a S.r.l., orari di ufficio e spedizioni.
- Stato attuale delle certificazioni (numeri e scadenze ICEC, rinnovo LWG dopo il 13/05/2026).
- Logo vettoriale e colore ufficiale (grigio della testata o azzurro dell'insegna e della facciata).
- Originali delle 28 foto delle fasi di lavorazione senza testo, delle foto del laboratorio e delle 4 foto chi siamo (chi sono le due persone ritratte).
- Diritti sulle 6 foto di divani e letti finiti (probabilmente di clienti).
- Clienti, settori e paesi serviti che si possono citare; dati produttivi (pelli al giorno, superficie dello stabilimento) se pubblicabili.
- Wayback Machine: esiste uno snapshot del 20/01/2012, ma `web.archive.org` non è raggiungibile da questo ambiente (connessione chiusa in https, http bloccato dalla policy): da riprovare da un altro computer per cercare foto più grandi.

## Fonti e file di lavoro

- Crawl del sito: `_prova/crawl/site/` (419 file, 3 lingue), elenco con esito in `_prova/crawl/crawl-urls.json`; sottosito in `_prova/crawl/zh/` (`zh-urls.json`, `uploads/` con 93 originali WordPress).
- Registri e portali: `_prova/crawl/fonti/` (aziende.it, PagineBianche, LinkedIn, dichiarazione di accessibilità, payload della ricerca Google Maps).
- Screenshot e misure: `_prova/attuale/` (`misure-*.json`, `peso-*.json`, `cookie-prima-del-consenso.json`).
- Script: `_prova/script/` (`crawl.py`, `crawl_zh.py`, `misura.mjs`, `foglie.mjs`, `fasi.mjs`, `ruota.mjs`, `portatile.mjs`, `cookie.mjs`, `peso.mjs`, `zhshot.mjs`, `originali.py`).
- Fonti pubbliche: https://www.aziende.it/conceria-europa-s-a-s-di-faggiana-agostino-e-renato-c ; https://www.companyreports.it/conceria-europa-sas-di-faggiana-agostino-e-renato-c-00166680249 ; https://www.paginebianche.it/scheda/montebello-vicentino/conceria-europa-faggiana-ziggiotti.3403299 ; https://it.linkedin.com/company/conceria-europa ; https://app.allystudio.it/accessibility-report/450324f9-b8c5-41ea-a5e8-33666bbfad6f
