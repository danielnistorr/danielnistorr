# Tecnoplastic, proposta di nuova home: LEGGIMI

Proposta non richiesta, solo la home. Non è stata pubblicata né inviata all'azienda.

- Pagina: `sito/index.html` con `sito/img/` e `sito/fonts/`. Si apre con file:///.
- Rifare tutto: `sh _prova/script/build_finale.sh` (immagini, caratteri, pagina, screenshot).
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md`). Analisi con le fonti: `01-analisi.md`. Prototipi: `_prova/home/a` e `_prova/home/b`.

## Pagine del sito nuovo a cui puntano i link

`/galleggianti/` (con `/galleggianti/taurus/`, `/supertec/`, `/fox/`, `/olympic/`, `/mouse/`, `/elettronici/` per Spider, Snake e Crab, `/accessori/`), `/filtri/` (con `/filtri/dolphin/`, `/whale/`, `/cartucce/`, `/accessori/`), `/chi-siamo/`, `/certificazioni/`, `/download/`, `/distributori/`, `/privacy/`, `/cookie/`, `/en/`. Link esterni: la brochure 2024 in PDF sul sito di oggi, Water Fitters, il canale YouTube, Google Maps.

## Da confermare con l'azienda

- Anno di fondazione: il sito dice 1994, Atoka "da 33 anni" (circa 1993); la P.IVA 00046450284 è molto bassa per il 1994 (società più vecchia, gli "anni 70" della frase di about-it?).
- "ISO 9001 dal 2004": è la prima emissione del certificato ICIM (04/10/2004).
- Logo ufficiale: in pagina c'è il marchio vettoriale della brochure più "tecnoplastic" in Comfortaa resa in tracciati. Va bene, o vale la scritta dell'insegna? Esiste un file vettoriale completo del logo?
- Il canale YouTube @tecnoplasticsrl (65 iscritti, 1 video): è loro e vogliono mostrarlo nel piede sotto "Seguici"? Se no, si toglie il blocco. Altri social non trovati.
- Water Fitters come "Negozio online" nel piede: che rapporto ha con Mondeo e con Tecnoplastic? Resta il link?
- REA, capitale sociale (Atoka: 47.000 euro, non certificato), PEC: non in pagina finché non li confermano; poi vanno nella riga legale del piede.
- 23 galleggianti e 7 accessori, contati dalla pagina del catalogo (Fox-Drink compare due volte).
- Gli "stampi termoplastici per conto di terzi" della brochure: lo fanno ancora? Meriterebbe una voce.
- Le macchine del reparto (presse, numero, tonnellaggi) per una prova in numeri.
- Lingue del sito nuovo: italiano e inglese come oggi? Francese e spagnolo (le brochure esistono)?
- Newsletter: non messa, perché non hanno notizie né fiere da comunicare, i clienti sono costruttori e distributori che ricevono la brochure annuale e i privati comprano da Water Fitters. Se un giorno servisse, va collegata a un servizio di invio con la casella del consenso.

## Foto da rifare dal vero

Oggi la pagina usa solo foto di Tecnoplastic, ma a bassa risoluzione (1000 px, PNG a 256 colori): per questo il Taurus d'apertura è mostrato al massimo alla sua misura nativa (corpo 456x642 px nel file, 347x488 a 1440) e il sezionato non supera 600 px di altezza. Lo still life qui sotto è il prerequisito per consegnare la pagina: con un file da 4000 px il Taurus d'apertura può crescere e restare nitido anche sugli schermi 2x.
- Taurus giallo intero (priorità alta), appeso al cavo con la punta in alto: still life su fondo neutro chiaro, luce morbida dall'alto e da sinistra, 4000 px sul lato lungo, cavo lungo almeno quanto il corpo, senza riflessi duri; meglio ancora una versione dentro una vasca di vetro con il pelo dell'acqua vero sopra la punta.
- Taurus sezionato, stesso set, senza numeri stampati (i numeri li mette la pagina).
- Le sei versioni (Taurus, Drink, EX, Fep, PUR, SiHF) con la stessa luce, lo stesso angolo e la stessa lunghezza di cavo.
- Dolphin in batteria da tre, stessa luce.
- Facciata con la fontana in formato pieno (priorità alta: oggi è una striscia 1600x373, mostrata a 1:1 in un riquadro alto 373 px e a 390 alta solo 186 px), di mattina, con una macchina vera e un 35 mm, inquadratura frontale e centrata sull'insegna; anche un taglio verticale per il telefono.
- Due ore in reparto per "Dallo stampo al collaudo": stampo aperto sulla pressa, il pezzo appena stampato, l'assemblaggio, il collaudo in acqua sotto depressione. È il materiale che manca di più (l'area foto della home è al 21,9 % contro il 35 % della guida).

## Note tecniche

- I caratteri si caricano dal `@font-face` senza preload, perché aperta come file:/// la pagina dava errori CORS sui preload. Sul server (http o https) si possono rimettere i due `<link rel="preload" ... crossorigin>` in testa.
- Controlli ripetibili: `node _prova/script/larghezze.mjs` (sbordi da 320 a 2560, testata, console) e `node _prova/script/prova_gesto.mjs` (gesto con mouse, tastiera e tocco, collegamenti, misure delle immagini).

## Licenze

- Foto: tutte di Tecnoplastic (sito e brochure 2024), elencate in `assets/CREDITI.md`. Le foto esterne in `assets/esterne/` (Pexels e Unsplash, licenze lette sulla pagina di ogni foto) non sono usate nella home finale.
- Caratteri: Red Hat Display e Red Hat Text, Google Fonts, SIL Open Font License 1.1, serviti dalla pagina (`sito/fonts/`, con i due file OFL). Comfortaa (OFL) solo dentro il logo, trasformata in tracciati.
- Loghi: il marchio "tp" è estratto senza ridisegno dalla brochure 2024 (`assets/originali/logo-marchio-tp.svg`); la parola è ricomposta in Comfortaa come nel logo della brochure, da far approvare. `logo-water-fitters.svg` è di terzi e non è usato.
