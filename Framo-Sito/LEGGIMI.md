# F.R.A.M.O. S.r.l.: proposta di nuova home

Proposta non richiesta, solo la home. Nessun contatto con l'azienda, nulla pubblicato.

- Home: `sito/index.html` con `sito/img/` e `sito/fonts/`. Screenshot e nota in `screenshot/home/` (`NOTA.md`, sezione "Livello professionale").
- Rifare tutto: `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot). Controlli: `node _prova/script/pro_controlli.mjs`.
- Versione di prima (tavola tecnica con il calibro): `_prova/versione-1-originale/`. Analisi con le fonti: `01-analisi.md`. Scheda d'uso: `_prova/uso/SCHEDA.md`.

## Da collegare prima di pubblicare

- **Modulo "Scrivici che cosa ti serve"**: oggi compone un'email (mailto a commerciale@framosrl.com con oggetto e campi) e la apre nel programma di posta di chi scrive; non invia nulla da solo e non porta allegati. Va collegato a un servizio di invio (il modulo del sito nuovo, per esempio Contact Form 7 o un servizio di form con allegati per le foto e i disegni), con la casella di consenso privacy e la pagina di ringraziamento (oggi `/richiesta-inviata/`).
- **Google Maps**: "Apri la navigazione" cerca "FRAMO srl - Oleodinamica, Via Liguria 32, 35020 Saonara PD"; "La scheda F.R.A.M.O. su Google Maps" apre la scheda con il suo identificativo (`https://maps.google.com/?cid=4249055688706121423`, ricavato dalla mappa incorporata nel loro sito del 2020, `0x3af7ada2ec2e5ecf`). Da verificare che apra ancora la scheda giusta; per la navigazione si può aggiungere `destination_place_id` con il Place ID della scheda.
- **Ferie e chiusure**: nello script della pagina c'è l'elenco `CHIUSURE` (vuoto). Con le date dell'azienda (una coppia per periodo, per esempio `['2027-08-09','2027-08-20']`) lo stato dice "Chiuso per ferie, riapre lunedì 23 agosto alle 8.30".
- **Link interni**: usano gli indirizzi delle pagine del sito di oggi (`/catalogo/manuli/`, `/prodotti/oleodinamica/distributori-walvoil/`, le pagine per zona come `/tubazioni-oleodinamiche-monselice-ed-este/`, i PDF in `/wp-content/uploads/...`). Se il sito nuovo cambia gli indirizzi, vanno aggiornati qui o reindirizzati. `/prodotti/oleodinamica/accessori` oggi risponde 404 e non è usato. Waircom non ha una pagina sua: il link va a `/prodotti/pneumatica/`.

## Da chiedere all'azienda

1. **Privati** (in pagina, da confermare): la home scrive "Anche se sei un privato, con lo spaccalegna, il trattorino o il rimorchio: porta il tubo o manda le foto, ti diciamo noi che cosa serve", dalla scelta "Privato" del loro modulo. Se non servono i privati, togliere la riga `.privati` e la nota "(se sei un privato, lascia vuoto)" nel modulo.
2. **Certificazione ISO 9001:2015** (RINA 44143/23/S, IQNet IT-146659): il PDF sul sito scadeva il 22.06.2026. Per questo il piede non ha più i link "Certificazioni" e "Politica per la qualità" (PDF del 05.12.2022). Con il rinnovo: "ISO 9001, certificato n. ..., valido fino al ..." nella fascia dei numeri con il PDF, e i due link di nuovo nel piede.
3. **Recensioni**: la scheda Google dà 4,8 su 11. Se si possono citare, con due o tre testi veri (nome e comune del cliente), servono per la regola delle prove; i testi non si leggono senza accesso.
4. **Lavori con un nome**: tre lavori fatti (cliente o luogo, anno, due-tre dati: per esempio tubi per un costruttore di macchine, una centralina, un intervento urgente in campo) con una foto larga. Oggi la home non ne ha.
5. **Clienti con il nome** che si possono citare (costruttori, officine, contoterzisti) e i marchi di cui sono rivenditori autorizzati oltre ad AMI.
6. **Tempi del servizio da campione**: il sito dice "in breve tempo". Se c'è un tempo vero (in giornata, in un'ora) va nella sezione "Vieni in azienda con il campione".
7. **Orari**: patrono, ferie estive, ponti e chiusure di Natale (lo stato "Aperto ora" oggi conosce solo i festivi nazionali e Pasquetta).
8. **Squadra e titolare**: nomi, ruoli e anni di mestiere di chi sta al banco e di chi risponde al telefono e su WhatsApp (la struttura S prevede una sezione squadra; oggi non c'è perché mancano nomi e foto).
9. **Uscite**: se fanno interventi fuori sede (in campo, in cantiere): se sì, il modulo deve chiedere anche l'indirizzo della macchina.
10. Dati legali: REA PD 200928, dipendenti e fatturato vengono da companyreports.it e non dalla visura (non in pagina); capitale sociale e PEC non trovati; CAP 35020 (sito) o 35022 (certificato RINA), in pagina 35020; email su dominio .com con sito .it: quale tenere.
11. Se FOR, NUMATICS, Cast, Donaldson, MP, Emmegi e Stopflex sono ancora distribuiti (non messi nella griglia dei marchi, che tiene i 16 della scheda).
12. Chi ha scattato IMG-9594 e IMG-9596 (il prima e dopo in pagina) e se esistono gli originali più grandi (oggi 1024 px).
13. **Foto della sede** (`azienda-01` e `azienda-02` del loro sito): portano la filigrana "© 2018 Google", sono catture di Google Street View. Non sono in pagina; vanno tolte anche dal sito di oggi o sostituite (foto 2 qui sotto).
14. **Centraline**: una foto di una centralina loro e tre dati tipici (pressioni, potenze, componenti montati), solo se confermati: oggi la home dice solo "progettiamo e assembliamo".
15. **Loghi** in vettoriale dei marchi distribuiti (almeno AMI, Manuli, Walvoil, Danfoss), con il permesso d'uso: oggi i marchi sono scritti, non disegnati.
16. **Il conteggio "16 marchi"** della fascia dei numeri è quello della griglia (i 16 della scheda d'uso): se ne trattano di più (vedi punto 11), aggiornarlo.

## Foto da fare dal vero (mezza giornata in via Liguria 32)

Il committente ha deciso: niente foto di repertorio e niente disegni. In pagina oggi c'è solo il prima e dopo (IMG-9594 e IMG-9596). Tolte nel ritocco: la macro IMG-9592 (la scritta più grande è il marchio TEXMASTER, ed è un SAE 100R6 a bassa pressione) e la sede azienda-01 (cattura di Street View). L'apertura oggi è un blocco tipografico giallo con 3/16" e 3"; i servizi hanno copertine tipografiche. Un solo fotografo, una sola luce, un formato (3:2), almeno 3000 px di lato lungo:

1. **Apertura**: il banco con la pressa raccordatrice e una persona di F.R.A.M.O. al lavoro su un tubo ad alta pressione a due trecce, luce di giorno dalla porta dell'officina, la persona guarda il pezzo. Va al posto del blocco giallo (o accanto, con il blocco più stretto).
2. **La sede**, fatta da loro di giorno con il cielo pulito, dal marciapiede di fronte al cancello: palazzina, fascia gialla e blu, numero 32, insegna. 3:2. Va nella sezione "Dove siamo", a sinistra della tabella degli orari: serve a riconoscere il posto.
3. **Da campione**: la coppia "tubo vecchio portato dal cliente / tubo nuovo rifatto", stesso fondo e stessa luce, al posto del Push Lock (che il loro articolo dà "fino a 16 BAR" e non è la specialità).
4. **Una foto per ogni servizio**, per le sei schede di "Che cosa facciamo" (regola 9), nell'area 3:2 della copertina: tubi su misura, tubo da campione al banco, magazzino di 600 mq (scaffali e bobine), centraline assemblate, pneumatica, sollevamento (funi e brache).
5. **La squadra** davanti alla sede o al banco, con i nomi (per la sezione squadra).
6. Un tubo fatto da loro montato su una macchina di un cliente (agricola o da cantiere), se il cliente lo permette: per i lavori con un nome.

## Pagine che il sito nuovo deve avere (link della home)

Catalogo e schede (`/catalogo/`, `/catalogo/manuli/`, `/catalogo/balflex/`, `/catalogo/zec/`), prodotti (`/prodotti/oleodinamica/` e le pagine di marca, `/prodotti/oleodinamica/centraline/`, `/prodotti/oleodinamica/tubazioni/`, `/prodotti/oleodinamica/raccordi/`, `/prodotti/pneumatica/`, `/prodotti/sollevamento/`, `/brochure-prodotti/`), settori (`/agricoltura/`, `/edilizia/`, `/industria/`), zone (`/oleodinamica-padova/` e le pagine "tubazioni-oleodinamiche-..." per zona), guida `/come-misurare-un-tubo-oleodinamico/`, `/azienda/`, `/azienda/certificazioni/`, `/news/`, i PDF della politica qualità e delle condizioni di fornitura, `/termini-duso-e-informative/` e l'informativa privacy.

Niente newsletter e niente social (non esistono; c'è solo WhatsApp Business sul fisso).

## Licenze

- Caratteri: Anybody (Etcetera Type Co.) per titoli e cifre e Barlow (The Barlow Project) per testo e interfaccia, Google Fonts, SIL Open Font License 1.1 (uso commerciale libero), serviti dalla pagina in `sito/fonts/` con le licenze `OFL-Anybody.txt` e `OFL-Barlow.txt`.
- Foto F.R.A.M.O. (IMG-9594, IMG-9596) e logo: dal loro sito, da usare solo per la loro proposta.
- Nessuna foto di repertorio in pagina. Le foto Unsplash e Pexels scaricate per i prototipi restano in `assets/esterne/` (vedi `assets/CREDITI.md`) ma non sono usate. Le foto Adobe Stock del sito vecchio non sono usate.

## Logo

`sito/img/logo-framo-chiaro.png` è il PNG 500x90 del loro sito con la scritta FRAMO resa bianca per i fondi neri (il simbolo giallo è quello originale), mostrato a 178 px in testata e 196 nel piede; `sito/img/simbolo-96.png` è il simbolo per le testate strette e l'icona della scheda. Per il sito vero: chiedere il vettoriale all'azienda o ricostruirlo dal simbolo 1616x1616 (`assets/originali/logo-simbolo-1616.png`).
