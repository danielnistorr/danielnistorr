# Perché le 31 home non sono ancora "super professionali"

Diagnosi del 3 novembre 2026, scritta come la scriverebbe il direttore creativo di uno studio che lavora per aziende di alto livello.

**Materiali guardati**
- Fogli in `alto/diagnosi/`:
  - `prime-31.jpg` e `prime-31-390.jpg`: le 31 prime schermate a 1440 e a 390;
  - `riferimenti-14.jpg` e `riferimenti-14-390.jpg`: i 14 riferimenti;
  - `media-prime-schermate.jpg`: le 31 aperture sovrapposte, accanto alle 14 dei riferimenti.
- Pagine intere a 1440 guardate a pezzi: Ruffatti, BCMEnologia, NicDean, OverdriveCustoms, Belletti, SanMarcoTimbri, Framo, PanificioFornasiero e Nardi. Per confronto anche barth, Klindworth e Joseph Brot.
- `index.html` letti: Ruffatti (con la NOTA e il giudizio), BCMEnologia e NicDean. Ho anche contato in tutti e 31 gli H1, gli H2, i moduli e le voci ricorrenti.

**Come ho misurato**
- Playwright sulle 31 pagine statiche e sui siti dal vivo di 11 riferimenti: Joseph, Petersham, Poilâne, Union, barth, Budri, Cly-Del, Holzrausch, Odermatt, Dulwich e Klindworth. Kline e Wilson non si raggiungono dal container; eggentaler.com è un albergo omonimo e l'ho escluso.
- Nella prima schermata conto solo quello che si vede davvero: l'elemento deve essere quello in primo piano nel suo punto, quindi niente menu nascosti e niente banner sotto.
- Dati grezzi e script in `alto/diagnosi/misure/`.
- Dove un valore è stimato sulla schermata lo dico.

---

## In una frase

Le home sono **corrette e complete, ma non sono progettate**. Ognuna mette nella prima schermata tutto quello che serve a tutti, e tutte usano lo stesso scheletro. Gli studi dei riferimenti fanno il contrario: per ogni azienda scelgono **una cosa sola** e le danno tutto lo spazio. Il resto lo mettono dopo, oppure lo tolgono.

La mancanza di foto pesa, ma meno di quanto si dica. La stimo in **circa un quinto** della distanza dai riferimenti. Il resto viene da impaginazione, tipografia, testi e soprattutto dal metodo: regole che premiano la presenza delle cose e agenti che riempiono.

---

## I numeri chiave

Mediane; tra parentesi minimo e massimo.

| Misura | 31 home | Riferimenti (11 dal vivo) | Rapporto |
|---|---|---|---|
| Elementi cliccabili nella prima schermata 1440 | 15 (9-23) | 8,5 (4-16) | 1,8 volte |
| Bottoni pieni o bordati nella prima schermata 1440 | 4 (2-11) | 1 (0-3) | 4 volte |
| Caratteri di testo visibili nella prima schermata 1440 | 634 (289-998) | 118 (20-279) | 5,4 volte |
| Caratteri di testo visibili nella prima schermata 390 | 393 (251-607) | 190 (51-410) | 2 volte |
| Cliccabili nella prima schermata 390 | 8 (5-14) | 4 (3-10) | 2 volte |
| Parte della prima schermata 1440 occupata da foto | 26% (0-50%) | 70-100% dove c'è una foto (stima sulle schermate: Joseph, Union, Poilâne, Budri, Odermatt, Eggentaler) | da 3 a 4 volte meno |
| Larghezza reale della foto d'apertura | 655 px (355-1440) | 1260-1536 px (Poilâne, Budri, Holzrausch, barth, Klindworth) | circa la metà |
| Parole nella home | 1083 (671-1386) | 441 (363-1275) | 2,5 volte |
| Bottoni in tutta la pagina | 12 (6-26) | 4 (0-11) | 3 volte |
| Misure di carattere distinte | 8 (6-10) | 9 (3-14) | uguale: questo **non** è il problema |
| Quota di testo sotto i 16 px | 1% | non misurata | anche questo **non** è il problema |
| Densità di bordi nella prima schermata (media delle immagini) | 0,161 | 0,116 | +39% di "rumore" |

Le stesse home, contate una per una:

| Schema ricorrente | Home su 31 |
|---|---|
| H1 allineato esattamente a 80 px dal bordo | 27 |
| Apertura "titolo a sinistra, foto o riquadro a destra" | 27 (21 rilevate dallo script, più Panificio, StefanoAiti, Finiture, Argenteria, Framo e Unicar viste a occhio) |
| Occhiello maiuscolo spaziato sopra l'H1 | 28 |
| Occhiello maiuscolo spaziato sopra gli H2 | 125 su 273 H2 (46%) |
| Fila di 3-8 ingressi o fatti in fondo alla prima schermata | 24 (misurata) |
| Fascia di cifre grandi (almeno 30 px) | 30, in media 6 cifre |
| Testata fissa alta 81-89 px | 27 (tutte e 31 sono fisse) |
| Spazio di 120 px tra le sezioni | 27 |
| Modulo di contatto in home | 31 |
| Telefono come titolo gigante (almeno 40 px) | 17 |
| Bottone "Indicazioni" | 23 |
| "Aperto ora" calcolato | 16 |
| "Prepara l'email" | 14 |
| H1 che è un elenco di prodotti o servizi, o "mestiere + dal anno" | 27 (fanno eccezione PanificioFornasiero, Unicar, LaTermica, Obygroupitalia) |

L'immagine `media-prime-schermate.jpg` lo mostra senza bisogno di numeri. Le 31 aperture sovrapposte disegnano **un modulo solo**:
- la riga della testata;
- una colonna di testo a 80 px;
- un rettangolo di foto tra 860 e 1360 px;
- una riga orizzontale in basso.

Le 14 dei riferimenti sovrapposte non disegnano niente: ognuna ha la sua composizione.

---

## Le 10 ragioni, in ordine di peso

Il peso è la mia stima di quanto ogni ragione conta nella distanza tra il 6 di oggi e un 8-9. La somma fa 100.

### 1. La prima schermata fa il lavoro di tutta la pagina (peso 17)

**Prove**
- Nella prima schermata a 1440 ci sono in mediana 634 caratteri, 15 cliccabili e 4 bottoni. Nei riferimenti sono 118 caratteri, 8,5 cliccabili e 1 bottone.
- ArgenteriaVarotto arriva a 998 caratteri, SanMarcoTimbri a 887, Obygroupitalia a 805, Negrizzolo a 804, Finiture a 779.
- **Ruffatti**, prima schermata: occhiello, H1, frase con due cifre e anno, due bottoni, email, "che cosa mandarci", due ingressi con descrizione, riga degli ultimi strumenti, foto con didascalia, testata con 6 voci, 3 lingue e telefono. Sono 18 cliccabili.
- **barth**: logotipo, "building tomorrow's interiors since 1877", menu. Sono 4 cliccabili veri, il quinto è il banner dei cookie.
- **Joseph**: un pane, quattro parole, 51 caratteri.

**Perché pesa così tanto**: in un secondo l'occhio legge la quantità prima del contenuto. Molta roba con lo stesso peso dice "gestionale" o "volantino", non "azienda che sceglie".

**Da che cosa dipende**: foto 10%, impaginazione 30%, metodo 60%.
- La regola A3 e C2 impone mestiere, luogo, prova, azione e immagine tutti nella prima schermata.
- Le schede d'uso aggiungono i compiti dei clienti tipo. La NOTA di Ruffatti elenca 9 cose che la commissione americana deve trovare "in prima vista".
- La prima schermata diventa la somma di tutti i compiti.
- I clienti tipo danno 7-8,5 proprio per questo, e lo stesso motivo costa il voto da agenzia.

### 2. La foto è un riquadro, non l'apertura (peso 15)

**Prove**
- La foto occupa il 26% della prima schermata a 1440 (massimo 50%, OverdriveCustoms) e il 18% a 390.
- Nei riferimenti con foto la foto è la pagina: Joseph, Union, Poilâne, Budri, Odermatt, Eggentaler occupano il 70-100%.
- Nei riferimenti senza foto c'è un gesto tipografico o un disegno a tutta altezza: barth, Holzrausch, Cly-Del, Dulwich.
- Larghezza reale della foto d'apertura nelle nostre: 655 px in mediana. Ruffatti 574, BertoGuerrino 500, Obygroupitalia 522, BCMEnologia 624, LaTermica 599. Le foto sono messe quasi alla loro misura, in un riquadro di 500-840 px.

**Il punto che cambia la diagnosi**: in molte cartelle `assets/originali/` le foto grandi ci sono, ma restano fuori dall'apertura.

| Home | Foto originali di almeno 1600 px | Larghezza della foto in apertura |
|---|---|---|
| LaTermica | 307 | 599 px |
| Finiture | 194 | 820 px |
| Nardi | 104 | 720 px |
| SerenissimaService | 103 | 720 px |
| StefanoAiti | 101 (ed è un fotografo) | 763 px |
| DistilleriaRizzi | 61 | 648 px |
| MolonGiovanni | 60 | 835 px |
| BCMEnologia | 58 | 624 px |
| PeruzzoGrafiche | 54 | 720 px |

La foto d'apertura è stata scelta per **quello che dice**, cioè l'ultimo lavoro o la sede, e non per **quanto regge in grande**.

È vero che le foto mancano davvero dove le foto vere sono sotto i 1200 px:
- NicDean: lato lungo mediano 339 px, massimo 1024;
- Unicar: massimo 939 px;
- Negrizzolo: 6 foto di almeno 1200 px;
- Belletti: nessuna di almeno 1600 px;
- Ciesseci: 11.

**Da che cosa dipende**: foto 50%, impaginazione 40%, metodo 10%. La regola C3 chiede "un'immagine vera" ma non dice quanto grande, né che si sceglie prima la foto e poi il testo.

### 3. Uno scheletro solo per 31 aziende diverse (peso 14)

**Prove**: la tabella degli schemi qui sopra e `media-prime-schermate.jpg`.
- Dopo l'apertura la sequenza si ripete quasi uguale: fascia di fatti, servizi in schede, blocco scuro con le cifre, chi siamo con le date, contatti con il telefono gigante e il modulo "Prepara l'email", piede a 4 colonne.
- SanMarcoTimbri, Framo e Belletti hanno colori diversi (rosso, giallo, verde) ma lo stesso ordine e le stesse proporzioni.
- Un organaro che lavora per le cattedrali americane (Ruffatti) e un'officina di rimorchi (Negrizzolo) hanno la stessa apertura e la stessa griglia.
- Il modello d'apertura è quello di **Kline e Wilson**: occhiello, titolo, due bottoni, foto a destra. Sono i due riferimenti più "da modulo" dei 14, ed è stato esteso a manifattura e lusso.
- Budri, barth, Holzrausch e Odermatt non hanno niente di quello schema.

**Da che cosa dipende**: foto 0%, impaginazione 30%, metodo 70%.
- Stesse regole e stessi riferimenti.
- Le famiglie sono per settore e non per posizionamento.
- Nessun controllo confronta una home con le altre.

### 4. Tutto ha lo stesso peso: la home è un fascicolo (peso 12)

**Prove**
- 1083 parole in mediana, contro 441.
- 9 H2 per home: Belletti 14, ServalliPadova 14, MolonGiovanni 13, Unicar 12.
- 12 bottoni per pagina contro 4.
- Ogni sezione ha da 3 a 6 sottoblocchi.
- **BCMEnologia** (1351 parole):
  - sotto ogni scheda di prodotto la riga "Catalogo PDF, 1,4 MB, IT DE EN FR";
  - due tabelle di misure da 8 e 5 righe;
  - 4 cataloghi in riquadri;
  - 4 rivenditori con il testo in 4 lingue;
  - 10 brochure in ZIP;
  - poi chi siamo, le date e il modulo.
- **Ruffatti**: 6 cifre, 3 citazioni, 5 video, il concorso di Miami con i premi in dollari, 4 riconoscimenti, la famiglia. Tutto alla stessa voce.
- **Klindworth** (411 parole): tre parole giganti (WORK, KUDOS e il nome dei clienti sulle foto), poche schede, molta foto.
- **Joseph** (414 parole): un racconto in quattro capitoli e due indirizzi.

**Il risultato**: la pagina non ha pause e non ha un culmine. Nessuna sezione è più importante delle altre, quindi nessuna si ricorda.

**Da che cosa dipende**: foto 5%, testi 35%, metodo 60%.
- Le regole C9, C10, C11, C14 e C15 chiedono ognuna un blocco.
- "Nessun dato inventato" spinge a mettere **tutti** i dati veri trovati, senza sceglierne tre.

### 5. Manca l'idea: nessun gesto che appartenga solo a quell'azienda (peso 10)

**Prove**
- Nei riferimenti c'è sempre un'idea che si riconosce dalla miniatura senza leggere:
  - barth: il logotipo alto 245 px su nero;
  - Klindworth: le parole WORK e KUDOS a 362 px e le diagonali sulla foto;
  - Dulwich: l'escavatore al tratto verde su verde;
  - Union: la scritta a mano sulla foto del forno;
  - Joseph: il pane visto dall'alto con la luce della finestra.
- Nelle 31 i gesti propri sono tre:
  - il logotipo corsivo a 1280 px di **Ruffatti**, che però è sotto la prima schermata;
  - il "3/16" fino a 3"" di **Framo**;
  - la foto di Matteo con le moto di **OverdriveCustoms**.
- OverdriveCustoms è anche l'unica apertura con una foto a tutta larghezza, ed è la più vicina a un sito di studio.
- Il resto si riconosce solo dal colore.

**Da che cosa dipende**: foto 20%, direzione creativa 50%, metodo 30%. La regola A5 chiede "almeno un gesto di scala per pagina", e lo si soddisfa con la fascia di cifre grandi. Un gesto messo per regola non è un'idea.

### 6. Tipografia di serie (peso 9)

**Prove**
- 22 H1 su 31 sono un grottesco in peso 700.
- Gli stessi caratteri gratuiti tornano: **Archivo in 9 home**, **Switzer in 6**, General Sans, Encode Sans, Gambetta, Zodiak, Sofia Sans e Anybody in 2 ciascuno.
- I riferimenti usano caratteri di fonderia scelti per il marchio: Neue Haas Grotesk (barth), Tiempos e Lausanne, Larken. Nessun carattere si ripete tra due riferimenti.
- L'**occhiello maiuscolo spaziato** (14-16 px, spaziatura 1-2 px, colorato) sta sopra 28 H1 su 31 e sopra il 46% degli H2.
  - Non è una pillola, ma **fa lo stesso lavoro del "badge sopra il titolo"** che il committente vieta: annuncia la categoria prima del titolo.
  - È il segno più riconoscibile delle pagine fatte con un modello.
  - Nei 14 riferimenti sta sopra il titolo d'apertura solo in 4 (Dulwich, Klindworth, Kline, Eggentaler), e in Klindworth contiene un fatto: il numero di licenza.
- La scala non ha contrasto: H1 di 64-88 px con testo di 17 px. Il salto c'è, ma è sempre quello.
- I riferimenti usano o un salto enorme (barth, Klindworth, Holzrausch con il testo a 30 px come manifesto) o niente (Joseph tutto in maiuscolo misurato).
- Le misure distinte (8) sono già dentro la regola, e i riferimenti ne hanno di più (Poilâne 14, Petersham 14, Cly-Del 11). La regola C7 controlla una cosa che non distingue un sito buono da uno mediocre.

**Da che cosa dipende**: foto 0%, tipografia 60%, metodo 40%. A4 indica accoppiate "che funzionano" e gli agenti le pescano dallo stesso piccolo catalogo gratuito.

### 7. Testi da scheda prodotto e da istruzioni per l'uso (peso 8)

**Prove**
- Gli H1 sono elenchi di prodotti o "mestiere dal anno":
  - "Torchi, martinetti DAVID e pompe, dal 1960";
  - "Rimorchi, carribotte e vasche inox. Riparazioni di qualsiasi marca. Taglio laser.";
  - "Stucchi, gessi e malte";
  - "Forniture alberghiere dal 1953".
- In 5 home l'H1 contiene anche il sottotitolo e arriva a 13-22 parole (Belletti 22, Ciesseci 21, ArgenteriaVarotto 18, LaTermica 16).
- Sono chiari e indicizzabili, ma non hanno voce: Mascioni o qualsiasi concorrente potrebbe firmarli.
- I riferimenti scrivono una frase che ha un punto di vista:
  - "Brot wie es sein soll";
  - "Nourrir";
  - "Une boulangerie de quartier pour le quartier";
  - "Höchste Qualität. Egal wo.";
  - "Your local, independent plant hire".
- In pagina sta in vista il testo di servizio:
  - "Si apre il tuo programma di posta con la richiesta già scritta" (14 home);
  - "Dalla targhetta, per esempio torchio idraulico 60";
  - "Tocca una scarpa: si apre una mail a info@nicdean.it con il nome già scritto".
- È utile, ma è testo da interfaccia messo al livello del racconto.

**Da che cosa dipende**: testi 70%, metodo 30%. Il vincolo "niente parole d'ordine" è stato letto come "solo descrizioni". Una frase con carattere non è una parola d'ordine.

### 8. A 390 la prima schermata è una pila di bottoni (peso 6)

**Prove**
- A 390 nelle nostre ci sono 8 cliccabili e 4 bottoni impilati; nei riferimenti 4 cliccabili.
- La foto occupa il 18% dello schermo, contro il 91% di Joseph, l'84% di Union e il 49% di Budri.
- Nel foglio `prime-31-390.jpg`, per esempio:
  - PeruzzoGrafiche ha 3 bottoni a tutta larghezza;
  - Scaleabotola ha 4 tessere gialle e 2 bottoni;
  - NordService ha 2 bottoni arancio e nero più il link "info@";
  - Ciesseci ha 3 bottoni.
- Quasi nessuna mostra una foto prima di scorrere: fanno eccezione OverdriveCustoms, ArtificioBattagin, Ruffatti (in parte) e Negrizzolo (in parte).
- Il telefono a tutta larghezza è giusto per le imprese di servizi. Il resto lo segue per abitudine.

**Da che cosa dipende**: foto 20%, impaginazione 40%, metodo 40%. La regola C2 dice "a 390 il bottone è a tutta larghezza" e ogni scheda d'uso aggiunge il suo.

### 9. Le foto non sono dirette: scelta, taglio e serie (peso 5)

**Prove**
- BCMEnologia mescola foto da telefono del 2022 con prodotti scontornati su grigio. Gli scontornati sono 8 tessere uguali e fanno e-commerce. Nelle cartelle ci sono anche foto di stand in fiera con pareti verdi e blu.
- NicDean ha 8 scarpe scontornate su tessere grigie con "Chiedi il tuo numero" ripetuto 8 volte. La foto della fila è di 1024 px ed è servita anche a 1480, ingrandita 1,45 volte.
- LaTermica ha 300 foto di magazzino del 2014 a 2000 px, tutte con la stessa luce di neon e senza un'inquadratura forte.
- Ruffatti ha un trattamento comune (`pro_img.py`), ma usa la foto di New Orleans a 574 px. Intanto c'è un organo verticale col rosone a 900x1600 (`2016_02_home-ruffatti2.jpg`) e un interno di chiesa a 3264x2448 (`2018_11_P1270600-1.jpg`).
- Il problema non è solo avere poche foto: **nessuno ha fatto da photo editor**. Nessuno ha scelto la foto migliore, l'ha tagliata con coraggio e ha buttato il resto.

**Da che cosa dipende**: foto 70%, direzione 30%. Questa parte la risolve davvero solo il servizio fotografico.

### 10. Colore a fasce e componenti di servizio dappertutto (peso 4)

**Prove**
- Il colore del marchio è usato come fondo di fasce intere, alternate al nero:
  - il rosso di BCMEnologia, SanMarcoTimbri, NicDean, DistilleriaRizzi e Negrizzolo;
  - il giallo di Framo e BertoGuerrino;
  - il verde di Belletti e Nardi.
- Lo spazio tra le sezioni è sempre 120 px e i colori di fondo sono sempre 3-5.
- Sopra, gli stessi componenti funzionali in quasi tutte: "Aperto ora" (16), "Indicazioni" (23), telefono in 9 link `tel:` per pagina in mediana, telefono a 40 px e più (17), modulo (31).
- La pagina sembra il pannello di un servizio, non la presentazione di un'azienda.
- Nei riferimenti di manifattura il colore è quasi assente: barth nero e un verde, Budri foto e bianco, Holzrausch bianco e un arancio nella foto.
- Nei riferimenti le funzioni stanno in testata e nel piede, non in ogni sezione.

**Da che cosa dipende**: impaginazione 40%, metodo 60%. C6 "la palette viene dal marchio" è stata applicata riempiendo fasce, e C12 chiede "almeno 2 sezioni su fondo scuro o di colore pieno".

### Quanto pesano le foto, in tutto

Ho pesato la quota foto di ogni ragione col suo peso:

17x0,10 + 15x0,50 + 14x0 + 12x0,05 + 10x0,20 + 9x0 + 8x0 + 6x0,20 + 5x0,70 + 4x0 = **16,5 su 100**

Quindi con le stesse foto si può recuperare circa l'80% della distanza. Lo dimostrano barth, Holzrausch, Cly-Del e Petersham: tre di loro aprono senza una foto.

---

## Che cosa farebbe uno studio con le stesse foto scarse

Regola di lavoro dello studio: **prima si sceglie l'immagine (o la frase) che regge da sola, poi si decide che cosa ci sta intorno, infine si toglie.** In ognuno dei tre casi la home scende a 450-600 parole, 5-6 sezioni e 1 bottone nella prima schermata.

### Ruffatti (organi a canne, Padova, dal 1940)

**Oggi**
- Fondo mogano.
- A sinistra 18 cliccabili e 731 caratteri.
- A destra l'organo di New Orleans a 519x649, dalla foto di 574 px.
- Il logotipo corsivo d'ottone è la loro idea migliore, ma sta **sotto** la prima schermata.

**Toglierei**
- Dalla prima schermata:
  - la frase con le cifre del 2016;
  - il secondo bottone;
  - l'email e "che cosa mandarci";
  - i due ingressi descritti;
  - la riga degli ultimi strumenti;
  - la didascalia.
- La fascia delle 6 cifre: ne resta una sola, "oltre 500 organi", scritta grande nel testo.
- La lista dei 5 video: diventa un link "Ascolta".
- Il concorso di Miami: passa nel piede o in una pagina sua.
- I 4 riconoscimenti in fila: ne resta uno, Maestro d'Arte e Mestiere, accanto alla firma.

**Ingrandirei**
- La prima schermata diventa il logotipo d'ottone a tutta larghezza sul mogano, con una riga sola: "Costruttori e restauratori d'organi a canne. Padova, dal 1940". In testata "Scriveteci" e il telefono. È l'apertura di barth, con il loro segno al posto di quello di barth.
- Subito sotto, a tutta altezza (900 px), l'organo del rosone in verticale. La foto è `2016_02_home-ruffatti2.jpg`, 900x1600: a 506x900 regge alla misura vera e a densità 1,8.
- Accanto, solo il nome dello strumento e la città.
- Poi "Organi nuovi" e "Restauro" come due porte fotografiche grandi:
  - l'interno della chiesa a 3264x2448 (`2018_11_P1270600-1.jpg`);
  - il laboratorio dei falegnami a 1597x1198 (`2016_04_falegnami-21.jpg`).
- Le trombe en chamade (`2016_04_xSfondo-trombe.jpg`) come unico dettaglio a tutta altezza.

**Cambierei**
- La sezione "Ultimi strumenti" diventa una sequenza di uno strumento per schermata, con foto grande e tre dati, invece di elenco più foto piccola.
- Gli strumenti senza foto (Grand Rapids, Pershore, Coral Ridge) restano nella pagina Realizzazioni e non in home.
- Il modulo resta, ma nella pagina Contatti. In home basta il telefono grande, che c'è già.

### BCM Enologia (macchine enologiche, Saonara, dal 1960)

**Oggi**
- Apertura spezzata: titolo da catalogo, foto dei torchi a 576x720 (dalla foto di 624 px), fila di 8 prodotti con le misure sotto.
- Poi schede scontornate su grigio, ognuna con la riga del PDF in MB.
- Poi tabelle, cifre rosse, cataloghi, rivenditori in 4 lingue, brochure ZIP, chi siamo e modulo. Sono 1351 parole e 99 cliccabili.

**Toglierei**
- La fila degli 8 prodotti sotto l'apertura.
- I "Catalogo PDF, 1,4 MB" sotto ogni scheda: un solo link "Cataloghi in quattro lingue".
- Le due tabelle di misure: vanno nella pagina Misure, perché chi le cerca le cerca lì.
- I 4 rivenditori con il testo in 4 lingue e le 10 brochure ZIP: vanno nel piede o nella pagina Dove trovarci.
- La fascia rossa delle 4 cifre: il 1960 c'è già nel titolo.
- Tutte le foto degli stand in fiera con le pareti verdi e blu.

**Ingrandirei**
- Le loro foto di officina del 2022 a 1920x1440. Le basi rosse dei torchi in fila con le viti (`gallery--torchi-martinetti-e-gabbie--img-20220625-wa0002.jpg`) e le gabbie di legno con i martinetti (`...wa0019.jpg`) sono **ripetizione di forme**, il soggetto che regge meglio un taglio a tutta larghezza.
- Tagliate a 1920x1080 e passate tutte con lo stesso trattamento (bilanciamento verso il neutro, colore 0,85, stessa curva), aprono la pagina a tutta larghezza.
- Sopra, una riga sola: "Torchi e martinetti, fatti a Saonara dal 1960". Un bottone: "Ricambi: mandateci la foto della targhetta".
- Il martinetto DAVID (è un loro marchio registrato) diventa il gesto: il nome a 200 px con la foto del pezzo in ghisa (`apertura` di chi siamo) alla misura vera.

**Cambierei**
- Gli 8 scontornati diventano 4, su fondo bianco uguale, a 400 px l'uno, con il solo nome. Niente descrizione di tre righe e niente doppio link.
- Il modulo resta, perché è il loro lavoro (ricambi dalla foto della targhetta), ma diventa l'ultima sezione con un titolo che lo dice. Non è la ripetizione di un modulo standard.

### Nic Dean (calzaturificio e spaccio, Villatora, dal 1975)

**Oggi**
- È la home più corta (671 parole), la più vicina alla misura giusta.
- Fa però **negozio online di serie**:
  - titolo nero maiuscolo a sinistra, colonna degli orari a destra, due bottoni rossi;
  - la foto della fila delle 5 décolleté a 845 px;
  - poi 8 scarpe scontornate in tessere grigie con "Chiedi il tuo numero" sotto ognuna;
  - poi fasce rossa, nera e rossa.
- Le foto vere sono davvero poche e piccole: la fila a 1024x683, le scarpe a 500x375, il resto grafica del sito vecchio.

**Toglierei**
- La colonna degli orari dalla prima schermata: "Aperto ora" resta, piccolo, in testata.
- Il secondo bottone.
- La riga sotto la foto ("Décolleté con plateau, firma NicDean sul sottopiede").
- 4 delle 8 scarpe.
- Il "Chiedi il tuo numero" ripetuto 8 volte: basta una frase sopra la griglia.
- Le cifre 1975 e 2013 a 160 px: il 1975 è già nel titolo.

**Ingrandirei**
- Con foto così una home la costruisci sulla tipografia, come barth e Holzrausch.
- "Scarpe fatte a Villatora dal 1975" a tutta larghezza, a 140-180 px, in un carattere con carattere (un grottesco stretto o un serif da calzoleria, non un altro League Spartan). Fondo il bianco caldo della foto.
- Sotto, la fila delle 5 décolleté alla sua misura vera di 1024 px, centrata, senza ingrandirla, con molta aria intorno. È il loro "pane visto dall'alto": cinque colori, una forma.

**Cambierei**
- Le 4 scarpe rimaste in una riga su fondo bianco, a 300 px, senza tessera grigia e senza bordo.
- Lo spaccio come una sezione sola: indirizzo, tabella degli orari, "Indicazioni".
- "Per negozi, fiere ed eventi" come una frase e un'email, senza modulo in home.
- Il servizio fotografico qui non è un'aggiunta: va proposto **prima** di questa home. Senza le mani del montaggio e il reparto, il calzaturificio resta un negozio.

---

## Che cosa del metodo porta all'uniformità, e come cambiarlo

### Che cosa la produce

1. **Le regole sono liste di presenze.**
   - 14 delle 15 regole si controllano contando che una cosa ci sia: il bottone, la prova, le cifre, le schede, il modulo, il piede.
   - La NOTA di Ruffatti scrive "passa" a 14 regole su 15 e il voto da agenzia resta 6,5.
   - Una home si migliora per le regole solo aggiungendo. Nessuna regola chiede di togliere, e nessuna misura il peso relativo delle cose.
2. **Le soglie sono alte e mai massime.** "Da 4 a 8 cifre", "almeno 3 tipi di prove", "almeno 2 sezioni su fondo pieno", "almeno 4 link `tel:`", "modulo in home". Agli agenti mancano dei tetti: quante parole al massimo, quanti cliccabili al massimo nella prima schermata, quante sezioni al massimo.
3. **La prima schermata è una lista d'obbligo (A3, C2), e le schede d'uso dei clienti tipo la allungano.** Ogni compito ("il parroco deve vedere Restauro senza scorrere") diventa un elemento in più sopra la piega. I clienti tipo premiano la reperibilità, e la reperibilità messa tutta in alto uccide la gerarchia. Così il 7-8,5 dei clienti tipo e il 6 del controllore da agenzia vengono dalla stessa causa.
4. **Il modello d'apertura è uno solo ed è quello dei servizi.** Le famiglie S, B e M cambiano l'ordine delle sezioni, ma la prima schermata di tutte e tre è descritta con gli stessi 5 punti e gli agenti la risolvono allo stesso modo: il modello di Kline e Wilson. Budri, barth, Holzrausch e Odermatt non hanno niente di quella lista, eppure sono i riferimenti di M.
5. **Le famiglie sono per settore, non per posizionamento.** Ruffatti (cattedrali, Stati Uniti) e Negrizzolo (rimorchi agricoli) sono entrambe M. Uno studio le metterebbe ai due estremi.
6. **I controlli premiano la conformità numerica anche dove la regola è sbagliata.** C7 (al massimo 8 misure) e C8 (al massimo 2 famiglie) sono rispettate da tutte, mentre i riferimenti ne usano di più. La regola che conta, "c'è una sola idea e si riconosce", non c'è.
7. **Nessun controllo tra le home.** Ogni agente lavora da solo con le stesse regole e gli stessi 14 riferimenti, e quindi converge sulla media. Il giudizio di Ruffatti (K6) segnala una copia da un'altra home, ma solo come penalità, non come regola di progetto per tutta l'ondata.
8. **"Nessun dato inventato" è diventato "tutti i dati veri".** Gli agenti mettono in pagina tutto quello che trovano: MB dei PDF, premi in dollari, 6 cifre datate, 5 video. Uno studio sceglie i tre fatti più forti e lascia gli altri alle pagine interne.
9. **Le foto si scelgono per il contenuto, dopo il testo.** Nessuna regola dice "parti dalla foto più forte e falla grande, oppure non metterla e fai una home di tipografia". La via di mezzo, cioè la foto di 600 px nel riquadro a destra, è quella che dà il 6.
10. **Il catalogo dei caratteri è piccolo e gratuito,** e nessuno vieta di ripetere lo stesso carattere tra home vicine (Archivo 9 volte).

### Che cosa cambiare

1. **Tetti, non soglie.** Prima schermata a 1440:
   - al massimo 6 cliccabili, testata compresa;
   - 1 bottone;
   - 160 caratteri di testo;
   - foto o gesto tipografico su almeno il 60% dello schermo.

   A 390: al massimo 4 cliccabili e 1 bottone. Per S, il bottone è la chiamata.

   Home intera:
   - 450-650 parole;
   - al massimo 6 sezioni;
   - al massimo 5 bottoni;
   - fascia di cifre al massimo in una home su tre, e con al massimo 3 cifre.
2. **Una scheda "idea" prima dell'impaginazione:** una frase sul che cosa ha solo quell'azienda, e **un** gesto che la mostra (la foto, la parola o il segno). Controllo: nella miniatura a 300 px, senza logo, si capisce di chi è? Se due home dell'ondata hanno lo stesso gesto, una lo cambia.
3. **Prima la foto, poi la pagina.**
   - L'agente apre `assets/originali/`, sceglie le 3 foto più forti per taglio e risoluzione e le misura.
   - Se una regge a 1440 o a tutta altezza, apre la pagina.
   - Se nessuna regge, la home è di tipografia (barth, Holzrausch, Petersham) e le foto piccole vanno più giù, alla loro misura, in serie.
   - È vietata la foto di 500-800 px come metà dell'apertura.
4. **Le schede d'uso si soddisfano entro due schermate o dal menu, non nella prima.** Il compito del cliente tipo passa se lo trova in 5 secondi, anche scorrendo. Non serve che lo veda senza scorrere.
5. **Quattro modelli d'apertura diversi, assegnati per ondata in modo che due vicine non coincidano:**
   - foto a tutta pagina con una frase (Joseph, Union, Odermatt);
   - tipografia a tutta pagina (barth, Holzrausch);
   - disegno o oggetto con molta aria (Cly-Del, solo con foto vere scontornate bene);
   - modello di servizio con telefono e foto della squadra (Kline, Wilson), **solo** per le imprese che vivono di chiamate, che tra le 31 sono una decina: SerenissimaService, Unicar, FratelliZuin, Belletti, LaTermica, Obygroupitalia, NordService, Scaleabotola, Ciesseci e SanMarcoTimbri.
6. **Famiglie per posizionamento:** lusso e committenza alta (Ruffatti, ArgenteriaVarotto, ArtificioBattagin, DistilleriaRizzi, StefanoAiti), industria per industria (Framo, Finiture, MartoranaElettronica, BCMEnologia, ZetaItaly), servizi di pronto intervento, botteghe e spacci. Il settore viene dopo.
7. **Divieti nuovi**, che si aggiungono a quelli del committente:
   - l'occhiello maiuscolo spaziato è vietato come default: al massimo 1 per pagina, e solo se contiene un fatto (numero di licenza, anno, città);
   - niente telefono gigante e modulo nella stessa home salvo per S;
   - niente riga del peso dei PDF;
   - niente testo d'istruzioni dell'interfaccia sopra i 14 px;
   - niente fila di ingressi sotto l'apertura come default.
8. **Controllo dell'ondata:** dopo ogni ondata si rifà `media-prime-schermate.jpg`. Se le aperture sovrapposte disegnano un modulo riconoscibile, l'ondata non passa.
9. **Tipografia:**
   - ogni carattere al massimo in 2 home per ondata;
   - nella pagina, almeno un punto di scala forte (titolo o parola oltre i 140 px, oppure testo-manifesto a 28-34 px come Holzrausch);
   - via la regola delle 8 misure: si controlla solo che il testo corrente sia di almeno 17 px.
10. **Il voto da agenzia prima del test dei clienti tipo**, sulla miniatura e sulla prima schermata, e con il diritto di bocciare per "troppa roba" anche se tutte le regole passano.

---

## Che cosa tenere

Queste cose sono già al livello e non vanno perse nel taglio:
- OverdriveCustoms: foto a tutta larghezza in apertura, le special con nome e premio;
- Ruffatti: il logotipo d'ottone;
- Framo: il "3/16" fino a 3"";
- PanificioFornasiero: i due negozi con orari;
- Belletti: i lavori con i numeri;
- le palette prese dal marchio;
- il fatto che nessuna home usa repertorio.

Il problema non è la qualità del contenuto, ma la quantità messa insieme e l'assenza di una scelta.
