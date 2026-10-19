# Bazzato: proposta di nuova home

Proposta non richiesta di una nuova homepage per Bazzato snc, autofficina a Tombelle di Vigonovo (VE). È solo la home. L'azienda non è stata contattata e nulla è stato pubblicato.

## Cosa c'è

- **La home**: `sito/index.html`, statica. Si apre anche come file e usa le immagini in `sito/img/` e il carattere in `sito/fonts/`.
- **Screenshot e nota**: `screenshot/home/`, con `NOTA.md` (idea, caratteri, colori, interazione, foto, controlli).
- **Analisi con le fonti**: `01-analisi.md`.
- **Le due bozze viste dal committente**: `_prova/home/a/` e `_prova/home/b/`. La finale è costruita sulla B, "Il ponte".
- **Script**: `_prova/script/`. `build_finale.sh` rifà immagini, caratteri, pagina, screenshot e controlli.
- **Crediti e licenze delle foto**: `assets/CREDITI.md`.

## Dati da confermare con Bazzato prima di pubblicare

In pagina c'è solo ciò che è scritto sul loro sito o nelle fonti di `01-analisi.md`. Restano da confermare:

1. **Prezzi**, presi dal sito di oggi:
   - revisione € 79,00 con la pre-revisione gratis;
   - clima "circa € 70" (R134a) e "circa € 180" (R1234yf); le grafiche del clima citano un'offerta di giugno 2021;
   - batterie QParts da € 80 a € 185, Iva compresa e montaggio escluso.
2. **Orari**:
   - officina dal lunedì al venerdì, 08.00-12.00 e 14.00-18.00;
   - uffici 08.00-12.30 e 14.00-19.00, il venerdì fino alle 18.00;
   - sabato chiuso;
   - appuntamenti di revisione dalle 09.00 alle 11.00 e dalle 14.30 alle 16.00.
3. **Chiusure per lo stato dell'officina** (in grande nella prima schermata, accanto al bottone per chiamare). Lo script (in fondo a `index.html`, voci `CHIUSURE` e `FESTIVI`) conosce le ferie del 6-21 agosto 2026 prese dal sito, i festivi nazionali e Pasquetta. Va chiesto:
   - se chiudono anche nei festivi, il che è probabile ma non è scritto da nessuna parte;
   - per il santo patrono di Vigonovo;
   - per i ponti;
   - le date delle ferie di ogni anno. Le ferie del 2027 vanno aggiunte a mano.
4. **"L'officina di Andrea e Paolo Bazzato"**: viene dalla ragione sociale. Va chiesto se sono loro a lavorare in officina e se vogliono comparire in foto.
5. **L'anno 2005** (fondazione della snc secondo companyreports, "anzianità 21 anni" secondo atoka) e i 5 dipendenti (atoka): non sono in pagina finché non si vedono nella visura.
6. **Marchio Opel**: non è in pagina, finché non si sa se l'officina è ancora autorizzata Opel nel 2026. In pagina restano Eurorepar Car Service e GPL Landi.
7. **Rivenditore autorizzato Pirelli**: lo dice solo misterimprese, quindi non è in pagina.
8. **Altri servizi**:
   - carrozzeria: interna o affidata fuori?
   - "vendita auto": nuove o usate, e di quali marche?
   - auto sostitutiva: a pagamento o no? In pagina c'è "a noleggio", come sul loro sito.
9. **"Tra Padova e Venezia"**: è geografia, non è una loro frase. Va bene se piace a loro.
10. **Informativa privacy**: il link punta alla pagina di oggi (`informativa-privacy-agli-utenti.html`), che va aggiornata con il nuovo sito.
11. **PEC**: non trovata; il piede ne ha bisogno se si vuole metterla.
12. **Numero verde Opel Assistance 800 836063**: non usato in home; va verificato se servirà nella pagina del soccorso.
13. **"Prezzi chiari, sconti chiari"**: è una loro frase, ma in home il listino ora si chiama "Lavori e prezzi", perché in pagina non c'è nessuno sconto. Se Bazzato ha sconti veri e fissi, si può rimettere la frase come titolo con una riga dello sconto, solo se confermato da loro.

## Foto da rifare dal vero

Le due foto in pagina sono segnaposto con licenza libera (Pexels), ritoccate per togliere i marchi e il disordine; in pagina portano l'etichetta "Foto indicativa". Nessuna è dell'officina Bazzato e nessuna va pubblicata come se lo fosse. Serve mezza giornata di scatti in viale Serenissima 3, al mattino, con l'officina pulita e le luci accese.

Attenzione all'apertura: nella foto segnaposto l'auto sul ponte è senza paraurti posteriore e a destra c'è la porta a vetri di una cabina di verniciatura, quindi racconta una carrozzeria dopo un incidente, non un tagliando. Serve solo a mostrare la luce e l'inquadratura. È la prima foto da rifare.

1. **Apertura** (la più importante):
   - l'officina vista dal fondo del capannone, in asse, macchina all'altezza del petto, obiettivo 24-28 mm;
   - una loro auto intera, pulita e integra (con il paraurti, nessun pezzo smontato), chiara se possibile, alzata sul ponte al centro e larga almeno metà dell'inquadratura;
   - il pavimento libero in primo piano per il titolo;
   - niente carrelli, scale e cavi in vista, niente targhe leggibili, niente marchi di attrezzature in primo piano;
   - luce dei neon più quella del portone aperto; bilanciamento neutro;
   - uno scatto orizzontale (almeno 4000 px di larghezza) e uno verticale per il telefono, con l'auto nel terzo alto.
2. **Il ponte** (la seconda foto della home): un'auto intera alzata, vista di fianco, con aria ai due lati e l'officina chiara dietro, con la stessa luce dell'apertura; formato 3:2 orizzontale con margine per il taglio 5:4 del telefono. Niente gomme a terra, persone o insegne con marchi nel quadro.
3. **Per le pagine dei servizi**: mani di un loro meccanico che montano una ruota sul mozzo, in luce naturale, da vicino, guanti senza marchi.
4. **Utili per le altre pagine**:
   - la linea revisione con un'auto in prova;
   - la facciata dritta con l'insegna, al mattino;
   - i titolari, se vogliono;
   - il banco attrezzi in ordine.

Le foto di oggi sul loro sito non servono: sono materiale stampa Opel e QParts, foto da telefono del vano motore e repertorio fuori registro (voti in `_prova/inventario-immagini.json`).

## Licenze

- **Foto segnaposto**:
  - Renee Razumov (Pexels 33814736) e Artem Podrez (Pexels 8985667), con la Pexels License;
  - la foto di Podrez usata prima (Pexels 8986138, il SUV tagliato a metà col fumo) resta scaricata ma non è più in pagina;
  - le mani sulla ruota di Jimmy Nilsson Masth (Unsplash 9uHal2Dd9aE) erano nella bozza B e non sono più usate.
  - Uso libero anche commerciale e modifiche ammesse. Licenze lette il 19/10/2026 sulla pagina di ogni foto; i dettagli sono in `assets/CREDITI.md`.
- **Carattere**: General Sans di Indian Type Foundry (Fontshare), con la ITF Free Font License 2.0 (`sito/fonts/FFL.txt`).
  - È gratuito anche per l'uso commerciale e si può ospitare sul proprio server.
  - I file però non si modificano e non si passano a terzi: chi pubblica il sito per Bazzato deve scaricare la propria copia da fontshare.com.
- **Materiale del sito di oggi** (`assets/originali/`): molto è di Opel, di QParts o di terzi (biglietti dei soccorritori), e i diritti vanno chiariti prima di riusarlo.

## Logo

Il logo di oggi esiste solo raster (la scritta su una fascia azzurra #00C3EF con quattro icone). In testata, per ora, c'è il nome scritto in General Sans. Serve il vettoriale, e va chiesto se vogliono tenere le quattro icone. L'azzurro del logo è usato nella pagina solo per il punto dello stato "aperto".
