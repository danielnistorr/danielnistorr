# 01. Analisi del sito attuale (www.rosygarbo.it)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[DA CONFERMARE]** da verificare con il cliente.
Misure prese con Playwright (Chromium) a 1440 e a 390 px; tempi presi attraverso un proxy, quindi solo indicativi.

## In breve

- Il sito online è una **copia statica fatta con HTTrack il 28 ottobre 2020** del vecchio sito PHP firmato "Web by Dynamica": ogni pagina porta il commento `Mirrored from www.rosygarbo.it/... by HTTrack Website Copier/3.x`, gli indirizzi sono diventati `it_rosygarbo_atelier_linea_moda_sposa_abiti3309.html?azione=show&url=padova`. Ultima modifica sul server: 7 marzo 2021 (aggiunta la voce "vini"). [Certo]
- **Non è fatto per il telefono**: nessun meta viewport, a 390 px la pagina è larga 990 px e il menu si legge a circa 5,5 px, il footer a 4,3 px. A 1440 regge ancora: foto di sfondo elegante e menu leggibile. [Certo]
- Gli **indirizzi vecchi .php sono tutti in errore 404** (anche `linea alta moda` e `linea arte`, voci che oggi sono commentate nel codice e non si vedono nel menu) e `index.php`, la vecchia home, mostra la pagina di Aruba **"sito in costruzione"**. Nella versione inglese la voce "contacts" della galleria New York porta a un 404. [Certo]
- Il patrimonio è fotografico: **94 tavole di catalogo 1125x800** in 6 collezioni (New York, Villa Contarini, White Milano, Venezia, Mexico Lutecia, Padova), che contengono **circa 130 foto di abiti**, quasi tutte verticali da **~562x800**: sono nitide fino a ~560 px di larghezza, non oltre. Solo 6 foto sono orizzontali a 1125 px. Più una foto di sfondo 1286x1041 e un **catalogo vini PDF** del 2021 da cui si ricava il **logo nero in vettoriale**. [Certo]
- Testi pochi ma veri e utilizzabili: la pagina "il brand" (produzione in Veneto, ricami a mano, Camera Nazionale della Moda, sfilate a Roma, Si Sposa Italia) e l'elenco degli atelier nel mondo, fermo al 2020 e in parte superato. [Certo]
- Mancano: P.IVA, privacy, cookie, H1, descrizioni, testi alternativi delle immagini. La mappa nei contatti non compare (iframe http bloccato). [Certo]

## Pagine esistenti

| Pagina | URL attuale (copia HTTrack) | URL originale (PHP, oggi 404) | Stato |
|---|---|---|---|
| Home IT | `/` e `/index.html`, doppione `/index-2.html` | `/index.php` (oggi pagina Aruba "sito in costruzione") | logo grande con payoff "sognamo le vostre idee", una frase in corsivo, foto di sfondo |
| Il brand ROSY GARBO | `/it_rosygarbo_atelier_alta_moda_abiti_sposa.html` | `/it_rosygarbo_atelier_alta_moda_abiti_sposa.php` | unico testo vero del sito (8 frasi) |
| Linea moda sposa | `/it_rosygarbo_atelier_linea_moda_sposa.html` | `.php` | 6 banner-immagine, uno per collezione, nessun testo HTML |
| 6 gallerie | `/it_rosygarbo_atelier_linea_moda_sposa_abiti{e884,37fe,b9f9,fa8d,ecc0,3309}.html?azione=show&url={new-york,villa-contarini,milano,venezia,messico,padova}` | `/it_rosygarbo_atelier_linea_moda_sposa_abiti.php?azione=show&url=...` | Fotorama (jQuery 1.10.2), 11-24 tavole ciascuna, pulsante "Torna alle nostre linee >>" (fa `history.go(-1)`) |
| I nostri Atelier | `/it_rosygarbo_atelier_nel_mondo.html` | `.php` | elenco di 12 punti vendita (3 in Italia, 9 all'estero) in 3 colonne |
| Contatti | `/it_rosygarbo_contatti.html` | `.php` | sede operativa di Cona, direttore artistico, riquadro della mappa vuoto |
| Vini | `/files/Rosy Garbo Wines.pdf` | | PDF di 30 pagine, 4,8 MB, aperto in una nuova scheda |
| Linea alta moda, Linea arte | voci commentate nel menu | `/it_rosygarbo_atelier_linea_alta_moda.php`, `/it_rosygarbo_atelier_linea_arte.php` | 404 "Not Found" (screenshot `_prova/attuale/10-linea-alta-moda-404-1440.png`) |
| Versione inglese | `/en_index.html` (+ `en_index-2.html`) e `en_` + stesso nome per ogni pagina | | stessi contenuti tradotti; titolo della pagina rimasto in italiano |

## Testi reali (verbatim, con i refusi originali)

Testo completo estratto pagina per pagina in `_prova/testi-verbatim.txt`.

Home (testo in corsivo Dancing Script, 30 px):
1. "L'azienda rosyGarbo opera nel settore dell'alta moda da oltre trent'anni, con creazioni di pregiata sartoria da sposa e cerimonia rigorosamente "Made in Italy"."
2. Payoff dentro il logo (immagine): "sognamo le vostre idee". Inglese: "we dream of yours ideas".

Il brand ROSY GARBO:
3. "L'azienda rosyGarbo opera nel settore dell'alta moda da oltre trent'anni, con creazioni di pregiata sartoria da sposa e cerimonia, rigorosamente "Made in Italy"."
4. "La produzione viene completamente eseguita nella sede veneta, con l'utilizzo di tessuti provenienti dalle più rinomate industrie tessili italiane e con l'impegno di tecniche artigianali che consentono di curare con massima attenzione rifiniture e particolari."
5. "Ogni capo viene prodotto dal filo ed in tutte le sue successive fasi di lavorazione esclusivamente in Italia da manodopera altamente qualificata."
6. "I ricami e le applicazioni sono realizzate a mano e rendono ogni capo esclusivo."
7. "Lo stile rosyGarbo si contraddistingue per la continua ricerca del contrasto di tessuti, colori e per gli accostamenti innovativi che permettono di creare giochi di luce e seducenti trasparenze."
8. "Le linee sono sempre raffinate ed eleganti, spesso ispirate alle bellezze artistiche dei palazzi veneti ed alla cultura e tradizione veneziana, con qualche richiamo anche all'antica arte vetraria di Murano."
9. "Iscritta alla Camera Nazionale della Moda Italiana, la griffe partecipa a molteplici manifestazioni di carattere nazionale, e ha sfilato alle consuete edizioni dell'alta moda romana e alla prestigiosa manifestazione internazionale "Donna sotto le stelle" di Piazza di Spagna. Ogni anno le collezioni rosyGarbo vengono presentate alla rassegna internazionale "Si Sposa Italia" di Milano."
10. "La rete di vendita commerciale è dislocata su territorio nazionale ed internazionale con ateliers mono marca e altri punti vendita."

Linea moda sposa (solo testo dentro le immagini, trascritto): "NEW YORK", "villa CONTARINI", "white MILANO", "venice VENEZIA", "mexico LUTECIA", "padua PADOVA". Nelle gallerie: "Torna alle nostre linee >>".

I nostri Atelier (in ordine di pagina):
11. "Atelier Padova / Passaggio San Fermo, 6 / 35137 Padova / Tel. e Fax 049.656883 / E-mail: info@rosygarbo.it"
12. "Showroom Venezia / Via Stazione, 71 - Cona 30010 / Tel. 0426 59418 / Fax 0426 309473"
13. "Atelier Bologna / Via Barberia, 6 - 40123 / Tel/Fax 051 331844"
14. "U.S.A. New York / 85 John Street - ATP 9F / 10038 Manhattan USA"
15. "U.S.A. New York - Kleinfeld / 110 West 20th Street / New York N.Y. 10011 / Tel. +1 212 352 2180 / Fax +1 212 229 0396 / E-mail: rosygarbousa@rosygarbo.it"
16. "Greece Athens - Teokath / Spefsippou 11, Kolonaki / 106 75 Athens / Tel. +30 2107242530"
17. "Greece Thessaloniki - Teokath / Mitropoleos 89 / 546 22 Thessaloniki / Tel. +30 2310276274"
18. "Germany Berlin - Brautmoden Petsch / Kleistrasse 42, 10787 Berlin / am Nollendorfplatz / Tel. +49 030 216 3938 / Fax +49 030 219 96123"
19. "Hungary Budapest - Atelier / 1066, Teréz krt. 22 III em. 15 / Tel. +36 1269 1123"
20. "Mexico City - Atelier / Masaryk 393 esquina Lafontain / local 18, Polanco / Tel. +52 (55) 5281 1835 / Fax +52 (55) 5281 1066 / E-mail: rosy_garbo@yahoo.com.mx"
21. "Russia Moscow / Moscow Bol. Yakimanka 22 / Himeney shopping center 2° floor / Etra evening & wedding / Tel. +7 495 645 0404"
22. "UAE Dubai / 48 Burj Gate / Downtown Dubai (UAE) / Tel. +971 4 321 62 60 / Cel. +39 335 7692695"

Contatti:
23. "Sede Opeativa / Via Stazione, 71 / 30010 Cona (Venezia) / Tel. +39.335.7692695 / Fax +39.042.6309473 / info@rosygarbo.it"
24. "Direttore Artistico / Mauro Belcaro / mauro.belcaro@rosygarbo.it"

Footer di tutte le pagine: "rosyGarbo - Passaggio San Fermo, 6 - 35137 Padova / Tel/Fax +39 335 7692695 - info@rosygarbo.it / Web by Dynamica".
Titolo di tutte le 24 pagine, italiane e inglesi: "rosyGarbo - Abiti da sposa pregiati - Abiti da cerimonia - Abiti alta moda - Abiti da sposa - Matrimonio - Vestito da sposa - Abito sposa - Padova - Milano - Venezia - Bologna - New York".

Versione inglese, differenze da notare: home "for over thirty years", pagina brand "for over forty years"; "strictly ceremonies "Made in Italy""; payoff "we dream of yours ideas".

Catalogo vini PDF (InDesign, 26 febbraio 2021; il testo è vettorializzato, trascritto dalle pagine renderizzate):
25. Pagina 2: "Dalla passione per lo stile, per l'eleganza e l'unicità, nata 40 anni fa con la fondazione della nostra casa di alta moda, Rosy Garbo Haute Couture, nasce l'esclusiva linea Rosy Garbo Wine, la nuova linea di vino frutto dell'amore per il nostro territorio Veneto che affonda le radici nella pluriennale tradizione vitivinicola delle colline di Valdobbiadene e Conegliano, aree riconosciute ed inserite tra i patrimoni dell'umanità tutelati dall'UNESCO."
26. Pagina 2: "Ogni singola bottiglia Rosy Garbo Wine è come un abito sartoriale e ,come esso viene creato su misura ed ideato in esclusiva per la persona che lo indossa, allo stesso modo ogni bottiglia viene studiata, adattata, rielaborata ai gusti del mercato cui è destinata, con possibilità di adornare le medesime con particolari capi, in modo da renderle oltre che oggetti di uso quotidiano,veri e propri articoli da collezione unici ed esclusivi, si viene a creare quindi un connubio perfetto tra moda e vino."
27. Pagina 2: "Le bottiglie sono singolarmente controllate nei minimi dettagli, con amore,attenzione e cura, una ad una, durante tutto il processo di lavorazione sino alle rifiniture ed ai dettagli estetici."
28. Pagina 29: "Le bottiglie abbigliate si propongono come articolo unico da collezionare,rivoluzionando,al contempo,l'attitudine al consumo,instillando nell'acquirente il desiderio di consumare il vino della bottiglia abbinandovi il proprio outfit,una particolare atmosfera,una particolare location." e "Ogni anno,per promuovere il concept,sarà realizzata una collezione di bottiglie abbigliate secondo i trend della stagione che sfileranno in eventi dedicati,portate in passerella da modelle vestite con abiti semplici,monocromatici(in pendant con il colore del vino presentato)in modo tale da concentrare il focus sulla bottiglia,perno portante degli eventi."
29. Pagina 3 (testo del produttore): "I vigneti penetrano le proprie radici in un terreno ben strutturato, argilloso, incastonato nella DOCG Conegliano Valdobbiadene: zona rigidamente regolata da specifico disciplinare a garanzia di un prodotto di altissima qualità per quegli estimatori pronti a diffonderne l'ottima reputazione." Didascalia: "Cantina di Fossalta di Piave (Venezia)", marchio "ARDENGHI".
30. Pagina 28: "ROSY GARBO s.n.c. di Belcaro Mauro & C. / Passaggio San Fermo 6, 35137 Padova - Italy / info@rosygarbo.it - www.rosygarbo.it / Tel. +39 049-656883 - Mauro +39 335 7692695". Sulla mappa: "Punto vendita e degustazione / Concept store and tasting / Via Giambellino, 5 - 35129 (PD) / USCITA PADOVA EST".

Refusi e incoerenze da non riportare: "Sede Opeativa"; "le applicazioni sono realizzate" (realizzati); "ateliers mono marca"; "we dream of yours ideas"; "Fax +39.042.6309473" (è 0426 309473); "Kleistrasse" (Kleiststraße); "Lafontain" (Lafontaine); virgole senza spazio e "e ,come" nel PDF; anni di attività in tre versioni ("oltre trent'anni", "over forty years", "40 anni fa"). Il nome compare come "rosyGarbo", "ROSY GARBO", "Rosy Garbo": nel logo è **rosyGarbo**, nei testi conviene **Rosy Garbo**. Parole dei testi originali che il nuovo sito non riprende (PAROLE_VIETATE): "innovativi" (frase 7), "passione" (frase 25).

## Cosa fanno o vendono

- **Abiti da sposa e da cerimonia di alta moda, prodotti in proprio** "nella sede veneta" (Cona, Via Stazione 71), con tessuti italiani, ricami e applicazioni a mano. [Certo, dal sito]
- **6 collezioni sposa** pubblicate, con nomi di città e luoghi: New York, Villa Contarini, White Milano, Venezia, Mexico Lutecia, Padova. Anno delle collezioni: non indicato [DA CONFERMARE]. Esistevano anche una **linea alta moda** e una **linea arte**, oggi tolte dal menu (contenuto sconosciuto) [DA CONFERMARE].
- **Atelier a Padova** (Passaggio San Fermo 6), **showroom a Cona**, **atelier a Bologna** (Via Barberia 6) e rete di rivenditori all'estero (elenco del 2020). [Certo come dichiarato; validità oggi DA CONFERMARE]
- Dalla scheda Matrimonio.com (testo scritto dal fornitore, data ignota): abiti da sposa "a partire da 500€", disegno e confezione su misura, accessori da sposa (lingerie, scarpe, gioielli, veli, mantiglia e scialle, cappelli, guanti), abiti da cerimonia per madrina, paggetti e damigelle, consulenza d'immagine, abiti da uomo (foto "abito-uomo"). [DA CONFERMARE]
- **Rosy Garbo Wine** (catalogo 2021): 16 vini e 2 grappe prodotti con la cantina Ardenghi di Fossalta di Piave: Conegliano Valdobbiadene Prosecco Superiore DOCG Millesimato Extra Dry e Brut; Prosecco DOC Millesimato Extra Dry e Brut; Ambra Cuvée Millesimato Extra Dry; Agata Cuvée Millesimato Brut; Amistà Cuvée Rosè Extra Dry (l'etichetta in foto dice "Prosecco DOC Rosè Extra Brut"); Venezia DOC Cabernet Sauvignon e Merlot; delle Venezie IGT Chardonnay e Sauvignon; Cuvée Vino Spumante Brut; Veneto IGT Merlot, Cabernet, Pinot Grigio, Chardonnay (marchio "Valdopino"); Grappa La Filata Bianca; Grappa Barricata Prosecco Riserva; confezioni regalo. Se la linea vini è ancora attiva: [DA CONFERMARE].
- Riconoscimenti dichiarati: iscrizione alla Camera Nazionale della Moda Italiana; sfilate all'alta moda romana e a "Donna sotto le stelle" in Piazza di Spagna; presenza annuale a "Si Sposa Italia" (Milano). MAM-e aggiunge: dal 1996 nella Camera Nazionale della Moda, abiti pubblicati su Book Moda Sposa, Vogue Sposa, Vogue Italia, Collezioni Sposa, Collezioni Haute Couture, Sposabella. Nessun documento del cliente lo prova: [DA CONFERMARE] prima di usarli.

## Immagini usate oggi

| Tipo | Quantità | Dimensioni | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Tavole delle gallerie (versione `_3`, la più grande sul server; `_0`, `_2` e senza suffisso danno 404) | 94 (16 New York, 24 Villa Contarini, 13 White Milano, 14 Venezia, 11 Mexico Lutecia, 16 Padova) | 1125x800 | impaginate come doppie pagine: due foto verticali da ~562x800, oppure foto + cartello col logo (38 tavole), oppure foto + foto B/W di architettura. Foto professionali, luce buona, JPEG compresso (qualità circa 55-60). Styling datato ma abiti leggibili | ritagliate per foto singola, mostrate al massimo a ~560 px (280 px su retina). Bene per griglie di collezione e schede; non per aperture a tutta larghezza |
| Foto orizzontali a tavola intera | 6 (Villa Contarini 02, 06, 09, 16; Padova 12; Venezia 01) | 1125x800 | le uniche foto larghe | aperture di sezione fino a 1125 px; a 1440 si ingrandirebbero del 28% |
| Foto di sfondo del sito | 1 | 1286x1041 | sposa con pizzo e tulle, bordi già sfumati a bianco | possibile apertura della home a mezza pagina; la sfumatura è incisa nella foto |
| Banner collezione | 6 | 450x140 | nome della collezione scritto nell'immagine | no (solo per i nomi) |
| Logo grigio con tricolore (PNG) | 3 (con payoff IT, con payoff EN, piccolo) | 443x290, 443x290, 298x89 | grigio chiaro su trasparente, sgranato su retina | no: si usa il logo nero del PDF |
| **Logo nero vettoriale** dal catalogo vini | 1 | renderizzato a 2249x514, trasparente | nitido, serif con barra verde e barra rossa | testata e footer (`assets/originali/logo-rosygarbo-nero-tricolore-da-catalogo-vini.png`) |
| Bottiglie scontornate dal PDF | 7 | ~280-340 x 760-808 | pulite ma piccole | eventuale pagina vini |
| Fonti esterne (`assets/esterne/`) | 3 | 1400x800 (sfilata tra getti d'acqua, MAM-e), 800x1200 (tre modelle in sala affrescata, MAM-e), 3456x4608 (interno atelier, Google Maps, utente) | le prime due sono materiale del marchio pubblicato da terzi; la terza è di un utente | prime due solo con conferma dei diritti; la terza no |

Inventario foto per foto (soggetto, larghezza massima, uso) in `_prova/inventario-immagini.json`; provenienza in `assets/originali/manifest.json` e `assets/esterne/manifest.json`. Le 28 foto della scheda Matrimonio.com (caricate dal fornitore; il nome di un file indica il fotografo Nicola Da Lio) non si scaricano dal nostro accesso (403): elenco degli URL nel manifest. **Mancano**: foto dell'atelier di Padova e dello showroom di Cona, foto di laboratorio (taglio, ricamo, prove), ritratti, foto recenti delle collezioni, il logo in vettoriale come file.

## Problemi tecnici da segnalare al cliente

1. **Non si usa da telefono.** Nessun `<meta name="viewport">` in 24 pagine su 24. A 390 px `document.documentElement.scrollWidth` = 990: il telefono rimpicciolisce la pagina a circa il 39%, il menu (14 px) diventa ~5,5 px, l'elenco atelier (16 px) ~6,3 px, il footer con telefono ed email (11 px) ~4,3 px. Prova: `_prova/attuale/01-home-390-telefono.png`, `06-atelier-390-telefono.png`. [Certo]
2. **Indirizzi vecchi rotti e "sito in costruzione".** Tutti gli URL `.php` del sito originale rispondono 404 (21 indirizzi controllati, italiani e inglesi, gallerie comprese), compresi `it_rosygarbo_atelier_linea_alta_moda.php` e `it_rosygarbo_atelier_linea_arte.php`; `https://www.rosygarbo.it/index.php` mostra la pagina Aruba "www.rosygarbo.it sito in costruzione" (`_prova/attuale/09-index-php-1440.png`). Chi arriva da vecchi link o segnalibri trova un errore. Nella galleria New York inglese la voce di menu "contacts" punta a `ent_rosygarbo_contatti.html`: 404. Le voci "linea alta moda" e "linea arte" non si vedono più nel menu: sono commentate nel codice (la ricerca iniziale le dava come voci visibili in 404: rettificato). [Certo]
3. **Contenuti fermi.** Copia HTTrack del 28/10/2020, ultima modifica 07/03/2021 (header `last-modified`). Elenco dei rivenditori esteri del 2020: il negozio di Berlino (Brautmoden Petsch) risulta oggi in Kaiser-Friedrich-Str. 3, non più in Kleiststraße 42; la presenza degli altri non è verificata. Anni di attività in tre versioni diverse (30, 40, "40 anni fa"). Nessun anno sulle collezioni, nessun copyright. [Certo]
4. **Dati obbligatori e privacy.** Nessuna P.IVA in nessuna pagina (obbligatoria per le società sul sito). Nessuna informativa privacy, nessuna informativa o banner cookie. Il codice carica Google Analytics "UA-45932201-1" (Universal Analytics, che Google ha chiuso il 1 luglio 2023) via `http://`: il browser lo blocca come contenuto misto, quindi oggi non misura nulla. [Certo]
5. **Errori in console su tutte le pagine**: "Mixed Content: ... requested an insecure script 'http://www.google-analytics.com/analytics.js'. This request has been blocked". Nella pagina contatti anche l'iframe della mappa `http://maps.google.it/...` viene bloccato: **il riquadro della mappa resta vuoto** (`_prova/attuale/07-contatti-1440.png`). [Certo]
6. **HTTPS a metà.** Certificato valido (Actalis, `*.rosygarbo.it`, scade il 22/11/2026), `rosygarbo.it` e `rosygarbo.com` rimandano a `https://www.rosygarbo.it`, ma `http://www.rosygarbo.it/` risponde 200 senza passare a https. [Certo]
7. **Tecnologia.** Nessun CMS: HTML statico XHTML 1.0 impaginato con tabelle (3-4 tabelle di layout per pagina), font Josefin Sans e Dancing Script in EOT/WOFF/SVG, jQuery 1.10.2 del 2013 (vulnerabilità note, per esempio CVE-2020-11022) caricato solo nelle gallerie, slider Fotorama. Il cliente non può aggiornare nulla senza uno sviluppatore. [Certo]
8. **Peso e tempi.** Home: 9-10 richieste, 260-320 KB; galleria: 34 richieste, ~610 KB (16 tavole grandi caricate tutte insieme). Il peso è basso; i tempi misurati (evento load 2,4-8 s in home, 6-25 s in galleria) sono gonfiati dal proxy e vanno rimisurati da una linea normale [DA RIMISURARE]. [Certo per peso e richieste]
9. **SEO.** Lo stesso titolo-elenco di parole chiave su tutte le 24 pagine, anche inglesi; nessuna meta description; nessun H1; `lang` assente; 224 immagini, 0 con testo alternativo; `sitemap.xml` e `robots.txt` assenti (404). [Certo]
10. **Testi chiusi in immagini**: i nomi delle 6 collezioni (banner 450x140), il payoff "sognamo le vostre idee", tutto il catalogo vini (testo vettorializzato: `pdftotext` legge solo la pagina dei contatti). [Certo]
11. **Immagini**: le tavole 1125x800 sono mostrate a 930x661 (rimpicciolite, nitide su schermo normale, morbide su retina); il logo 443x290 mostrato a 443 px è sgranato su retina. Nessuna immagine ingrandita oltre la dimensione naturale a 1x. [Certo]
12. **Schede esterne**: su Google Maps la scheda si chiama ancora "Rosy Garbo Di Giannina Garbo & C. (S.A.S.)", categoria "Negozio di abbigliamento", **non rivendicata** ("Rivendica questa attività"), 1 sola foto di un utente; Virgilio e PagineGialle riportano "Rosy Garbo S.n.c. di Giannina Garbo e C."; Prontoimprese ha l'atelier di Bologna come "Rosy Garbo S.N.C. Di Giannina Garbo & C. Atelier". Ragione sociale attuale diversa (vedi sotto). [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | ROSY GARBO SNC DI BELCARO MAURO & C. (nel PDF: "ROSY GARBO s.n.c. di Belcaro Mauro & C.") | VIES 06/10/2026, catalogo vini p. 28 [Certo] |
| P.IVA | 02260670282 (valida su VIES) | VIES [Certo] |
| Sede legale | Largo Europa - Passaggio San Fermo 6, 35137 Padova (PD) | VIES [Certo] |
| Sede operativa e produzione | Via Stazione 71, 30010 Cona (VE) | sito, Matrimonio.com [Certo] |
| Atelier | Padova, Passaggio San Fermo 6; Bologna, Via Barberia 6 (Tel/Fax 051 331844) | sito [Certo]; Bologna attivo oggi [DA CONFERMARE] |
| Telefoni | 049 656883 (atelier Padova, anche su Google); 335 7692695 (cellulare, nel footer come "Tel/Fax"; nel PDF "Mauro"); showroom Cona 0426 59418, fax 0426 309473 | sito, PDF, Google Maps [Certo] |
| Email | info@rosygarbo.it; mauro.belcaro@rosygarbo.it; rosygarbousa@rosygarbo.it; rosy_garbo@yahoo.com.mx (Messico). Dominio con MX attivo su Aruba | sito, DNS [Certo] |
| PEC | non trovata: cercarla su INI-PEC (inipec.gov.it) con la P.IVA 02260670282 (ricerca con captcha, da fare a mano) | [DA CONFERMARE] |
| Orari | Google Maps (scheda non rivendicata) mostra solo martedì 10-12:30 e 15:30-19:30 e "Apre mer alle ore 10"; il sito non indica orari | [DA CONFERMARE] |
| Anni di attività | snc costituita il 3 marzo 1989, ATECO 47.71 (commercio al dettaglio di abbigliamento), 0-9 addetti, attiva (registro aggiornato a luglio 2026, dalla ricerca iniziale e da fatturatoitalia.it, pagina non aperta: 503). Il marchio dichiara "oltre trent'anni" (2020), "40 anni fa" (2021). MAM-e: la stilista Rosy Garbo è nata in Veneto nel 1950, ha lavorato a Parigi negli anni Ottanta | [DA CONFERMARE] l'anno da usare nel sito |
| Persone | Rosy Garbo, stilista (MAM-e: "Nata in Veneto nel 1950"); Mauro Belcaro, "Direttore Artistico" sul sito e socio nella ragione sociale | sito, MAM-e [Certo] |
| Fatturato | non pubblicato (snc) | |
| Marchi | rosyGarbo (sposa e cerimonia), Rosy Garbo Haute Couture, Rosy Garbo Wine | sito, PDF [Certo] |
| Certificazioni | nessuna dichiarata | |
| Social | nessun link nel sito; Facebook e Instagram non verificabili senza login | |

Prima del contatto: c'è rassegna stampa locale (2016-2017) sul socio della ragione sociale che l'utente deve leggere prima di decidere se procedere. Dettagli e fonti sono nel riassunto della fase 2.1 consegnato all'orchestratore, non qui.

## URL vecchi (per `plugin/redirect-301.csv`)

URL della copia oggi online (rispondono 200):
- `/`, `/index.html`, `/index-2.html`
- `/it_rosygarbo_atelier_alta_moda_abiti_sposa.html`
- `/it_rosygarbo_atelier_linea_moda_sposa.html`
- `/it_rosygarbo_atelier_linea_moda_sposa_abitie884.html?azione=show&url=new-york`
- `/it_rosygarbo_atelier_linea_moda_sposa_abiti37fe.html?azione=show&url=villa-contarini`
- `/it_rosygarbo_atelier_linea_moda_sposa_abitib9f9.html?azione=show&url=milano`
- `/it_rosygarbo_atelier_linea_moda_sposa_abitifa8d.html?azione=show&url=venezia`
- `/it_rosygarbo_atelier_linea_moda_sposa_abitiecc0.html?azione=show&url=messico`
- `/it_rosygarbo_atelier_linea_moda_sposa_abiti3309.html?azione=show&url=padova`
- `/it_rosygarbo_atelier_nel_mondo.html`, `/it_rosygarbo_contatti.html`
- `/en_index.html`, `/en_index-2.html`, `/en_rosygarbo_atelier_alta_moda_abiti_sposa.html`, `/en_rosygarbo_atelier_linea_moda_sposa.html`, le 6 gallerie `en_rosygarbo_atelier_linea_moda_sposa_abiti{e884,37fe,b9f9,fa8d,ecc0,3309}.html?azione=show&url=...`, `/en_rosygarbo_atelier_nel_mondo.html`, `/en_rosygarbo_contatti.html`
- `/files/Rosy Garbo Wines.pdf` (da tenere o reindirizzare alla pagina vini)

URL del sito PHP originale (oggi 404 o "sito in costruzione", da reindirizzare comunque perché possono essere ancora nei link esterni):
- `/index.php`
- `/it_rosygarbo_atelier_alta_moda_abiti_sposa.php`, `/it_rosygarbo_atelier_linea_moda_sposa.php`, `/it_rosygarbo_atelier_nel_mondo.php`, `/it_rosygarbo_contatti.php`
- `/it_rosygarbo_atelier_linea_moda_sposa_abiti.php?azione=show&url={new-york,villa-contarini,milano,venezia,messico,padova}`
- `/it_rosygarbo_atelier_linea_alta_moda.php`, `/it_rosygarbo_atelier_linea_arte.php`
- versioni `en_` degli stessi nomi (controllate: 404)
- immagini: `/wfolder/filesgallery/file/*_1.jpg` e `*_3.jpg` (188 file), `/images/collezioni/*.png`

Elenco completo di link e risorse con codice di risposta: `_prova/crawl/link-stato.txt` (227 risposte 200, 1 errore 404).

## Fonti e file di lavoro

- Copia completa del sito: `_prova/crawl/mirror/` (246 file, wget del 06/10/2026); pagine renderizzate del PDF in `_prova/crawl/pdf-vini/`.
- Screenshot a 1440 e 390 (più la versione ridotta come la vede un telefono): `_prova/attuale/`; misure di rete e console: `_prova/attuale/misure.json`.
- Fonti pubbliche salvate in `_prova/crawl/fonti/`: VIES (`vies.json`), MAM-e Enciclopedia della moda (moda.mam-e.it/rosy-garbo/), Google Maps (place_id ChIJF5KnxUTafkcRXTKLT4F2ZQM), Virgilio, Prontoimprese, Matrimonio.com (letta con WebFetch), Il Mattino di Padova 27/04/2011, Flash Style Magazine 22/10/2014.
- Wayback Machine: non raggiungibile da qui il 06/10/2026 (429 e connessioni chiuse ripetute). Da riprovare per le pagine "linea alta moda" e "linea arte", che potrebbero avere altre foto [DA FARE].
