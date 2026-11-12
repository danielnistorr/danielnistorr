# 03. Mappa delle pagine

Il sito attuale ha quattro pagine più quella del contributo FESR (Home con la poesia, L'Angelo e il Diavolo, Ristorante, Contatti,
`Bando_pr_veneto.htm`) e 303 parole in tutto (01). Il nuovo sito parte da quello che viene a fare chi lo apre, quasi sempre dal
telefono, in piazza o in macchina verso Marostica (brief di linguaggio, paragrafo 1): sapere se stasera è aperto, cosa si mangia, a
che numero si chiama e dove si entra. Specifica completa, sezione per sezione: `_prova/spec.md`.

L'idea, in una frase: **il sito è la porta dell'osteria la sera**. In alto, sul vino dello stemma, il cartello con la data di oggi,
il titolo della pagina e una frase dell'oste; sotto, su carta bianca, il foglio della casa (la carta, gli orari, la piazza
disegnata, il disegno di Don Backy); in fondo, la striscia "Stasera" con lo stato di oggi e il telefono.

| Sito attuale | Nuovo sito | Slug | Perché |
|---|---|---|---|
| Home | **Home** | `/` | la poesia lascia il posto al cartello: stato di oggi, rima dell'oste, telefono, mappa; poi la carta in breve e la tessera degli orari |
| Ristorante | **In tavola** | `/in-tavola/` | oggi due schede (porcetto, specialità romane) e una gallery dietro `javascript:;`; diventa la carta intera in testo, con la cantina |
| (orari nel piede e in Contatti) | **Orari** | `/orari/` | tre versioni degli orari fra sito, Google e Comune: una pagina sola che li dice giorno per giorno, con le regole di prenotazione e il modulo per tavolate e porcetto |
| Contatti | **Dove siamo** | `/dove-siamo/` | la mappa Google incorporata (35-36 richieste a Google prima del consenso) diventa la piazza disegnata con il 41/A, più la foto della porta e i recapiti |
| L'Angelo e il Diavolo | **L'osteria** | `/l-osteria/` | Apo, Bruna e Lorenzo con le loro frasi, il nome spiegato dal disegno di Don Backy, la sala, la poesia della vecchia home, Voci dal Cuore |
| Bando_pr_veneto.htm | **Progetto FESR** | `/progetto-fesr/` | pubblicità obbligatoria del contributo; non nel menu, collegata dal piede di ogni pagina |

Più due blocchi globali con il plugin gratuito Ultimate Addons for Elementor: **Header** sul vino (logo con lo stemma in gesso, menu
di quattro voci, telefono 0424 72312 sempre a vista; fino a 1024 px il bottone "Menu" con un pannello notte) e **Footer** notte
(logo, indirizzo e recapiti, social, loghi e riga del contributo FESR, ragione sociale, P.IVA, REA, sede legale, link a Privacy e
Cookie). Privacy e Cookie sono pagine WordPress semplici, fuori dalla numerazione.

## Sezioni per pagina

### Home (`/`)
1. **Il cartello** (Bocca di Lupo, Roscioli): sul vino la data di oggi in rosa, lo stato calcolato sull'ora di Marostica ("STASERA
   APERTI DALLE 18 A MEZZANOTTE"), la regola della settimana, la rima "Si riposa il lunedì perché il fegato respiri", il bottone
   "Prenota al 0424 72312"; a destra la Piazza degli Scacchi disegnata con l'osteria al 41/A e "Apri in Maps".
2. **In tavola** (Via Carota, Padella): la carta in due colonne (specialità romane, secondi, dal forno a legna, di stagione), il link
   "Tutta la carta e la cantina"; a destra il disegno di Don Backy con la battuta sul bianco e il rosso, e la cantina divisa in due.
3. **Il mosaico** (Via Carota): la sala del 2023 grande, il porcetto nel forno e i rigatoni in padella, Bruna ai fornelli, Apo al banco.
4. **La porta** (Masuelli, Quality Chop House): la tessera degli orari giorno per giorno, con la riga di oggi in rosa, appesa sulla
   foto della facciata sotto il portico; come si prenota; link a tavolate e porcetto.

### In tavola (`/in-tavola/`)
1. Il cartello: "IN TAVOLA", cucina romana e veneta, «Un luogo dove non si confonde l'assaporare con il masticare»; le tagliatelle
   impiattate.
2. **La carta** (Da Enzo al 29, Padella): specialità romane, secondi, dal forno a legna, pizzeria, di stagione, su tre colonne;
   nessun prezzo finché l'oste non lo dà.
3. Dalla cucina: tagliolini in padella, panetti per la pizza, pizza con le olive, in una fila.
4. **Il porcetto e la cantina** (Brat): affiancati, il porcetto della domenica (gli altri giorni su prenotazione) e il bianco e il
   rosso, con Il Rosso di Apo.
5. Stasera: stato di oggi, telefono, indirizzo.

### Orari (`/orari/`)
1. Il cartello: "ORARI E PRENOTAZIONI", lo stato di oggi, la rima, il bottone del telefono; a destra la tessera giorno per giorno con
   la nota sul lunedì d'estate.
2. **Come si prenota** (Asador Etxebarri): al telefono, su Facebook, il porcetto, le tavolate, i coperti in sala e all'aperto, il
   lunedì; righe brevi senza icone.
3. **Tavolate e porcetto su prenotazione**: il modulo (Contact Form 7: nome, telefono, email, giorno, pranzo o cena, ora, persone,
   porcetto o tavolo all'aperto, note per allergie, consenso privacy), che è una richiesta da richiamare, non una prenotazione; a
   fianco la sala.

### Dove siamo (`/dove-siamo/`)
1. Il cartello: "PIAZZA CASTELLO 41/A", sotto il portico di Piazza degli Scacchi, il verso «in Piazza degli Scacchi dove ha aperto
   un'osteria!», il bottone "Apri in Maps"; a destra la mappa disegnata, più grande che in home.
2. **La porta**: la facciata a tutta larghezza, con le insegne descritte (la scritta, il neon "Enoteca Bar Caffè da Apo", "Ristorante
   Pizzeria", lo stemma dorato).
3. La piazza: Piazza degli Scacchi di notte; ovoli e porcini in piazza davanti al Castello Inferiore.
4. Telefono, email e social: telefono, email, indirizzo, Facebook, Instagram, Tripadvisor.
5. Stasera.

### L'osteria (`/l-osteria/`)
1. Il cartello: "L'OSTERIA DI APO", la frase di Apo «Un oste di passaggio...»; Apo che accoglie i clienti al banco.
2. **Il nome**: il disegno di Don Backy del 1998 e la battuta «Vorrà dire che il bianco lo chiameremo l'Angelo... e il rosso il
   Diavolo!»; lo stemma di oggi con le ali e il tridente.
3. **Apo, Bruna e Lorenzo**: la storia di Apo (Roma, il 1986, il ritorno a Marostica, il libro «Vita!»), i tre ritratti con il nome e
   le frasi del sito.
4. La sala: la sala piena di sera, novembre 2012, a tutta larghezza.
5. **La poesia e la musica**: "Vieni con me stasera andiamo", la vignetta "GOAL!" della vecchia tovaglietta, Voci dal Cuore e "30 Nodi
   per il fegato".
6. Stasera.

### Progetto FESR (`/progetto-fesr/`)
1. Loghi, titolo "Progetto finanziato con il PR Veneto FESR 2021-2027", titolo e obiettivi del progetto, i quattro importi, la
   descrizione del Distretto in PDF, la foto della cucina rinnovata.

## Navigazione

Menu: In tavola, Orari, Dove siamo, L'osteria (menu WordPress "Menu principale", widget Navigation Menu di Ultimate Addons); la voce
della pagina in cui si è in rosa con un filo sotto. Il telefono 0424 72312 resta a destra in ogni testata e sul telefono la testata
resta in alto mentre si scorre. Fino a 1024 px il menu diventa il bottone "Menu" con un pannello notte a tutta larghezza. La pagina
del progetto FESR, Privacy e Cookie si raggiungono dal piede.

Per `ciclo.sh`:

```
PAGINE="/:01-home /in-tavola/:02-in-tavola /orari/:03-orari /dove-siamo/:04-dove-siamo /l-osteria/:05-l-osteria /progetto-fesr/:06-progetto-fesr"
MENU="in-tavola,orari,dove-siamo,l-osteria"
```

Redirect dai vecchi URL (dettaglio in `_prova/spec.md`, paragrafo 14, e poi in `plugin/redirect-301.csv`): `/index.htm` alla home,
`/l-angelo-e-il-diavolo.htm` a `/l-osteria/`, `/ristorante.htm` a `/in-tavola/`, `/contatti.htm` a `/dove-siamo/`,
`/Bando_pr_veneto.htm` a `/progetto-fesr/`, le foto delle due gallery alle pagine corrispondenti; `http` verso `https` e il dominio
senza `www` verso quello con `www`.
