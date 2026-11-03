# Martorana Elettronica, proposta di nuova home

Proposta non richiesta di nuova homepage per Martorana Elettronica S.r.l. (Mestrino, PD). Nessun contatto con l'azienda, niente pubblicato.

## Cosa c'è

| Percorso | Contenuto |
|---|---|
| `sito/index.html` | la home "Stazioni di collaudo su misura" (livello professionale, 03/11/2026), statica: si apre con un doppio clic |
| `sito/img/` | le sole immagini usate, tutte dell'azienda (WebP e JPEG alla misura del file o sotto, loghi PNG) |
| `sito/fonts/` | Hubot Sans e Mona Sans in woff2 e `OFL.txt` (SIL Open Font License 1.1, Google Fonts) |
| `screenshot/home/` | `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (che cosa è cambiato, le 15 regole una per una, i compiti della scheda d'uso, controlli) |
| `_prova/script/build_finale.sh` | rifà tutto: immagini (`pro_img.py`), controlli sul sorgente, screenshot, controlli delle regole (`pro_controlli.mjs`, esito in `_prova/pro_controlli.json`) |
| `_prova/uso/SCHEDA.md` | chi apre il sito, che cosa viene a fare, identità |
| `_prova/versione-1-originale/` | la home precedente "Corretto o scarto" (pagina, immagini, screenshot, NOTA) |
| `_prova/controlli/` | screenshot ridotti a 320, 768, 1024 e 1920 |
| `01-analisi.md` | fatti con le fonti, materiale visivo, riferimenti |
| `assets/` | immagini scaricate dal sito dell'azienda (`originali/`) e segnaposto Unsplash d'archivio (`esterne/`, non usati), licenze in `assets/CREDITI.md` |

## Il modulo di contatto va collegato

Il modulo della sezione "Inviateci le specifiche del prodotto" oggi **compone un'email** (mailto a martorana@martoranaelettronica.com con oggetto e campi): non invia niente da solo e non porta allegati (chi lo usa deve aggiungere disegni e foto nel programma di posta, e la pagina lo dice). Prima di pubblicare va collegato a un servizio di invio con gli allegati (il modulo del CMS scelto, oppure Formspree, Basin o simili), con l'informativa privacy e un messaggio di conferma. Gli altri bottoni email (specifiche, assistenza, intervento o ricambio, inglese) restano mailto con oggetto e traccia.

## Da chiedere all'azienda prima di pubblicare

In pagina c'è solo quello che dicono le loro pagine (01-analisi.md, SCHEDA.md); queste cose vanno chieste:
1. **Orari** d'ufficio e dell'assistenza (non pubblicati da nessuna parte): oggi non compaiono, né in pagina né nel piede.
2. **Il 38%** ("il 38% degli elettrodomestici prodotti nel mondo viene collaudato dalle nostre attrezzature"): da dove viene e se si può scrivere in home. Con la conferma va come quinto numero nella fascia "Azienda".
3. **I clienti** citati sul loro sito (Electrolux-Zanussi, De Longhi, Ocean, Gruppo Merloni Indesit, Gruppo Air Liquide) e quelli della saldatura e dell'illuminazione: quali si possono nominare, con il permesso. Con i nomi si fa la fascia "Clienti" (regola 10) e, con anno e due dati, i "Lavori" (regola 11).
4. **Le recensioni**: su Pagine Gialle ce ne sono due (media 5,0, Sergio P. sull'intervento in azienda, Matteo D. sulle prove elettriche di sicurezza), lette solo da riassunto perché la pagina risponde 403: vanno ricontrollate e servono il permesso e il testo intero prima di metterle.
5. **Certificazioni** (ISO 9001 o altre): nessuna è citata. Le normative di prova in pagina sono CEI, EN, VDE, UL e BSI; "UL IEE, SEL, BSI" del loro sito va riscritto con loro.
6. **Zanussi Grandi Impianti**: la frase sulla stazione degli anni '70 è della loro pagina Chi siamo; va chiesto se si può tenere in home.
7. **"Fornitori ufficiali delle aziende più prestigiose del settore della saldatura"**: è nella loro pagina Chi siamo; va confermato che si può scrivere oggi.
8. **Interventi in azienda e ricambi**: la pagina invita a chiederli per email o al telefono (la scheda d'uso li mette tra i compiti del manutentore); va confermato che li fanno e con quali tempi.
9. **Assistenza remota e area clienti**: se TeamViewerQS (`/download/TeamViewerQS.exe?v=15`), l'Area riservata e l'Area download servono ancora e con che indirizzo nel sito nuovo. Oggi i link puntano al loro sito attuale (che risponde a un browser automatico solo con una pagina di verifica: non ho potuto aprirli da qui).
10. **Quali modelli sono a catalogo**: Mod. 1200, Mod. 1000, serie /NET, Mod. 1294/A, M0524-LED (foto 2025) sono di oggi; Mod. 1200G, M0704N, Mod. 0507, il sistema per saldatrici e i modelli 1200DB, 1200RS, 0586, 0103, 200, 0204, 0290 vengono dalle pagine vecchie.
11. **MccManager**: che cosa fa, in una riga loro (oggi è solo nominato).
12. **L'inglese**: il blocco "In English" è una mia traduzione dei loro testi; va riletto da loro. Il sito nuovo deve avere una home inglese completa all'indirizzo che oggi apre "EN".
13. **Chi guida l'azienda oggi**, l'anno della S.r.l. (2002 secondo Europages) rispetto al 1973, dipendenti e superficie (8 addetti secondo UfficioCamerale, da riassunto: non in pagina).
14. **Sede legale**: Via El Alamein 12 (LinkedIn, Europages, Pagine Bianche) senza comune certo; in pagina c'è solo la sede operativa di Via Torino 10/B. Il vecchio numero 049 5082432 (telefono.click) non va usato.
15. **PEC, REA, capitale sociale** (non pubblici): la riga legale ha solo ragione sociale, P.IVA e indirizzo.
16. **Il logo vettoriale** (AI, EPS, PDF o SVG): in testata c'è il PNG a colori da 237 x 84 mostrato a 142 px (meno di 2x, un poco morbido sugli schermi ad alta densità), nel piede il PNG bianco.

## Pagine del sito nuovo collegate dalla home

`sicurezza-elettrica.html` (con `#mod-1294a`), `tenuta-portata.html`, `saldatrici.html`, `trasformatori.html`, `apparecchi-illuminanti.html`, `alimentatori.html`, `software.html#iridium`, `chi-siamo.html`, `privacy.html`, `cookie.html`. Sono le schede delle prove e le voci del piede: vanno fatte con il sito, oggi non esistono. Il menu in alto porta alle sezioni della home (Prove e stazioni, Assistenza, Azienda, Contatti), all'area riservata del sito attuale e al blocco inglese.

Niente newsletter e niente "Seguici": fanno macchine su misura per pochi clienti industriali, non pubblicano notizie; il profilo LinkedIn ha 13 follower e nessun post.

## Foto da fare dal vero

Il materiale di oggi sono foto piccole su bianco (da 151 a 581 px) e PNG a 256 colori: in pagina reggono solo perché sono mostrate alla loro misura o sotto. Nessuna mostra persone, il laboratorio o la sede. Per la pubblicazione basta una giornata:
1. **Il laboratorio con le persone** (la prima da fare, per l'apertura e per la regola 3): un tecnico al banco con una stazione aperta, le mani sui moduli o sul cablaggio, luce del reparto, la persona che guarda il lavoro e non l'obiettivo. Orizzontale 3:2, almeno 4000 px, RAW.
2. **La sede**: la facciata di Via Torino 10/B con l'insegna, di giorno con cielo coperto, frontale, senza auto davanti. Sostituisce il banner "NEL SETTORE DA OLTRE 40 ANNI" con il cielo disegnato e serve per "Dove siamo".
3. **Le stazioni del catalogo**, stessa serie e stessa luce: fondo grigio chiaro senza giunta, luce morbida dall'alto a sinistra, un'ombra di appoggio, vista a tre quarti con il pannello leggibile e i display accesi: Mod. 1200, Mod. 1000, una della serie /NET, Mod. 1294/A, M0524-LED, Mod. 1200G, M0704N, il sistema per saldatrici, un alimentatore. Almeno 3000 px sul lato lungo.
4. **Una stazione installata** sulla linea di un cliente (con il suo permesso e senza marchi riconoscibili): per la scheda "Sicurezza elettrica in linea" e per i lavori con il nome.
5. **L'archivio**: l'originale della foto della stazione anni '70 per la Zanussi Grandi Impianti (stampa o negativo da scansionare a 1200 dpi), o la stazione stessa se esiste ancora.

## Licenze

- **Immagini dell'azienda** (`assets/originali/`, scaricate da martoranaelettronica.com il 24/10/2026): proprietà di Martorana Elettronica S.r.l., usate solo per la proposta. Le uniche in pagina.
- **Segnaposto**: nessuno in pagina. Tolto il cestello Unsplash della versione 1; le dieci foto di `assets/esterne/` restano in archivio con le licenze in `assets/CREDITI.md`. Nessuna immagine generata dall'IA.
- **Caratteri**: Hubot Sans e Mona Sans di GitHub, SIL Open Font License 1.1, scaricati da Google Fonts e serviti dalla pagina (`sito/fonts/OFL.txt`).

## Da segnalare all'azienda, a parte

Il banner dei cookie del sito di oggi chiede il consenso "scorrendo la pagina" (non più ammesso dalle linee guida del Garante del 2021, da far verificare), il server gira con PHP 5.6 senza aggiornamenti dal 2019 e il sito risponde in http senza passare a https.
