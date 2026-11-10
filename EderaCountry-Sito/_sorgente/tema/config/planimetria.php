<?php
/**
 * Planimetria: la foto dall'alto, i pallini e le foto del Rustico (shortcode [edera_planimetria]).
 *
 * Si apre da Aspetto > Editor dei file del tema > config/planimetria.php, oppure via FTP in
 * wp-content/themes/edera/config/planimetria.php. Dopo una modifica basta ricaricare la pagina.
 *
 * Foto ("foto"): si indicano in uno di tre modi.
 *   - il nome dato dall'installatore (per esempio 'rustico-1'): sono le foto caricate da Aspetto > Installa Edera;
 *   - il numero della foto nella libreria media (Media > clic sulla foto: e' il numero dopo "post=" nell'indirizzo);
 *   - l'indirizzo completo della foto (https://...).
 * Una foto nuova va caricata prima in Media > Aggiungi file multimediale.
 *
 * Pallini: posizione in percentuale sulla foto ("x" da sinistra, "y" dall'alto, con il punto per i decimali),
 * nome, lato dell'etichetta ('destra' o 'sinistra'). Facoltativi:
 *   - 'capienza'   la capienza come e' scritta sul sito (solo per gli spazi che sul sito ce l'hanno);
 *   - 'preventivo' lo spazio del calcolatore da spuntare con "Scegli nel preventivo"
 *                  (rustico, serra, piscina, esterno: le chiavi di config/preventivo.php);
 *   - 'galleria'   true: la scheda del pallino ha "Vedi le foto", che apre le foto qui sotto.
 * L'ordine dei pallini e' quello dei numeri sulla mappa e dell'elenco accanto.
 *
 * @package edera
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

return array(

	// La foto dall'alto: tenuta com'e', senza ritocchi (solo compressa).
	'mappa'           => array(
		'foto' => 'planimetria',
		'alt'  => "Planimetria di Edera Country House vista dall'alto",
	),

	'pallini'         => array(
		array(
			'nome'       => 'Rustico',
			'x'          => 29.5,
			'y'          => 47.5,
			'etichetta'  => 'destra',
			'capienza'   => 'fino a 50 persone',
			'preventivo' => 'rustico',
			'galleria'   => true,
		),
		array(
			'nome'       => 'Serra',
			'x'          => 33,
			'y'          => 32.5,
			'etichetta'  => 'destra',
			'capienza'   => 'fino a 70 persone',
			'preventivo' => 'serra',
		),
		array(
			'nome'       => 'Piscina',
			'x'          => 49.5,
			'y'          => 47.5,
			'etichetta'  => 'destra',
			'capienza'   => 'fino a 30 persone, anche mezza giornata',
			'preventivo' => 'piscina',
		),
		array(
			'nome'      => 'Casetta bar',
			'x'         => 36,
			'y'         => 66.5,
			'etichetta' => 'sinistra',
		),
		array(
			'nome'      => 'Grill',
			'x'         => 16,
			'y'         => 32.5,
			'etichetta' => 'sinistra',
		),
		array(
			// Nel prototipo si chiama "Spazio verde": sul sito c'e' "Spazio esterno" (fino a 120 persone),
			// ma non e' detto che siano lo stesso spazio. Finche' non e' confermato, niente capienza.
			'nome'      => 'Spazio verde',
			'x'         => 24,
			'y'         => 61.5,
			'etichetta' => 'sinistra',
		),
	),

	// Le foto che si aprono da "Vedi le foto" (il nome della finestra e' quello del pallino con la galleria).
	'galleria'        => array(
		array(
			'foto'       => 'rustico-1',
			'didascalia' => 'Esterno della struttura',
		),
		array(
			'foto'       => 'rustico-2',
			'didascalia' => 'Sala interna',
		),
		array(
			'foto'       => 'rustico-3',
			'didascalia' => 'Sala interna – seconda vista',
		),
		array(
			'foto'       => 'rustico-4',
			'didascalia' => 'Vista dal soppalco',
		),
		array(
			'foto'       => 'rustico-5',
			'didascalia' => 'Panoramica piscina e struttura',
		),
	),
);
