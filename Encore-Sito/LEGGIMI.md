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

## Scelte rispetto al brief

- **Testo secondario.** Il "stone" `#8C857B` su avorio arriva a 3,2:1, sotto la soglia di leggibilità (4,5:1). Per filetti e testo su fondo scuro l'ho tenuto. Per il testo piccolo su avorio ho usato `#6E685F` (4,85:1).
- **Foto.** Vengono tutte da Pexels: Unsplash blocca le ricerche automatiche da qui. Per cinque foto su sei l'autore va letto sulla pagina Pexels, link in `assets/web/CREDITS.md`.
- **Stili comuni** (pulsanti, scala tipografica, margini) stanno nella sezione header. Se incolli le sezioni del Formato B una per una, la sezione header deve esserci.
- **Spaziature.** Tutte multipli di 8: lato 64, 40 o 16 px; sezioni 160, 112 o 80 px.

## Collaudo (9 ottobre 2026)

- Lighthouse 12, modalità telefono, sull'anteprima: **prestazioni 100, accessibilità 100, buone pratiche 100, SEO 100** (LCP 1,4 s, CLS 0,003).
- Nessuno scorrimento orizzontale a 1440, 768 e 375 px. Su telefono la tabella scorre dentro il suo riquadro.
- Provati con Chromium: menu a scomparsa su telefono, ancore, modulo (vuoto non parte, compilato mostra "Thank you.").
- **Non provato** l'import in WordPress. Il formato JSON è lo stesso di Benvegnù, che è stato collaudato su Elementor 4.3.3.
