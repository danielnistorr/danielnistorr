# Impreservice: proposta di nuova home

Proposta non richiesta di nuova homepage per Impreservice S.r.l. (Grisignano di Zocco, VI). Solo la home, in italiano e in inglese (selettore IT / EN in testata).

- Pagina: `sito/index.html` (statica, si apre con doppio clic), immagini in `sito/img/`, caratteri e licenza in `sito/fonts/`.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md`, sezione "Livello professionale", con l'esito delle 15 regole).
- Rigenerare immagini, controlli e screenshot: `bash _prova/script/build_finale.sh` (usa `pro_img.py`, `pro_controlli.mjs`, `pro_shoot.mjs`). Esito dei controlli in `_prova/pro_controlli.json`.
- Versione precedente (sezione del connettore ricostruita, foto di repertorio): `_prova/versione-1-originale/` (pagina e screenshot com'erano).
- Analisi con le fonti: `01-analisi.md`. Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`. Crediti delle immagini: `assets/CREDITI.md`.

## Il modulo va collegato a un servizio

Il modulo "Offerta o scheda tecnica" oggi **non invia nulla**: controlla nome, azienda ed email, poi apre il programma di posta con un'email già scritta a info@impreservicesrl.it (oggetto "Richiesta offerta: prodotto (azienda)", nel testo tutti i campi compilati). Un link mailto non porta allegati: chi compila deve allegare il disegno nel suo programma di posta, e la pagina glielo dice.

Per il sito vero va collegato a un servizio di invio che accetti file (il loro server, oppure un servizio di moduli con allegati fino ad almeno 20 MB per PDF, DWG, DXF, STEP), con risposta automatica e copia a carlo@ se lo vogliono. Il campo "Disegno del concio" è già un vero campo file: basta cambiare l'invio nello script in fondo alla pagina (funzione del `submit`).

## Cosa chiedere all'azienda

In pagina c'è solo ciò che sta in `01-analisi.md` e in `_prova/uso/SCHEDA.md`. Queste cose mancano o sono incerte: quelle incerte non sono in pagina, tranne i punti 2 e 3, che sono in pagina perché vengono da loro comunicati, ma datati.

1. **Schede tecniche in PDF** di Smart, Medium, Magnum, Smart HD e Hybrid: valori di taglio, diametri, materiale, giunto in cui lavorano. In pagina ogni versione porta al modulo con la scheda tecnica già spuntata; con i PDF diventa un link di download.
2. **Smart HD (480 kN) e Hybrid (boccola L140 passo 5 mm)**, in pagina: sono in produzione? La fonte è la notizia tunnelbuilder.it del 23/09/2022.
3. **Bulloni e barre di guida**, in pagina: ancora a catalogo? La fonte è il comunicato Viatec del 2013 (e la stessa fiera nella fascia delle prove).
4. **Linea ponti e viadotti**: nomi dei prodotti attivi (Sapjoint e la membrana Sapeflex del 2013 non sono in pagina finché non li confermano), se la posa la fa una loro squadra, e un elenco di opere per ANAS, Autostrade per l'Italia e Province autonome con luogo e anno.
5. **Orari** di ufficio e di magazzino: oggi non sono pubblicati, quindi in pagina non ci sono. Servono nel piede e accanto all'indirizzo.
6. **Certificazioni**: di sistema (per esempio ISO 9001) e di prodotto, e i nomi dei laboratori indipendenti che hanno fatto le prove ("independent laboratory assessments and approvals"). Con i PDF si fa la fascia delle certificazioni scaricabili.
7. **Referenze**: per i 42 cantieri, anno, opera, impresa e fornitura vera (le 14 schede di oggi dicono tutte "Diga, 2020"); quali si possono nominare con il cliente; i 16 cantieri italiani che mancano dall'elenco in pagina; tre lavori da raccontare con foto e due o tre numeri (anelli, connettori, anni).
8. **Recensioni**: non ne esistono (vendono a imprese ed enti). Si possono chiedere due o tre dichiarazioni firmate di clienti (impresa, cantiere, ruolo), da pubblicare con il loro permesso.
9. **Brevetto IT 1391815**: come vogliono citarlo (è in contitolarità con Innotek Srl, che in pagina non è nominata); se ci sono altri brevetti, anche esteri.
10. **Cellulare +39 335 5618004** (notizia del 2022): va pubblicato per i clienti in cantiere? Oggi in pagina c'è solo il fisso.
11. **carlo@impreservicesrl.it**: è nel piede del sito di oggi; confermare che va bene in home.
12. **Rivestimento in materiale composito** contro corrosione e abrasione (comunicato 2013): vale per le versioni di oggi? Tolto dalla pagina.
13. **Come stanno le bussole nel concio** e in quale giunto lavora il perno: la vecchia sezione ricostruita è stata tolta proprio perché era una nostra lettura dei disegni.
14. **Il video YouTube** "SISTEMI DI CONNESSIONE / Conci attrezzati con tecnologia EasyClick": confermare che si può incorporare (si carica solo al clic) e di chi è il cantiere ripreso.
15. **Testi in inglese**: scritti da noi a partire dai loro comunicati in inglese (tunnelbuilder.com); vanno riletti da loro.
16. Non in pagina perché incerti: "dal 1998" (la srl è del 2000), "24 paesi" (l'elenco ne nomina 11), aeroporti e strade, fatturato, numero di dipendenti, capitale interamente versato, PEC.

## Foto da fare dal vero

In pagina non c'è nessuna foto di repertorio. Le sole immagini sono loro: i tre render (nero su bianco, mostrati piccoli nelle schede) e il fotogramma del video. Per il sito vero serve una giornata con un solo fotografo e una sola luce per tutta la serie, al massimo due formati (3:2 e 16:9):

1. **Easy Click in studio**, la foto più importante: ogni versione da sola (Smart, Medium, Magnum, Smart HD, Hybrid) sullo stesso fondo grigio chiaro, stessa distanza e stessa luce morbida da sinistra, poi bussola e perno separati e agganciati. Sostituiscono i render nelle schede e possono entrare nell'apertura.
2. **Un concio attrezzato in stabilimento**, con la bussola annegata in vista, luce di giorno di taglio sul calcestruzzo.
3. **Persone di Impreservice al lavoro** a Grisignano: montaggio, controllo, magazzino; le mani sul pezzo, non lo sguardo in macchina.
4. **Un giunto antisismico posato su un impalcato**, con la squadra di posa, per la sezione Ponti e viadotti.
5. **La sede** di via Serenissima 8/b con l'insegna, per i contatti.
6. **Un anello appena posato** in un cantiere che si può nominare, con il permesso del committente, per le referenze.

## Licenze

- **Geologica** (Monokrom), Google Fonts, SIL Open Font License 1.1 (`sito/fonts/OFL.txt`): uso commerciale libero, file serviti dalla pagina.
- **Render, fotogramma del video e logo**: dell'azienda, presi dal loro sito e dal loro canale YouTube. Dettagli in `assets/CREDITI.md`.
- Nessuna immagine generata dall'IA, nessuna foto di repertorio, nessun disegno.

## Loghi

- In pagina c'è il simbolo blu (testata) e bianco (piede), ritagliati dai PNG del sito di oggi; il nome "Impreservice" accanto è composto in Geologica, perché un logo con la scritta non l'ho trovato.
- Da chiedere: il **logo vettoriale originale** (SVG, AI o PDF) e, se esiste, la versione con la scritta.

## Inglese

Il selettore IT / EN cambia i testi della pagina senza ricaricarla (testi inglesi negli attributi `data-en`, scelta ricordata nel browser) e si può aprire direttamente in inglese con `index.html?lang=en`. Nel sito vero conviene farne una pagina a sé (`/en/`), per i motori di ricerca.

## Pagine del sito nuovo (link di piede e referenze)

Il menu porta alle sezioni della home. Questi link puntano a pagine che nella proposta non esistono ancora:

| Pagina | File | Da dove ci si arriva |
|---|---|---|
| Easy Click (con le ancore `#smart`, `#medium`, `#magnum`, `#smart-hd-hybrid`) | `easy-click.html` | piede, colonna Prodotti |
| Ponti e viadotti | `ponti-e-viadotti.html` | piede |
| Referenze (i 42 cantieri) | `referenze.html` | sezione referenze ("Tutte le referenze"), piede |
| Azienda e brevetti | `azienda.html` | piede |
| Fiere e notizie | `notizie.html` | piede |
| Privacy, Cookie | `privacy.html`, `cookie.html` | riga legale del piede |
| Segnalazioni D.Lgs. 24/2023 | portale esterno già attivo, https://segnalazioni.impreservicesrl.it | riga legale del piede |

Social: solo YouTube (@Impreservicesrl). Newsletter: non prevista (due notizie in dieci anni, nessun catalogo).
