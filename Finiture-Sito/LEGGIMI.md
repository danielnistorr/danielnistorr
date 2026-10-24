# Finiture S.r.l.: proposta di nuova home

Proposta non richiesta, solo la home. Nulla è stato inviato all'azienda né pubblicato.

- Pagina finale: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md`).
- Per rifare tutto (immagini, pagina, screenshot, controlli): `bash _prova/script/build_finale.sh`. Gli script sono `finale_img.py` (immagini), `finale_pagina.py` con il modello `finale_pagina.html` (pagina e grafico delle barre), `finale_shoot.mjs` (screenshot), `finale_schede.mjs` (schede a 1440 e 390, menu, fisarmonica), `finale_controlli.mjs` (larghezze da 320 a 2560, tastiera, tocco, newsletter, collegamenti).
- Analisi con le fonti: `01-analisi.md`. Prototipi scartati e scelto: `_prova/home/a` (base) e `_prova/home/b`.

## Dati da confermare con l'azienda

- **Uso delle foto e dei render** presi da finiture.it: proprietà, nome del fotografo del servizio `*_R01`, permesso di usarli nel sito nuovo.
- **Clienti citati in home**: Distner (Wiesau), Setz Fensterbau (Schötz), Bruppacher, Malenfer (Villers-Farlay). Vengono dalle loro notizie; va chiesto se si possono nominare in home e se i numeri delle linee (barre, robot, colori, superfici) sono ancora quelli giusti.
- **Area test**: la pagina Servizi parla di "una nuova area test" ma non dice dove. In pagina non c'è il luogo; confermare se è a Villatora di Saonara e se l'attrezzatura descritta (flow coating verticale, robot RAS, cabina, tunnel LDP, ventilatori assiali, lampade alogene, linea orizzontale per profili) è quella di oggi.
- **Giovanni Sedino**: in pagina "oggi diretta da Giovanni Sedino" (pagina Company). Ruolo esatto da confermare (CEO, amministratore unico).
- **Export e paesi**: "oltre il 90% del nostro mercato è all'estero" e "impianti in Europa, Asia, Australia e Nord America" (sintesi di "Europa, Cina, Giappone, India, Australia, Canada e Stati Uniti", pagina Company). Confermare che sono ancora attuali.
- **Foto dell'apertura**: la home apre sulla domanda "Cosa vuoi verniciare?" e la scelta iniziale è Porte, con la porta verde a doghe e la porta rossa appesa ai ganci del trasportatore. Le didascalie ("Porta a doghe laccata verde; dietro, una porta rossa appesa ai ganci del trasportatore", "Anta con vetro appesa in cabina, sotto lo spruzzo", "Pannello CLT appeso al trasportatore aereo", "Sedie laccate arancio sui pianali del trasportatore a terra") descrivono quello che si vede: da far rileggere all'ufficio tecnico, con il nome dell'impianto o del cliente se si può dire.
- **Macchine abbinate ai settori**: Finestre dal caso Distner; Porte dalla notizia sulla verniciatura delle porte; CLT dalla notizia sulle case in legno; Sedie e mobili dalle schede dei trasportatori a terra e della birotaia IMB. Da validare, in particolare Sedie e mobili.
- **Codice fiscale**: nel piede di oggi c'è "C.F. 02832330241", diverso dalla P.IVA 03569090289. Non è nella riga legale finché non si verifica in visura. PEC non trovata: non è in pagina.
- **Newsletter**: va collegata a un servizio (oggi il modulo non invia nulla) e va chiesto se quella attuale è attiva e con quale servizio. L'informativa privacy deve citarla.
- **Divisione Handling & Assembling**: nel piede è una voce di Macchine; confermare se va ancora presentata anche con il nome Tambone.
- **Fiere**: HOLZ-HANDWERK 2028 (padiglione 9, stand 9-212) non è in pagina; se confermata, è la notizia giusta da aggiungere.

## Pagine del sito nuovo a cui puntano i link

Azienda (`azienda.html`), Impianti con i quattro settori (`impianti/finestre.html`, `impianti/porte.html`, `impianti/clt.html`, `impianti/sedie-mobili.html`), Macchine (`macchine.html` e sette famiglie: `macchine/robot.html`, `impregnazione.html`, `trasporto.html`, `essiccazione.html`, `cabine.html`, `acqua.html`, `handling.html`), Area test (`area-test.html`), Assistenza (`assistenza.html`), Usato (`usato.html`), Notizie (`notizie.html`), Contatti (nella home, `#contatti`), Privacy (`privacy.html`), Cookie (`cookie.html`), versioni EN, DE, FR (`en/`, `de/`, `fr/`). Social esistenti: LinkedIn e YouTube (Facebook e Instagram non trovati).

## Foto da rifare dal vero

Il materiale di oggi regge la proposta ma è tutto a 1920 px o meno, con ritocchi d'epoca. Prima di tutto chiedere al fotografo gli **originali ad alta risoluzione del servizio `*_R01`** (circa 2016). Poi, se si scatta di nuovo:

1. **I pezzi dell'apertura.** La home mostra un pezzo appena verniciato per settore, appeso alla macchina Finiture. Oggi sono foto del 2016 a 1440-1920 px, con un leggero effetto HDR (Finestre soprattutto). Servono, per ogni settore, un pezzo appena uscito dal tunnel appeso al Power&Free rosso, fotografato con il gancio e un tratto di rotaia in vista: luce radente da un lato per far leggere la buccia della vernice e gli spigoli, obiettivo 85-100 mm, diaframma 8-11, almeno 6000 px, nessun HDR, orizzontale con margine per il taglio quadrato del telefono. Porta: la verde a doghe o una nuova in un colore pieno; finestra: un'anta laccata con vetro; CLT: un pannello con lo spigolo dei suoi strati; sedie: due o tre sedie laccate sul trasportatore a terra.
2. **Finestre.** Un'anta con vetro appena spruzzata in cabina, in luce bianca, ripresa a mezza figura con lo spruzzo nitido (tempo 1/500 o lampo); orizzontale, almeno 4000 px.
3. **Sedie e mobili.** Le sedie sul trasportatore a terra in luce pulita, senza il soffitto affollato; un punto di vista più basso.
4. **Area test oggi.** La cabina con un pezzo di un cliente in prova e un tecnico al lavoro, luce del giorno, senza teli sul robot: è la foto che più manca alla home (oggi il robot è coperto dal telo).
5. **Chiusura.** Le curve del Power&Free con un carico di pezzi colorati, cielo del lucernario non bruciato.
6. **Squadra.** L'originale della foto davanti alla sede (online solo a 567x397).

Le foto da telefono delle notizie (WhatsApp) restano buone per le notizie, non per la home.

## Licenze

- Caratteri: Archivo (Omnibus-Type), SIL Open Font License 1.1, da Google Fonts; licenza in `sito/fonts/OFL-Archivo.txt`. Uso commerciale libero.
- Foto e render: di Finiture S.r.l. (finiture.it), da confermare (vedi sopra). Nessuna foto di repertorio è usata nella versione finale; le nove foto in `assets/esterne/` restano solo come riserva, con licenza e autori in `assets/CREDITI.md`.
- Nessuna immagine generata dall'IA.

## Loghi

- Logo usato: ritaglio dall'avatar del canale YouTube (`assets/originali/logo-finiture-da-youtube-ritagliato.png`, 879x313), bianco reso trasparente, PNG a 300 e 400 px (`sito/img/logo-300.png`, `logo-400.png`): nitido a 2x in testata (150 px) e nel piede (180 px). Viene da un JPEG, quindi i bordi della pennellata rossa sono un po' morbidi a ingrandimenti forti.
- Non è stato ricostruito in SVG: la pennellata non verrebbe fedele. Va chiesto all'azienda il logo vettoriale (AI, EPS, SVG o PDF) e, se c'è, il marchio della divisione Handling & Assembling.

## Scelte da spiegare (soglie "da guardare" e altro)

- Nessuna sezione con titolo a sinistra e testo a destra, nessuna riga di numeri grandi: i fatti dell'azienda sono una frase sopra il grafico delle barre.
- Il grafico "barra per barra" usa quattro filetti di riga: è un elenco di dati veri, non una tabella.
- L'area test è a tutta larghezza e non a 2/3 come proponeva il giudice: con 2/3 l'area coperta da foto scendeva sotto la soglia del 35 %.
- Archivo è nella guida tra i "tic di casa" solo in coppia con IBM Plex Mono: qui è da solo, senza monospazio.
- Il modulo della newsletter controlla email e consenso e risponde con un messaggio, ma non invia nulla: va collegato al servizio scelto dall'azienda (Mailchimp, Brevo o quello che usano oggi), con il doppio consenso e l'informativa aggiornata.
