# Fratelli Ruffatti, home finale: "Una canna"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `_prova/script/build_finale.sh` (immagini con `finale_img.py`, controlli con `finale_prova.mjs`, screenshot con `finale_shot.mjs`). Alta 6649 px a 1440 compreso il piede.

## Idea

Una sola canna ad ancia vera della Fratelli Ruffatti, aperta e messa in piedi, sull'asse della pagina. La prima schermata è simmetrica come il prospetto di un organo, che si legge attorno alla torre centrale.
- Il titolo, la loro frase "Tutte le canne, costruite in casa", corre su una riga sola a tutta misura, come la scritta sulla cornice di una cassa d'organo.
- Sotto il titolo, al centro, c'è la canna alla sua misura vera, 800 px, mai ingrandita. Scende oltre la piega e si chiude in dissolvenza sulla sezione dopo.
- Ai lati, sulla stessa linea, ci sono due testi brevi. A sinistra chi sono, il bottone e il telefono; a destra le tre parti della canna.

Con il nome di Mascioni o di Rieger la pagina non regge, perché la canna, il titolo e le frasi sono loro.

## Cosa è cambiato in quest'ultimo passaggio

Sono cambiate tre cose chieste dal committente il 2 novembre ("più alta gamma, meno uguali tra loro"):
1. **Niente legende sull'oggetto.** Sono spariti i numeri sulla canna. Resta solo la didascalia "Una canna ad ancia Ruffatti, aperta" sopra l'indice. Il legame tra l'indice e l'oggetto ora è il gesto (vedi Interazione), non un segno disegnato.
2. **Il fondo viene dal mestiere.** Il fondo #E7E8E2 è il grigio chiaro della lega di stagno, lo stesso tono del metallo della canna e delle canne di facciata nelle foto delle opere. La ragione si vede: la canna sembra fatta del fondo. Il piede è #DCDDD7, la lastra appena più scura. Il bordeaux del logo resta l'unico colore caldo, con l'ottone del canaletto. Il fondo della foto della canna è portato con PIL esattamente al colore della pagina e salvato senza sottocampionamento del colore, quindi non si vede nessun riquadro.
3. **Un'impaginazione che nella campagna non c'è.** Tutte le altre home hanno il titolo a sinistra. Qui la composizione è simmetrica sull'asse, il titolo è una sola riga a tutta larghezza (102 px a 1440, fino a 132 px) e la foto è un taglio verticale stretto, alto 800 px, al centro. A 390 tutto resta sull'asse, centrato.

Dal giudizio cieco, oltre a quanto sopra (alcune cose erano già state fatte in un passaggio precedente e sono state verificate):
- La canna non è mai ingrandita: rapporto 1,0 da 1024 px in su, ridotta sotto. `canna-890.jpg` non c'è più.
- La foto sfuma in alto e in basso a tutte le larghezze, quindi non ci sono più bordi netti sul metallo.
- La chiusura da 768 a 1023 px ha la foto alla stessa altezza della frase.
- Il gesto a 390: indice e frase stanno sopra la canna, la frase cambia dentro la prima schermata e non c'è più il riquadro azzurro al tocco.
- Laboratorio:
  - foto a filo del bordo sinistro, larga al massimo 800 px;
  - taglio 800x800 sulle campane a fuoco;
  - colore portato al neutro, con lo stagno grigio e il legno bruno, senza più la dominante salmone.
- Opere: tre sulla stessa riga anche a 768, stesso bianco neutro, taglio 3:5.
- Testi:
  - "dal 1968 sono soci";
  - niente fibra di carbonio per Boteå e niente "cento file" per Buckfast (vanno confermati, LEGGIMI);
  - la frase "Ben pochi organari" è tolta;
  - accanto alla canna c'è la loro frase "Costruire canne ad ancia è diventata attività rara per gli organari".
- Il bottone "Iscriviti" è bordeaux come l'azione principale.
- Il menu dice "Chiudi" quando è aperto e si chiude con Esc e toccando una voce.
- Il ritmo verticale è un po' più stretto (sezioni a 88 px e attacchi a 56 px): la pagina resta sotto 7000 px.

## Le prime due schermate

1. **A 1440x900.**
   - In testata: logo corsivo bordeaux, quattro voci, IT EN RU e telefono.
   - Sotto, il titolo su una riga, centrato, in Gambetta 300.
   - Al centro la canna. Si vedono la noce tornita, il canaletto d'ottone con la molla d'accordatura e l'imboccatura del piede.
   - A sinistra "Organi a canne nuovi e restauri, a Padova dal 1940.", il bottone "Scriveteci" (mailto:) e il telefono (tel:).
   - A destra la didascalia, l'indice 1 Noce, 2 Canaletto, 3 Piede e la frase.
2. **A 390x844.** Titolo su due righe, centrato. Sotto la riga, l'indice e la frase, poi la canna (alta 434 px), poi bottone e telefono.

Dopo vengono:
- **Laboratorio**: "Ogni componente possibile, in laboratorio", la foto del registro di Tromba a filo del bordo sinistro con il testo a destra, poi tre misure tra filetti sottili (95 % di stagno, mogano sipo stagionato cinque anni, pannelli da 48 mm).
- **Opere**: la frase di Michela Ruffatti, poi Davies Symphony Hall, Buckfast e Boteå, poi la riga dei numeri.
- **Storia**: la foto delle maestranze in bicromia inchiostro e stagno, poi La famiglia e Il restauro.
- **Chiusura "b con foto"**: la loro frase "La tradizione è forte solo se continua ad evolversi", il telefono grande con tel:, l'email con mailto:, l'indirizzo e "Apri la mappa" (Google Maps). Le trombe en chamade arrivano fino al bordo destro.
- **Piede**:
  - logo e una riga su chi sono;
  - la newsletter, che esiste già e ha notizie da mandare, con email, bottone e consenso privacy;
  - quattro colonne: Azienda, Organi, Notizie, e Contatti con Seguici (Facebook, Instagram, YouTube, che esistono tutti);
  - in fondo © 2026 Fratelli Ruffatti, P.IVA 00207160284, Privacy, Cookie, IT EN RU.
  - A 390 le colonne vanno due per riga, in ordine.

## Caratteri e colori

- **Gambetta** (titoli, pesi 300 e 400) e **Switzer** (testo, pesi 400 e 500), tutti e due di Indian Type Foundry su Fontshare.
  - Licenza ITF Free Font License, uso commerciale gratuito. I woff2 sono serviti dalla pagina in `sito/fonts/`.
  - Perché: Rieger, il riferimento più vicino del mestiere, abbina un serif da frontespizio a un grottesco sobrio. Gambetta ha la voce di un'iscrizione incisa e sta accanto al corsivo del logo senza imitarlo.
  - Nessun corsivo in pagina. Numeri tabellari su anni, misure e telefoni; apostrofi tipografici.
- **Colori.**
  - Stagno #E7E8E2 per la pagina, #DCDDD7 per il piede.
  - Inchiostro #1C1A17.
  - Grigio #52554F solo per didascalie e note: contrasto 6,2:1 sulla pagina e 5,5:1 sul piede.
  - Bordeaux del logo #6A0C10 per logo, bottoni e voce scelta: 10,1:1; il bianco sul bordeaux 12,6:1.
  - Bordo del campo email #7E8279, cioè 3,2:1.

## Interazione

Le tre voci dell'indice sono bottoni veri, con `aria-pressed` e `aria-controls`.
- **All'inizio** la canna è intera e la frase è quella generale.
- **Toccando una voce** compare la sua frase, presa parola per parola dalla pagina "Canne ad ancia". La parte scelta della canna resta piena e il resto si vela del colore dello stagno (velo al 58 %). Il cambio è netto, senza animazione.
- **Un secondo tocco** sulla stessa voce torna alla canna intera.

È l'unico gesto della pagina. Le sole transizioni sono il cambio di colore di fondo dei due bottoni (0,15 s). Niente comparse allo scorrere, niente effetti al cursore.

## Foto: origine e licenza

Sono tutte della Fratelli Ruffatti, prese dalla libreria media di ruffatti.com: nessuna foto di repertorio, nessuna foto di altri costruttori, nessuna immagine generata dall'IA. I diritti delle foto delle installazioni vanno confermati (LEGGIMI).

| Foto in pagina | File originale | Misura vera | In pagina a 1440 |
|---|---|---|---|
| Canna ad ancia aperta | `2016_04_xtrompette3.jpg` | 800x603 (ruotata 595x800) | 595x800, 1 volta |
| Registro di Tromba | `2016_04_xSfondo-trombe-2.jpg`, taglio 800x800 | 800x800 | 800x800, 1 volta |
| Davies Symphony Hall | `2016_03_xDavies-Symphony-e1480329573331.jpg` | 800x1085 | 421 px di larghezza |
| Abbazia di Buckfast | `2018_11_756A0922-3.jpg` | 1028x758 (taglio 505x758) | 421 px |
| Boteå | `2018_11_P1270600-1.jpg` | 3264x2448 | 421 px |
| Maestranze, archivio | `2016_03_storia1-575.jpg` | 900x575 | circa 1040x665, ingrandita 1,16 volte |
| Trombe en chamade | `2016_04_xOrgan064modif.jpg`, taglio 600x600 | 600x600 | circa 676x780, ingrandita 1,3 volte |

Il trattamento è lo stesso per tutte: colore portato verso uno stesso bianco neutro e un po' più sobrio, contrasto appena più deciso; l'archivio è in bicromia inchiostro e stagno. Ogni foto è esportata in due o tre larghezze con srcset. Quello che a 2x resta morbido è elencato nel LEGGIMI, con come rifarlo.

## Controlli fatti

- **Larghezze.**
  - Guardati a pezzi gli screenshot interi a 1440 e a 390, le prime schermate a 320, 768, 1024 e 1920 e la chiusura a 768.
  - scrollWidth uguale a innerWidth a 2560, 1920, 1440, 1280, 1100, 1024, 1000, 768, 390, 360 e 320.
  - Nessun testo sopra l'oggetto (`finale_prova.mjs`).
  - Sotto i 1200 px il menu si apre con un vero bottone.
- **Gesto.**
  - Con la tastiera, Tab e Invio, a 2560, 1920, 1440, 1280, 1100 e 1024. Col dito a 1000, 768, 390, 360 e 320.
  - Voce premuta, frase visibile e parte lasciata piena cambiano insieme.
  - La frase è nella vista dopo il tocco a tutte le larghezze.
  - Il secondo tocco torna alla canna intera.
- **Collegamenti.**
  - tel:+39049750666 in testata, in apertura, nella chiusura e nel piede.
  - mailto:organs@ruffatti.com.
  - La mappa va su Google Maps con l'indirizzo "Via Facciolati 166, 35127 Padova".
  - I social sono le tre pagine che esistono.
- **Segnali da IA.** `_metodo/kit/segnali.sh` dà tutte le 18 soglie OK:
  - foto al 35,1 % della pagina;
  - Switzer 85 % e Gambetta 15 %;
  - nessuna etichetta maiuscola, nessun numero grande con etichetta, nessuna freccia;
  - 7 filetti larghi;
  - due fasce di fondo, la pagina e il piede.
- **Testo.**
  - Nessun U+2014 nella pagina, nella NOTA e nel LEGGIMI (controllato dallo script).
  - Nessun dato fuori da `01-analisi.md` e dai testi scaricati; nessun segnaposto in pagina.
- **Divieti del committente.** Niente Inter, niente icone Lucide, niente gradienti nei colori, niente card, niente badge, niente legende con pallino e filetto, niente oggetti disegnati.
