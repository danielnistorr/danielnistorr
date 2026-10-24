# Belletti S.r.l.: proposta di nuova homepage

Proposta non richiesta, solo la home. Azienda: Belletti S.r.l., ascensori, Via della Tecnica 29, Mestrino (PD). Non è stata contattata e non è stato pubblicato niente.

## Dove sta cosa

- `sito/index.html`: la home finale, statica, che si apre con file:///. `sito/img/` contiene solo le immagini usate (WebP in più larghezze e il logo SVG), `sito/fonts/` il carattere Radio Canada.
- `screenshot/home/`:
  - `home-1440.jpg` e `home-1440-prima-schermata.jpg`;
  - `home-390.jpg` e `home-390-prima-schermata.jpg`;
  - `chiusura-1440.jpg`;
  - `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini, controlli e screenshot. Usa `finale_img.py` e `shot_finale.mjs`; `prova_finale.mjs` prova lo scorrimento orizzontale da 320 a 2560, la nitidezza dell'apertura, il selettore con tastiera, tocco e link, il menu, la fisarmonica, i bersagli di tocco e la console.
- `01-analisi.md` raccoglie fatti e fonti, `assets/CREDITI.md` le licenze e l'origine delle foto. I prototipi stanno in `_prova/home/a` (base della finale) e `_prova/home/b`.

## Dati da confermare (non sono in pagina, o ci sono come li dice il sito)

- **Lavori**:
  - Il 1908 come anno d'inizio dell'attività di Rodolfo Belletti. In pagina c'è "Dal 1908 progettiamo…" nel lead e "Storia dal 1908" nel piede, come nel depliant e nelle pagine TOP; il sito dice "nel Novecento".
  - Che Galleria Cavour, Ca' Michiel e Ca' della Nave si possano nominare e siano di Belletti dalla progettazione alla posa. I redazionali scrivono "Installazione: Belletti Srl" per Cavour e "Impianto: Belletti Ascensori" per Martellago e Ca' Michiel.
  - Se l'"ing. A. Viel" dei redazionali è l'AD Andrea Viel. In pagina c'è scritto "ing. Andrea Viel".
  - I nomi dei progettisti (Zambusi, Ziffer, Rigo, Danzi) e la datazione "seconda metà del '600" dell'ala ovest di Ca' della Nave: vengono dai redazionali DiBaio.
  - La grafia: in pagina c'è "Ca’ della Nave", con l'apostrofo come "Ca’ Michiel" e come il testo del redazionale; la scheda tecnica del redazionale scrive "Cà della Nave". Va bene a Belletti?
- **Persone e numeri**:
  - "Trenta addetti" (sito) contro i 31-33 dei registri; "oltre venti tecnici".
  - Le date e i nomi di "Botti e Belletti", "Officine Meccaniche Belletti" e "PBP Elevatori": non sono in pagina.
- **Impianti**:
  - La portata massima dei montacarichi: 24.000 kg sul sito, 12.000 nel depliant. In pagina non c'è nessuna portata dei montacarichi.
  - Se scale mobili e servoscala sono fatti in proprio o con partner, e se il Safety Lift Group esiste ancora.
- **Assistenza**: ogni quanto si fa la manutenzione preventiva? Il sito dice "ogni anno gli impianti vengono sottoposti ad accurati controlli", il depliant "con frequenza variabile in funzione di tecnologia, intensità di servizio…". In pagina non c'è nessuna frequenza.
- **Certificati**: le copie online di ISO 9001 (scaduta il 24/10/2021) ed Eurofins Allegato XI (scaduta il 22/12/2024) vanno aggiornate. In pagina non c'è nessuna certificazione; nel piede c'è il link alla pagina Certificazioni del sito nuovo.
- **Recapiti e dati societari**:
  - Gli orari degli uffici non sono pubblicati, quindi nella chiusura non ci sono.
  - Mancano anche la PEC e la conferma che il capitale sociale di 167.000 € sia versato: per questo il capitale non è nella riga legale.
  - Il fax 049 9003778 serve ancora? Non è in pagina.
- **Social e sponsor**:
  - La pagina Facebook è attiva? Dal nostro client risponde con errore 400, quindi non è nel piede; Seguici ha solo YouTube, verificato.
  - Lo sponsor Pallavolo Padova va nel piede sì o no? Per ora no.
- **Foto**: che `d-027` mostri davvero la sede di Via della Tecnica 29.

## Foto da rifare dal vero, o da chiedere in originale

Tutte le foto in pagina sono di impianti Belletti, prese dai PDF pubblicati sul loro sito: il depliant del 2008 e i redazionali della rivista DiBaio. Il fotografo non è indicato.
1. Prima di tutto vanno chiesti gli originali del fotografo e i diritti d'uso, anche all'editore DiBaio per i redazionali.
2. Le foto sono di 590-950 px. In pagina nessuna è mostrata oltre la sua larghezza reale: l'apertura è a 900 px su 942. A densità 1x sono nitide, sugli schermi 2x restano morbide. Per questo l'area coperta da foto è al 20 % e non al 35 %.

Se gli originali mancano, servono due giorni di fotografia, a luce naturale, almeno 4000 px di lato, in RAW:
- **Apertura, Ca' della Nave dalla corte**: stesso punto di vista di oggi, di mattina con il sole di lato sul muro dell'ala. Obiettivo decentrabile o 24-35 mm a bolla, verticali dritte; l'ala a sinistra e il cilindro poco oltre il centro, senza le panchine in primo piano, in 16:10 per i 900 px della pagina (meglio 1800 px o più). Serve anche uno scatto verticale 4:5 per il telefono.
- **Ca' della Nave, scala a chiocciola dall'alto**: dal pianerottolo più alto, in asse con il cilindro, senza persone.
- **Galleria Cavour di giorno**: volume in vetro e acciaio dalla piazza, con il palazzo dietro; uno scatto anche la sera, come quello del depliant.
- **Ca' Michiel**: la cabina con il mosaico Bisazza dal cortile e dall'alto, con le verticali dritte (oggi la foto del depliant è storta ed è tagliata sulla parte alta della cabina).
- **Sede di Mestrino di sera**: con il furgone dell'assistenza davanti all'ingresso, un po' più da lontano, e la targa coperta o girata.
- **Per il resto del sito**: un tecnico al lavoro in cabina, una cabina finita in officina, i ritratti di Gaetano e Irma Belletti e dell'ing. Viel; i ritratti seppia della famiglia (`storia1-4`) in originale, con i nomi.
- **Villa Pavan (Treviso)**: tolta dalla home perché il colore della stampa CMYK resta falso. Se Belletti ha le foto originali, può tornare come quarto lavoro, con i dati del redazionale XXI Investimenti.

## Licenze

- **Carattere**: Radio Canada, Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina in `sito/fonts/`.
- **Foto**: tutte di Belletti, con i diritti da confermare (sopra). In pagina non c'è nessuna foto di repertorio. Le foto di repertorio scaricate in `assets/esterne/` per i prototipi (licenze Pexels e Unsplash in `assets/CREDITI.md`) non sono usate nella home finale.
- **Logo**: vettoriale vero, estratto dai tracciati della pagina 28 del depliant del 2008 (`assets/originali/logo-belletti-depliant.svg`, script `_prova/script/logo_svg.py`) e confrontato con il PDF a 600 dpi. Rispetto al logo del sito manca solo la "®": da chiedere a Belletti se va aggiunta e il file ufficiale del marchio.

## Pagine del sito nuovo a cui puntano i link del piede

- Azienda: `storia/`, `lavori/`, `certificazioni/`, `contatti/`.
- Impianti: `impianti/ascensori/`, `impianti/panoramici-e-strutture/`, `impianti/montacarichi/`, `impianti/montauto/`, `impianti/piattaforme/`, `impianti/scale-mobili/`.
- Assistenza: `assistenza/manutenzione/`, `assistenza/emergenza-24-ore/`, `assistenza/verifiche/`, `assistenza/servoscala/`.
- Legali: `privacy/`, `cookie/`.
- Il menu in alto porta alle sezioni della home (`#lavori`, `#impianti`, `#assistenza`, `#storia`, `#contatti`). Seguici porta a https://www.youtube.com/@BellettiAscensori.

## Newsletter

Non c'è, e non avrebbe senso: la pagina News è vuota da anni, non ci sono fiere né cataloghi nuovi e i clienti cercano un numero di telefono, non aggiornamenti.

## Segnali da IA, righe da guardare

- **Area foto 20,3 %**: le foto vere sono piccole e non sono state stirate (vedi sopra).
- **Due numeri grandi** ("6" persone e "2" fermate): sono i dati tecnici veri della scheda del lavoro.
