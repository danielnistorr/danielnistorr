# Serenissima Service: proposta di nuova homepage

Proposta non richiesta, solo la home. Nessun contatto con l'azienda, niente di pubblicato.

- Pagina finale (livello professionale con il ritocco finale, 3/11/2026: apertura con la foto a tutta altezza e la fascia verde dei percorsi, telefono a 96 px in chiusura, fascia delle prove sotto i numeri): `sito/index.html` con `sito/img/` e `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh`.
- Screenshot e nota: `screenshot/home/` (`NOTA.md` con l'esito delle 15 regole, `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`).
- Versione precedente com'era: `_prova/versione-1-originale/`. Scheda d'uso: `_prova/uso/SCHEDA.md`. Analisi con le fonti: `01-analisi.md`.
- Controlli: `node _prova/script/pro_controlli.mjs` (regole, compiti, orari, larghezze, collegamenti; esito in `_prova/pro_controlli.json`). Viste della finestra: `_prova/script/pro_viste.mjs`.

## Il modulo va collegato

Il modulo "Prenota il tagliando" oggi non invia nulla: controlla nome, telefono e targa e compone un'email a info@serenissimaservice.it con oggetto ("Prenotazione: Tagliando, targa AB123CD") e tutti i campi, che si apre nel programma di posta di chi scrive. Nel sito vero va collegato a un servizio (Contact Form 7 come oggi, oppure un servizio di moduli) che riceva gli stessi campi, permetta di allegare le foto del danno (un campo "Foto del danno" nel modulo: oggi con il `mailto` non si può, quindi c'è solo l'istruzione di allegarle all'email), controlli l'indirizzo quando si chiede il ritiro (come fa già la pagina) e mandi la risposta "ti confermiamo via email o telefono". Serve anche la riga sul trattamento dei dati con il link alla privacy, come nel modulo di oggi.

## Da chiedere o confermare con l'azienda

In pagina c'è solo quello che dicono le loro pagine o fonti pubbliche; questi punti vanno confermati prima di pubblicare.
1. **Soccorso stradale**: il numero da chiamare (in pagina il cellulare 335 5639355 del piede di oggi; sul carro del 2015 c'è lo 049 760655) e gli orari (non promessi in pagina).
2. **Interno "Carrozzeria"** dello 049 760655 per i sinistri: ancora valido.
3. **Orari**: chiusure per il patrono (13 giugno) e chiusure estive o di fine anno. Lo stato "Aperto ora" tiene conto solo dei festivi nazionali e di Pasquetta.
4. **Compagnie fiduciarie**: in pagina le 26 della loro pagina sinistri più Vittoria Assicurazioni (news del 22/02/2024), 27 nomi; il numero 27 ora è nel titolo, nella fascia delle prove e nel collegamento sotto il CID, quindi va aggiornato insieme all'elenco. Elenco aggiornato e nomi giusti di oggi (alcuni marchi, come Amissima, Credit Ras e Cariparma, potrebbero avere cambiato nome o non esistere più).
5. **Noleggi**: link e scadenze di Ayvens, Alphabet, Athlon, Sifà, Leasys e Volkswagen Lease (presi dalla loro pagina flotte del 3/11/2026). Provati il 3/11/2026: Ayvens e Athlon rispondono; Alphabet rimanda a `area-drivers-gestione-sinistri-e-furti.html` (già messo); **sifa.it rimanda a unipolrental.it**: chiedere se Sifà è ora Unipol Rental e quale numero e pagina indicare; i due Leasys (`http://www.leasysdenunciasinistri.com/...`, ancora in `http`) e Volkswagen Lease non hanno risposto dalla prova: verificarli dal vivo prima di pubblicare. Il PDF DEN001 di Leasys e quello di Alphabet sono quelli del loro sito (`wp-content/uploads/2018/05/den001_LEASYS.pdf`, `2016/11/ALPHABET_...pdf`). Le etichette "Entro 3 giorni" (Alphabet, Leasys) e "Subito, 8-19" (Sifà) vengono dalla stessa pagina. Se sono ancora **centro autorizzato Leasys** (news 2018): un cliente tipo lo chiede in testa alla sezione noleggi ("Centro autorizzato Leasys dal 2018"), ma non è in pagina finché non lo confermano.
6. **Numeri di `chi-siamo`** ancora veri: 3000 mq, 9 cabine, 12 ponti, 40 auto sostitutive (il sito dice anche "oltre 40"), fotovoltaico da 100 kWp, anno 1993.
7. **ISO 9001**: ancora valida, ente (TÜV Nord nel 2016), anno (la news del 2016 sul decimo anniversario fa pensare al 2006, non scritto in pagina) e numero. Oggi è nella fascia delle prove sotto i numeri, con la sola didascalia: con la conferma si aggiungono ente, anno, il marchio dell'ente in un colore e il certificato in PDF.
8. **Albo fornitori della Polizia di Stato** 2023-2025 (trovato in un PDF di poliziadistato.it): rinnovato per il 2026 e se vogliono mostrarlo.
9. **Recensioni**: la quarta prova della regola 10. Chiedere il permesso di citare 3-6 recensioni Google vere con nome, comune e data (il "4,5 su 370" di Cylex non è verificato e non è in pagina). Dove vanno: tra "Tutto nella stessa sede" e "Prenota il tagliando", tre schede in tre colonne su grigio chiaro con testo, nome, comune, data e fonte Google.
10. **Lavori con un nome** (regola 11, l'unica che non passa): almeno tre lavori recenti con tipo di auto o cliente (se lo permette), anno e due o tre dati (per esempio "grandinata di giugno 2025, 14 auto di una flotta, riconsegnate in 6 giorni"; l'esempio è inventato e serve solo a far capire che cosa chiedere), con una foto larga. Dove vanno: dopo le recensioni, tre schede con una foto 2:1 larga otto colonne e tre dati.
11. **Zone servite** (regole 14 e 15): i comuni dove arriva il carro attrezzi e dove fanno ritiro e consegna a domicilio. In pagina non c'è nessun elenco perché nessuna fonte lo dice. Dove va: un elenco in quattro colonne nella chiusura "Chiamaci o passa in sede" e una colonna "Zone" nel piede.
12. **Garanzie**: "garanzia a vita" sul levabolli e "riparazione in giornata" (pagina grandine), "garanzia sulle riparazioni" (durata), smart repair "da 1 a 4 ore", furgoni "fino a 35 quintali", ricambi originali o paralleli.
13. **Ferrari 488 del 2018**: è l'auto di un cliente; in pagina è solo nominata in "Chi siamo", senza foto. Se il cliente e l'azienda sono d'accordo si può mostrare come lavoro con nome.
14. **Revisioni**: il cartello "egroup / Consorzio Zambelli Revisioni" è davanti alla sede nella foto del 2015 (ora tagliato fuori dall'apertura; resta piccolo nella foto della facciata e la scritta "revisioni" sulla fiancata del carro); se le fanno ancora, diventano una scheda di servizio. "Gommista" compare solo nella meta description di oggi: non dichiarato.
15. **Il motto "Botta? Risposta!"** resta nel logo ed è scritto in una riga sopra il titolo; il titolo è "Pensiamo a tutto noi" (loro frase). Il soprannome «Il Socio» e il nome della carrozzeria storica degli anni Sessanta.
16. **Moduli PDF**: il CID e il modulo Alphabet puntano ai PDF già sul loro sito (`wp-content/uploads/...`): vanno spostati nel sito nuovo.
17. **Stato "Sede aperta ora"**: vale per la sede; se il soccorso stradale risponde anche fuori orario (la loro pagina dice "a qualsiasi ora del giorno e della notte" senza numero), dirlo accanto al bottone del soccorso solo dopo la conferma.
18. REA, PEC e capitale sociale: non trovati su fonti affidabili, quindi non nel piede. La pagina Sanificazione anti Covid: tenerla o toglierla (non è nella home).

## Pagine del sito nuovo a cui puntano i link della home

`servizi/carrozzeria/` (con l'ancora `#verniciatura`), `servizi/officina-meccatronica/`, `servizi/centro-cristalli/`, `servizi/grandine-levabolli/`, `servizi/soccorso-stradale/`, `servizi/gestione-sinistri/`, `servizi/flotte-noleggio-lungo-termine/`, `privacy-policy/`, `cookie-policy/`. Le voci del menu vanno alle sezioni della home (`#incidente`, `#compagnie`, `#noleggio`, `#servizi`, `#tagliando`, `#chi-siamo`, `#dove`). Facebook: https://www.facebook.com/Serenissima-Service-1667868210177791/ (l'unico social trovato). Newsletter: no (nessuna novità periodica; i promemoria vanno legati al veicolo).

## Foto da rifare dal vero

Tutte le foto della home sono loro, ma vengono da tre momenti (servizio Nikon del 2015 a 1920 px, iPhone 2018, levabolli 2019): reggono a 1x, sugli schermi 2x sono morbide e mostrano impianti di undici anni fa. Una mattina in sede, con luce del giorno e il capannone in ordine, un solo fotografo, a piena risoluzione (4000 px e più sul lato lungo), basta per tutta la home. Formati: 4:3 e 2:1 come in pagina, più un verticale (circa 7:8) per l'apertura a 1440, che riempie a tutta altezza la metà destra.
- **Apertura (la più importante)**: il carro attrezzi di oggi davanti all'ingresso con l'insegna verde intera e nessun cartello di terzi davanti, con il titolare o due persone della squadra in divisa accanto (che guardano il lavoro o l'obiettivo, non in posa rigida), 4:3, a 1,5 m da terra, sole alle spalle del fotografo. Niente recapiti personali sulle portiere (su quello del 2015 c'era una mail personale, coperta in post produzione).
- **Le sei schede, 4:3, stessa luce**: carrozziere al lavoro su un'auto senza marchio riconoscibile in primo piano; una cabina con un'auto appena verniciata; l'officina dall'alto del soppalco con i ponti occupati, senza il pavimento rosso a metà foto; la ventosa su un parabrezza con le mani del tecnico; la lampada a righe del levabolli su un'auto chiara; il carro "Il Socio" in uscita.
- **Facciata (2:1)**: frontale sull'insegna e sull'ingresso giallo, cielo vero, senza le auto dei clienti con le targhe.
- **Accettazione e squadra**: il banco accettazione con chi risponde al telefono, e un ritratto della squadra per "Chi siamo" (regola A1: squadra con nome, anni di mestiere e ruolo; nomi da chiedere).
- **Tre lavori** per la regola 11: prima e dopo, stessa inquadratura.

## Licenze e loghi

- Foto: tutte di Serenissima Service, dalla libreria media pubblica del loro sito (`assets/CREDITI.md`). Uso solo per la proposta; nel sito vero con il loro consenso, chiedendo chi ha i diritti del servizio fotografico 2015. Nessuna foto di repertorio in pagina (i segnaposto Pexels di `assets/esterne/` non sono usati).
- Carattere: Archivo, SIL Open Font License 1.1 (Google Fonts), servito da `sito/fonts/` con il testo della licenza in `sito/fonts/OFL.txt`.
- Logo: `logo-2016-03-LOGO-02.png` (testata e piede), PNG a 1x, 2x e 3x. Un SVG fedele non è realistico (sagome delle auto e corsivo di "Service"): va chiesto il vettoriale. Il tondo FIAT è un marchio di terzi e non compare se non sull'edificio nella foto.
