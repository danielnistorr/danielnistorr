# 03. Mappa delle pagine

Il sito attuale ha 14 pagine: la home senza testo, Chi siamo, sette gallerie "Lavorazioni per privati", tre "Lavorazioni per
l'industria", Dove siamo e la privacy (01). Le gallerie ripetono tutte lo stesso paragrafo e cambiano solo le foto. Il nuovo sito
le riordina per quello che viene a fare chi visita un serramentista (`_prova/linguaggio.md`, paragrafo 1): vedere che fanno il
suo lavoro, chiedere il sopralluogo, telefonare subito dopo un furto. Specifica completa, sezione per sezione, in
`_prova/spec.md`.

| Sito attuale | Nuovo sito | Slug | Perché |
|---|---|---|---|
| Home (slider di 5 foto, nessun testo) | **Home** | `/` | la fiancata del camion, le dieci lavorazioni con foto e sottotipi, lavori finiti, dopo un furto, l'azienda, la scheda del sopralluogo |
| Lavorazioni per privati (7 gallerie) | **Per la casa** | `/per-la-casa/` | una pagina con le sette lavorazioni, ognuna con la sua scheda (tipi, forme, colori visti nei lavori) e quattro foto; le ancore sostituiscono le sette pagine |
| Lavorazioni per l'industria (3 gallerie) | **Per le aziende** | `/per-le-aziende/` | le tre lavorazioni, i lavori per i Comuni, i dati per l'ordine |
| le foto delle 10 gallerie | **Lavori** | `/lavori/` | l'archivio dei lavori finiti: 129 foto con il nome del pezzo, senza le foto sfocate, col timbro data e i doppioni |
| Chi siamo, "I servizi" (effrazioni) | **Dopo un furto** | `/dopo-un-furto/` | il servizio che nessun concorrente mostra (02) diventa una pagina: telefono, cosa facciamo, il preventivo per l'assicurazione, il modulo con la foto del danno |
| Chi siamo | **Chi siamo** | `/chi-siamo/` | 1974, 1982, 1997; i mezzi; i quattro passi; per chi lavoriamo |
| Dove siamo e contatti (nessun modulo) | **Contatti** | `/contatti/` | la scheda del sopralluogo con misure e foto, le due sedi, quale sede risponde |
| Privacy e cookie (D.Lgs. 196/2003) | **Privacy** e **Cookie** | `/privacy/`, `/cookie/` | pagine WordPress semplici, testo nuovo sul Regolamento UE 2016/679 (da far scrivere: LEGGIMI) |

Più due blocchi comuni, globali con Ultimate Addons for Elementor:
- **Testata**: barra inchiostro "Furto o effrazione? Chiamate il 049 579 81 94" con le due sedi; testata bianca con il logo, il
  menu su una riga da 1025 px in su (con le tendine delle lavorazioni) e il telefono sempre a vista; sotto 1025 il bottone "Menu".
  È un widget HTML, identico nell'anteprima HTML, perché le tendine con i sottotipi non si fanno con il widget menu.
- **Piede**: ragione sociale completa, sede, unità locale, telefono, fax, email, PEC, P.IVA, REA, codice SDI, link a `/privacy/`
  e `/cookie/`.

## Sezioni per pagina

### Home
1. **Fiancata** (il camion): campo blu flotta con "Serramenti metallici", "Serramenti in alluminio da Borgoricco, dal 1974", la
   riga su chi progetta, costruisce e monta, "Padovano: Borgoricco (PD) · Varesotto: Brebbia (VA)", un solo invito "Chiedete un
   sopralluogo"; a destra la foto dell'autogru con la scritta ZOCCARATO.
2. **Per la casa**: sette lavorazioni con foto, nome, sottotipi e numero di lavori (35, 20, 18, 3, 6, 9, 8).
3. **Per aziende, negozi e stazioni di servizio**: tre lavorazioni (24, 3, 3), le compagnie di distribuzione carburanti, i due
   lavori per i Comuni.
4. **Lavori finiti**: otto foto in coppie, con il nome del pezzo; link alla pagina Lavori.
5. **Dopo un furto**: due righe, il telefono grande, due foto (serranda divelta, porta ripristinata).
6. **Fascia azienda** (alluminio): foto del 1974, 1974-1982-1997 in una frase, i quattro passi, la sede dall'alto.
7. **Sopralluogo e preventivo**: la scheda con le miniature da spuntare, le misure L x H, il comune che decide la sede, le foto
   del vecchio serramento; accanto le due sedi.

### Per la casa
1. Fiancata con l'indice delle sette lavorazioni; foto dello scorrevole effetto legno sotto il porticato.
2. Le sette schede, tutte uguali: nome, frase, tipi, forme o dettagli, colori visti nei lavori, link "Le N foto di ...", quattro
   foto (tre verticali per portoncini e porte interne) con il nome del pezzo. Ancore: `#finestre`, `#scorrevoli`, `#oscuranti`,
   `#portoncini`, `#porte-interne`, `#pergole`, `#speciali`.
3. Chiusura comune: "Chiedete un sopralluogo" con le otto miniature che aprono la scheda con la voce già spuntata.

### Per le aziende
1. Fiancata con l'indice; foto del punto vendita di una stazione di servizio.
2. Tre schede: Commerciali e industriali (`#commerciali`), Pensiline commerciali (`#pensiline`), Monoblocchi prefabbricati
   (`#monoblocchi`).
3. **Lavori per i Comuni** (`#comuni`): Laveno Mombello, dicembre 2021, porte di Villa Frua; Cocquio Trevisago, ottobre 2023,
   infissi dell'asilo nido Torre; con il CIG [DA CONFERMARE il permesso].
4. **Dati per l'ordine** (`#dati`): ragione sociale, sede, unità locale, P.IVA, REA, SDI, PEC, ATECO, recapiti.
5. Chiusura comune.

### Lavori
1. Fiancata con l'indice in due righe (Per la casa, Per le aziende); foto della villa col bovindo.
2. Dieci gallerie con le stesse ancore delle schede: per ognuna una griglia di foto orizzontali e una di verticali, didascalia col
   pezzo, link alla scheda della lavorazione; ogni foto si apre grande nel lightbox di Elementor.
3. Chiusura comune.

### Dopo un furto
1. Fiancata col telefono grande; foto della vetrata a terra.
2. **Cosa facciamo**: interveniamo in fretta, il preventivo per l'assicurazione, il serramento rimesso a posto; due foto.
3. **Quando chiamate, diteci**: comune e indirizzo, cosa è stato forzato, se si chiude ancora, casa o attività.
4. **Modulo d'intervento** (Contact Form 7 "Intervento dopo un furto") con le foto del danno; accanto telefono ed email.

### Chi siamo
1. Fiancata con il camion del 1974 in bianco e nero.
2. **Come siamo cresciuti**: 1974, 1982, 1997, oggi; foto aerea del 1982.
3. **I nostri mezzi**: autogru, furgoni nel piazzale, la sede dall'alto.
4. **Dal sopralluogo alla rifinitura**: i quattro passi.
5. **Per chi lavoriamo**: privati e professionisti, stazioni di servizio, Comuni.
6. Chiusura comune.

### Contatti
1. Fiancata col telefono e l'email; foto dei furgoni nel piazzale.
2. **Sopralluogo e preventivo** (`#scheda`): il modulo Contact Form 7 "Sopralluogo e preventivo", identico alla home; accanto le
   due sedi con "Apri in Google Maps" (nessuna mappa incorporata) e la PEC.
3. **Dopo la richiesta**: i quattro passi.

## Navigazione

Menu: **Per la casa, Per le aziende, Lavori, Dopo un furto, Chi siamo, Contatti**, in minuscolo con l'iniziale maiuscola. "Per la
casa" e "Per le aziende" hanno una tendina con le lavorazioni e i loro sottotipi (link alle ancore). Voce attiva in blu
sottolineata. Il telefono 049 579 81 94 sta in testata e nella barra del furto su ogni pagina. Da 1024 px in giù il menu si apre
dal bottone "Menu"; le tendine diventano voci che si aprono con il `+`.

Ogni vecchio URL ha il suo redirect 301 (`plugin/redirect-301.csv`, elenco in `_prova/spec.md`, paragrafo 20): le dieci gallerie
vanno alla scheda della loro lavorazione, `chi-siamo.html` a `/chi-siamo/`, `dove-siamo-contatti.html` a `/contatti/`,
`cookie-policy.htm` a `/cookie/`.
