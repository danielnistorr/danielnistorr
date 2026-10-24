# Martorana Elettronica, proposta di nuova home

Proposta non richiesta di nuova homepage per Martorana Elettronica S.r.l. (Mestrino, PD). Nessun contatto con l'azienda, niente pubblicato.

## Cosa c'è

| Percorso | Contenuto |
|---|---|
| `sito/index.html` | la home finale "Corretto o scarto", statica: si apre con un doppio clic |
| `sito/img/` | le sole immagini usate (WebP con trasparenza per gli scontornati, JPEG per le foto, in più larghezze con srcset; logo PNG) |
| `sito/fonts/` | Hubot Sans e Mona Sans in woff2 (SIL Open Font License 1.1, Google Fonts) |
| `screenshot/home/` | `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (idea, caratteri, colori, interazione, foto, controlli) |
| `_prova/script/build_finale.sh` | rifà tutto: immagini (`finale_img.py`), caratteri, controlli sulla pagina, screenshot (`shoot_finale.mjs`), segnali da IA |
| `_prova/script/prova_gesto.mjs`, `larghezze.mjs` | prova del gesto (tocco a 390, tastiera, righe a 1024) e controllo dello scorrimento orizzontale da 320 a 2560 |
| `_prova/controlli/` | screenshot ridotti a 320, 768, 1024 e 1920 e le soglie dei segnali a 1440 |
| `_prova/home/a`, `_prova/home/b` | i due prototipi da cui è nata la versione finale (scelto A) |
| `01-analisi.md` | fatti con le fonti, materiale visivo, direzioni, riferimenti |
| `assets/` | immagini scaricate dal sito dell'azienda (`originali/`) e segnaposto Unsplash (`esterne/`), licenze in `assets/CREDITI.md` |

## Dati da confermare con l'azienda

In pagina c'è solo quello che il loro sito dice; queste cose vanno chieste prima di pubblicare:
- **Mod. 1294/P**: se è ancora a catalogo (è l'apertura) e quali prove fa (le spie "Prove in corso" del pannello fanno pensare a terra, rigidità, isolamento e dispersione, ma nessuna scheda lo dice: nel gesto non è più indicato tra le stazioni che fanno le prove). Se è fuori produzione, l'apertura si rifà con una loro stazione da banco attuale: stessa idea, stesse due legende.
- **Quali modelli sono ancora a catalogo**: 0586_TN, RN, AD, Mod. 0507, Mod. 200, M1294A_EXP1. Nelle quattro famiglie e nelle otto prove compaiono solo nomi presi dal loro sito.
- **Le frasi su cosa misura ogni prova** (gesto "Otto prove, un esito") sono descrizioni generali delle prove: da far rileggere al loro ufficio tecnico.
- **La Zanussi Grandi Impianti** sotto la foto d'archivio: è nella pagina Chi siamo, ma va chiesto se si può nominare in home. I clienti citati sul sito (Electrolux-Zanussi, De Longhi, Ocean, Merloni Indesit, Air Liquide) e il "38 % degli elettrodomestici del mondo" sono fuori dalla home finché non li confermano.
- **Normative**: in pagina solo CEI, VDE, EN e UL; "UL IEE, SEL, BSI" del loro sito va riscritto con loro.
- **Chi guida l'azienda oggi**, e l'anno della S.r.l. rispetto al 1973.
- **Mestrino**: se l'azienda è sempre stata a Mestrino e se le stazioni si costruiscono lì. In pagina c'è solo "Dal 1973, oggi a Mestrino", che non lega i due fatti; con la conferma si può scrivere "progettate e costruite a Mestrino dal 1973".
- **PEC, REA, capitale sociale** (non pubblici): la riga legale del piede ha solo ragione sociale, P.IVA e indirizzo. **Orari d'ufficio** (non pubblici): non ci sono né in chiusura né nel piede.
- Se l'**assistenza remota** con TeamViewer e l'**area riservata** servono ancora.
- La riga "Per una stazione nuova, mandateci il prodotto da provare" è un invito scritto da noi: va bene solo se è il loro modo di lavorare.

## Pagine del sito nuovo collegate dal piede

`chi-siamo.html` (con `#ricerca`), `contatti.html`, `sicurezza-elettrica.html`, `tenuta-portata.html`, `saldatrici.html`, `trasformatori.html`, `apparecchi-illuminanti.html`, `alimentatori.html`, `software.html` (`#iridium`, `#mccmanager`, `#mccdotnet`), `assistenza.html`, `area-riservata.html`, `privacy.html`, `cookie.html`. Il menu in alto porta alle sezioni della home (Azienda, Le prove, Stazioni, Alimentatori e software, Contatti).

Niente newsletter: fanno macchine su misura per pochi clienti industriali, non pubblicano notizie, fiere o cataloghi e non hanno clienti privati. Niente colonna "Seguici": nessun profilo social.

## Foto da rifare dal vero

Il materiale del sito di oggi sono PNG a 256 colori e foto piccole: in pagina reggono come proposta, non per la pubblicazione. Mezza giornata di still life basta.
1. **Apertura, Mod. 1294/P** (o la stazione da banco attuale che lo sostituisce). Oggi in pagina è mostrato alla metà dei 1492 px del file per restare nitido sugli schermi 2x, e le scritte minute del pannello restano impastate: con lo still life può tornare grande e tagliato al bordo destro, come nell'idea di partenza. Come: fondo grigio chiaro senza giunta vicino a #EEF0EF, luce morbida dall'alto a sinistra e una sola ombra di appoggio, vista frontale a tre quarti come oggi con il pannello leggibile, display accesi (".000" e una misura), pulsanti CORRETTO e SCARTO ben visibili. Almeno 4000 px di lato lungo, RAW, nessun riflesso sui display.
2. **Stessa serie, stessa luce**: Mod. 0507, M0704N, Mod. 1200G, M0524-LED, un Mod. 1200 intero, i moduli 0586, il sistema per saldatrici.
3. **Chiusura**: una loro stazione installata sulla linea di un cliente (con il permesso del cliente, senza marchi riconoscibili), verticale, luce di reparto, al posto del cestello Unsplash.
4. **Archivio**: l'originale della foto della stazione anni '70 per la Zanussi Grandi Impianti (stampa o negativo da scansionare a 1200 dpi), oppure la stazione stessa se esiste ancora.
5. Facoltativo: un dettaglio del cavo di terra giallo-verde e della presa dell'apparecchio da provare, per le pagine interne.

## Licenze

- **Immagini dell'azienda** (`assets/originali/`, scaricate da martoranaelettronica.com il 24/10/2026): proprietà di Martorana Elettronica S.r.l., usate solo per la proposta.
- **Segnaposto**: in pagina c'è solo il cestello di Vlad Deep (Unsplash, https://unsplash.com/photos/ykivphUagM4, Unsplash License verificata il 24/10/2026, uso commerciale senza attribuzione obbligatoria). Riga completa in `assets/CREDITI.md`. Non compare in nessun'altra home della campagna. Nessuna immagine generata dall'IA.
- **Caratteri**: Hubot Sans e Mona Sans di GitHub, SIL Open Font License 1.1, scaricati da Google Fonts e serviti dalla pagina.

## Logo

Il logo è il PNG bianco del loro sito (485x158, ritagliato a 471x143): bianco nel piede (mostrato a 180 px, più di 2x) e ricolorato in inchiostro #16191C nella testata (148 px). Non l'ho ricostruito in SVG: le lettere di "MARTORANA" sono disegnate su misura e un rifacimento non sarebbe fedele al pixel. Va chiesto all'azienda il logo vettoriale (AI, EPS, PDF o SVG). L'insegna sulla facciata usa una versione più vecchia del marchio.

## Da segnalare all'azienda, a parte

Il banner dei cookie del sito di oggi chiede il consenso "scorrendo la pagina" (non più ammesso dalle linee guida del Garante del 2021, da far verificare), il server gira con PHP 5.6 senza aggiornamenti dal 2019 e il sito risponde in http senza passare a https.
