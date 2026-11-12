# Edera Preventivo

Il plugin che fa cambiare dal pannello di WordPress, senza toccare file, i prezzi e le regole del calcolatore "Preventivo flash" della Home.

- Si gestisce dal menu **Preventivo** del pannello, solo per gli amministratori.
- Il calcolatore sul sito resta uguale, con le stesse classi e lo stesso aspetto, e con le regole iniziali dà gli stessi numeri e la stessa mail di oggi.
- I conti li fa il browser di chi compila. La richiesta resta una mail precompilata: il sito non riceve e non salva dati.
- Il plugin non tocca pagine, testi o dati di Elementor: disegna soltanto lo shortcode `[edera_preventivo]`, che è già nella Home.
- È separato dal tema: resta anche se un giorno si cambia tema.

## Installare (prima il plugin, poi il tema)

L'ordine conta. All'attivazione il plugin copia i prezzi da `config/preventivo.php` del tema attivo, comprese le modifiche fatte a mano. Il tema nuovo sovrascrive quel file.

1. **Plugin**: *Plugin > Aggiungi nuovo > Carica plugin*, scegli `edera-preventivo.zip`, *Installa ora*, poi *Attiva plugin*.
   - Da qui il calcolatore usa i prezzi del plugin. Sono quelli di oggi, quindi sul sito non cambia niente.
2. **Tema 1.2**: *Aspetto > Temi > Aggiungi tema > Carica tema*, scegli `edera-tema.zip`, *Installa ora*, poi **"Sostituisci quello attuale con quello caricato"**.
   - Con il plugin attivo, il tema 1.2 non carica più il suo calcolatore. Con il tema 1.1 il plugin funziona lo stesso: prende comunque il posto del calcolatore del tema.
   - Il tema nuovo sovrascrive i file del tema, anche `config/contatti.php`. Se avevate cambiato a mano email, telefono o indirizzo in quel file, ricopiateli dopo l'aggiornamento. Dal tema 1.2 si scrivono in *Aspetto > Personalizza > Recapiti*, senza toccare file.

## Dove si cambiano i prezzi

Menu **Preventivo**. Dopo ogni modifica premete **Salva le regole** (il bottone resta in fondo allo schermo). Se c'è un errore, per esempio un prezzo negativo o una data scritta male, le regole non si salvano: in cima compare cosa correggere, e quello che avete scritto resta nel modulo.

- **Spazi**: nome, capienza, prezzo.
  - "Base + persone in più": prezzo base fino alle persone comprese, poi un prezzo per ogni persona in più, fino alla capienza.
  - "Fisso per durata": un prezzo per la giornata intera e uno per la mezza, come la piscina.
  - Si sceglie anche se lo spazio è attivo, se è già scelto all'apertura e se ammette la mezza giornata.
  - Con ↑ ↓ si cambia l'ordine, con *Togli* si toglie. Sulla tariffa "sul primo spazio" conta l'ordine.
- **Durate**: etichette, regola per la mezza giornata, note sotto il campo.
- **Tariffe e supplementi**: in certi mesi (oggi la tariffa stagionale, 125 € da ottobre a marzo), in certi giorni della settimana (per esempio il weekend) o in un periodo.
  - Valore fisso in euro o in percentuale.
  - Si applica sul primo spazio, su ogni spazio o sul totale.
  - Vale per la data scelta nel calcolatore: senza data, nessun supplemento.
- **Sconti e minimi**: sconto per più spazi insieme, sconto oltre un numero di persone, minimo di partecipanti, spesa minima, arrotondamento del totale.
- **Servizi aggiuntivi**: nome, prezzo fisso o a persona. I servizi attivi diventano caselle nel calcolatore. Oggi l'elenco è vuoto: i servizi sono nel PDF.
- **Testi e invio**: email che riceve la richiesta, oggetto e testo della mail, nota sotto il prezzo (IVA), avvertenza, messaggi per data non disponibile e oltre capienza.
  - Nel testo della mail i segnaposti si riempiono da soli: `{azienda}` `{email}` `{telefono}` `{tipo}` `{spazi}` `{data}` `{persone}` `{durata}` `{totale}` `{servizi}` `{dettaglio}`.
  - `{servizi_riga}` scrive la riga "Servizi aggiuntivi: ..." solo se ce ne sono.
- **Prova**: un piccolo calcolatore con le regole salvate, per controllare un prezzo prima che lo veda un cliente. Mostra anche il testo della mail.

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
- I testi sono traducibili, con il dominio `edera-preventivo`.
