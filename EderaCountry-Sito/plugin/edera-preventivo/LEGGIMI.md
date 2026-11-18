# Edera Preventivo

Il plugin che fa cambiare dal pannello di WordPress, senza toccare file, i prezzi e le regole del calcolatore "Preventivo flash" della Home.

- Si gestisce dal menu **Preventivo** del pannello, solo per gli amministratori.
- Il calcolatore sul sito resta uguale, con le stesse classi e lo stesso aspetto, e con le regole iniziali dà gli stessi numeri e la stessa mail di oggi.
- I conti li fa il browser di chi compila. La richiesta resta una mail precompilata: il sito non riceve e non salva dati.
- Il plugin non tocca pagine, testi o dati di Elementor: disegna soltanto lo shortcode `[edera_preventivo]`, che è già nella Home.
- È separato dal tema: resta anche se un giorno si cambia tema.
- Versione 1.0.1: capienza superabile ("Oltre la capienza") e fasce di prezzo per numero di persone.
- Versione 1.1.0: il riscaldamento (e ogni tariffa o supplemento) si applica solo agli spazi scelti; sedie, tavoli, panche, area piscina, audio e video, gazebo e servizi extra si aggiungono al prezzo, a persona, a pezzo o per fasce, con la disponibilità massima.

## Installare (prima il plugin, poi il tema)

L'ordine conta. All'attivazione il plugin copia i prezzi da `config/preventivo.php` del tema attivo, comprese le modifiche fatte a mano. Il tema nuovo sovrascrive quel file.

1. **Plugin**: *Plugin > Aggiungi nuovo > Carica plugin*, scegli `edera-preventivo.zip`, *Installa ora*, poi *Attiva plugin*.
   - Da qui il calcolatore usa i prezzi del plugin. Sono quelli di oggi, quindi sul sito non cambia niente.
2. **Tema 1.2**: *Aspetto > Temi > Aggiungi tema > Carica tema*, scegli `edera-tema.zip`, *Installa ora*, poi **"Sostituisci quello attuale con quello caricato"**.
   - Con il plugin attivo, il tema 1.2 non carica più il suo calcolatore. Con il tema 1.1 il plugin funziona lo stesso: prende comunque il posto del calcolatore del tema.
   - Il tema nuovo sovrascrive i file del tema, anche `config/contatti.php`. Se avevate cambiato a mano email, telefono o indirizzo in quel file, ricopiateli dopo l'aggiornamento. Dal tema 1.2 si scrivono in *Aspetto > Personalizza > Recapiti*, senza toccare file.

## Aggiornare il plugin (dalla 1.0.x alla 1.1.0)

1. *Plugin > Aggiungi nuovo > Carica plugin*, scegli il nuovo `edera-preventivo.zip`, *Installa ora*.
2. WordPress dice che il plugin c'è già: premete **"Sostituisci quello attuale con quello caricato"**.

Le regole già salvate restano come sono, e il plugin resta attivo. Le impostazioni nuove partono spente, quindi sul sito non cambia niente finché non le cambiate voi dal pannello:
- ogni tariffa vale su tutti gli spazi e si somma al prezzo dello spazio, come prima;
- i servizi già inseriti restano "Servizi extra", a prezzo fisso o a persona, con le stesse righe nella stima e la stessa mail;
- le voci del listino (sedie, tavoli, panche...) non ci sono finché non premete "Aggiungi le voci del listino" e non le attivate.

Pagine e dati di Elementor non vengono toccati. Lo stesso aggiornamento vale anche dalla 1.0.0.

## Dove si cambiano i prezzi

Menu **Preventivo**. Dopo ogni modifica premete **Salva le regole** (il bottone resta in fondo allo schermo). Se c'è un errore, per esempio un prezzo negativo o una data scritta male, le regole non si salvano: in cima compare cosa correggere, e quello che avete scritto resta nel modulo.

- **Spazi**: nome, capienza, prezzo.
  - "Base + persone in più": prezzo base fino alle persone comprese, poi un prezzo per ogni persona in più, fino alla capienza.
  - "Fisso per durata": un prezzo per la giornata intera e uno per la mezza, come la piscina.
  - Si sceglie anche se lo spazio è attivo, se è già scelto all'apertura e se ammette la mezza giornata.
  - Con ↑ ↓ si cambia l'ordine, con *Togli* si toglie. Sulla tariffa "sul primo spazio" conta l'ordine.
  - **Fasce per numero di persone** (facoltative): vedi la sezione qui sotto.
  - **Oltre la capienza** e **massimo assoluto di partecipanti**: in fondo alla sezione Spazi, vedi più giù.
- **Durate**: etichette, regola per la mezza giornata, note sotto il campo.
- **Tariffe e supplementi**: in certi mesi (oggi la tariffa stagionale, 125 € da ottobre a marzo), in certi giorni della settimana (per esempio il weekend) o in un periodo.
  - Valore fisso in euro o in percentuale.
  - Si applica sul primo spazio, su ogni spazio o sul totale.
  - **Si applica a**: gli spazi su cui vale (nessuno spuntato = tutti gli spazi). Vedi l'esempio del riscaldamento qui sotto.
  - **Voce separata nella stima**: il supplemento ha una riga sua ("Riscaldamento (Rustico, Serra): 250 €") invece di sommarsi al prezzo dello spazio. Il totale non cambia.
  - Vale per la data scelta nel calcolatore: senza data, nessun supplemento.
- **Sconti e minimi**: sconto per più spazi insieme, sconto oltre un numero di persone, minimo di partecipanti, spesa minima, arrotondamento del totale.
- **Servizi e dotazioni**: arredi, attrezzature e servizi extra che si aggiungono al prezzo. Vedi la sezione qui sotto.
- **Testi e invio**: email che riceve la richiesta, oggetto e testo della mail, nota sotto il prezzo (IVA), avvertenza, messaggi per data non disponibile e oltre capienza, testi per la capienza superabile e per le fasce.
  - Nel testo della mail i segnaposti si riempiono da soli: `{azienda}` `{email}` `{telefono}` `{tipo}` `{spazi}` `{data}` `{persone}` `{capienza}` `{durata}` `{totale}` `{servizi}` `{dettaglio}`.
  - `{servizi}` scrive le voci scelte con le quantità ("Sedie (65), Grill").
  - `{servizi_riga}` scrive le righe "Dotazioni: ...", "Servizi aggiuntivi: ..." e "Compresi nell'affitto: ...", solo quelle che ci sono.
  - `{note_riga}` scrive le note della stima (oltre la capienza, fuori dalle fasce, pezzi che non bastano). Se il testo non ce l'ha, le note vanno da sole sotto la riga con `{persone}`: la riga "oltre la capienza" c'è sempre.
  - `{supplementi_riga}` scrive i supplementi con "Voce separata nella stima". Se il testo non ce l'ha (e non ha `{dettaglio}`), vanno da soli sotto la riga con `{spazi}`.
  - Con le fasce, `{spazi}` scrive anche la fascia applicata, per esempio "Rustico (31-50 persone, 15 € a persona)".
  - Un testo nuovo lasciato vuoto torna a quello iniziale.
- **Prova**: un piccolo calcolatore con le regole salvate, per controllare un prezzo prima che lo veda un cliente. Mostra anche il testo della mail.

## Fasce per numero di persone

Servono quando uno spazio ha un prezzo sotto un certo numero di persone e un altro sopra. Si mettono nella riga dello spazio, sotto **"Fasce per numero di persone"**.

**Esempio pratico.** Rustico: fino a 30 persone 400 € fissi, da 31 a 50 persone 15 € a persona.
1. Menu **Preventivo**, sezione **Spazi**, riga del Rustico: aprite *Fasce per numero di persone* e premete *Aggiungi una fascia*.
2. Prima fascia: *Da* 1, *A* 30, *Tipo di prezzo* "fisso per la fascia", *Importo* 400.
3. *Aggiungi una fascia* ancora: *Da* 31, *A* 50, "a persona", *Importo* 15.
4. **Salva le regole**.

Risultato sul sito:

| Partecipanti | Stima | Riga nella stima e nella mail |
|---|---|---|
| 30 | 400 € | Rustico (1-30 persone, prezzo fisso) |
| 31 | 465 € (31 × 15) | Rustico (31-50 persone, 15 € a persona) |
| 50 | 750 € (50 × 15) | Rustico (31-50 persone, 15 € a persona) |

Con una data da ottobre a marzo si aggiunge come sempre la tariffa stagionale di 125 € sul primo spazio (31 persone: 465 + 125 = 590 €).

Come funzionano:
- Con almeno una fascia, quello spazio si calcola **solo con le fasce**, al posto di "base + persone in più" o del "fisso per durata".
- Vale la fascia in cui cade il numero di partecipanti (per uno spazio si contano al massimo le persone della sua capienza, come per il prezzo a persona).
- **A vuoto** vuol dire senza limite superiore ("da 31 persone" in su).
- **Mezza giornata**: un importo a parte, facoltativo. Vale se lo spazio ammette la mezza giornata; se è vuoto vale l'importo normale.
- Un numero che non cade in nessuna fascia: vale il prezzo normale dello spazio, e la stima e la mail lo segnalano ("Serra: per 10 persone non c'è una fascia di prezzo...").
- Tariffe e supplementi, sconti, servizi, minimi e arrotondamento si applicano dopo, come sempre.
- Le fasce si mettono in ordine da sole. Se due fasce dello stesso spazio si sovrappongono (per esempio 1-30 e 25-50), se "da" è più grande di "a" o se un importo è negativo, le regole non si salvano e in cima compare cosa correggere.
- Il testo della riga ("Rustico (31-50 persone, 15 € a persona)") si cambia in *Testi e invio > Fasce per numero di persone*.

## Riscaldamento solo su certi spazi

Ogni tariffa o supplemento ha le caselle **"Si applica a"**: si spuntano gli spazi su cui vale. Nessuna casella spuntata vuol dire tutti gli spazi, come prima.
- "Sul primo spazio scelto": il primo, nell'ordine della pagina, fra gli spazi spuntati che il cliente ha scelto.
- "Su ogni spazio scelto": ognuno degli spazi spuntati che il cliente ha scelto.
- "Sul totale": una volta sola, se il cliente ha scelto almeno uno degli spazi spuntati; in percentuale si calcola solo sul prezzo di quegli spazi.
- Se il cliente non ha scelto nessuno degli spazi spuntati, il supplemento non si applica.

**Esempio pratico.** Riscaldamento solo sul Rustico e sulla Serra, 125 € per spazio, da ottobre a marzo.
1. Menu **Preventivo**, sezione **Tariffe e supplementi**, riga "Tariffa stagionale".
2. *Nome*: Riscaldamento.
3. *Su che cosa*: "su ogni spazio scelto".
4. *Si applica a*: spuntate **Rustico** e **Serra**.
5. Se volete il riscaldamento su una riga a parte, spuntate anche **Voce separata nella stima**.
6. **Salva le regole**.

Risultato sul sito, 40 persone, una data di gennaio:

| Spazi scelti | Stima | Righe nella stima |
|---|---|---|
| Rustico + Serra | 1300 € | Rustico 825 €, Serra 475 € (con la voce separata: Rustico 700 €, Serra 350 €, Riscaldamento (Rustico, Serra) 250 €) |
| Serra + Piscina | 875 € | Serra 475 €, Piscina 400 € (con la voce separata: Serra 350 €, Piscina 400 €, Riscaldamento (Serra) 125 €) |
| Piscina + Spazio esterno | 800 € | Piscina 400 €, Spazio esterno 400 €: niente riscaldamento |

Con "sul primo spazio scelto" invece di "su ogni spazio", Rustico + Serra fanno 1175 €: il riscaldamento va solo sul Rustico. Da aprile a settembre il riscaldamento non c'è (Rustico + Serra, 40 persone: 1050 €). Con la voce separata, la riga va anche nella mail, sotto gli spazi.

## Servizi e dotazioni

Sezione **Servizi e dotazioni** (prima "Servizi aggiuntivi"). Ogni voce si apre premendo sul suo riassunto, per esempio "Sedie · 1 € a pezzo · max 65 · attivo", e mostra solo i campi che servono per il suo prezzo.
- **Gruppo**: "Dotazioni" o "Servizi extra". Nel calcolatore compaiono in quest'ordine, ognuno con il suo titolo.
- **Prezzo**:
  - *prezzo fisso*: una volta;
  - *a persona*: per il numero di partecipanti;
  - *a pezzo*: per la quantità. La quantità la scrive chi compila (da 1 al massimo disponibile) oppure è *automatica*, un pezzo ogni tante persone, arrotondato per eccesso (sedie 1, tavoli 8, panche 4);
  - *compreso nell'affitto*: 0 €, non si sceglie. Compare nel calcolatore sotto "Compresi nell'affitto" e nella mail.
- **Massimo disponibile** (0 = nessun limite): chi compila non può scrivere di più. Con la quantità automatica, se ne servono di più si contano quelli disponibili e la stima e la mail lo dicono ("Sedie: ne servono 80, disponibili 65: il resto da concordare con la struttura.").
- **Pezzi compresi nell'affitto**: quelli che non si pagano, poi il prezzo (50 sedie comprese, poi 1 € l'una).
- **Fasce per numero di persone** (facoltative), come quelle degli spazi: fisso per la fascia, a persona o a pezzo. Fuori da tutte le fasce vale il prezzo della voce, con una nota.
- **Disponibile solo con**: la voce compare solo se è scelto uno di questi spazi (l'area piscina con la Piscina). Se il cliente toglie lo spazio, la voce sparisce e perde la spunta.
- **Nota**: una riga sotto il nome ("Tavoli da 6-8 persone").
- Gli sconti valgono solo sugli spazi; le voci si aggiungono dopo, poi la spesa minima e l'arrotondamento, come prima.
- Nella stima: "Sedie (65 × 1 €): 65 €", "Audio e video (31-70 persone): 150 €". Quando al posto del totale c'è "Da valutare con la struttura", la mail ha solo i nomi e le quantità, senza euro.

**Aggiungi le voci del listino**: mette nel modulo, senza salvare, le voci del PDF che mancano (tavoli, panche, sedie, area piscina, audio e video, gazebo, grill, casetta bar, pulizia finale). Sono tutte spente: sul sito non cambia niente finché non mettete i prezzi, spuntate "Attivo" e salvate. Grill (80 €) e casetta bar (50 €) hanno già il prezzo del PDF; audio e video, gazebo e pulizia finale hanno 0 € da completare. Per la pulizia finale le fasce non ci sono: il PDF dice "da 80 a 300 €", decidete voi come dividerle.

**Esempio pratico.** Sedie a 1 € l'una, una per persona, al massimo 65; audio e video con prezzi per fasce.
1. Sezione **Servizi e dotazioni**: premete **Aggiungi le voci del listino** (se le voci non ci sono già).
2. Aprite **Sedie**: *Prezzo* "a pezzo", *Prezzo (€)* 1, *Quantità* "automatica, per persone", *Un pezzo ogni quante persone* 1, *Massimo disponibile* 65 (i nomi "sedia" e "sedie" ci sono già). Spuntate **Attivo**.
3. Aprite **Audio e video**: *Prezzo* "prezzo fisso", *Prezzo (€)* 150 (vale per un numero fuori dalle fasce). In *Fasce per numero di persone* premete tre volte *Aggiungi una fascia*:
   - *Da* 1, *A* 30, "fisso per la fascia", *Importo* 80;
   - *Da* 31, *A* 70, "fisso per la fascia", *Importo* 150;
   - *Da* 71, *A* vuoto, "a persona", *Importo* 2.

   Spuntate **Attivo**.
4. **Salva le regole**.

Risultato sul sito, Rustico + Serra, sedie e audio e video spuntati, nessuna data:

| Partecipanti | Stima | Righe delle voci |
|---|---|---|
| 25 | 855 € | Sedie (25 × 1 €) 25 €, Audio e video (1-30 persone) 80 € |
| 45 | 1345 € | Sedie (45 × 1 €) 45 €, Audio e video (31-70 persone) 150 € |
| 80 | 1575 € | Sedie (65 × 1 €) 65 €, Audio e video (da 71 persone, 2 € a persona) 160 €, e la nota "Sedie: ne servono 80, disponibili 65: il resto da concordare con la struttura." |

Sotto il nome delle sedie il calcolatore scrive quante ne conta ("65 sedie per 80 persone, il massimo disponibile"); nella mail c'è la riga "Dotazioni: Sedie (65), Audio e video".

## Oltre la capienza

In fondo alla sezione **Spazi**, l'impostazione **"Se chi compila scrive più persone della capienza degli spazi scelti"** ha tre scelte:
- **Limite rigido** (com'è oggi, ed è il valore iniziale): il numero torna alla capienza e sotto il campo compare il messaggio "oltre capienza".
- **Si può superare, con la stima**: chi ha scritto 52 su uno spazio da 50 manda la richiesta con 52.
  - Negli spazi con prezzo "base + persone in più" le persone in più si contano al prezzo per persona dello spazio (Rustico con 52 persone: 400 € + 32 × 15 € = 880 €).
  - Gli spazi a prezzo fisso, come la piscina, restano al loro prezzo, e una nota dice che l'importo non tiene conto delle persone in più.
  - Con le fasce, le persone in più usano la fascia che le contiene, oppure l'ultima fascia senza limite superiore. Se non c'è, al posto del totale compare "Da valutare con la struttura".
- **Si può superare, senza importo**: al posto del totale compare "Da valutare con la struttura".

Quando si può superare, sotto il campo compare "Capienza indicativa con gli spazi scelti: 50 persone...". Oltre la capienza, la stima e la mail hanno sempre la riga "52 persone, oltre la capienza indicata di 50: da valutare con la struttura."

**Massimo assoluto di partecipanti** (0 = nessuno): vale sempre, per evitare numeri assurdi come 5000. Con 150, chi scrive 151 si vede correggere il numero a 150, con il messaggio "oltre capienza".

Tutti questi testi si cambiano in *Testi e invio*. La **Prova** in fondo al pannello segue le stesse impostazioni.

## Escludere dei giorni

Sezione **Calendario e giorni esclusi**:
- **Date escluse**: *Aggiungi una data*, per festività o giorni già prenotati. La nota è solo per voi.
- **Periodi di chiusura**: *Aggiungi un periodo*, dal ... al ... (compreso).
- **Giorni della settimana chiusi**: per esempio il lunedì.
- **Preavviso minimo** in giorni: con 7, la prima data possibile è fra una settimana.
- **Finestra massima** in mesi: con 12, non si può scegliere una data oltre un anno.

Appena c'è almeno una di queste regole, nel calcolatore compare il campo **"Data dell'evento"** con un calendario. I giorni che non si possono scegliere sono barrati e non si selezionano. La data scelta finisce nella mail, scritta per esteso ("10 dicembre 2026"). Senza regole resta il campo "Data indicativa" di oggi.

Il calendario è flatpickr (licenza MIT), in italiano, ospitato nel plugin: nessun servizio esterno.

## Copia delle regole

Sezione **Copia delle regole**:
- **Esporta le regole**: scarica un file JSON con tutte le regole. Conservatelo prima di cambiamenti grossi.
- **Importa**: carica un file esportato. Prima di salvare, il plugin controlla le regole del file come quelle del modulo.
- **Ripristina i valori iniziali**: torna ai prezzi del file `config/preventivo.php` del tema attivo (con il tema Edera, quelli del sito originale). Chiede conferma.

## Se si disattiva

- Disattivato il plugin, il calcolatore torna quello del tema Edera, con i prezzi di `config/preventivo.php` del tema. Le regole del pannello restano salvate e tornano valide quando lo riattivate.
- Se lo **eliminate** da *Plugin*, il plugin cancella anche le sue regole (l'opzione `edera_preventivo_regole`). Pagine e contenuti non li ha mai toccati.

## Per chi sviluppa

- `includes/regole.php`: valori iniziali, lettura e controllo delle regole (opzione `edera_preventivo_regole`).
- `includes/admin.php`: la pagina del pannello, con nonce e controllo di `manage_options` su ogni azione.
- `includes/sito.php`: lo shortcode, registrato su `init` con priorità 20, quindi dopo il tema.
- `assets/calcolo.js` è il motore dei conti, usato dal sito e dalla prova. `assets/preventivo.js` collega il calcolatore della pagina.
- Dalla 1.0.1: `generali.oltre_capienza` (`rigido`, `stima`, `senza`), `generali.massimo_assoluto` e `spazi[].fasce` (`da`, `a` con 0 = senza limite, `modo` `fisso` o `persona`, `importo`, `importo_mezza` o null). Le regole salvate con la 1.0.0 non hanno queste voci: si leggono con i valori iniziali, cioè come prima.
- Dalla 1.1.0:
  - `tariffe[].spazi` (chiavi degli spazi, vuoto = tutti) e `tariffe[].riga` (riga a parte);
  - `servizi[].modo` anche `pezzo` e `incluso`;
  - `servizi[].gruppo` (`dotazione`, `servizio`), `quantita` (`cliente`, `automatica`), `persone_per_pezzo`, `massimo` (0 = nessun limite), `comprese`, `unita`, `unita_plurale`;
  - `servizi[].fasce` (`da`, `a`, `modo` `fisso`, `persona` o `pezzo`, `importo`) e `servizi[].spazi`.
  - Le regole della 1.0.x non hanno queste voci: `edera_preventivo_regole()` le completa con i valori che danno gli stessi conti, e così anche l'esportazione e un file importato della 1.0.x.
- I testi nuovi del calcolatore (righe della stima, prezzi, note delle voci) sono in `edera_preventivo_testi_js()`, traducibili; PHP e `calcolo.js` usano gli stessi.
- I testi sono traducibili, con il dominio `edera-preventivo`.
