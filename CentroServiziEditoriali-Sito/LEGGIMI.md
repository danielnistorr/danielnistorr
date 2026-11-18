# Centro Servizi Editoriali: proposta di nuova home

Proposta non richiesta, solo la home. Non è stata pubblicata né inviata all'azienda.

## Dove sono le cose
- `sito/index.html`: la home finale, scritta a mano (HTML e CSS in un file, un piccolo script per i formati e il menu).
- `sito/img/`: solo le immagini usate, in WebP in più larghezze; il logo anche in PNG.
- `sito/fonts/`: Piazzolla variabile (`piazzolla-latin.woff2`) e la sua licenza (`OFL-Piazzolla.txt`).
- `screenshot/home/`: screenshot a 1440 e 390, la chiusura, e la `NOTA.md` con idea, scelte e controlli.
- `_prova/script/finale_prove.mjs`: le prove finali (320, 768, 1024, 1920, scrollWidth da 320 a 2560, tastiera, tocco, collegamenti).
- `_prova/script/build_finale.sh`: rifà le immagini (`finale_img.py`), controlla la pagina a sei larghezze (`finale_check.mjs`) e rifà gli screenshot (`finale_shot.mjs`).
- `01-analisi.md`: i fatti con le fonti. `_prova/home/a` e `b`: i due prototipi da cui è nata la versione finale (A scelto dal giudice).

## Pagine che il sito nuovo dovrà avere (link del piede)
- **Pagine**:
  - `chi-siamo.html`
  - `galeati.html` (storia della Galeati dal 1816)
  - `contatti.html`
  - `stampa-in-rotativa.html`
  - `manualistica.html`
  - `postalizzazione.html`
  - `grafica-e-redazione.html`
  - `pagine-di-servizio.html` (pagine di servizio e infografiche)
  - `privacy-policy.html` (esiste già sul sito di oggi)
  - `cookie.html`
- **Ancore della home**: `#formati`, `#manuali`, `#postalizzazione`, `#grafica`, `#sedi` (la chiusura con le sedi e i recapiti), `#contenuto`.
- **Link esterni del Gruppo** (indirizzi finali, verificati con risposta 200 il 24/10/2026): https://www.galeati.it/, https://litostampaveneta.it/, https://3d-venice.com/.

## Dati da confermare con l'azienda
- **I modelli delle rotative**:
  - il sito CSE dice "2 Goss Universal giro macchina 578 e 600";
  - galeati.it dice Universal 75 e Universal 45 a Imola;
  - nelle foto di Grisignano si legge "Universal 75".

  In pagina c'è "2 rotative Goss Universal", con le 4 torri e le 64 pagine a colori.
- **Le copie dell'apertura** (foto 69): è un periodico locale stampato da loro. Va confermato che si possa mostrare (la testata si legge appena, in piccolo) e in che formato è, così da poterlo citare nella didascalia.
- **La rotativa MAN giro 630 dei manuali**: in quale sede sta. In pagina non c'è la sede.
- **Le linee Sitma**: dove sono e quante.
- **PEC e orari**: non pubblicati. Vanno aggiunti alla chiusura e al piede quando arrivano.
- **L'anno da dire**: 1983, 1994 (famiglia Comin) o 1997 (società attuale). In pagina non c'è nessun anno di CSE, solo Galeati 1816 e la rilevazione del 2014.
- **Il rapporto con Litostampa Veneta e con 3D Venice**, per la colonna "Gruppo" del piede: 3D Venice è una società distinta.
- **I diritti del reportage fotografico del 2020** (chi l'ha scattato, se l'uso copre il sito nuovo).
- **Le testate stampate e i clienti che si possono nominare.** Oggi in pagina non c'è nessun nome.
- **Le certificazioni**: FSC compare su galeati.it senza codice di licenza.
- **Il reparto Marketing e consulenza**: se va citato.

## Foto da rifare dal vero
1. **Lo still life dei loro prodotti, la prima cosa da commissionare.**
   - Cosa: un loro quotidiano, una rivista autocopertinata e un manuale, su fondo carta chiaro.
   - Luce: laterale e morbida, con un'ombra corta.
   - Inquadrature: una dall'alto e una a 30 gradi.
   - Perché: è la sola cosa che renderebbe la home impossibile da confondere con quella di un altro centro stampa.
2. **Le copie dell'apertura, in alta risoluzione.**
   - Cosa: la stessa scena della foto 69 (pile di copie appena piegate e la mano con il guanto), con luce più chiara e lo sfondo in ordine.
   - Formato: almeno 4000 px di lato. La sorgente di oggi, tagliata, è larga 1960 px: a 1440 è circa 1,4x, a 1920 è 1x.
3. **Imola e Mestre**: oggi tutte le foto sono di Grisignano. Servono la rotativa di Imola e il reparto grafico di Mestre, con la stessa luce del reportage.
4. **La squadra o la famiglia Comin**: una foto sul lavoro, non in posa.

## Licenze
- **Foto**: tutte dell'azienda (libreria media del sito, reportage di Grisignano). Diritti da confermare (vedi sopra). Nessuna foto esterna nella home finale. Le foto Unsplash e Pexels in `assets/esterne/` restano scaricate per i prototipi, con licenza in `assets/CREDITI.md`.
- **Carattere**: Piazzolla, Huerta Tipográfica, Google Fonts, SIL Open Font License 1.1 (uso commerciale libero, testo della licenza in `sito/fonts/`).

## Loghi
- Non c'è un SVG nel codice del sito di oggi.
- Il logo usato è l'orizzontale ricavato dal PNG trasparente da 4000 px (`2020-03-logoCSE_Black.png`), in PNG e WebP a 2x: 392 px per la testata (mostrato a 196) e 472 px per il piede (mostrato a 236).
- Non l'ho ridisegnato in SVG: l'anello cromato in sfumatura non sarebbe fedele.
- Va chiesto il file vettoriale originale.

## Newsletter e social
- **Newsletter**: niente. Il lavoro è B2B su commessa, il blog è vuoto, non ci sono fiere, cataloghi o clienti privati.
- **Social**: niente colonna "Seguici". Facebook e LinkedIn del sito puntano a `#`. Se esistono pagine vere, vanno aggiunte al piede come parole.
