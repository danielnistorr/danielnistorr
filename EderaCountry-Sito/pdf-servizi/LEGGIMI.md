# PDF "Servizi e dotazioni"

Stessa grafica del PDF originale (A4, Newsreader e Jost, foto della piscina), con i contenuti aggiornati a novembre 2026.

- `servizi.html`: il testo e lo stile. Si cambiano qui voci, prezzi e note.
- `crea-pdf.cjs`: rifà il PDF con Chromium.
  `node EderaCountry-Sito/pdf-servizi/crea-pdf.cjs "$PWD/EderaCountry-Sito/pdf-servizi/servizi.html" EderaCountry-Sito/pdf-servizi/servizi-aggiuntivi.pdf`
  Il controllo stampa "altezza contenuto/foglio": se il primo numero supera il secondo, il testo non sta in una pagina.
- Caratteri: istanze statiche (TrueType) dei file variabili di Jost e Newsreader (SIL OFL), così il PDF incorpora caratteri normali e non "Type 3".
