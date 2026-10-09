# Encore: landing page per WordPress + Elementor

Una sola pagina in inglese per Encore (Team Atelier Zero, Startup Generation Challenge Verona 2026, Sfida 02 "Da scarto a risorsa"), costruita con lo stesso generatore di Benvegnù. I testi sono quelli del brief, senza aggiunte. L'unica eccezione è "Thank you.", lo stato che compare dopo l'invio del modulo.

## Cosa c'è nella cartella

| Cartella / file | Contenuto |
|---|---|
| `elementor-json/pagine-complete-senza-pro/enc-01-home-completa.json` | **da importare**: la landing con header e footer già dentro, modello *Canvas* |
| `elementor-json/enc-01-home.json`, `enc-00-header.json`, `enc-99-footer.json` | la stessa pagina divisa in corpo, header e footer, per chi usa header e footer di sito |
| `html-fallback/` | Formato B: un file `.html` per sezione, da incollare in un widget HTML di Elementor |
| `anteprima/01-home.html` | la pagina completa, da aprire nel browser |
| `assets/web/` | le 6 foto in WebP (2 o 3 larghezze ciascuna) e `CREDITS.md` con le fonti |
| `logo/` | logo in SVG e PNG: orizzontale scuro e bianco, solo marchio, icona quadrata (generati da `_sorgente/logo.py`) |
| `plesk/encore-statico.zip` | la landing come sito statico (index.html + 20 file), pronta da caricare su un server |
| `screenshot/` | la pagina intera a 1440, 768 e 375 px |
| `_sorgente/` | `contenuti.py` (testi, stili, sezioni), `motore.py` e `build.py` di Benvegnù, `prepara_immagini.py` |

## Vedere la pagina subito

Apri `anteprima/01-home.html` nel browser, oppure dalla cartella `Encore-Sito` lancia `python3 -m http.server 8000` e vai su http://localhost:8000/anteprima/01-home.html

## Metterla su WordPress

1. WordPress con Elementor gratuito, contenitori attivi (*Elementor > Impostazioni > Funzionalità*), accesso da amministratore.
2. *Template > Template salvati > Importa template*: `enc-01-home-completa.json`.
3. Crea una pagina, *Modifica con Elementor*, inserisci il template e imposta la pagina come homepage (*Impostazioni > Lettura*).

Non servono altri plugin: menu, tabella e modulo sono dentro la pagina. Il modulo non spedisce nulla, mostra solo il ringraziamento come chiede il brief.

**Immagini.** Le sezioni sono widget HTML, quindi Elementor non copia le foto nella libreria media. Le foto vengono caricate da `raw.githubusercontent.com`, dal ramo `claude/benvegnu-sito` di questo repository, e funzionano solo se il repository è pubblico. Altrimenti carica i file di `assets/web/` nella libreria media e rigenera con `python3 _sorgente/build.py --base https://TUO-SITO/wp-content/uploads/AAAA/MM/`.

## Logo

Un anello aperto con un punto nel varco: il ciclo che si chiude, ogni chilo che torna al marchio. Accanto, ENCORE in Instrument Sans SemiBold spaziato, convertito in tracciati, così il file non dipende dal font. Il punto sta a destra e l'icona ha gli angoli vivi, per non ricordare l'icona di Instagram. È nell'header del sito ed è anche la favicon.

## Metterla online come sito statico (Plesk)

Il server di evoxconsulting.it usa Plesk (nginx). `encore.evoxconsulting.it` punta già allo stesso indirizzo IP.
1. Plesk: *Siti web e domini > Aggiungi sottodominio*: `encore`.
2. *Gestione file* del sottodominio: carica `plesk/encore-statico.zip` nella cartella principale, poi *Estrai*.
3. *SSL/TLS > Let's Encrypt* per il sottodominio.

La pagina ha `noindex`: va tolto quando si vuole che Google la trovi.

## Direzione (seconda versione, 9 ottobre 2026)

Su richiesta del committente la prima versione (avorio, Bodoni Moda, bordeaux) è stata sostituita da una impaginazione e una palette prese da evoxconsulting.it:
- **Hero:** video al vivo in loop (macchina da cucire su maglia, colori smorzati), titolo grande bianco in basso a sinistra, header trasparente con pulsante a pillola. Il video parte 2,5 secondi dopo il caricamento della pagina. Prima si vede il suo primo fotogramma come immagine fissa. Con "riduci movimento" attivo resta fermo.
- **Palette e carattere:** nero `#131316`, bianco, grigi caldi `#F5F5F3`. Un solo carattere, Instrument Sans: titoli grandi in peso 400, spaziatura stretta.
- **Sezioni:** ogni sezione si apre con un filetto e un'etichetta (il nome della sezione nel brief). I tre passi sono schede con foto. "Why Encore" e il risultato stanno su fasce scure. Il piè di pagina ha il marchio grande in filigrana.
- **Disegno del ciclo:** nella sezione "The solution" c'è un SVG con le cinque tappe (nomi presi dalla tabella del brief) e un punto che percorre il cerchio in 16 secondi. Su telefono le etichette diventano un elenco sotto il cerchio.

Non ho ripreso la numerazione di Evox con la lineetta lunga dopo il numero, perché le lineette sono vietate dal brief, né le schede con i numeri grandi.

## Scelte rispetto al brief

- **Font:** i Google Fonts sono collegati anche dentro la sezione header, perché in Elementor i widget HTML non li caricano da soli.
- **Foto e video:** le foto vengono da Pexels, il video da Mixkit (licenza libera, attribuzione non richiesta). Fonti e licenze in `assets/web/CREDITS.md`.
- **Spaziature:** tutte multipli di 8. Lato 48, 32 o 16 px; sezioni 160, 120 o 88 px.

## Collaudo (9 ottobre 2026)

- Lighthouse 12, modalità telefono, sull'anteprima: **prestazioni 100, accessibilità 100, buone pratiche 100, SEO 100** (LCP 1,1-1,4 s, CLS 0,001).
- Nessuno scorrimento orizzontale a 1440, 768 e 375 px.
- Provati con Chromium: menu su telefono, ancore, modulo (vuoto non parte, compilato mostra "Thank you.").
- **Import in WordPress provato** in locale (WordPress con SQLite, Elementor 4.3.3, tema Hello):
  - tutti e 3 i template entrano, con 22 elementi su 22 per la pagina;
  - la pagina con header e footer, modello Canvas, impostata come homepage, si vede come l'anteprima;
  - screenshot in `screenshot/wordpress-*.jpg`.
