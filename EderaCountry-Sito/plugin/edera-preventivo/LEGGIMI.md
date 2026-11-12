# Edera Preventivo

Il plugin che fa cambiare dal pannello di WordPress, senza toccare file, i prezzi e le regole del calcolatore "Preventivo flash" della Home.

- Si gestisce dal menu **Preventivo** del pannello, solo per gli amministratori.
- Il calcolatore sul sito resta uguale, con le stesse classi e lo stesso aspetto, e con le regole iniziali dà gli stessi numeri e la stessa mail di oggi.
- I conti li fa il browser di chi compila. La richiesta resta una mail precompilata: il sito non riceve e non salva dati.
- Il plugin non tocca pagine, testi o dati di Elementor: disegna soltanto lo shortcode `[edera_preventivo]`, che è già nella Home.
- È separato dal tema: resta anche se un giorno si cambia tema.
- Versione 1.0.1: capienza superabile ("Oltre la capienza") e fasce di prezzo per numero di persone.

## Installare (prima il plugin, poi il tema)

L'ordine conta. All'attivazione il plugin copia i prezzi da `config/preventivo.php` del tema attivo, comprese le modifiche fatte a mano. Il tema nuovo sovrascrive quel file.

1. **Plugin**: *Plugin > Aggiungi nuovo > Carica plugin*, scegli `edera-preventivo.zip`, *Installa ora*, poi *Attiva plugin*.
   - Da qui il calcolatore usa i prezzi del plugin. Sono quelli di oggi, quindi sul sito non cambia niente.
2. **Tema 1.2**: *Aspetto > Temi > Aggiungi tema > Carica tema*, scegli `edera-tema.zip`, *Installa ora*, poi **"Sostituisci quello attuale con quello caricato"**.
   - Con il plugin attivo, il tema 1.2 non carica più il suo calcolatore. Con il tema 1.1 il plugin funziona lo stesso: prende comunque il posto del calcolatore del tema.
   - Il tema nuovo sovrascrive i file del tema, anche `config/contatti.php`. Se avevate cambiato a mano email, telefono o indirizzo in quel file, ricopiateli dopo l'aggiornamento. Dal tema 1.2 si scrivono in *Aspetto > Personalizza > Recapiti*, senza toccare file.

## Aggiornare il plugin (dalla 1.0.0 alla 1.0.1)

1. *Plugin > Aggiungi nuovo > Carica plugin*, scegli il nuovo `edera-preventivo.zip`, *Installa ora*.
2. WordPress dice che il plugin c'è già: premete **"Sostituisci quello attuale con quello caricato"**.

Le regole già salvate restano come sono. Le impostazioni nuove partono spente: limite rigido sulla capienza e nessuna fascia, quindi sul sito non cambia niente finché non le cambiate voi dal pannello. Pagine e dati di Elementor non vengono toccati.

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
  - Vale per la data scelta nel calcolatore: senza data, nessun supplemento.
- **Sconti e minimi**: sconto per più spazi insieme, sconto oltre un numero di persone, minimo di partecipanti, spesa minima, arrotondamento del totale.
- **Servizi aggiuntivi**: nome, prezzo fisso o a persona. I servizi attivi diventano caselle nel calcolatore. Oggi l'elenco è vuoto: i servizi sono nel PDF.
- **Testi e invio**: email che riceve la richiesta, oggetto e testo della mail, nota sotto il prezzo (IVA), avvertenza, messaggi per data non disponibile e oltre capienza, testi per la capienza superabile e per le fasce.
  - Nel testo della mail i segnaposti si riempiono da soli: `{azienda}` `{email}` `{telefono}` `{tipo}` `{spazi}` `{data}` `{persone}` `{capienza}` `{durata}` `{totale}` `{servizi}` `{dettaglio}`.
  - `{servizi_riga}` scrive la riga "Servizi aggiuntivi: ..." solo se ce ne sono.
  - `{note_riga}` scrive le note della stima (oltre la capienza, fuori dalle fasce). Se il testo non ce l'ha, le note vanno da sole sotto la riga con `{persone}`: la riga "oltre la capienza" c'è sempre.
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
- I testi sono traducibili, con il dominio `edera-preventivo`.
