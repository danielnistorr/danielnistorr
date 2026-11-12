# Edera Country House in WordPress

Il sito è **lo stesso di ederacountry.it**, pagina per pagina: stessi testi, foto, colori, caratteri e calcolatore. Ora è fatto in WordPress con **Elementor** (la versione gratuita basta; va bene anche Elementor Pro).

- Le pagine sono tre: **Home**, **Informativa privacy** (`/privacy/`) e **Cookie** (`/cookie/`).
- Ogni testo, titolo, foto e bottone è un widget normale di Elementor (Titolo, Editor di testo, Immagine, Pulsante, Elenco icone). Si cambia dall'editor visuale, senza toccare codice.
- Il calcolatore "Preventivo flash" è un blocco unico, con i prezzi in un file a parte (sotto).
- Dal tema 1.1 c'è la **planimetria**: la foto dall'alto con i pallini degli spazi, subito dopo la sezione 01. È tutta in Elementor, pallini compresi (sotto, "La planimetria").
- Il tema dà l'aspetto: testata, menu del telefono, barra in basso sul telefono, piede, caratteri e colori.
- In più ci sono tre movimenti discreti, che si spengono con un clic.

## Cosa c'è in questa cartella

| File | A cosa serve |
|---|---|
| `edera-tema.zip` | Il tema da caricare in WordPress (4,6 MB, versione 1.2). Dentro ci sono anche foto, caratteri e PDF. |
| `edera-preventivo.zip` | Il plugin "Edera Preventivo": prezzi e regole del calcolatore dal pannello (menu Preventivo). Istruzioni in `EderaCountry-Sito/plugin/edera-preventivo/LEGGIMI.md`. |
| `edera/` | Lo stesso tema scompattato, da caricare via FTP se il pannello rifiuta lo zip. |
| `installa-su-server.sh` | Fa tutto da solo con WP-CLI, se sul server c'è l'accesso SSH. |

Il tema si rifà con un comando: `python3 EderaCountry-Sito/_sorgente/build.py`.

## Prima strada: WordPress nuovo su un sottodominio di prova (consigliata)

Il sito di oggi resta online finché il nuovo non è approvato.

1. **Sottodominio**: dal pannello Plesk crea per esempio `prova.ederacountry.it` e attiva il certificato HTTPS (Let's Encrypt).
2. **WordPress**: installalo sul sottodominio con *WordPress Toolkit* di Plesk (WordPress 6.4 o più recente, PHP 7.4 o più).
3. **Tema**: entra come amministratore. *Aspetto > Temi > Aggiungi tema > Carica tema*, scegli `edera-tema.zip`, poi *Installa ora* e *Attiva*.
   - Se WordPress dice che il file è troppo grande, carica via FTP la cartella `edera/` dentro `wp-content/themes/`, poi attivala da *Aspetto > Temi*.
4. **Elementor**: *Aspetto > Installa Edera*, bottone *Installa e attiva Elementor*.
   - Se non riesce, installalo da *Plugin > Aggiungi nuovo* (cerca "Elementor", *Installa*, *Attiva*) e torna su *Aspetto > Installa Edera*.
5. **Sito**: nella stessa pagina lascia spuntato "Nascondi il sito ai motori di ricerca" e premi *Installa il sito*. In un colpo:
   - carica le 15 foto (9 del sito, la foto dall'alto e 5 del Rustico) e il PDF dei servizi aggiuntivi nella libreria media;
   - crea le tre pagine in Elementor, con la planimetria nella Home;
   - imposta la Home come pagina iniziale e gli indirizzi belli (`/privacy/`, `/cookie/`);
   - spegne colori, caratteri e Google Fonts di Elementor, che cambierebbero l'aspetto;
   - mette nel cestino la pagina e l'articolo di esempio di WordPress.

Si può rilanciare quando vuoi: non crea doppioni, e una pagina che hai già modificato resta com'è (a meno di spuntare "Riscrivi anche le pagine cambiate nell'editor").

### Con SSH, un comando solo

Se hai SSH, `installa-su-server.sh` fa i passi 2-5 con WP-CLI. Se nella cartella non c'è WordPress, lo installa (chiede i dati del database; la password non si vede e non viene salvata) e crea l'utente `edera-admin` con una password che stampa una volta sola.

```
curl -sSLO https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/EderaCountry-Sito/wordpress/installa-su-server.sh
bash installa-su-server.sh /percorso/della/cartella https://prova.ederacountry.it tua@email.it
```

- Lo zip del tema si scarica da GitHub. Per usarne uno già sul server, aggiungilo come quarto argomento: `bash installa-su-server.sh ... ... ... /percorso/edera-tema.zip`.
- Sul sottodominio il sito resta nascosto ai motori di ricerca; su `https://ederacountry.it` è visibile.
- Si può rilanciare: non crea doppioni. Per riscrivere anche le pagine modificate: `EDERA_RISCRIVI=1 bash installa-su-server.sh ...`.

## Avete già il tema 1.0? Aggiornamento alla 1.1 (la planimetria)

Per chi ha già WordPress con il tema Edera 1.0 e le pagine installate. Le modifiche fatte alla Home restano.

1. *Aspetto > Temi > Aggiungi tema > Carica tema*, scegli il nuovo `edera-tema.zip`, *Installa ora*.
2. WordPress risponde che il tema c'è già: premi **"Sostituisci quello attuale con quello caricato"**.
   - Se lo zip è troppo grande per l'hosting, carica via FTP la cartella `edera/` in `wp-content/themes/` sopra quella che c'è.
3. *Aspetto > Installa Edera*, riquadro "Novità del tema 1.1": premi **"Aggiungi la planimetria alla Home"**. Il bottone:
   - carica la foto dall'alto e le 5 foto del Rustico nella libreria media;
   - aggiunge la sezione della planimetria subito dopo la sezione 01 ("Il luogo giusto per dare spazio alle idee.");
   - porta i numeri delle sezioni successive da 02-06 a 03-07 (si vedono solo sugli schermi da 1400 px), solo se erano ancora quelli;
   - dà al lightbox di Elementor i colori del sito, senza condivisione e senza zoom, se non li avevate già cambiati.

   Non tocca il resto della Home. Si può premere di nuovo: se la planimetria c'è già, non fa niente.
4. Non serve rilanciare "Installa il sito".

Con SSH basta rilanciare `installa-su-server.sh` come sopra: fa anche questo passo.

### Avete già il tema 1.1? Aggiornamento alla 1.1.1

1. *Aspetto > Temi > Aggiungi tema > Carica tema*, il nuovo `edera-tema.zip`, *Installa ora*, poi **"Sostituisci quello attuale con quello caricato"**.
2. Facoltativo: *Aspetto > Installa Edera* > **"Semplifica il link del Rustico"**. Cambia il link del pallino del Rustico da `#elementor-action...` a `#foto-rustico` e dà alla sua galleria l'ID CSS `foto-rustico`: così il Rustico segue la stessa regola degli altri pallini (sotto). Cambia solo quel link, e solo se è ancora quello scritto dal tema. Si può premere di nuovo senza effetti. Anche senza questo passo il vecchio link continua a funzionare.

Non premete "Aggiungi la planimetria alla Home": la planimetria c'è già, e comunque il bottone non la toccherebbe.

### Avete già il tema 1.1.1? Il plugin del preventivo e il tema 1.2

L'ordine conta: **prima il plugin, poi il tema**.
1. *Plugin > Aggiungi nuovo > Carica plugin*, `edera-preventivo.zip`, *Installa ora*, *Attiva plugin*.
   - All'attivazione il plugin copia i prezzi da `config/preventivo.php` del tema, anche se li avevate cambiati a mano.
   - Il calcolatore da quel momento è del plugin, con gli stessi prezzi: sul sito non cambia niente.
2. *Aspetto > Temi > Aggiungi tema > Carica tema*, `edera-tema.zip` (1.2), *Installa ora*, **"Sostituisci quello attuale con quello caricato"**.
3. Il tema nuovo sovrascrive i suoi file, anche `config/contatti.php`. Se in quel file avevate cambiato a mano email, telefono, indirizzo o partita IVA, scriveteli in *Aspetto > Personalizza > Recapiti*: un campo pieno vale più del file, un campo vuoto usa il file.

Né il plugin né il tema 1.2 toccano le pagine, i testi o i dati di Elementor: le modifiche fatte alla Home restano.

## Seconda strada: direttamente sul dominio

Solo quando il sito di prova è approvato, oppure se preferisci saltare la prova.

1. **Copia del sito di oggi**: dal *File Manager* di Plesk scarica tutto `httpdocs` (`index.html`, `privacy.html`, `cookie.html`, `servizi-aggiuntivi.pdf`, `img/`, `fonts/`). Una copia è anche in `EderaCountry-Sito/originale/`.
2. **Togli il sito statico**: sposta quei file in una cartella fuori da `httpdocs` (per esempio `vecchio-sito/`). È importante: se `index.html` resta, il server mostra lui e non WordPress.
3. Installa WordPress in `httpdocs` e segui i passi 3-5 della prima strada, oppure lancia lo script con `https://ederacountry.it`. Questa volta togli la spunta "Nascondi il sito ai motori di ricerca".
4. **Vecchi indirizzi**: chi ha salvato `privacy.html` o il PDF deve arrivare alle pagine nuove. Aggiungi in cima al file `.htaccess` di `httpdocs`, sopra le righe di WordPress:
   ```
   Redirect 301 /index.html /
   Redirect 301 /privacy.html /privacy/
   Redirect 301 /cookie.html /cookie/
   Redirect 301 /servizi-aggiuntivi.pdf /wp-content/uploads/edera/servizi-aggiuntivi.pdf
   ```
   Se il dominio usa solo nginx, gli stessi rinvii si fanno in Plesk, *Impostazioni Apache e nginx*.
5. Se il sito di prova era su un sottodominio e lo sposti sul dominio, dopo lo spostamento lancia *Elementor > Strumenti > Sostituisci URL* (da `https://prova.ederacountry.it` a `https://ederacountry.it`).

## Cambiare i testi e le foto

*Pagine > Home > Modifica con Elementor*. Un clic su un elemento della pagina apre il suo pannello a sinistra.

- **Titoli e testi**: si scrivono nel pannello o direttamente sulla pagina.
  - Il titolo d'apertura ha due parti tra `<span>`: ogni parte è una riga. Lo spazio tra "il" e "segno." è unificatore, così la riga non va a capo lì.
- **Foto**: clic sulla foto, poi sull'anteprima nel pannello, e scegli o carica un'altra immagine dalla libreria media.
  - Le foto di oggi hanno già le misure pronte. Una foto nuova va bene, ma conviene caricarla larga almeno quanto quella che sostituisce (per esempio 1500 px per l'apertura).
  - La foto d'apertura ha una versione verticale per il telefono ("Apertura, versione per il telefono" nella libreria media). Se cambi la foto d'apertura, sul telefono si vede la nuova, ritagliata al centro.
- **Bottoni**: testo e indirizzo nel pannello. Una freccia alla fine del testo (↗ o ↓) prende da sola lo stile dell'originale.
- **Aspetto**: lo danno le classi nel campo *Avanzate > Classi CSS* di ogni elemento (per esempio `pulsante pulsante-verde`, `g-a`, `n-sez`). Non vanno cancellate. Un bottone nuovo uguale a quelli del sito: classi `pulsante pulsante-verde` (o `pulsante-chiaro`).
- **Pagine legali**: *Pagine > Informativa privacy* (o *Cookie*) *> Modifica con Elementor*. Ogni sezione è un Titolo e un Editor di testo.
- **Testata, menu del telefono, barra in basso e piede**: sono nel tema. Email, telefono, indirizzo e partita IVA si cambiano in *Aspetto > Personalizza > Recapiti* (dal tema 1.2). Un campo vuoto usa il valore del file `config/contatti.php`. I recapiti della sezione "Contatti" della home si cambiano invece in Elementor.
- **PDF dei servizi aggiuntivi**: carica il nuovo PDF in *Media > Aggiungi file multimediale* e premi *Copia l'URL negli appunti*. Poi in Elementor clic sul calcolatore: nel blocco Shortcode, in `[edera_preventivo pdf="..."]` metti l'indirizzo copiato al posto di quello che c'è (oggi c'è il numero del PDF nella libreria media: vanno bene tutti e due).

Si salva con il bottone *Pubblica* (o *Aggiorna*) in alto a destra.

## La planimetria

*Pagine > Home > Modifica con Elementor*, sezione "Planimetria". Nel pannello *Struttura* (icona in alto) gli elementi hanno un nome: "Mappa e pallini", "Pallini (si spostano trascinandoli)", "Legenda e foto".

- **Spostare un pallino**: trascinalo sulla foto. Oppure: clic sul pallino, *Avanzato > Posizionamento*, e cambia l'offset orizzontale e verticale (in %).
  - L'offset verticale si conta sulla larghezza della foto, non sull'altezza: è il modo in cui Elementor lo calcola quando si trascina. Per questo valori oltre 100% sono normali (i pallini nella parte bassa).
- **Nome di un pallino**: è il testo del Pulsante. L'etichetta a destra o a sinistra si sceglie con le classi CSS (*Avanzato > Classi CSS*): `pallino`, più `pallino-sinistra` per metterla a sinistra.
- **Numeri**: li conta il tema, nell'ordine dei pallini nel pannello Struttura; la legenda accanto si numera allo stesso modo. Se aggiungi, togli o sposti un pallino nell'elenco, fai lo stesso con la riga della legenda (widget Elenco icone).
- **Il pallino del Rustico** (classe `pallino pallino-attivo`) ha il link `#foto-rustico`: apre con il lightbox di Elementor le foto della galleria che ha ID CSS `foto-rustico`. Nei siti aggiornati dalla 1.1 il link può essere ancora `#elementor-action...`: funziona lo stesso (vedi sopra, "Semplifica il link del Rustico"). Gli altri pallini non hanno link: sono segni con il nome.
- **Le foto del Rustico**: nel widget Galleria di base si aggiungono, tolgono o riordinano dalla libreria media. La didascalia nel lightbox è il titolo della foto nella libreria media.
- **Capienze**: nella legenda (Elenco icone), come sono scritte sul sito.
- **La foto dall'alto**: si cambia nel widget Immagine. È tenuta com'è, solo compressa. Se la nuova foto ha altre proporzioni, i pallini vanno risistemati.
- Sul telefono, e sugli schermi fra 901 e 1299 px dove la mappa sta in mezza colonna, sulla foto restano i numeri e i nomi stanno nella legenda (classe `etichette-mappa-larga` del contenitore "Mappa e pallini": togliendola i nomi restano sempre, ma possono accavallarsi).
- "Scegli nel preventivo" è un Pulsante che porta al calcolatore (`#preventivo`).

### Aggiungere le foto a un pallino (per esempio la Serra)

La regola: un pallino con il link `#foto-serra` apre il lightbox sulle foto della galleria che ha ID CSS `foto-serra`. Vale per qualunque nome: `#foto-piscina` e `foto-piscina`, e così via. Va bene una Galleria di base o un Carosello di immagini.

1. **Galleria**: nella colonna accanto alla mappa ("Legenda e foto") aggiungi un Titolo (per esempio "Serra") e un widget Galleria di base. Più semplice: duplica il titolo e la galleria del Rustico (tasto destro > Duplica), ma poi cambia l'ID CSS come al passo 3.
2. **Foto**: nella galleria, *Aggiungi immagini*, scegli o carica le foto della Serra nella libreria media.
3. **ID**: sulla galleria, *Avanzato > ID CSS*: `foto-serra` (senza cancelletto, minuscole, senza spazi).
4. **Pallino**: clic sul pallino della Serra, *Link*: `#foto-serra` (con il cancelletto). Se deve sembrare cliccabile come il Rustico, in *Avanzato > Classi CSS* scrivi `pallino pallino-attivo` (con `pallino-sinistra` in più se l'etichetta sta a sinistra).
5. **Foto solo nel lightbox** (facoltativo): sulla galleria, *Avanzato > Responsive*, nascondi su desktop, tablet e mobile. La galleria non si vede nella pagina, ma il pallino apre lo stesso tutte le sue foto.

Poi *Aggiorna*. Il testo sotto il titolo della sezione ("Seleziona il pallino sul Rustico per aprire le fotografie.") non cambia da solo: aggiornalo a mano, per esempio nominando anche la Serra. Se la galleria con quell'ID non c'è, il pallino non fa niente.

Nell'editor un clic su un pallino con link può far scorrere l'anteprima fino alla galleria (Elementor lo fa con i link interni alla pagina). Per spostare un pallino basta trascinarlo; per sceglierlo senza scorrere usa il pannello Struttura.

## Cambiare i prezzi del calcolatore

**Con il plugin "Edera Preventivo" attivo** (consigliato) i prezzi e tutte le regole si cambiano dal pannello, menu **Preventivo**. Lì ci sono anche i giorni esclusi con il calendario, i supplementi (per esempio il weekend), gli sconti, i minimi, i servizi aggiuntivi e i testi della mail. Le istruzioni sono nel LEGGIMI del plugin.

**Senza il plugin** vale quello che segue.


I prezzi sono in un file solo: `wp-content/themes/edera/config/preventivo.php`. Si apre da *Aspetto > Editor dei file del tema > config/preventivo.php* oppure via FTP. Ogni riga è spiegata nel file.

- Per ogni spazio: capienza (`persone`), prezzo base, persone comprese nel base, prezzo per ogni persona in più. La piscina ha due prezzi fissi, giornata intera e mezza.
- La tariffa stagionale: i mesi e il supplemento.
- L'email che riceve le richieste e l'avvertenza sotto la stima.

I numeri si scrivono con il punto per i decimali (`2.5`). Dopo il salvataggio basta ricaricare la pagina.

La richiesta parte come prima: "Invia per email" apre il programma di posta di chi scrive, con il riepilogo già pronto per edera@ederacountry.it. Il sito non riceve e non salva dati, quindi non serve un modulo come Contact Form 7.

## Movimenti

Tre movimenti discreti, tutti fermi a pagina ferma:
- **il titolo d'apertura sale riga per riga** quando la pagina si apre;
- **la grande foto della piscina** nella Gallery si scopre con un taglio netto dal basso, la prima volta che arriva sullo schermo;
- **la testata**: sugli schermi da 900 px in su resta a disposizione, si nasconde scendendo e torna salendo, con il fondo chiaro dopo l'apertura. Sul telefono resta com'era (lì c'è già la barra in basso con "Preventivo flash" e "Chiama").

**Spegnerli tutti**: *Aspetto > Personalizza > Movimenti*, togli la spunta "Movimenti attivi", *Pubblica*. Senza la spunta la pagina è identica al sito di oggi. Si possono spegnere anche scrivendo `define( 'EDERA_SENZA_MOVIMENTI', true );` in `wp-config.php`.

- Chi ha chiesto al telefono o al computer di "ridurre il movimento", e chi naviga senza JavaScript, vede sempre la pagina ferma e completa.
- Ogni movimento si accende con una classe nel campo *Classi CSS* in Elementor: `moto-righe` su un Titolo, `moto-taglio` su un'Immagine, `moto-testata` sul contenitore dell'apertura. Togliendo la classe si toglie quel movimento solo.
- Nell'editor di Elementor la pagina resta ferma, per lavorare comodi.

## Prima della messa online

1. **Motori di ricerca**: sul dominio vero togli la spunta in *Impostazioni > Lettura* ("Scoraggia i motori di ricerca"), se è rimasta.
2. **Indirizzo**: se il sito passa dal sottodominio al dominio, *Elementor > Strumenti > Sostituisci URL*.
3. **Cookie**: il sito pubblico non usa cookie (WordPress li usa solo per chi entra nel pannello), come oggi: il banner non serve. Se un giorno si aggiungono statistiche (Google Analytics, Tag Manager) o mappe incorporate, il banner diventa obbligatorio e la pagina Cookie va aggiornata.
4. **Aggiornamenti**: WordPress ed Elementor vanno tenuti aggiornati (*Bacheca > Aggiornamenti*). Il tema non dipende da una versione precisa di Elementor.
5. **Elementor Pro**: se lo installate, non va usato il suo Theme Builder per testata e piede: li fa già il tema.

## Cosa sapere

- Il collaudo completo (misure, prove del calcolatore, editor) è in `EderaCountry-Sito/02-collaudo.md`.
- Elementor porta con sé i suoi script (anche jQuery): la home pesa circa 1,0 MB al telefono e 1,4 MB al computer al primo caricamento, contro 0,4 e 0,8 MB del sito statico. Con la compressione del server (attiva di solito su Plesk) il peso degli script si riduce di circa due terzi.
- Le pagine legali hanno lo stile del sito di oggi, diverso dalla home (carattere Bodoni Moda, toni sabbia): è stato replicato così com'è.
- La planimetria aggiunge al primo caricamento circa 180 KB al telefono e 255 KB al computer con la compressione del server (450 e 520 KB senza). Più della metà sono gli script del lightbox di Elementor, che Elementor carica appena nella pagina c'è una galleria con il lightbox.
- Da confermare con la struttura:
  - **"Spazio verde"** (il nome del prototipo) è lo "Spazio esterno" del sito, fino a 120 persone? Finché non è confermato, nella legenda non ha capienza.
  - La finestra delle foto nel prototipo si chiamava "Casetta rossa": sul sito è diventata "Rustico", come il pallino.
