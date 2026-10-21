# 247LAB, il sito nuovo: LEGGIMI

È una proposta non richiesta: il sito completo, statico, in italiano, nello stesso design della home. Si apre con `file:///` da `sito/index.html`, senza server e senza dipendenze esterne (caratteri, immagini, cataloghi e schede PDF sono in locale).

## Mappa del sito

**130 pagine**: la home, fatta a mano, e 129 pagine generate.

| Pagina | File | Cosa c'è |
|---|---|---|
| Home | `index.html` | la home approvata (cambiati solo i numeri dei modelli, il link a G-label e i link privacy/cookie: vedi sotto) |
| Collezioni | `prodotti.html` | le tre collezioni con le famiglie, i campioni delle finiture e i cataloghi |
| Collezione RB | `collezione-rb.html` | il testo della collezione, le tre finiture, **49 modelli** in 8 famiglie con filtro per famiglia |
| Collezione Twentyfour7 | `collezione-tecnica.html` | **24 modelli** in 7 tipi, filtro per tipo e per colore, potenza, temperatura, ottica e IP sotto ogni foto |
| G-label | `g-label.html` | il sistema a binario: SPOT G-6 e LINEA L-20, binari e accessori con i codici, il catalogo |
| Schede prodotto | `prodotti/<slug>.html` | **75 schede** (49 RB, 24 Twentyfour7, 2 G-label): foto, descrizione, finiture, "Chiedi informazioni" (mail), scheda tecnica e catalogo in PDF, dati tecnici, disegno, altri della stessa famiglia |
| Progetti | `progetti.html` | **41 progetti** dal 2006 al 2025: i due più recenti in grande, poi tre per riga; filtro per tipo e per anni; gli studi con i loro progetti |
| Schede progetto | `progetti/<slug>.html` | **41 schede**: committente, luogo, anno, tipo, studio, fotografo, prodotti riconosciuti nelle foto, le foto in sequenza, precedente e successivo |
| Su misura | `su-misura.html` | come si lavora insieme, quattro progetti di esempio, i recapiti |
| Cataloghi | `cataloghi.html` | i tre cataloghi 2026 in PDF, le condizioni generali di vendita |
| Chi siamo | `chi-siamo.html` | Roberto e Marco, le tappe, gli studi, Saonara |
| Contatti | `contatti.html` | recapiti, modulo che prepara una mail, indirizzo, ragione sociale, P.IVA, social |
| Shop | `shop.html` | MINA nelle tre finiture con prezzo e codice, la lampada, la spedizione |
| Schede MINA | `shop/mina.html`, `shop/mina-marrone-brunito.html`, `shop/mina-antracite.html` | scelta della finitura (cambia foto, prezzo, codice e mail), ordine via mail, dati tecnici |

Ogni pagina interna ha la testata e il piede della home (stesse voci; la voce del menu della sezione è segnata), le briciole `Home / Sezione / Pagina` e il titolo `Nome | 247LAB`.

## Cosa c'è e dove

- `sito/` è il sito: `css/base.css` (token, tipografia, griglia, testata, piede, bottoni, campioni delle finiture) più un foglio per gruppo (`collezioni.css`, `prodotto.css`, `progetti.css`, `azienda.css`), `js/` (menu del telefono e newsletter in `base.js`, filtri, galleria, modulo e scelta di MINA), `img/` (WebP a più larghezze), `fonts/`, `cataloghi/` (i tre PDF 2026), `schede/` (79 schede tecniche PDF).
- `_prova/dati/` sono i dati da cui nascono le pagine: `prodotti.json`, `progetti.json`, `collezioni.json`, `sito.json`, con le fonti e le correzioni in `NOTE.md`.
- `_prova/script/` è il generatore (`genera.py`, `base.py`, i quattro `pagine_*.py`, vedi `LEGGIMI-generatore.md`) e il controllo dei link (`controlla_link.py`).
- `screenshot/sito/` contiene gli screenshot di 14 pagine a 1440 e a 390 (e tre pagine anche a 768 e 320); `screenshot/home/` quelli della home, con `NOTA.md` su idea, caratteri, colori e controlli.
- `01-analisi.md` raccoglie i fatti con le fonti. `assets/CREDITI.md` dice l'origine di ogni immagine.

## Come si rigenera

```
python3 /home/user/danielnistorr/Lab247-Sito/_prova/script/genera.py          # rifà le 129 pagine (non la home)
python3 /home/user/danielnistorr/Lab247-Sito/_prova/script/controlla_link.py  # controlla link, immagini, srcset, css, js, ancore
```

Serve Python 3 con Pillow. Un giro basta: chi ha una scheda e chi sta nelle griglie lo decide `pubblicabile()` in `base.py`, dai dati. Per cambiare un testo o un numero si cambiano i dati in `_prova/dati/`, non le pagine. La home si modifica a mano in `_prova/script/finale.html` e `sito/index.html` (oppure `bash _prova/script/build_finale.sh solo-pagina`).

`controlla_link.py` apre tutte le 130 pagine e controlla ogni `href`, `src`, `srcset`, foglio di stile, script, ancora e `url()` dei CSS. Oggi: nessun link rotto, nessun percorso assoluto, nessun U+2014. I link esterni sono solo quelli che servono: EN e English (sito di oggi), WhatsApp, la mappa, i social, Artemest e Archiproducts.

## Correzioni fatte nell'unione (da sapere)

- **Numeri dei modelli in home**: 49 RB (era 51) e 24 Twentyfour7 (era 25), come nelle pagine delle collezioni.
- **KYLE con tige PS** è nel catalogo RB 2026: ora è nella griglia RB, tra i soffitti, oltre che nella sua scheda. I due G-label (SPOT G-6, LINEA L-20) hanno la scheda e il link dalla pagina G-label.
- **G-label in home** porta ora alla pagina `g-label.html` ("Il sistema G-label"), con il catalogo accanto come per RB e Twentyfour7.
- **Privacy e cookie**: i testi non esistono, quindi non ci sono pagine né link finti. Nel piede restano copyright, P.IVA e English; i consensi della newsletter e del modulo contatti dicono "Ho letto l'informativa privacy" senza link. **I testi di privacy e cookie vanno forniti prima di andare online**, e allora si rimettono i link nel piede e nei due consensi.
- **MINA**: gli alt della seconda foto dicevano "accesa", ma la lampada è spenta (e del brunito marrone si vede solo il piede): corretti nei dati.
- **Campioni delle finiture**: un solo insieme di colori in collezioni, schede e shop (ottone #B8924A, brunito #5A4130, antracite #3A3D40, come il selettore della home; bianco, nero e alluminio per Twentyfour7). Sono colori approssimati: vanno confrontati con i campioni veri.
- **Misure**: lo spazio tra numero e unità (7 W, 3000 K, 405 mm) è lo stesso in griglie, schede, G-label e shop.
- **Archivio progetti**: da 15.800 a 8.500 px di altezza a 1440, con tre progetti per riga dopo i due più recenti (due per riga a 768, uno sul telefono).

## Da confermare con l'azienda

**Home e azienda**

- **Il motto in inglese come titolo**: "We don't fear the dark" con il sottotitolo italiano "La bellezza della luce nella sua forma più pura" (la frase della collezione tecnica). Va bene così o serve un titolo in italiano?
- **Ragione sociale** nella riga legale: "247LAB di Marco Bertelli, ditta individuale", con P.IVA 05375130282. Non sono in pagina:
  - il REA, perché non è stato trovato;
  - la PEC certificata@pec.247lab.it, letta solo in un estratto di ricerca.

  Il capitale sociale non si applica a una ditta individuale.
- **Indirizzo**: Via Emilia Romagna 31, oppure 31/33 come in un estratto camerale?
- **Orari**: non sono pubblicati, quindi non sono in pagina. Se ci sono, vanno nella chiusura sotto l'indirizzo.
- **"Fatte a mano in Italia" e "fatto a mano"** (RB): dove si producono le lampade? A Saonara o da terzisti? La pagina non dice "laboratorio".
- **"Dal 2021"** e "quasi due decenni" per Roberto. I progetti partono dal 2006, ai tempi di TWENTYFOUR7: quale anno di inizio vogliono dichiarare?
- **Nomi e dati dei prodotti**:
  - CIUCCIO in F066 è confermato a vista: è la stessa applique della scheda `ciuccio` e della pagina 104 del catalogo RB 2026. In pagina ci sono i dati del catalogo 2026 (1xE27 LED 6 W, 3000K, IP44, ottone naturale e vetro, alta 700 mm). La scheda del sito dice invece IP54: quale dei due è giusto?
  - La foto delle collezioni (F346, Casa P) mostra due fari in ottone su un'asta: non sappiamo il nome del modello, quindi la didascalia dice solo progetto, città, anno e fotografo. Se è un modello RB, va aggiunto il nome.
  - BOATY S (F024) viene dalla pagina dove compare la foto.
  - KYLE terra in Casa G è dedotta dalla forma.
- **G-label**: è già in vendita? Il sito nuovo ha la pagina `g-label.html` e le due schede, con i dati del catalogo G-label 2026 (che sul sito di oggi non ha una pagina).
- **Committenti citati in home**: Ferragamo, 10 Corso Como, Hotel Mediterraneo, Fendi, Casadei, Tiziana Fausti, Palazzo Vendramin, H-Farm, Hotel Coast, Dolce&Gabbana, Enoteca S. Lucia, Casa G, Harry's Piccolo. Sono presi dalle loro schede di progetto: va chiesto se si possono citare in home e nelle 41 schede dei progetti.
- **Studi citati**: Marco Costanzi Architects, Parisotto + Formenton Architetti, Zanon Architetti Associati, MIDE architetti.
- **Newsletter**:
  - il servizio a cui collegarla;
  - chi la scrive e ogni quanto;
  - il testo dell'informativa privacy.

**Prodotti** (dettagli e fonti in `_prova/dati/NOTE.md`)

- **Sei schede Twentyfour7 senza catalogo 2026** (6493, 7009, 7010, TELE-3, INC-3, MINI TUBE): esistono sul sito di oggi ma non sono linkate né nel catalogo. Sono fuori produzione? Oggi non hanno una pagina; se sono vive basta cambiare `pubblicabile()` in `base.py`. CORNER 45 è nella pagina di oggi ma non nel catalogo 2026: è in pagina.
- **Dati in conflitto tra scheda del sito, scheda PDF e catalogo**, risolti con la scheda PDF o il catalogo 2026: IP di CIUCCIO (44 o 54), TREDUE93 (20 o 40), 1111 (44 o 20), 6493 e INC-3; potenza di 55-OR (10 o 8 W); testo di RDN (ripeteva quello di 55-OR); codice di MODULO; MICRO KYLE PT da parete e non a plafone; RO' S con tige anche in antracite.
- **Designer**: indicato solo per DEUS 600, DEUS 1250 e DEUS terra (Nicola Ceciliot) e per 2006 (TWENTYFOUR7). Gli altri non hanno designer in pagina.
- **Prezzi di listino** di RB, Twentyfour7 e G-label: non pubblicati, quindi non in pagina (le schede hanno "Chiedi informazioni"). Per RB c'è la frase del catalogo sul sovrapprezzo delle finiture brunito e antracite.
- **Disegno tecnico di SQUARE CANDLE**: manca (il file del sito non è stato riconosciuto); gli altri 48 RB lo hanno.
- **Foto piccole**: molte Twentyfour7 (533-886 px sul sito di oggi), le foto G-label (tre, una è un render), Hotel Coast (900 px). Servono originali più grandi.
- **Colori dei campioni** delle finiture: approssimati, da confrontare con i campioni veri.

**Progetti**

- **Titoli corretti**: "Branzino Felice" (resto del modello Wix) è diventato **Casa AL**; First Padova, Massimo Alba, Tiziana Fausti Lugano, Harry's Piccolo senza i resti di formattazione.
- **Casa R** (Padova 2024) e **Casa R+S** (Padova 2018) sono due schede diverse: sono due progetti?
- **Tipo**: dato solo dove è certo (8 case, 2 hotel, 5 uffici, 10 negozi); gli altri 16, tra cui ristoranti ed enoteche, sono senza tipo e compaiono solo con "Tutti". Se serve un filtro "Ristoranti", va aggiunto ai dati.
- **Testi dei progetti**: le schede di oggi non ne hanno; le schede nuove mostrano solo i dati e le foto. Un paragrafo per progetto (anche solo per i 10 principali) le renderebbe più ricche.
- **Alt delle foto dei progetti**: veri ma generici ("Casa AL, Lussino: foto 3 di 8"), da migliorare con l'azienda.
- **Prodotti nei progetti**: la riga "Prodotti" compare solo dove un modello è nominato nella descrizione della foto (per esempio KYLE terra in Casa G, dedotta dalla forma). L'azienda può dare l'elenco vero per ogni progetto.

**Shop**

- **Prezzi** 135,00 € (ottone) e 155,00 € (brunito marrone e antracite), IVA inclusa, codici 247M.001-.003, spedizione gratuita in Italia, 10 € Europa, 25 € resto del mondo: sono quelli dello shop di oggi. Sono aggiornati?
- **Resi**: il sito di oggi ha due testi diversi (contributo di 15 € oppure reso entro tre giorni a spese del cliente); nessuno è in pagina finché l'azienda non sceglie.
- **Materiale**: le schede di oggi dicono "alluminio anodizzato ottone" anche per le brunite; in pagina c'è "alluminio anodizzato" con la finitura a parte.

## Per metterlo online

1. **Privacy e cookie**: servono i due testi (con la ragione sociale, la PEC se confermata, il servizio della newsletter). Poi due pagine `privacy.html` e `cookie.html` nel generatore, i link nel piede e nei consensi della newsletter e del modulo contatti. Senza statistiche né contenuti di terzi il sito non ha cookie; se si aggiunge un servizio di statistiche serve il banner.
2. **Modulo contatti**: oggi prepara una mail (`mailto:` con nome, cognome, email, oggetto e messaggio) a info@247lab.it e non invia niente da solo. Online lo si può collegare a un servizio di moduli (Formspree, Netlify Forms, o lo script dell'hosting) con il doppio controllo antispam; il consenso resta.
3. **Newsletter**: il modulo del piede controlla i dati e risponde "L'iscrizione apre a breve" con il mailto. Va collegato a Brevo o Mailchimp con il doppio consenso (dettagli sotto).
4. **Shop**: oggi il bottone "Prepara l'ordine via mail" apre una mail d'ordine con finitura, codice e prezzo; niente carrello né pagamento. Due strade da scegliere con l'azienda: tenere l'ordine via mail (e il pagamento con bonifico o link di pagamento), oppure portare il bottone al checkout di oggi (`https://www.247lab.it/category/all-products`, finché Wix resta attivo) o a un negozio vero (Shopify Lite, Stripe Payment Links) con le condizioni di vendita e il diritto di recesso.
5. **Versione inglese**: EN e English portano oggi al sito di oggi, che non ha una versione inglese nella sitemap. Le schede tecniche PDF hanno già il testo in inglese. Per farla: tradurre i testi dei dati (un campo `_en` per ogni testo) e far generare `sito/en/` allo stesso generatore, con `hreflang` tra le due versioni.
6. **Indirizzi del sito di oggi**: per non perdere i link e la ricerca servono i redirect 301 dagli indirizzi Wix alle pagine nuove: `collezione-decorativa-1` → `collezione-rb.html`, `copia-di-nuova-pagina` → `collezione-tecnica.html`, `portfolio` → `progetti.html`, `about-3` → `chi-siamo.html`, `cataloghi` → `cataloghi.html`, `category/all-products` → `shop.html`, `product-page/mina*` → `shop/mina*.html`; ogni scheda prodotto e ogni progetto ha il suo `url_originale` nei dati, da cui si fa la tabella completa.
7. **Hosting**: il sito è statico (circa 81 MB di immagini e 31 MB di schede PDF): va bene un hosting statico qualsiasi. Prima di pubblicare aggiungere `canonical`, `sitemap.xml` e `robots.txt`.

## Newsletter: non funziona finché non si collega

Il modulo nel piede ha campo email, bottone e consenso, e controlla i dati in pagina, ma non invia niente a nessuno. Per non fingere un'iscrizione, oggi risponde "L'iscrizione apre a breve: intanto scrivici a info@247lab.it", con il link mailto. Per farlo funzionare:
1. collegarlo a un servizio (Brevo o Mailchimp) con il loro modulo incorporato o con le API;
2. attivare il doppio consenso;
3. scrivere l'informativa privacy e rimettere il link in "informativa privacy".

Ha senso perché ogni anno esce un catalogo nuovo, la G-label è appena uscita, lo shop vende ai privati e gli architetti aspettano i cataloghi.

## Foto da rifare dal vero, con le indicazioni di scatto

- **Roberto e Marco insieme al banco**, di sera, con una sola lampada accesa. Il muro scuro va lasciato libero a sinistra per il titolo e il banco deve essere senza libri né oggetti di altri marchi. Formato orizzontale 2:1, più una verticale 4:5. Nella F018 di oggi i libri e il televisore sono stati tolti con il taglio.
- **BOATY S accesa per l'apertura**, a una risoluzione più alta (oggi è l'originale Wix 4000x6000, ma il paralume occupa solo 1788 px di larghezza). Fondo nero, il fusto deve uscire dal bordo alto, il paralume va ripreso leggermente dal basso perché si veda l'interno acceso, con molto spazio nero sotto.
- **G-label e Twentyfour7 in luce del giorno**, come F346: un solo apparecchio su parete chiara. Oggi la sezione Tre collezioni ha una sola foto (F346) perché le foto di 1111 e dello SPOT G-6 (un render del catalogo) non reggevano accanto.
- **MINA nelle tre finiture con la stessa inquadratura vera**: le tre foto dello shop sono scattate da punti diversi. Oggi sono riportate con PIL alla stessa scala e allo stesso riquadro, e le ombre sono aperte perché il brunito si legga sul muro nero; va rifatta una serie a camera ferma, su fondo grigio medio.
- **Un macro della lavorazione dell'ottone** (taglio, brunitura) e il banco di lavoro di Saonara, se esistono.

## Licenze e permessi

- **Foto**: sono tutte dell'azienda.
  - Casa G (F288) e Casa P (F346) sono di Alessandro Cusano, come risulta dalle schede del sito: servono il permesso e il credito.
  - Delle foto di prodotto (BOATY S, MINA, CIUCCIO) e del ritratto F018 non è indicato l'autore: va chiesto chi le ha fatte e con quali diritti.
  - Nel prototipo B c'erano anche le foto di Harry's Piccolo di Roberto Pastrovicchio. Nella home finale non ci sono più, ma restano da chiarire se tornano nelle pagine Progetti.
- **Caratteri**: Jost e Hanken Grotesk, SIL Open Font License 1.1 (Google Fonts), serviti in locale. L'uso commerciale è libero.
- **Foto di repertorio**: nessuna nella home finale. Quelle in `assets/esterne/` restano solo come riserva, con le licenze in `assets/CREDITI.md`.

## Loghi

- **Logo 247LAB**: SVG ricostruito dal PNG originale 2246x455 con il tracciamento dei contorni (IoU 0,988), in `currentColor`. In pagina è in colore luce sul nero e in inchiostro sulla carta. Da chiedere all'azienda il vettoriale originale.
- **Favicon**: il pittogramma del faretto su binario, ricostruito in SVG.
- **Logo RB**: ricostruito (`assets/originali/logo-rb.svg`), non usato in home.
