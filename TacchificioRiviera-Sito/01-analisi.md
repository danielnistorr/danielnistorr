# Tacchificio Riviera: analisi per la nuova home

Sito: https://www.tacchificioriviera.it/ (crawl e screenshot del 19/10/2026). È una pagina unica a schermate (IT, e EN in /en). Le fonti sono citate come URL + frase; il testo del sito è in `_prova/crawl/home.html` e `en.html`, i certificati in `_prova/crawl/cert/`.

## 1. In breve

- **Chi**: Tacchificio Riviera S.r.l., sede legale in Via Pola 22 a Stra (VE), sede operativa e amministrativa in Viale Serenissima 30 a Vigonovo (VE), nella Riviera del Brenta. Il marchio è la firma "Valentino Boldrin" in un timbro tondo.
- **Cosa fanno davvero**: progettano e producono tacchi per scarpe di lusso. Lo scopo dei certificati SGS è preciso: "Progettazione e fabbricazione (attraverso le fasi di stampaggio ad iniezione, finissaggio ed imballaggio) di tacchi in plastica per calzature di lusso". Il lavoro parte dal disegno del cliente: "Il cliente presenta un disegno con la sua idea, viene interpretata e realizzata". La galleria mostra prototipi avorio, tacchi in plastica nera, trasparente e sfumata, un tacco in metallo, uno in plexiglas, uno in ottone inciso e due in legno grezzo.
- **Per chi**: i calzaturifici delle griffe: "le più grandi griffe di moda del mondo calzaturiero si affidano al Tacchificio Riviera" (modale Territorio). Nessun cliente è nominato.
- **Da quando**: il marchio dal 1945 ("un padre affiancato dal figlio, realizza il primo tacco in legno. Lui si chiama Giovanni Boldrin"); la società attuale dal 1985 (companyreports.it, "Fondazione 1985"). Tre generazioni: Giovanni, Valentino (le materie plastiche nel 1970), Fabio (dagli anni 80; nuova sede nel 2010).
- **Quanti**: 32 dipendenti e 4,12 milioni di fatturato nel 2024 (aziende.it); 6,26 milioni e un utile di 745.977 euro nel 2025 (companyreports.it). Sul sito c'è solo il dato storico, "un team di oltre 50 dipendenti" negli anni 80.
- **Correzioni alla nota di partenza**: il mestiere e le sezioni sono giusti. Va precisato che il prodotto certificato è il tacco in plastica stampato a iniezione e che la sede legale è a Stra, non a Vigonovo. Il sito dice "Da oltre mezzo secolo", ma dal 1945 sono 81 anni.

## 2. Il sito di oggi

**Pagine**: una sola pagina a otto schermate a tutto schermo: Home, Ispirazioni, Linee, Nascita, Unico, Territorio, Certificazioni, Contatti. Ci sono i modali Ispirazioni (due video YouTube), Nascita (la galleria di 17 tacchi), Territorio (la storia in tre schede) e Contatti, più Privacy e Cookie. La sitemap risponde 404.

**Testi veri essenziali (verbatim, IT)**:
- Home: "Ogni storia è un percorso. Disegniamo il tuo."
- Ispirazioni: "Disegniamo le linee della tua ispirazione. Il cliente presenta un disegno con la sua idea, viene interpretata e realizzata. Le persone vedono un tacco, io ascolto la musica che interpretano, camminandoci." Bottone: "Diamo forma alla tua idea?"
- Linee ("Seguire le linee"): "Realizziamo i sogni del cliente, intagliandoli nella bellezza di un prodotto unico. Da oltre mezzo secolo."
- Nascita: "L'idea si tocca, l'astratto diventa materia. E' nato il tacco." Bottone: "Galleria".
- Unico: "Controlliamo ogni prodotto: osserviamo i dettagli, le caratteristiche della sua composizione. Ogni forma è unica come le persone che lo indosseranno."
- Territorio ("I luoghi hanno un'anima"): "Seguendo le tracce di chi ci ha preceduto, troviamo l'ispirazione per realizzare creazioni artigianali con le tecnologie più avanzate." Bottone: "Dal 1945 ad oggi".
- Modale storia: "E' il 1970: il Tacchificio Riviera diventa una grande realtà artigiana della Riviera del Brenta"; "Il 2010 è l'anno della svolta. ... Fabio Boldrin inaugura una nuova sede con le più avanzate tecnologie in grado di unire l'artigianalità di quel primo tacco in legno, all'uso di macchinari sempre più all'avanguardia."
- Certificazioni: ISO 9001, ISO 45001, ISO 14001, ISO 50001, SA8000 (Politica Sociale, Problematiche, Scheda Informativa, Tutela Minori, Modulo di Segnalazione), tutti in PDF. Ente: SGS.
- Macchine: nessun elenco. I video YouTube "Ispirazioni - Dettagli Video Tacco" e "... Zeppa" (canale @tacchificioriviera928) mostrano una fresa a controllo numerico su un tacco in legno e un centro di lavoro.
- Numeri sul sito: solo 1945, 1970, 2010 e "oltre 50 dipendenti" (storico).

**Tecnologia**:
- Pagina unica fatta su misura (meta author "Davide Borsatto"), con Swiper, TweenMax (GSAP 1) e lo scorrimento della rotella catturato per passare da una schermata all'altra.
- Font Abril Fatface (titoli) e PT Sans da Google.
- Video di sfondo mp4/webm/ogg del 21/06/2016. Google Analytics "UA-79289228-1", servizio dismesso.
- nginx con PHP 8.1. Il CSS chiama gli sfondi desktop di home, unico, territorio e certificazioni, che rispondono 404.
- La privacy è aggiornata al "4 dicembre 2018" e il modulo cita ancora il "D. LGS. N. 196/03".

**Problemi a 1440** (`_prova/attuale/0*-1440.jpg`, `90-menu-1440.jpg`):
- Otto schermate identiche: foto a tutto schermo scurita, titolo in Abril Fatface bianco, cornice bianca, puntini a destra. Il ritmo non cambia mai.
- Le foto più belle, i 17 tacchi su fondo chiaro, sono nascoste dietro il bottone "Galleria", che è quasi invisibile (grigio su grigio).
- "Unico" ha come sfondo il fotogramma sfocato dell'etichetta di una scatola; Territorio e Certificazioni usano la stessa Villa Pisani nella nebbia.
- Sopra le foto ci sono grafiche aggiunte: una costellazione di punti (Linee) e la manina con i cerchi tratteggiati (Nascita).
- I certificati sono nove bottoni a filo. Il modulo contatti è grigio su foto scura.
- Il banner dei cookie copre l'alto di ogni schermata. Il menu laterale ripete le otto foto in strisce.
- Il testo storico contiene un errore: "De Sica gira 'Roma città aperta'" (il regista è Rossellini). La versione EN ha refusi ("The heel il born").

**Problemi a 390** (`_prova/attuale/0*-390.jpg`):
- La home è un fondo nero con il titolo e nient'altro: il video non parte.
- Il banner dei cookie occupa due righe e copre il logo.
- I bottoni delle certificazioni si spezzano o si tagliano ("Problematic", "Segnalazion"), e "Galleria" non si legge.
- Le linguette Trovaci/Scrivici sono a basso contrasto.
- Lo zoom è bloccato ("maximum-scale=1, user-scalable=0").

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | TACCHIFICIO RIVIERA S.r.l. | certificati SGS (`_prova/crawl/cert/`): "TACCHIFICIO RIVIERA S.r.l."; privacy del sito |
| P.IVA / CF | 02005670274 | privacy del sito: "c.f. 02005670274"; https://www.aziende.it/tacchificio-riviera-s-r-l: "P.IVA 02005670274" |
| REA | VE-190999 | aziende.it: "REA VE-190999" |
| Sede legale | Via Pola, 22, 30039 Stra (VE) | sito, Contatti: "Sede Legale: Via Pola, 22 – 30039 Stra (VE)" |
| Sede operativa | Viale Serenissima, 30, 30030 Vigonovo (VE) | sito: "Sede operativa e amm.va: Viale Serenissima, 30 -30030 Vigonovo (VE)"; certificati: "Via Serenissima, 30" |
| Telefono / fax | +39 049 502844 / +39 049 504969 | sito: "Tel. +39 049 502844 - Fax +39 049 504969" (il numero è anche nel logo) |
| Email | tacchificioriviera@tacchificioriviera.it; reclami@tacchificioriviera.it (SA8000) | sito, Contatti; politica sociale SA8000 |
| PEC | tacchificioriviera@pec.tacchificioriviera.it | privacy del sito: "una PEC all'indirizzo tacchificioriviera@pec.tacchificioriviera.it"; aziende.it |
| Anno | marchio 1945; società 1985 | modale Territorio: "Il 1945 ... realizza il primo tacco in legno"; https://www.companyreports.it/tacchificio_riviera_srl-02005670274: "Fondazione 1985" |
| ATECO | 15.20.1 fabbricazione di calzature | aziende.it: "ATECO 15.20.1"; companyreports: "15.20.10 - Fabbricazione di calzature, escluse parti in cuoio" |
| Fatturato | 2025: 6.264.577 euro, utile 745.977; 2024: 4.124.063, utile 172.936; 2022: 7.109.027 | companyreports.it ("€ 6.264.577 (2025)"); aziende.it ("€ 4.124.063 Fatturato 2024", "2022 € 7.109.027") |
| Dipendenti | 32 (2024), fascia 20-49 | aziende.it: "32 Dipendenti"; companyreports: "da 20 a 49" |
| Capitale | 99.000 euro | aziende.it |
| ISO 9001:2015 | IT23/00000845, "valido dal 13 ottobre 2023 fino al 13 ottobre 2026" | certificazione-ISO-9001.pdf |
| ISO 14001:2015 | IT23/00000326, valido dal 28/04/2026 al 28/04/2029, "Certificata dal 28 aprile 2023" | certificazione-ISO-14001.pdf |
| ISO 45001:2018 | IT23/00000328, stesse date della 14001 | certificazione-ISO-45001.pdf |
| ISO 50001:2018 | IT23/00001097, "valido dal 11 dicembre 2026 fino al 11 dicembre 2029", "Certificata dal 11 dicembre 2023" | certificazione-ISO-50001.pdf |
| SA8000 | solo documenti di sistema, "Rev 00 del 20 Novembre 2025"; nessun certificato pubblicato | PDF SA8000 del sito |
| Social | YouTube @tacchificioriviera928 (2 video) | oEmbed di YouTube dei video in pagina |

## 4. Materiale visivo

**Cosa è stato scaricato:**
- 57 file in `assets/originali/`; inventario con misure, soggetto e voti (qualità / apertura, da 1 a 10) in `_prova/inventario-immagini.json`.
- Fogli di controllo in `_prova/attuale/foglio-*.jpg`.
- I tre video di sfondo (0,75-1,1 MB, 640x360 e 852x480) non sono stati tenuti per lo spazio su disco: restano quattro fotogrammi.

**Voti (qualità / apertura):**
- **Galleria "Nascita", 17 still life di tacchi su fondo chiaro, 800x650: 7 / 4-9.** È il materiale giusto: luce da studio coerente, un oggetto per foto, fondo #F5F2F8.
  - stiletto nero a calice (`tacco_11`, anche `territorio/modal3`): **7 / 9**;
  - ottone a losanghe con "RIVIERA" e "37" incisi (`tacco_1`): 7 / 8;
  - plexiglas, cuneo trasparente sfumato, due tacchi in legno, metallo satinato, anima metallica: 7 / 7;
  - prototipi avorio: 7 / 3-6.
  Il limite è la misura: 800 px bastano per un oggetto al centro a 1440 a densità 1, sono morbidi sugli schermi retina.
- **Sfondi di sezione, 1920x1080 molto compressi (60-90 KB):**
  - mano che incide un fiore su un tacco in metallo: 7 / 7;
  - disegnatrice al CAD: 6 / 4;
  - controllo del prototipo davanti agli scaffali: 6 / 4;
  - sede al crepuscolo: 6 / 4.
  Mancano le versioni desktop di home, unico e territorio (404).
- Prova del tacco sulla scarpa con la piastra blu timbrata (solo 1024x1024): 6 / 5.
- Mano guantata con prototipo: 5 / 4.
- Fotogrammi dei video: 3-4 / 1-3.
- Copertine YouTube (CNC su legno e centro di lavoro, 1280x720): 5 / 3-4.
- Archivio di famiglia in bianco e nero e anni 80 (488x562, 876x704): 4 / 2-3. Prezioso per la storia, non per l'apertura.
- Logo SVG vettoriale (timbro tondo con firma, in bianco): 6 / 0. Contiene il numero di telefono.

**Giudizio: il soggetto regge una home di alta gamma, la risoluzione no.** Voto medio del materiale: **6 su 10** (soggetto 9, misura 4). Gli still life sono già da catalogo di lusso e bastano per una proposta onesta, con l'oggetto mostrato non oltre la sua misura. Per il sito vero servono gli originali del servizio fotografico, o una giornata di still life sullo stesso fondo a 4000 px: 6-8 tacchi, il legno, il prototipo segnato in rosso, l'ottone, il plexiglas, più le mani al banco e la pressa a iniezione.

## 5. Due direzioni artistiche

**Quanto uso le ispirazioni (Graziella, Studio N19)**: molto, perché qui il soggetto le giustifica. Riviera fa per le griffe quello che Pelletteria Graziella fa per la pelletteria, nello stesso distretto e con lo stesso prefisso 049. Da Graziella prendo la tipologia: una frase che dice cosa fanno e per chi, un solo prodotto vero, i contatti in testata, molta aria. Da Studio N19 prendo il titolo enorme su fondo quasi bianco. Non prendo il corsivo sulle parole d'accento (vietato), il nero di default, il lettore audio, le dissolvenze sfocate né il pallino che segue il cursore.

**Direzione A: "Il tacco come scultura" (chiara, consigliata)**
- Idea visiva: prima schermata color carta (#F5F2F8, lo stesso fondo degli still life) con un solo tacco enorme al centro, lo stiletto nero a calice, e un titolo grande e diritto: "Tacchi per le calzature di lusso. Dal 1945." Sotto ci sono poche sezioni: il percorso dal disegno al tacco, la Riviera del Brenta, le certificazioni in una riga e i contatti.
- Immagini: solo still life su quel fondo, un oggetto per volta, a grandezza quasi reale. Una sola foto di mani al banco (l'incisione del fiore) come pausa.
- Tipografia: Bodoni Moda (Google Fonts, OFL), solo in tondo, per i titoli; Hanken Grotesk (Google Fonts, OFL) per testi e didascalie, con cifre tabellari per anni e numeri di certificato.
- Colore: carta #F5F2F8, inchiostro #151313, un solo accento rosso matita #B8322A preso dal segno rosso sui prototipi avorio della galleria.
- Gesto: cinque parole sotto il tacco (Legno, Prototipo, Plastica, Plexiglas, Ottone). Al clic o al tocco l'oggetto al centro cambia di colpo, senza dissolvenza, con la didascalia del materiale. Le foto sono tutte loro.

**Direzione B: "La mano e il metallo" (scura solo perché l'immagine lo chiede)**
- Idea visiva: la tipologia di Graziella. A sinistra c'è la frase grande; a destra, in un riquadro, la macro della mano che incide il fiore sul tacco in metallo, una foto nata scura. In testata: "Stra e Vigonovo, Riviera del Brenta" e il telefono. Sotto, il nero lascia subito il posto alla carta per la storia e i certificati.
- Immagini: reportage di laboratorio in luce radente (incisione, CAD, controllo del prototipo, pressa), l'archivio di famiglia in bianco e nero per il 1945, Villa Pisani per il territorio.
- Tipografia: Erode (Fontshare, ITF Free Font License) in tondo per la frase; General Sans (Fontshare, ITF Free Font License) per l'interfaccia, maiuscolo spaziato piccolo per le etichette.
- Colore: nero caldo #12100E solo nella prima schermata, poi carta #F2EFE9; ottone #A88A55 come unico accento; testo #1A1816.
- Gesto: tre anni in fila (1945, 1970, 2010). Il tocco cambia la foto del riquadro (il legno, il prototipo in plastica, la sede nuova) e una riga di testo verbatim dalla loro storia.

## 6. Immagini sostitutive

Ci sono 9 foto in `assets/esterne/`, tra 2000 e 2400 px di lato lungo. Licenza verificata sulla pagina di ogni foto (Unsplash License, Pexels "Free"); autori e URL in `assets/CREDITI.md`. Nessuna compare nei CREDITI delle altre home della campagna e nessuna mostra un marchio.
- Per A:
  - ombra lunga di uno stiletto nero su fondo chiaro (Daniela Messina, Pexels);
  - tacco a sfera nera su bianco (engin akyurt);
  - tacco a blocco decorato su bianco (engin akyurt);
  - décolleté nere su pelle naturale (José Martin Segura Benites, Pexels).
- Per B:
  - linea dello stiletto bianco su nero (Segura Benites, Pexels);
  - mani che intagliano un modello (Raoul Ortega);
  - modelli in plastica nelle cassette di produzione (Fernanda Simões, Pexels).
- Comuni:
  - forme in legno (Jez Timms), per il primo tacco del 1945;
  - Villa Pisani a Stra (Edoardo Bortoli), per il territorio.

Sono segnaposto: dove esiste una foto loro dello stesso soggetto, va usata la loro.

## 7. Riferimenti di alta gamma

Prime schermate in `riferimenti/<nome>-1440.jpg` e `-390.jpg` (JPEG 78), aperte dal vivo il 19/10/2026.

1. **Pelletteria Graziella** (pelletteriagraziella.com), pelletteria per le griffe, Venezia, "DAL 1986 MADE IN ITALY". È anche ispirazione del committente.
   - Cosa la rende di alta gamma: una sola frase da 79 px, "We develop and produce high-quality leather goods for luxury fashion brands.", una sola borsa fotografata, contatti e "Based in Venice, Italy" in testata.
   - Da non riprendere: il corsivo sulle parole chiave, le parole in grigio basso contrasto, il lettore "the sound of our work", il nero di default, il sito Wix con il bottone accessibilità.
2. **Maison Ernest** (maisonernest.com), "Le Talon Parisien depuis 1904".
   - Cosa la rende di alta gamma: un tacchificio diventato maison, che dichiara il mestiere in una riga ("L'ART DE LA CAMBRURE DEPUIS 1904"). Logo sottile e spaziato, una sola foto a tutta pagina.
   - Da non riprendere: gambe e borsa da campagna moda (Riviera vende ai calzaturifici, non al pubblico), le icone dell'e-commerce, la scritta minuscola sulla foto.
3. **Manolo Blahnik** (manoloblahnik.com).
   - Cosa lo rende di alta gamma: la scarpa è la protagonista in una stanza vera; logo in maiuscolo leggero al centro; un solo bottone.
   - Da non riprendere: il carosello con le barre di avanzamento, la barra promozionale, i servizi da negozio.
4. **Pierre Hardy** (pierrehardy.com).
   - Cosa lo rende di alta gamma: dittico con la scarpa come still life su un materiale (maglia grossa) accanto al ritratto; IBM Plex Sans pulito. Il dittico oggetto e materia serve alla direzione A.
   - Da non riprendere: la testata affollata, la barra newsletter; a 390 il popup del paese copre tutto.
5. **Tacchificio Monti** (tacchificiomonti.com), lo stesso mestiere: "Produzione Full Cycle".
   - Cosa funziona: la pagina Chi siamo, con tutta la squadra in piedi nel reparto stampaggio e il titolo "Tre generazioni, una sola passione". La scala produttiva è mostrata come credenziale.
   - Da non riprendere: la home a video, che nel browser di prova resta bianca con "SKIP VIDEO" (`tacchificio-monti-home-1440.jpg`), e il Cormorant ovunque.

Aperti e scartati:
- Rossimoda, Museo Ferragamo, Massaro: "Access Denied".
- Roger Vivier, Gianvito Rossi, Altofare, ACRIB: pagina vuota. Christian Louboutin: verifica Cloudflare. René Caovilla: errore e banner cookie.
- Aquazzura, Sergio Rossi: popup newsletter. Giuseppe Zanotti: video sgranato.
- Amina Muaddi, The Row, Khaite: modelle, niente oggetto.
- Formificio Romagnolo: impianto datato. Tre Zeta: testata blu e Inter.
- Bata Shoe Museum: manifesto di mostra. Villa Foscarini Rossi: modello da location per eventi.

## 8. Da confermare

- **ISO 9001**: il PDF in linea è scaduto il 13/10/2026. C'è il rinnovo?
- **ISO 50001**: il PDF dice "valido dal 11 dicembre 2026", una data futura. È un refuso o un'emissione anticipata?
- **SA8000**: sul sito ci sono solo i documenti di sistema (Rev 00, 20/11/2025). L'azienda è certificata o è in corso?
- Anno da usare in pagina: 1945 (il marchio) o 1985 (la srl, da companyreports). E chi guida oggi l'azienda: Fabio Boldrin?
- Dipendenti oggi (32 nel 2024) e fatturato 2025 (6,26 milioni da companyreports): si possono citare?
- Quali griffe si possono nominare: il sito non ne nomina nessuna.
- Cosa producono in casa: i certificati dicono plastica a iniezione, la galleria mostra anche legno, metallo, plexiglas e ottone inciso. Il metallo e l'incisione ("intagliandoli") sono interni o di fornitori? Quali macchine (presse, CNC, CAD)?
- "Viale" o "Via" Serenissima 30: il sito e i certificati non coincidono.
- Originali ad alta risoluzione degli still life e degli sfondi, nome del fotografo, permesso per le persone ritratte e per le foto d'archivio (chi sono gli uomini di `modal1` e `modal2`).
- Logo: esiste una versione senza il numero di telefono e una a colori?
- L'errore storico su "Roma città aperta" (Rossellini, non De Sica): va corretto o tolto dai nuovi testi.
- Lingue: il nuovo sito resta IT ed EN? Il testo inglese va rivisto.
