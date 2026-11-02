# Serenissima Service: proposta di nuova homepage

Proposta non richiesta, solo la home. Nessun contatto con l'azienda, niente di pubblicato.

- Pagina finale: `sito/index.html` con `sito/img/` e `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh`.
- Screenshot e nota del progetto: `screenshot/home/` (`NOTA.md`, `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`).
- Analisi con le fonti: `01-analisi.md`. Prototipi: `_prova/home/a/` (scelto) e `_prova/home/b/`.

## Da confermare con l'azienda

In pagina c'è solo quello che dicono le loro pagine o fonti pubbliche; questi punti vanno confermati prima di pubblicare.
- Numeri di `chi-siamo` ancora veri oggi: 9 cabine, 12 ponti, 4 dispositivi di diagnosi, 40 auto sostitutive, fotovoltaico da 100 kWp, 3000 mq.
- ISO 9001: ancora valida, ente (TÜV Nord nel 2016) e numero. In pagina "da oltre dieci anni", dedotto dalla news del decimo anniversario (26/05/2016).
- Albo fornitori della Polizia di Stato 2023-2025 (trovato in un PDF di poliziadistato.it): se vogliono mostrarlo e se è stato rinnovato.
- "Officina Carrozzeria autorizzata FIAT" e centro autorizzato Leasys: ancora attivi? Fuori dalla pagina finché non lo dicono.
- Interno "Carrozzeria" dello 049 760655 per i sinistri: ancora valido.
- Soccorso stradale: numero da chiamare e orari (in pagina il cellulare 335 5639355 del piede di oggi, senza orari promessi).
- "Garanzia a vita" sul levabolli e "riparazione in giornata": li dicono nella pagina grandine; durata e condizioni.
- Smart repair "da 1 a 4 ore", furgoni "fino a 35 quintali", ricambi originali o paralleli: confermare che valgono ancora.
- Elenco aggiornato delle 26 compagnie fiduciarie (in pagina ne nomino sette) e dei noleggi (Ayvens, Alphabet, Athlon, Sifà, Leasys, Volkswagen Lease).
- Il soprannome «Il Socio» e il motto "Botta? Risposta!": se vogliono tenerli. Nome della carrozzeria storica degli anni Sessanta.
- REA, PEC e capitale sociale: non trovati su fonti affidabili (10.000 euro solo da Atoka), quindi non nel piede. Anno di costituzione della srl.
- Il modulo CID punta al PDF già sul loro sito (`wp-content/uploads/2024/02/Modulo_Constatazione_amichevole.pdf`): va spostato nel sito nuovo.
- La pagina Sanificazione anti Covid: tenerla o toglierla (non è nella home).

## Pagine del sito nuovo a cui puntano i link della home

`servizi/carrozzeria/`, `servizi/officina-meccatronica/`, `servizi/centro-cristalli/`, `servizi/grandine-levabolli/`, `servizi/soccorso-stradale/`, `servizi/gestione-sinistri/` (con l'ancora `#compagnie` per le compagnie convenzionate), `servizi/flotte-noleggio-lungo-termine/`, `prenota-il-tagliando/`, `chi-siamo/`, `news/`, `contatti/` (contatti e dove siamo), `privacy-policy/`, `cookie-policy/`. Le voci del menu in testata vanno alle sezioni della home (`#reparti`, `#sinistro`, `#storia`, `#contatti`) e a `prenota-il-tagliando/`. Facebook: https://www.facebook.com/Serenissima-Service-1667868210177791/ (l'unico social trovato).

Newsletter: no, per scelta (nessuna novità periodica, i promemoria vanno legati al veicolo).

## Foto da rifare dal vero

Le foto in pagina sono loro, quasi tutte del servizio del 2015 a 1920 px: reggono a 1440 ma sono morbide sugli schermi 2x e mostrano impianti di undici anni fa. Una mattina in sede, con luce del giorno e il capannone in ordine, a piena risoluzione (3000 px e più sul lato lungo), basta per tutta la home.
- **Apertura (la più importante)**: la stessa cabina vista in asse dalla stessa posizione, obiettivo 24-35 mm, fotocamera a 1,2 m da terra e perfettamente in bolla, porte di fondo chiuse, tutte le lampade accese, con un'auto chiara appena verniciata sul sollevatore. Esposizione per i pannelli chiari, senza bruciarli. È il passo che dà alla prima schermata un oggetto illuminato invece di una stanza vuota.
- Colorimetria: la parete con la scritta "Serenissima Service" in asse, senza il tubo della pistola davanti.
- Officina: dall'alto del soppalco o in asse, con le auto ordinate, senza il pavimento rosso a metà foto.
- Cristalli e levabolli: la ventosa su un parabrezza e la lampada a righe su un'auto chiara, con le mani del tecnico.
- Carro attrezzi di oggi davanti al capannone, senza recapiti personali sulle portiere (su quello del 2015 c'era una mail personale, coperta in post produzione).
- Mani al lavoro sulla lucidatura con guanti senza marchio stampato (sulla foto del 2015 la stampa del guanto è attenuata in post produzione).
- Sede: frontale sull'insegna e sull'ingresso giallo, cielo vero, senza le auto dei clienti con le targhe.
- La squadra, per la pagina Chi siamo.

## Licenze e loghi

- Foto: tutte di Serenissima Service, dalla libreria media pubblica del loro sito (`assets/CREDITI.md`). Uso solo per la proposta; nel sito vero con il loro consenso, chiedendo chi ha i diritti del servizio fotografico 2015. In questa versione non c'è nessuna foto di repertorio (i segnaposto Pexels in `assets/esterne/` non sono usati).
- Carattere: Archivo, SIL Open Font License 1.1 (Google Fonts), servito da `sito/fonts/` con il testo della licenza in `sito/fonts/OFL.txt`.
- Loghi: `logo-2016-03-LOGO-02.png` (piede) e la scritta 2022 (testata), PNG a 2x. Un SVG fedele non è realistico (sagome delle auto e corsivo di "Service"): va chiesto il vettoriale. Il tondo FIAT è un marchio di terzi e non compare. Metron, Iveco, Würth e Festool che si vedono nelle foto sono fornitori, non concorrenti.
