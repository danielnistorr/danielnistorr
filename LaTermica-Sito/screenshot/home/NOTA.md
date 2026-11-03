# La Termica, home finale: nota

Pagina: `sito/index.html` (statica, nessuna libreria). Rigenera tutto: `sh _prova/script/build_finale.sh` (immagini, controlli, screenshot). Altezza: 8734 px a 1440 piede compreso, 12603 px a 390.

Schermate in questa cartella (stessi nomi di prima): `home-1440-prima-schermata.jpg`, `home-1440.jpg`, `home-390-prima-schermata.jpg`, `home-390.jpg`, `chiusura-1440.jpg`. La versione di prima ("Rame sui coppi", Brygada 1918 su carta beige) è conservata com'era in `_prova/versione-1-originale/` (pagina, immagini, caratteri, schermate e la sua nota).

## Livello professionale (3/11/2026)

Richiesta: "secondo me non rappresentano bene l'identità e l'utilizzo corretto di quello che dovrebbe essere il sito" e "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese). Scheda d'identità e d'uso: `_prova/uso/SCHEDA.md`.

Riferimenti guardati: le prime schermate a 1440 di tutti e 14 (foglio `riferimenti.jpg`), le prime schermate a 390 di Kline, Wilson, Klindworth, Dulwich, Eggentaler, Cly-Del e Union, le pagine intere di Kline e Wilson a pezzi. La home segue la struttura di Kline adattata a un magazzino con squadra di posa: testata con il telefono come bottone, apertura con mestiere, luogo, prova e mezzo con il marchio, fascia dei numeri e delle garanzie su fondo scuro, servizi in schede, lavori in schede fotografiche, telefono come titolo grande con il modulo, piede a quattro colonne.

### Che cosa è cambiato rispetto alla versione 1

- **L'identità.** Il titolo "Canne fumarie in rame e inox, su misura" e il rame in apertura spostavano l'azienda su un caso raro (la scheda, par. 7): il logo dice "camini inox" e il grosso del lavoro è inox, stufe, pulizia e banco. Il titolo è ora una loro frase, dallo slider del loro sito: **"Il Super Store della canna fumaria"**, e dentro lo stesso H1 la riga del mestiere "Canne fumarie, stufe, pulizia e video ispezioni. Magazzino a Mestrino." L'occhiello: "Canne fumarie e camini inox · Mestrino (PD) · dal 1978". Il rame resta tra i lavori ("Case e centri storici").
- **L'apertura.** Al posto delle canne in rame scontornate sulla carta, la loro foto del furgone con la livrea "LATERMICA camini inox" davanti a un condominio con due canne inox nuove (`DSC04042`, targa sfocata): mezzo con il marchio e lavoro finito nella stessa foto, cielo vero, nessun ritocco. A 390 lo stesso scatto in 3:2, sotto i bottoni.
- **Colori.** Via la carta #F3EEE7 e il rame #9A4F2C. Rosso del logo e dell'insegna #BF2B37 per i bottoni pieni e la chiusura, giallo del logo #FCB131 solo come trattino delle etichette e per i link sul fondo scuro, grafite #1C1F22 delle lettere "camini inox" per i blocchi scuri, fondo bianco e grigi neutri.
- **Caratteri.** Via Brygada 1918 (il "serif da rivista" che la scheda indica come falso per loro). Resta Host Grotesk, già nella versione 1, unico carattere in pesi 400 e 700.
- **Uso.** Orari a parte (vedi sotto), i compiti della scheda sono tutti a uno o due tocchi: chiamata in testata e in apertura, mappa nella prima schermata, "Cataloghi PDF" porta dritto all'elenco delle 15 serie con i PDF del loro sito, sei schede dei servizi detti come problemi, ognuna porta al modulo con il tipo già scelto, lavori per tipo di cliente con il link alle loro gallerie, "Mandate il disegno" con l'email già scritta, modulo con Ditta, sopralluogo e cosa allegare.
- **Tolti.** Il promemoria newsletter (mai avuto), le linguette "Palazzine / Ville" (nomi inventati dalle foto), il bianco e nero della chiusura, i cieli portati alla carta, l'armadio scontornato, la parola "showroom" al posto di "magazzino".

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito completo in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 320, 390, 768, 1024 e 1440.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa (sticky) alta 88 px a 1440 e 72 a 390, bottone "049 9002522" alto 48 px con la cornetta. A metà pagina, a 390 e a 1440, il bottone si vede e si tocca (`elementFromPoint`). 7 link `tel:`, tutti `tel:+390499002522`. Finché il bottone rosso dell'apertura è in vista, quello della testata è bordato; poi torna rosso pieno.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440 x 900: H1 con "Canne fumarie" e "Mestrino", occhiello con "inox" e "dal 1978", tavola con "Autorizzati dalla camera di commercio, con la certificazione del prodotto e dell'installazione", bottone di chiamata a 474 px, "Magazzino e cataloghi" e "Mandate un disegno" accanto, indirizzo con "Apri la mappa". A 390 x 844: lo stesso, bottone di chiamata largo quanto la colonna (350 px) a 321 px, sotto "Cataloghi PDF" e "Preventivo", indirizzo con la mappa, "In regola", e 139 px della foto.
3. **Immagine vera nell'apertura: passa.** Il furgone La Termica con la livrea e il condominio con le loro canne inox, a 1440 in 4:5 a 515 px (dal 1500 px d'origine, mai ingrandita). Non ci sono persone: la foto della squadra è la prima del LEGGIMI.
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; in `sito/img/` solo foto e logo di La Termica; nessuna foto di `assets/esterne/`.
5. **Foto in serie: passa.** 8 foto a 1440, tutte loro, scattate di giorno con la stessa compatta o lo stesso telefono (2012-2014), cielo vero, stesso trattamento leggero (livelli, saturazione al 94 %, nitidezza); 2 formati a 1440 (4:5 e 4:3) e 2 a 390 (3:2 e 4:3); nessuna didascalia; nessuna ingrandita oltre la misura del file.
6. **Palette dal marchio: passa.** `--rosso` #BF2B37 (logo, insegna, furgone) con `--rosso-scuro` per il passaggio del mouse, `--giallo` #FCB131 (logo), `--grafite` #1C1F22 ("camini inox" del logo); neutri `--bianco`, `--grigio`, `--linea`, `--testo-2`, `--linea-scura`, `--chiaro`. Fondo bianco, nessun beige. Bianco su rosso 5,8:1.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 24, 32, 48, 72, 112) e 7 a 390 (14, 16, 17, 20, 30, 40, 48); testo corrente 19 px a 1440 e 17 a 390; nessun testo sotto i 14 px; H1 72/40, H2 48/30. Tra 761 e 1199 px l'H1 scende a 56.
8. **Due famiglie al massimo: passa.** Una sola, Host Grotesk, pesi 400 e 700.
9. **Servizi in schede con la foto: non passa.** Sei schede in 3 colonne (2 a 1024, 1 sul telefono), tutta la scheda cliccabile, con etichetta loro, problema detto con le parole del cliente, riga e azione; ma senza foto, perché non ci sono foto vere di pulizia, stufe e messa a norma, e il committente non vuole repertorio né disegni. Le schede con la foto vera sono quelle dei lavori (3, tutte 4:5). Le foto da fare per ogni servizio sono nel LEGGIMI.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono 4 numeri aziendali (1978, 500 m², 15 serie con catalogo, servizio a 360°) e tre garanzie scritte con le loro frasi (camera di commercio, prodotto e installazione certificati, D.Lgs. 81/2008). Mancano recensioni (nessuna pubblica leggibile) e clienti con il nome: non sono nelle fonti e non sono stati inventati (LEGGIMI).
11. **Lavori con un nome: non passa.** Tre lavori per tipo (Condomini, Camini autoportanti, Case e centri storici), con foto loro grande e il link alla galleria; mancano luogo, anno e dati di ogni lavoro, che le fonti non danno (LEGGIMI).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: numeri e garanzie in grafite, lavori in grafite, chiusura in rosso; servizi e chi siamo in grigio. Sezioni a 120/120 px a 1440 e 72/72 a 390; margini 80 px a 1440 (contenitore 1280), 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno rosso e bordato (sul rosso: pieno bianco e bordo bianco), raggio 4 px, alti 56 px (48 in testata), testo 17 px (16 sul telefono); i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: non passa per una parte.** Il modulo ha i campi di A6 per la famiglia S: nome, ditta, telefono, email, tipo di richiesta (10 voci, dai pezzi a magazzino all'armadio su misura), comune e indirizzo del lavoro, descrizione o lista dei pezzi, sopralluogo sì/no/non so, quando (subito, entro un mese, senza fretta) e la nota di cosa allegare (un mailto non porta allegati). Nessun iframe di mappa: "Indicazioni stradali" e "Apri la mappa". Manca l'elenco dei comuni serviti: le zone di posa e di spazzacamino non sono nelle fonti (LEGGIMI).
15. **Piede completo: non passa per una parte.** Quattro colonne, testo di almeno 14 px, ragione sociale snc, P.IVA e C.F. 04138980281, indirizzo con la mappa, telefono ed email cliccabili, servizi, magazzino e azienda, "Autorizzati dalla camera di commercio", link all'informativa privacy del loro sito. Mancano gli orari e le zone, non confermati (LEGGIMI).

### Compiti della scheda d'uso (par. 8)

- *Privato, 390*: chiama senza scorrere (bottone 350 x 56 a 321 px, e in testata); legge l'indirizzo, che apre la mappa con un tocco; entro una schermata di scorrimento dopo i numeri trova "Canna da pulire prima dell'inverno" (spazzacamino) e "Stufa, caminetto o caldaia nuova da collegare", e la scheda porta al modulo con il tipo già scelto (provato: "Pulizia e spazzacamino"); in fondo, nella chiusura, la foto della facciata con l'insegna LATERMICA e "Indicazioni stradali". **Non riesce ancora: sapere quando sono aperti.** Gli orari non sono in pagina perché le schede pubbliche non concordano; c'è "Prima di passare al banco, chiamateci". È la prima cosa da chiedere (LEGGIMI).
- *Installatore*: a 1440 telefono in testata e "Magazzino e cataloghi" nella prima schermata; a 390 "Cataloghi PDF" porta all'elenco e la serie pellet è in vista: due tocchi per il PDF (provato). "Al dettaglio e all'ingrosso" in apertura e nel magazzino; "Chiedete disponibilità" apre un'email con oggetto e la traccia (ditta, serie e diametro, pezzi e quantità, ritiro o consegna, telefono).
- *Amministratore o azienda, 1440*: "Guardate i lavori" in apertura, poi le gallerie di condomini e camini autoportanti del loro sito (due clic); "Mandate un disegno" porta al modulo con la nota di cosa allegare, e c'è il mailto diretto con oggetto "Richiesta di preventivo"; la frase su camera di commercio e certificazione nella prima schermata e nella fascia delle garanzie; nel piede la ragione sociale snc con la P.IVA.
- *Identità*: logo vero a colori in testata (e in negativo nel piede); nessuna foto di repertorio; frasi loro in pagina: "Il Super Store della canna fumaria", "Siamo specialisti in materia di canne fumarie", "Qualunque necessità vi si presenti, vi basterà venirci a trovare per trovare subito tutto ciò che vi serve", "Non lasciamo niente al caso", "Noi amiamo ciò che facciamo", "Vi aspettiamo!"; "inox" nella prima schermata.
- Modulo provato: invio vuoto fermato con l'avviso a 17 px e il fuoco sul nome; compilato, compone l'email "Richiesta dal sito: Pulizia e spazzacamino, Prova snc" con tutti i campi, senza inviarla.

### Caratteri e licenze

- **Host Grotesk** (Element Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero, anche servito dal proprio sito. File in `sito/fonts/` (`host-grotesk-latin.woff2`, `host-grotesk-latin-ext.woff2`, variabile 300-800, usati 400 e 700) e licenza in `sito/fonts/OFL.txt`.
- Foto: solo materiale di La Termica dal loro sito (`assets/originali/sito/`) e il logo, da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

| File in `sito/img/` | Origine | Uso |
|---|---|---|
| `apertura-560`, `apertura-1040`, `apertura-tel-780` | `lavori-ultimati__2014-06-DSC04042.jpg` (furgone e condominio) | apertura, 4:5 e 3:2 sul telefono; targa sfocata |
| `lav-condominio-*` | `lavori-ultimati__2014-06-DSC03569.jpg` | lavori, Condomini |
| `lav-autoportante-*` | `camini-autoportanti__2014-06-DSC03636.jpg` | lavori, Camini autoportanti |
| `lav-rame-*` | `lavori-ultimati__2014-06-CAM00223.jpg` | lavori, Case e centri storici |
| `videoispezione-*` | `camini-autoportanti__2014-06-Immagine-077.jpg` | servizi (da 761 px in su) |
| `magazzino-*` | `magazzino__2014-06-DSC04701.jpg` | magazzino |
| `armadio-*` | `armadi__2014-06-DSC01936.jpg` | su misura |
| `sede-*` | `la-nostra-sede__2014-05-DSC01925.jpg` (1200 px) | dove siamo, al massimo 600 px |
| `logo-480.png`, `logo-640.png`, `logo-negativo-640.png` | `logo-completo-3000x938.jpg` | testata; piede scuro con "camini inox" in bianco |

### Controlli fatti

- `pro_controlli.mjs`: regole 1-8, 12 e 13 superate nelle misure; 9, 10, 11, 14 e 15 no o solo in parte (vedi sopra). Nessuna ancora senza destinazione, nessun errore di script.
- Nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione tra logo, bottoni della testata, titolo, bottoni, tavola e foto dell'apertura. A 320 e 360 la testata stringe logo e margini (16 px) perché telefono e Menu stiano sulla riga.
- Collegamenti: `tel:+390499002522` (7), 5 `mailto:info@latermicacamini.com` con oggetto (disponibilità, disegno su misura, informazioni, preventivo) più quello composto dal modulo, mappe Google `maps/search` e `maps/dir` su "La Termica, Via Bologna 6, 35035 Mestrino PD", 15 PDF del loro sito (URL letti dalla pagina Prodotti il 3/11/2026), gallerie del loro sito.
- Menu a 390 aperto e chiuso dopo il clic, ancora "Magazzino e cataloghi" a 88 px, sotto la testata.
- Screenshot guardati a pezzi a 1440 e 390 (pagine intere e prime schermate), a 320, 768 e 1024 (prime schermate e pagine intere), la chiusura a 1440.
- Nessun carattere U+2014 in pagina, nei .md e negli script.
- Nessun dato inventato: ogni fatto viene da `01-analisi.md` o dalla scheda; orari, zone, marchi delle stufe, abilitazioni precise e lavori con luogo e anno sono nel LEGGIMI tra le cose da chiedere.
