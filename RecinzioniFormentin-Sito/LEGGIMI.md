# Recinzioni Formentin: proposta di nuova homepage

Proposta non richiesta di nuova home per Formentin Srl (insegna Recinzioni Formentin), via Lombardia 17, Villatora di Saonara (PD). Solo la home; nessun contatto con l'azienda, nessuna pubblicazione.

## Dove sono le cose

- `sito/index.html`: la home finale, statica (si apre con file:///). `sito/img/`: solo le immagini usate, JPEG a 1x e 2x, più `marchio.svg` (icona della scheda). La rete ondulata dell'apertura non è una foto: è disegnata in SVG dallo script nella pagina. `sito/fonts/`: Geologica e la sua licenza.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini (`finale_img.py`), pagina (copia `index.sorgente.html` in `sito/`) e screenshot (`shots.mjs`). Controlli: `misura.mjs` (scorrimento orizzontale da 320 a 2560), `prova_gesti.mjs` (campionario, menu, fisarmonica, console, collegamenti).
- `01-analisi.md`: fatti con le fonti, voti delle foto, direzioni, riferimenti. `assets/CREDITI.md`: origine e licenza di ogni immagine. `_prova/home/a` e `b`: i due prototipi.

## Dati da confermare con l'azienda

Nella pagina ci sono solo fatti presi dal sito di oggi (citati in `01-analisi.md`); questi vanno verificati prima di pubblicare:
- **P.IVA 00074590282**: presa da atoka.io, il sito di oggi non la mostra (ed è obbligatoria). Mancano anche REA, PEC, codice fiscale e capitale sociale, che quindi non sono in pagina. Va chiarita la sede legale (via Andorra 11, Padova, su atoka, oppure già via Lombardia 17).
- **L'anno**: "primi anni Settanta" (pagina Azienda) contro i "32 anni" di atoka; se c'è un anno preciso e un nome del fondatore, sono il contenuto datato che oggi manca. In pagina non scrivo da quando sono a Saonara: prima stavano in via Andorra; va chiesta la data del trasloco (la mappa fa pensare a febbraio 2018).
- **Produzione in sede**: che la rete ondulata e le colonne si producano ancora, e se ringhiere, inferriate e tettoie siano di produzione propria ("produciamo ed installiamo" sul sito, anni 2014-2015).
- **Le sette maglie della rete ondulata** (pagina `reti-ondulate/`): se sono ancora quelle di serie e se la misura indica la luce della maglia (il disegno la tratta così: passo = luce + filo). Il disegno dell'apertura è indicativo nella forma dell'onda (due onde per maglia, prese dalle foto loro) e va confrontato con un pezzo vero; il titolo "La rete ondulata la facciamo noi" presuppone che la producano ancora in sede.
- **La foto della rete posata** (`gallery_reti-ondulate_IMG_1130-1.JPG`, didascalia "Rete ondulata posata, in pannelli con telaio"): se è un loro lavoro, dove, e se il telaio è di loro produzione.
- **Betafence**: che siano ancora rivenditori e installatori ufficiali; se ForFence è un loro sistema o un prodotto di terzi; che i modelli citati (Decofor, Nylofor, Securifor, cancelli in kit EN 13241-1) siano ancora a listino.
- **Esposizione e preventivi**: i preventivi gratuiti; se l'esposizione si visita negli orari di negozio o solo su appuntamento (la home di oggi dice "previo appuntamento", Azienda dà gli orari). In pagina per ora "su appuntamento".
- **Orari e numeri**: lun-ven 8.00-12.00 e 13.30-17.30, sabato su appuntamento; quale numero mettere in evidenza (in pagina il fisso 049 760801, il cellulare 335 7740278 come secondo).
- **La posa**: in pagina "eseguita anche dal nostro personale", come sul sito; zona servita e se lavorano per imprese e comuni.
- **Il negozio di attrezzature edili**: se è ancora attivo (è citato nella riga del piede e nel link Attrezzature edili).
- **I tre lavori in alluminio**: luogo e anno di ognuno (le didascalie dicono solo cosa sono) e il permesso dei clienti a mostrarli.
- **Social e recensioni**: nessun profilo trovato; se esistono si aggiunge una colonna "Seguici" nel piede.

## Pagine a cui puntano i link del piede

Da creare nel sito nuovo, con redirect 301 dagli indirizzi di oggi (che hanno `/index.php/` dentro, elenco in `01-analisi.md` sez. 8):
- Prodotti: `/reti-metalliche/`, `/reti-ondulate/`, `/pannelli-modulari/` (ForFence e Betafence), `/cancelli/`, `/ringhiere-e-parapetti/`, `/inferriate/`, `/tettoie/`.
- Azienda: `/azienda/` (Chi siamo), `#produzione` (sezione della home), `/esposizione/`, `/posa-in-opera/`, `/attrezzature-edili/`, `/contatti/` (oggi dà 404).
- Note legali: `/privacy/` e `/cookie/` (oggi mancano del tutto).
I link della testata portano alle sezioni della home (Produzione, Prodotti, Lavori, Esposizione). Le sigle e le misure dei sistemi (ForFence, Securifor, Nylofor, Decofor, colonne da 80x80 a 200x200 mm, cancelli in kit EN 13241-1) sono uscite dalla home e vanno nelle pagine prodotto. Niente newsletter: il motivo è nella NOTA.

## Foto da rifare dal vero

La foto di repertorio rimasta (la chiusura) è un segnaposto e va sostituita; le foto loro sono piccole (800 px) e fatte col telefono, per questo in pagina non superano i 400 px CSS. Una giornata di scatti, reflex o mirrorless da 24 MP in su, luce del mattino o cielo coperto chiaro, niente HDR:
1. **Apertura** (oggi disegno SVG): un pannello o un rotolo della loro rete ondulata davanti alla parete chiara dell'esposizione o del capannone, frontale e in piano, obiettivo da 85-100 mm, luce radente da sinistra che porti l'ombra della rete sul muro; formato molto largo (3:1) con la rete nella metà bassa e la parete libera sopra per il titolo, più una versione verticale per il telefono. Con questa foto il disegno può restare come risposta al campionario oppure passare sotto, nella sezione produzione.
2. **Rete ondulata**: la rete in macro sul banco e la macchina che la produce, a piena risoluzione, luce laterale morbida; una foto 3:2 e possibilmente un rotolo e un pannello finiti.
3. **Posa**: le mani del loro personale che fissano un pannello alla piantana (è la foto con le persone che oggi manca; non l'ho presa dal repertorio perché farebbe passare uno sconosciuto per il loro personale).
4. **Lavori**: tre lavori recenti in alluminio antracite, di mattina, con luogo e anno, a piena risoluzione (così si possono mostrare più grandi).
5. **Chiusura** (oggi Pexels 38439497): una loro ringhiera o recinzione con l'ombra netta su un muro chiaro, sole basso; formato quasi quadrato (0,9:1) e una versione 4:3.
6. Facoltativo: l'esposizione in via Lombardia vuota e ordinata, i pannelli in fila.

## Licenze

- **Carattere**: Geologica, Google Fonts, SIL Open Font License 1.1 (uso commerciale libero), servito da `sito/fonts/` con il testo della licenza in `sito/fonts/OFL.txt`.
- **Foto di repertorio**: una sola, Pexels License (van der Wolf 38439497, chiusura): uso libero anche commerciale, attribuzione non richiesta, modifiche ammesse. Licenza letta sulla pagina della foto; URL, autore e data in `assets/CREDITI.md`. Il pannello verde (Pexels 20182917) e la recinzione bianca (Unsplash YCEJqQeEsYA) del giro prima non sono più in pagina.
- **Foto dell'azienda**: due della rete ondulata e tre lavori in alluminio dalle gallerie del sito di oggi; l'uso va confermato con l'azienda e, per le case riconoscibili, con i clienti.

## Logo

Non esiste un vettoriale pubblico: la versione migliore è `logoOmbra.gif` 740x744 (`assets/originali/logo-ombra-740x744.gif`). In pagina c'è un ridisegno in SVG fedele alla forma e ai colori del GIF (rete a rombo azzurra #5A94F7, F verde #08B508 fatta di una L e un quadrato), senza l'ombra nera e con il numero di maglie stimato (12x12); file in `_prova/script/marchio.svg`. Accanto, "Formentin / Recinzioni e cancelli" è composto in Geologica: è una proposta, non il logotipo di oggi (un grottesco nero largo con ombra, `logo-testata-1050x100.png`). Va chiesto il vettoriale originale con i colori ufficiali, e se l'insegna del negozio (rete grigia, scritta verde) è la versione attuale.
