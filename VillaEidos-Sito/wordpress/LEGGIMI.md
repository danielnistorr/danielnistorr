# Villa Eidos in WordPress

Il sito di Villa Eidos (uffici, sedi di rappresentanza, sale riunioni e sala conferenze in una villa storica con barchessa ad Albignasego) è un tema WordPress con le pagine fatte in **Elementor** (la versione gratuita basta).

- Le pagine sono tre: **Home**, **Informativa privacy** (`/privacy/`) e **Cookie** (`/cookie/`).
- Ogni testo, titolo, foto e bottone è un widget normale di Elementor (Titolo, Editor di testo, Immagine, Pulsante). Si cambia dall'editor visuale, senza toccare codice.
- La **foto d'apertura** oggi è la sala conferenze (le finestre ad arco della barchessa): tiene il posto della foto della villa, che manca. Quando arriva si cambia con un clic (sotto, "La foto della villa").
- Gli **spazi** sono schede con la foto: ogni link "Richiedi" porta al modulo e sceglie già il tipo di spazio.
- Il modulo **Richiesta di disponibilità** prepara una mail per eidos@eco-management.it nel programma di posta di chi lo compila: il sito non riceve e non salva dati.
- Il tema dà l'aspetto: testata, menu del telefono, piede, carattere (Fustat) e colori. Il movimento è quasi nullo e si spegne con un clic.

## Cosa c'è in questa cartella

| File | A cosa serve |
|---|---|
| `villaeidos-tema.zip` | Il tema da caricare in WordPress (circa 0,45 MB, versione 1.0.0). Dentro ci sono foto, logo e carattere. |
| `villaeidos/` | Lo stesso tema scompattato, da caricare via FTP se il pannello rifiuta lo zip. |
| `installa-su-server.sh` | Fa tutto da solo con WP-CLI, se il server ha l'accesso SSH. |

Il tema e l'anteprima statica (`VillaEidos-Sito/anteprima/`) si rifanno con un comando: `python3 -I VillaEidos-Sito/_sorgente/build.py`.

## Installare su Aruba (il dominio è registrato lì)

Oggi villaeidos.it mostra la pagina di parcheggio di Aruba: il dominio c'è, manca lo spazio del sito. Servono un piano di hosting Aruba collegato al dominio (Hosting Linux, oppure un piano con WordPress già installato) e un database MySQL, che il piano comprende.

I nomi dei menu qui sotto vengono dalle guide del pannello di Aruba lette il 17/11/2026 (pagine di Aruba e una guida di Aranzulla): se Aruba li ha cambiati, la guida ufficiale è su guide.hosting.aruba.it, voce WordPress.

### 1. WordPress dal pannello (Softaculous)

Tutti i piani Hosting Linux di Aruba hanno Softaculous, che installa WordPress in pochi passaggi.

1. Su aruba.it, **Area clienti**, poi **Hosting e Domini**: entra con utente e password.
2. In **Domini**, accanto a villaeidos.it, **Pannello di controllo**.
3. A sinistra **Applicazioni**, poi **Softaculous App Installer**; nel riquadro WordPress, **Installa**.
4. Impostazioni:
   - dominio villaeidos.it, campo **Cartella vuoto** (il sito sta nella radice del dominio);
   - lingua **Italiano**, ultima versione di WordPress;
   - se chiede i dati del database, sono nella mail di Aruba di attivazione di MySQL;
   - nome del sito "Villa Eidos";
   - **utente amministratore e password robusta**: salvala subito in un gestore di password, non mandarla per mail;
   - togli la spunta ai plugin suggeriti: il sito non ne ha bisogno.
5. **Installa**. Il pannello del sito è su `https://villaeidos.it/wp-admin`.

Senza Softaculous si può caricare WordPress via FTP: si scarica lo zip da it.wordpress.org, si scompatta e si caricano i file nella cartella principale del dominio con FileZilla (dati FTP nella mail di attivazione di Aruba: server `ftp.villaeidos.it`, porta 21, FTP esplicito su TLS se disponibile). Poi si apre il sito e si segue la procedura di WordPress.

Prima di andare avanti:
- **HTTPS**: il certificato SSL deve essere attivo sul dominio (dal pannello di Aruba) e in WordPress, *Impostazioni > Generali*, i due indirizzi devono cominciare con `https://`.
- **PHP**: se il pannello lascia scegliere la versione di PHP, va bene la 8.2 o più recente (il tema chiede almeno la 7.4).

### 2. Il tema

1. *Aspetto > Temi > Aggiungi tema > Carica tema*, scegli `villaeidos-tema.zip`, *Installa ora*, *Attiva*.
   - Se WordPress rifiuta lo zip, carica via FTP la cartella `villaeidos/` dentro `wp-content/themes/` e attivala da *Aspetto > Temi*.
2. *Aspetto > Installa Villa Eidos*, bottone **Installa e attiva Elementor**. Se non riesce: *Plugin > Aggiungi nuovo*, cerca "Elementor", *Installa*, *Attiva*, e torna su *Aspetto > Installa Villa Eidos*.
3. Nella stessa pagina lascia spuntato "Nascondi il sito ai motori di ricerca" finché il sito è in prova, e premi **Installa il sito**. In un colpo:
   - carica nella libreria media la foto d'apertura e le quattro foto degli spazi, con le misure già pronte;
   - crea le tre pagine in Elementor;
   - imposta la Home come pagina iniziale e gli indirizzi belli (`/privacy/`, `/cookie/`);
   - spegne colori, caratteri e Google Fonts di Elementor, che cambierebbero l'aspetto;
   - mette nel cestino le pagine e l'articolo di esempio di WordPress.

Si può rilanciare quando vuoi: non crea doppioni, e una pagina che hai già modificato resta com'è (a meno di spuntare "Riscrivi anche le pagine cambiate nell'editor").

### Con SSH, un comando solo

Sull'hosting condiviso di Aruba l'accesso SSH di solito non c'è: in quel caso vale la strada qui sopra. Se il server ha SSH (per esempio un server cloud), `installa-su-server.sh` fa tutto con WP-CLI: se nella cartella non c'è WordPress lo installa (chiede i dati del database, la password non si vede e non viene salvata) e crea l'utente `villaeidos-admin` con una password che stampa una volta sola.

```
bash installa-su-server.sh /percorso/della/cartella https://prova.villaeidos.it tua@email.it /percorso/villaeidos-tema.zip
```

- Senza il quarto argomento lo zip si scarica da GitHub (ramo `claude/benvegnu-sito`): funziona solo dopo il commit e il push.
- Su un sottodominio il sito resta nascosto ai motori di ricerca; su `https://villaeidos.it` è visibile.
- Si può rilanciare. Per riscrivere anche le pagine modificate: `VILLAEIDOS_RISCRIVI=1 bash installa-su-server.sh ...`.

## Prima della messa online

1. **Ragione sociale e partita IVA**: oggi non le abbiamo e non sono inventate. Si scrivono in *Aspetto > Personalizza > Recapiti* (o in `config/contatti.php` del tema). Finché mancano, il piede scrive "Ragione sociale e partita IVA da completare" e il pannello lo ricorda in alto.
2. **Informativa privacy e Cookie**: completare i punti evidenziati `[DA COMPLETARE: ...]` (titolare, sede, fornitori, data). *Pagine > Informativa privacy > Modifica con Elementor*.
3. **Motori di ricerca**: togliere la spunta in *Impostazioni > Lettura* ("Scoraggia i motori di ricerca").
4. **Icona del sito**: *Aspetto > Personalizza > Identità del sito > Icona del sito*, con `VillaEidos-Sito/assets/web/logo/villaeidos-icona-512.png`. Senza, il tema usa già il marchio in SVG.
5. **Aggiornamenti**: WordPress ed Elementor vanno tenuti aggiornati (*Bacheca > Aggiornamenti*). Il tema non dipende da una versione precisa di Elementor.

## La foto della villa (un clic)

1. *Pagine > Home > Modifica con Elementor*.
2. Clic sulla foto a destra del titolo (la sala conferenze): a sinistra si apre il pannello **Immagine**.
3. Clic sull'anteprima della foto (**Scegli l'immagine**), poi *Carica file* e la foto della villa; *Inserisci file multimediale*.
4. *Aggiorna* in alto a destra.

Com'è meglio la foto:
- la cornice è **verticale, 4:5**, larga al massimo 480 px: va bene una foto verticale della facciata, oppure una orizzontale con il soggetto al centro (si ritaglia ai lati);
- almeno **1200 px di lato corto** (meglio di più): sullo schermo doppio dei telefoni e dei computer recenti resta nitida;
- nella libreria media scrivi il **testo alternativo** (cosa si vede: "La facciata della villa e la barchessa").

La foto della sala conferenze resta nella libreria media ("Apertura: la sala conferenze"): si rimette con lo stesso clic. Con la foto della villa in apertura, la sala conferenze resta solo nella sua scheda e non si ripete più.

## Cambiare testi e foto

*Pagine > Home > Modifica con Elementor*. Un clic su un elemento apre il suo pannello a sinistra; nel pannello *Struttura* (icona in alto) le sezioni hanno un nome: Apertura, Gli spazi, Il complesso, Per chi, Come arrivare, Richiesta di disponibilità.

- **Titoli e testi**: si scrivono nel pannello o sulla pagina.
- **Fatti sotto l'apertura** (A13, tangenziale, SS16, parcheggi, ingressi): ognuno è un Titolo e un Editor di testo nel contenitore "Fatti".
- **Foto degli spazi**: clic sulla foto, poi sull'anteprima nel pannello, e scegli o carica un'altra foto. Le schede sono 4:3 e la foto si ritaglia al centro; si vede al massimo a 1,25 volte la sua misura, quindi una foto nuova conviene larga almeno 1200 px.
- **Link "Richiedi" delle schede**: sono Pulsanti con il link `#disponibilita`. In *Link > Opzioni del link > Attributi personalizzati* c'è per esempio `data-tipo|Sala riunioni`: il valore dopo la barra deve essere uguale a uno dei tipi del modulo (`Ufficio o sede`, `Sala riunioni`, `Sala conferenze`) e lo sceglie da solo. Senza l'attributo il link porta al modulo senza scegliere.
- **Villa, Barchessa, Giardino, Parcheggi** ("Il complesso") sono Titoli con un Editor di testo sotto.
- **Il telefono** della richiesta è un Titolo con il link `tel:+390490990550`: se cambia il numero, vanno cambiati il testo e il link (e anche il bottone "Chiama" dell'apertura).
- **I tre ingressi** sono un elenco in un Editor di testo: ogni via apre Google Maps.
- **Aspetto**: lo danno le classi nel campo *Avanzate > Classi CSS* di ogni elemento (per esempio `scheda`, `scheda-foto`, `pulsante pulsante-verde`, `collegamento`). Non vanno cancellate. Un bottone nuovo uguale a quelli del sito: classi `pulsante pulsante-verde` (pieno) o `pulsante pulsante-filo` (a filo).
- **Testata, menu del telefono e piede**: sono nel tema. Telefono, email, indirizzi, ragione sociale e partita IVA si cambiano in *Aspetto > Personalizza > Recapiti*.

Si salva con *Pubblica* (o *Aggiorna*) in alto a destra.

## Il modulo di richiesta

È lo shortcode `[villaeidos_richiesta]` (sezione "Richiesta di disponibilità").

- Campi: azienda, nome e cognome, email, telefono, tipo di spazio (ufficio o sede, sala riunioni, sala conferenze), data indicativa, numero di persone, messaggio, presa visione dell'informativa.
- "Prepara la mail" mostra il testo della richiesta; "Apri la mail" lo apre nel programma di posta di chi scrive, già indirizzato a eidos@eco-management.it con l'oggetto "Richiesta di disponibilità, <tipo>, <azienda>"; "Copia il testo" lo copia, per chi non ha un programma di posta.
- L'indirizzo, l'oggetto e i tipi di spazio sono in `config/richiesta.php` del tema (*Aspetto > Editor dei file del tema*); le etichette dei campi in `parti/richiesta.html`.
- Il sito non riceve e non salva niente: non serve un plugin per i moduli e non servono cookie.

## Movimenti

Quasi niente, di proposito:
- la **testata si compatta** scorrendo (più bassa, logo più piccolo);
- la **foto d'apertura si scopre dal basso** con un taglio netto quando la pagina si apre, una volta;
- i bottoni si invertono di colpo al passaggio.

Niente dissolvenze e niente titoli che salgono. Si spengono in *Aspetto > Personalizza > Movimenti* (togli la spunta, *Pubblica*): la foto compare subito e la testata si compatta senza transizione. Oppure `define( 'VILLAEIDOS_SENZA_MOVIMENTI', true );` in `wp-config.php`. Chi ha chiesto al sistema di "ridurre il movimento", e chi naviga senza JavaScript, vede sempre la pagina ferma e completa. Nell'editor la pagina resta ferma.

## Cookie

Il sito pubblico non usa cookie: caratteri e immagini sono nel tema, la mappa è un link a Google Maps (nessuna mappa incorporata), il modulo non manda dati. WordPress usa cookie tecnici solo per chi entra nel pannello. Per questo il banner non serve. Se un giorno si aggiungono statistiche, mappe incorporate o video di terzi, il banner diventa obbligatorio e le pagine Privacy e Cookie vanno aggiornate.

## Cosa sapere

- Prove, pesi e voto: `VillaEidos-Sito/NOTA.md`. Direzione artistica: `VillaEidos-Sito/DIREZIONE-HE.md`.
- Elementor porta con sé i suoi script (anche jQuery): al primo caricamento la Home pesa circa 0,6-0,7 MB al computer e al telefono, senza compressione. Con la compressione del server il peso degli script scende di circa due terzi.
- Se installate Elementor Pro, non usate il suo Theme Builder per testata e piede: li fa già il tema.
