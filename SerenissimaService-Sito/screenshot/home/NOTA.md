# Serenissima Service, home: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `_prova/script/index.html`, screenshot). La versione precedente (apertura "Botta? Risposta!" con la Ferrari 488) è copiata com'era in `_prova/versione-1-originale/` (pagina, immagini e la sua nota).

Altezza: 9959 px a 1440, 14606 px a 390.

## Livello professionale, ritocco finale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessun repertorio, nessun disegno). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese). Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di Kline e Dulwich Diggers a pezzi (prima anche Kline e Wilson). Scheda d'uso: `_prova/uso/SCHEDA.md`. Il ritocco parte dal giudizio del controllore (voto 6, dieci difetti) e dalle prove dei due clienti tipo (voti 7,5 e 8).

### Che cosa è cambiato in questo ritocco

- **Apertura con un tratto proprio.** La foto della sede con il carro attrezzi arriva fino al bordo destro e copre tutta l'altezza dell'apertura (niente più riquadro arrotondato a destra del titolo). Sotto, i quattro percorsi stanno su una **fascia piena verde del logo**, in bianco: il colore del marchio è nella prima schermata a 1440 e a 390. La fascia delle garanzie, subito sotto, è passata su grigio chiaro per non avere due verdi di fila.
- **Foto d'apertura ritagliata di nuovo** (`pro_img.py`): solo la parte sinistra dell'originale, così il cartello di terzi "egroup / Consorzio Zambelli Revisioni" (servizio non confermato) resta fuori campo; via anche la fascia alta di cielo. Restano l'insegna "SERENISSIMA, officina e carrozzeria" e il carro blu "Soccorso stradale Serenissima Service" con "Il Socio" sulla cabina.
- **Il motto come testo**: "Botta? Risposta!" in verde, della misura di una riga, sopra il titolo (nel logo a 390 non si leggeva). Logo più grande: 76 px di altezza a 1440 (testata di 100 px), 56 px a 390 (testata di 76 px); a 390 il bottone della testata mostra solo il numero, come la pillola di Wilson.
- **Gesto di scala**: il telefono della chiusura è a 96 px a 1440 (80 a 1240, 72 a 900, 56 a 390), su una riga sua sopra le due colonne.
- **Prove in alto**: sotto i numeri, una fascia bianca con didascalia: "Certificazione ISO 9001, sistema di gestione per la qualità"; "Albo fornitori della Polizia di Stato, nel triennio 2023-2025"; "Carrozzeria fiduciaria di 27 compagnie, e punto di riparazione per sei società di noleggio". In "Chi siamo" le stesse prove sono state sostituite dalle loro date (anni Sessanta, 1993, 2001, 2018, 2023-2025), così non si ripetono.
- **Sinistro e compagnie**: "Non anticipi nulla" come titolo della prima garanzia, con la loro frase "Il cliente non dovrà anticipare nulla" nel testo (la lead dell'apertura non la ripete più). Sotto il CID il collegamento "La tua compagnia è convenzionata? Vedi le 27 compagnie"; titolo "Le 27 compagnie fiduciarie"; voce "Compagnie" nel menu ("Chi siamo" resta nel menu del telefono). Grandine, smart repair e parabrezza sono dopo l'elenco delle compagnie, con il titolo "Grandine, piccoli danni e cristalli".
- **Noleggi**: Alphabet e Leasys hanno due bottoni uguali (senza controparte, con controparte) al posto della scheda tutta cliccabile, e Leasys anche il PDF DEN001; l'etichetta "Entro 3 giorni" accanto al nome di Alphabet e Leasys, "Subito, 8-19" per Sifà, con il bottone "Chiama Sifà 800 037631". I quattro passi di Serenissima dopo la denuncia stanno prima delle schede (a 1440 e a 768 in colonne; sul telefono riassunti in una riga del testo d'apertura, così Alphabet resta in vista dopo il salto).
- **Stato**: "Sede aperta ora" / "Sede chiusa ora", così non sembra valere per il soccorso stradale.
- **Prima schermata del telefono**: "Indicazioni: Corso Stati Uniti 19" (si sa dove porta prima di toccare).
- **Chiusura**: un solo bottone "Indicazioni stradali (Google Maps)"; l'indirizzo è testo. Etichette di sezione in minuscolo, in grassetto (niente maiuscolo spaziato nei titoli).
- **Modulo**: se si chiede il ritiro a domicilio, l'indirizzo è obbligatorio (avviso e fuoco sul campo).
- **Minori**: a 390 "3000 mq" a tutta larghezza e le altre quattro cifre in 2x2; la scheda del soccorso dice "Soccorso stradale a disposizione, con il nostro carro attrezzi" (la loro frase, senza la parafrasi di prima); Alphabet punta all'indirizzo nuovo della pagina (`...-e-furti.html`, il vecchio rimanda lì).

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito completo in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440 e 390 e le pagine intere a 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata `sticky` di 100 px a 1440 e 76 a 390; bottone pieno alto 48 px ("Chiama 049 760655" a 1440, "049 760655" a 390), visibile e toccabile a metà pagina (`elementFromPoint`). 12 link `tel:`.
2. **Mestiere, luogo, prova e azione: passa.** H1 "Pensiamo a tutto noi / Carrozzeria, officina e soccorso stradale a Padova, dal 1993"; stato "Sede aperta ora, fino alle 12"; "Chiama 049 760655" a 553 px a 1440 e a 279 px a 390, a tutta larghezza (350 px). I quattro percorsi sono interi nella prima schermata a 1440 (fascia verde fino a 894 px) e a 390 (fino a 839 px).
3. **Immagine vera nell'apertura: passa.** Sede con insegna e carro attrezzi con la livrea, 708 x 600 a 1440 (a tutta altezza, fino al bordo), 390 x 195 a 390; il cartello delle revisioni è fuori campo.
4. **Zero repertorio: passa.** `indicativ` 0 volte; 0 svg, nessun `background-image`; in `sito/img/` solo foto e logo dell'azienda; i segnaposto Pexels di `assets/esterne/` non sono usati.
5. **Foto in serie: passa, con riserva.** Stesso trattamento per tutte (`pro_img.py`); tre formati a vista: apertura circa 8:7 a 1440 (1,15), 4:3 delle sei schede, 2:1 (apertura a 390 e facciata); una didascalia su otto foto; nessuna foto ingrandita. Riserva: scatti del 2015, 2018 e 2019, non un solo servizio (LEGGIMI).
6. **Palette dal marchio: passa.** `--verde` #076633 (logo e insegna), `--verde-scuro` (passaggio del mouse), `--blu` #16306E (il carro), neutri freddi. Fondo bianco, nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 64, 96) e 8 a 390 (14, 17, 19, 20, 26, 32, 40, 56); testo corrente 19/17 px; nulla sotto i 14 px; H1 64/32, H2 48/26; il telefono a 96 px è il gesto fuori scala.
8. **Due famiglie al massimo: passa.** Una sola, Archivo, pesi 400 e 700.
9. **Servizi in schede con la foto: passa.** Sei schede in tre colonne, tutte 4:3, nome, riga e link; tutta la scheda è il link; a 390 righe con la miniatura.
10. **Almeno tre tipi di prova: passa (3 su 4).** Cinque numeri della sede; fascia di certificazioni con didascalia (ISO 9001, albo fornitori della Polizia di Stato 2023-2025, fiduciaria di 27 compagnie), senza loghi; compagnie e noleggi per nome. Mancano le recensioni: nessuna fonte verificata (LEGGIMI).
11. **Lavori con un nome: non passa.** Nelle fonti c'è un solo lavoro con anno (la Ferrari 488 del 2018, ora nelle date di "Chi siamo"), senza dati e senza foto. Servono tre lavori con luogo, anno e dati (LEGGIMI).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: fascia verde dei percorsi nell'apertura, noleggi su blu, chiusura su verde; garanzie, compagnie e tagliando su grigio chiaro, alternati al bianco. Sezioni a 120 px a 1440 e 72 a 390; margini 80 a 1440 e 20 a 390. Nessuno scorrimento orizzontale da 320 a 1920.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 4 px, 56 px (48 in testata e dentro le schede dei noleggi), testo 17 px; i bottoni di chiamata contengono il numero (anche "Chiama Sifà 800 037631").
14. **Modulo e "dove" per il mestiere: passa in parte.** Tipo di cliente, che cosa serve (9 voci), urgenza, ritiro con l'indirizzo (ora obbligatorio se richiesto), note con l'istruzione per allegare le foto; compone l'email a info@ con oggetto. Nessun iframe. Non c'è un campo foto (un `mailto` non porta allegati: va con il servizio vero, LEGGIMI) e manca l'elenco dei comuni serviti, che nessuna fonte dà.
15. **Piede completo: passa.** Quattro colonne a 1440, ragione sociale, P.IVA e C.F., indirizzo, telefoni ed email cliccabili, mappa, orari, servizi, ISO 9001, Privacy e Cookie, Facebook con il sottotitolo; testo di almeno 14 px. Zone servite: solo la sede (vedi 14).

### Compiti della scheda d'uso (par. 8)

- *Botta, telefono*: chiamata e soccorso con un tocco nella prima schermata, interno Carrozzeria scritto sotto il bottone, "Sede aperta/chiusa ora" sull'ora di Roma (prove: lunedì 9, mercoledì 13, venerdì 18.30, sabato 11 e 15, 8 dicembre, Pasquetta, tutte giuste). "Non anticipi nulla" e auto sostitutiva uno scorrimento sotto. Compagnie: 27 nomi, ricercabili, raggiungibili dal menu ("Compagnie") o dal collegamento sotto il CID. CID con un tocco da "Ho avuto un incidente". Grandine e cristalli con i tempi, subito dopo le compagnie.
- *Noleggio, telefono*: "Auto a noleggio: denuncia il danno" nella prima schermata; dopo il tocco Ayvens e Alphabet sono in vista (Alphabet a 627 px con l'etichetta "Entro 3 giorni"); il secondo tocco apre il modulo giusto. Per Leasys due bottoni uguali, con e senza controparte, più il PDF DEN001. Indicazioni con un tocco dalla prima schermata.
- *Tagliando, computer*: "Prenota il tagliando" nella prima schermata; un clic porta al modulo; orari in tabella accanto al modulo e nella chiusura.
- *Identità*: logo più grande e motto scritto sopra il titolo; la loro sede e il loro carro nell'apertura; frasi loro, a tu, senza maiuscolo urlato.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; testo della licenza in `sito/fonts/OFL.txt`. Servito dalla pagina (`sito/fonts/archivo-latin.woff2`, `archivo-latin-ext.woff2`), nessuna chiamata a Google.
- Foto: solo materiale del loro sito (`assets/CREDITI.md`), da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1-10 e 12-15 superate nelle misure (14 e 15 senza elenco dei comuni), 11 no. Il controllo della regola 10 ora verifica la fascia delle prove; quello della 13 accetta anche il numero di Sifà. Nessuna ancora senza destinazione, nessun errore di script.
- Prove con il browser (390, tocchi veri): salto a "Noleggio" con Alphabet in vista; modulo con il ritiro chiesto e l'indirizzo vuoto fermato con l'avviso e il fuoco su "Indirizzo per il ritiro"; invio vuoto fermato sul nome; email composta e letta senza inviarla; menu del telefono con 7 voci che si chiude dopo il clic.
- Larghezze 320, 360, 390, 768, 1024, 1280, 1440, 1920: nessuno scorrimento orizzontale, nessuna sovrapposizione nell'apertura. Pagine intere a 320, 768 e 1024 guardate a pezzi.
- Collegamenti dei noleggi provati il 3/11/2026: Ayvens (nemo.aldautomotive.it) e Athlon rispondono; Alphabet rimanda all'indirizzo con `.html`, già messo; Sifà rimanda a unipolrental.it; Leasys (leasysdenunciasinistri.com) e Volkswagen Lease non hanno risposto dalla prova (LEGGIMI, punto 5).
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, in CREDITI e negli script.
