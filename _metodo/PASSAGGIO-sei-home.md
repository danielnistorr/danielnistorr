# Passaggio: sei home nuove con Mobbin

Questo file serve alla sessione nuova, aperta con il connettore Mobbin attivo. La sessione precedente non aveva Mobbin (i connettori si caricano all'avvio) e ha fatto solo l'analisi.

## La richiesta del committente (testuale)

> https://www.fmsistemisrl.it
> http://paragapelli.com/it/home/index.html
> https://www.daisyplast.it/daisyplast
> http://www.teklam.it
> https://www.marioagnoletto.it
> https://www.hambro.it
>
> rifai anche questi ma per piacere moderni, usa mcp mobbin per riprendere design, già quello di CFV mi fa cagare, per piacere fallo seriaemtne WOW come un designer di altissima gamma

Si fa solo la HOME di ognuna, come per Centro Filtri Veneto (era "solo homepage"). Se il committente chiede i siti interi, si allarga dopo.

## Perché la home di CFV è stata bocciata

`CentroFiltriVeneto-Sito/screenshot/home/home-1440.jpg`: corretta, utile, dati verificati, ma piatta e da manuale. Il giudice cieco le ha dato K1 6 per quattro volte. Le cause, in ordine:
1. la pagina è nata dal materiale (tre foto scarse dell'azienda) invece che da una direzione artistica;
2. le soglie numeriche interne (per esempio "area foto almeno 35 %" di `segnali.sh`) hanno bloccato scelte migliori e spinto verso impaginazioni prudenti;
3. il giudice premiava prima l'utilità (K3) e la correttezza, e solo dopo l'impressione.

## Cosa cambia nel metodo per queste sei

- Prima la direzione artistica: un'idea visiva forte per azienda, con immagine e tipografia protagoniste. Le informazioni servono, ma non fanno la pagina.
- Se le foto dell'azienda sono scarse (lo sono in tutte e sei, voti da 1 a 4 su 10), si usano foto di alta qualità con licenza libera come segnaposto dichiarati (elenco in `<Azienda>-Sito/assets/CREDITI.md`), e nel LEGGIMI si scrive lo scatto vero da fare. Mai costruire la pagina attorno a foto deboli. Niente immagini generate dall'IA.
- `segnali.sh` resta solo come controllo dei difetti da IA (lineette lunghe, Inter, card con bordo sinistro...): le soglie di area foto, numero di fasce e simili non sono bloccanti.
- Il giudice si chiede per prima cosa "uno studio di altissima gamma la firmerebbe?" (vedi sotto); utilità e voce vengono dopo.
- Mobbin: usarlo per davvero e citare nella nota di ogni home quali schermate o sezioni (app o sito, nome della schermata) hanno ispirato quale scelta. Attenzione: Mobbin è soprattutto app e prodotti digitali; per l'impressione da lusso contano anche i riferimenti del mestiere già raccolti in `<Azienda>-Sito/riferimenti/` (prime schermate a 1440 e 390) e descritti in `01-analisi.md`, sezione 7.

## Il gusto del committente

- Ha amato la home dell'osteria L'Angelo e il Diavolo (`AngeloEIlDiavolo-Sito/screenshot/home/`): un'idea sola che ha solo quell'azienda, colore deciso, calore, informazioni utili subito.
- Ha bocciato: CFV ("mi fa cagare"), le home industriali "troppo scarne" e "non adatte al contesto", e anche quelle troppo testuali ("non super mega testuale").
- Divieti espliciti: gradiente viola-blu, testo del titolo in gradiente, emoji nei titoli, Inter ovunque, card con bordo sinistro colorato, glassmorphism, modo scuro a basso contrasto, tre box con icona in fila, badge sopra il titolo, icone Lucide ovunque, componenti shadcn non toccati, sezioni che compaiono in dissolvenza allo scorrere, effetti che seguono il cursore, bottoni che sbiadiscono al passaggio, spaziature incoerenti, lineette lunghe, copy da parole d'ordine generiche, serif corsivo per le parole d'accento.
- Criteri ricalibrati del giudice: `_metodo/ricalibrazione-giudice/RAPPORTO.md`, sezioni 0 e 4. Per queste sei si aggiunge un K0 bloccante: "uno studio di altissima gamma la firmerebbe così com'è?" con voto almeno 8.

## Le sei aziende (dettagli in `<Azienda>-Sito/01-analisi.md`)

| Cartella | Chi sono davvero | Materiale | Direzione A | Direzione B |
|---|---|---|---|---|
| `FMSistemi-Sito` | Impianti elettrici e termoidraulici, clima, pompe di calore, fotovoltaico, Viessmann Partner, Vigonovo | 1/10 | "Materia": macro di rame, ottone, cavi su grafite, indice A-Z dei servizi | "Clima": interni in luce naturale, impianto invisibile, selettore Inverno/Estate |
| `ParagaPelli-Sito` | Ingrosso di pelle bovina, ecopelle e tessuti per arredo, contract, nautica, auto; LWG Gold | 3/10 | "La mazzetta": cartella colori, grana in macro, tono che cambia foto e scheda | "Pelle intera": reportage dal magazzino, bordo della pelle come segno |
| `Daisyplast-Sito` | Estrusione e saldatura di sacchi e shopper (vergine, rigenerato, compostabile) per grossisti | 3/10 | "La bolla": il film come materia preziosa, numeri come scheda tecnica | "Margherita": dal fiore del logo al compost, still life su fondi pieni |
| `Teklam-Sito` | Lavorazione lamiera: laser Bystronic, punzonatura, piega, saldatura, progetto 3D | 3/10 | "Il foglio": disegno quotato su acciaio, il pezzo davanti al foglio | "La scintilla": officina di notte, scintille su nero, spessori in scala vera |
| `MarioAgnoletto-Sito` | Incisore meccanico dal 1979: punzoni, fustelle, minuterie e accessori per calzatura e pelletteria | 4/10 | "Dritto e rovescio": punzone e impronta, titolo a specchio | "Tavola dei campioni": pezzi dall'alto con scala millimetrata |
| `Hambro-Sito` | Componenti per borse, cinture, scarpe: minuteria, lacci, nastri, rinforzi, fibbie ricoperte | 3/10 | "Sotto la pelle": still life su nero, una fibbia per schermata | "Campionario": griglia tecnica chiara, righello in mm |

Attenzione ai fatti che correggono le ipotesi iniziali: FM Sistemi e Teklam non lavorano per la moda; Paraga Pelli vende per l'arredo, non per la calzatura; per Daisyplast il compostabile è una linea su tre.

## Come ripartire in un contenitore nuovo

Le cartelle `_prova/`, `assets/originali/` e `assets/esterne/` sono escluse da git e nel contenitore nuovo non ci sono.
- Foto segnaposto: riscaricarle da `assets/CREDITI.md` (URL della foto e licenza) con curl; Unsplash e Pexels bloccano i browser automatici, curl funziona.
- Foto e logo dell'azienda: dal sito attuale, con gli URL citati in `01-analisi.md`.
- Strumenti: `_metodo/kit/` (`shoot.mjs` per gli screenshot, `slice.py` per tagliarli a pezzi, `segnali.sh`). Playwright si carica con `createRequire('/opt/node-tools/node_modules/')`; mai `playwright install`.

## Processo suggerito

Per ogni azienda: 3 prototipi (le due direzioni dell'analisi e una guidata da Mobbin), screenshot a 1440 e 390 guardati a pezzi, giudice cieco con K0 e K1-K7, home finale in `<Azienda>-Sito/sito/index.html`, screenshot in `<Azienda>-Sito/screenshot/home/` (home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, NOTA.md), LEGGIMI con i dati da confermare e gli scatti da fare. Gli agenti di un Workflow ricevono l'ultimo messaggio del committente: un giudice cieco va lanciato con lo strumento Agent, non dentro un Workflow, se quel messaggio contiene un suo giudizio.

## Regole fisse

- Il repository è pubblico: niente credenziali, niente materiali ESTARPRO, GEA o dei video.
- Tutto in italiano, mai il carattere U+2014.
- Niente dati inventati: ogni fatto con la fonte, il resto nel LEGGIMI.
- Non contattare le aziende, non inviare moduli, non pubblicare i prototipi.
- Ramo `claude/benvegnu-sito`; niente pull request se non richieste.
