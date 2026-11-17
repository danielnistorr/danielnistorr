<?php
/**
 * Recapiti di Villa Eidos usati da testata, menu del telefono, piede e modulo.
 * Si cambiano anche da Aspetto > Personalizza > Recapiti (un campo pieno vale piu' di questo file).
 * I recapiti dentro le sezioni della Home (telefono grande, ingressi) si cambiano invece in Elementor.
 *
 * @package villaeidos
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

return array(
	'telefono'      => '049 0990550',     // come si legge
	'telefono_link' => '+390490990550',   // come si chiama (prefisso internazionale, senza spazi)
	'email'         => 'eidos@eco-management.it',
	'comune'        => 'Albignasego (PD)',
	'indirizzi'     => 'Via Battaglia 67, via Colombo 2, via Colombo 6A',
	'mappa'         => 'https://www.google.com/maps/search/?api=1&query=Via%20Battaglia%2067%2C%20Albignasego%20PD',

	// DA CHIEDERE AL CLIENTE, mai inventare: ragione sociale e partita IVA della societa' che gestisce Villa Eidos.
	// Finche' restano vuote, il piede scrive "Ragione sociale e partita IVA da completare" e il pannello lo ricorda.
	'societa'       => '',   // DA CHIEDERE: ragione sociale (es. "Nome S.r.l.")
	'piva'          => '',   // DA CHIEDERE: partita IVA (11 cifre)
);
