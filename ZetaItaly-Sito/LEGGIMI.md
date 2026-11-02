# Zeta S.r.l., proposta di nuova homepage: LEGGIMI

Proposta non richiesta di una nuova home per https://www.zetaitaly.com (solo la home). Nessun contatto con l'azienda, niente pubblicato.

## Cosa c'è

- `sito/index.html`: la home finale, statica (si apre con file:///). `sito/img/`: solo le immagini usate, WebP in più larghezze. `sito/fonts/`: i tre caratteri serviti dalla pagina.
- `screenshot/home/`: screenshot a 1440 e 390 (intera e prima schermata), chiusura e piede a 1440, e `NOTA.md` (idea, cosa è cambiato nell'ultimo giro, schermate, caratteri, colori, interazione, foto, controlli).
- `01-analisi.md`: fatti con le fonti; `assets/CREDITI.md`: origine e licenza di ogni immagine.
- `_prova/script/build_finale.sh`: rifà immagini (`busta_img.py` per l'apertura, `finale_img.py` per le altre), caratteri, screenshot (`screenshot_finale.mjs`), collaudo (`collaudo.mjs`) e segnali. La pagina è scritta a mano. Le posizioni delle tasche nel CSS dell'apertura sono le percentuali stampate da `busta_img.py`: se si cambia la foto vanno rimisurate. `giro.sh` fa screenshot di prova a pezzi.
- `_prova/home/a` e `_prova/home/b`: i due prototipi; il giudice ha scelto A.

## Pagine che il sito nuovo deve avere (collegate dal piede)

Stessi indirizzi di oggi, così non servono redirect:

- `/chi-siamo/`, `/storia/`, `/ecosostenibilita/`, `/pvc-bio-origine-100-vegetale/`
- `/prodotti/` e le categorie `/categoria-prodotto/<nome>/`: in piede `raccoglitori-ad-anelli`, `buste-pvc`, `cartelle-cartelline`, `copertine-e-sovraccoperte`, `portadocumenti`, `album-fotografici`, `bioplastica`; le altre (custodie e buste per accessori, portaprezzi e promostop, pet food, medicali) restano nella pagina Prodotti
- `/contatti/`, `/privacy/`, `/cookies/` (oggi gestite da iubenda)
- Lingue: i domini attuali `zetaitaly.co.uk`, `.fr`, `.de`, `.es` (nel piede); `.at`, `.ch`, `.be` da decidere.

Nella home le voci del menu portano alle sezioni della pagina (#prodotti, #materiali, #storia, #contatti). Il bottone "Chiedete un preventivo" apre una mail a info@zetaitaly.com; nel sito vero può portare al modulo di `/contatti/`.

Colore: il fondo è il verde del marchio Zeta molto schiarito (#D9E7DF), non un beige: è il fondo che si vede attraverso la busta d'apertura. Va bene anche per il sito vero se Zeta tiene il verde del logo.

Newsletter: no, e non va collegata a niente. Zeta lavora su commessa per aziende, non ha notizie, fiere, cataloghi scaricabili o collezioni; LinkedIn basta.

## Dati da confermare con Zeta

In pagina c'è solo quello che ha una fonte in `01-analisi.md`. Restano da chiedere:

1. **La foto d'apertura**: che articolo è esattamente la busta a quattro spazi (`2019_12_busta-pvc-4-spazi.jpg`), se è in PVC cristal (in pagina c'è solo "busta in PVC a quattro spazi per raccoglitori ad anelli") e se le sue saldature sono ad alta frequenza. La foto è stata **raddrizzata in prospettiva, specchiata e trasformata in un film con trasparenza**: i riflessi e le saldature vengono dalla foto, il resto della foto (il fondo nero) è tolto. Da 601 px in su è anche **ruotata di 90 gradi**. Va detto all'azienda, e va rifatta dal vero (sotto).
2. **Il titolo "Trasparente come il vetro"**: è la loro frase sul PVC cristal delle custodie per vinile ("PVC opaco o cristal, trasparente come il vetro"), usata qui per la busta. Confermare che vale anche per le buste.
3. **Il primato del 1994 nell'apertura**: la frase è del loro testo di Storia ("buste fotografiche straordinariamente trasparenti senza aloni azzurrati e senza sgradevoli anelli di Newton"). Va confermato che si può mettere accanto a una busta per raccoglitori, che non è un albumino.
4. **Le foto del selettore**: che la vaschetta porta campioni sia una valva termoformata saldata alla cartella (didascalia "Valva termoformata trasparente in una cartella porta campioni") e che la cartella campionario bianca sia in PVC opaco; il permesso di mostrare le cartelle colore del cliente che contiene (si leggono solo codici come "2GY", nessun marchio).
5. **Le persone nelle foto del 2023**: chi è l'uomo al tavolo (chiusura, didascalia "In reparto, 2023") e se è Gavriel Sacerdoti; chi è l'operatore alla linea (Storia). Il permesso di mostrarli. "Al tavolo di taglio" non è scritto in didascalia finché non è confermato.
6. **Gli originali del servizio 2023**: chi l'ha fatto, i diritti, le versioni in alta risoluzione e gli altri scatti (in rete ci sono solo miniature da 200 px di saldatrici, bobine, controllo).
7. **Date e storia**: la Zeta esisteva prima del 1969 (LinkedIn dice 1967) e la home di oggi dice "oltre 50 anni"; il brevetto del 1994 (numero, se è ancora valido); se la linea automatica delle cartelle con molla del 1986 è ancora in uso.
8. **Macchine e produzione**: quante saldatrici ad alta frequenza, i robot che sigillano nelle buste i cartoncini delle tipografie (in home come fatto, dal loro testo di Chi siamo), quantità minime per articolo.
9. **Materiali sostenibili**: l'anno del PVC di origine vegetale (il certificato ISCC PLUS è del fornitore del materiale, non di Zeta); OK Compost dal 2019; "pannelli fotovoltaici sui tetti" dal 2022 ("stabilimenti" al plurale: quanti?).
10. **Settori**: se pet food e medicale si tengono in home; se le visiere COVID escono dal catalogo.
11. **Dati societari**: REA e PEC non trovati (il piede mostra ragione sociale, P.IVA e C.F., Registro Imprese di Padova, capitale sociale 51.480 euro i.v.); il codice ATECO dei database (20.10.00) non corrisponde al mestiere; se il fax 049 8070219 è ancora attivo; correggere l'email sbagliata "info@www.zetaitaly.com" nella pagina Chi siamo di oggi.
12. **Certificazioni**: la meta description di oggi dice "Qualità certificata", ma il sito non mostra certificati di qualità dell'azienda; in home non c'è nessuna certificazione aziendale.
13. **Lingue** del sito nuovo e l'errore di oggi (schede in francese nella home italiana).

## Foto da rifare dal vero

Le foto di prodotto di Zeta sono del 2019 su grigio scuro con polvere, o del 2015 su velluto nero con flash: in pagina sono state scontornate e posate sul piano verde chiaro della pagina (#CFDFD6), ma è un ripiego. Mezza giornata di still life basta per tutta la home.

- **Apertura**: la stessa busta a quattro spazi, vuota, fotografata dall'alto e perfettamente in piano, su un fondo verde chiaro uniforme (cartoncino tinto vicino a #D9E7DF, o direttamente sopra un foglio con il titolo stampato, per avere la trasparenza vera). Ci vuole luce grande e morbida da un lato, con un solo riflesso lungo sul film, senza polvere e senza impronte. Ottica 85-100 mm, f/8-11, almeno 6000 px di lato lungo, e una seconda versione con la busta in orizzontale. Con la foto vera il film non va più ricostruito: basta lo scontorno.
- **Saldature in macro**: la stessa busta, ottica macro 100 mm, luce radente che faccia leggere il bordo saldato e la saldatura ondulata tra le tasche.
- **Un articolo in tre materiali**, inquadrato sempre uguale (stessa posizione, stessa luce), per il selettore: cristal trasparente (con un foglio stampato dentro, per far vedere la trasparenza), opaco goffrato, colorato a Pantone.
- **Campioni di goffratura e di colore** (liscio, buccia d'arancia, similpelle) affiancati, dall'alto.
- **Reparto**: gli originali del servizio 2023; se si rifà, una persona alla saldatrice e mani al tavolo, luce naturale, foto orizzontali di almeno 3000 px: oggi la foto del tavolo (1200x500) e quella della linea (1024 px) sugli schermi retina si vedono morbide.
- Togliere sempre i marchi dei clienti dalle foto di prodotto, o chiedere il permesso.

## Licenze

- **Foto**: tutte di Zeta S.r.l. (dal loro sito), usate come materiale loro per la proposta. Nessuna foto esterna nella home finale; nessuna immagine generata dall'IA. Le dieci foto esterne in `assets/esterne/` (Unsplash e Pexels, licenze in `assets/CREDITI.md`) non sono usate.
- **Caratteri**: General Sans e Switzer, Indian Type Foundry, distribuiti da Fontshare con la ITF Free Font License (uso commerciale gratuito, anche web). Per il sito vero vanno scaricati da fontshare.com per il dominio di Zeta.

## Loghi

- In pagina il logo è il PNG con trasparenza del loro sito (`assets/originali/logo-zeta-2268x1098.png`, verde #0A6B42), ritagliato e convertito in WebP a 300 e 600 px (1x e 2x). Non è ricostruito in SVG.
- Non esiste un SVG vero: `favicon.svg` contiene solo un PNG, e il vettoriale estratto dalla scheda PDF del 2024 (`logo-zeta-variante-arrotondata-da-pdf.svg`) è un ridisegno con angoli arrotondati e la A senza occhiello: non va usato.
- Da chiedere a Zeta il file vettoriale originale (AI, EPS o PDF). In alternativa il logo, fatto solo di linee rette, si può ricostruire a poligoni sul PNG, verificando che combaci al pixel.
