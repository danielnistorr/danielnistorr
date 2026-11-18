<?php
/**
 * Recapiti usati dalla testata, dal menu del telefono, dalla barra fissa e dal piede.
 * (I recapiti della sezione "Contatti" della home si cambiano invece in Elementor.)
 *
 * @package edera
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

return array(
	'email'          => 'edera@ederacountry.it',
	'telefono'       => '349 473 1515',          // come si legge
	'telefono_link'  => '+393494731515',         // come si chiama (prefisso internazionale, senza spazi)
	'via'            => 'Via Palù Massara, 10',
	'comune'         => 'Albettone (VI)',
	'mappa'          => 'https://www.google.com/maps/search/?api=1&query=Via%20Pal%C3%B9%20Massara%2010%2C%20Albettone%20VI',
	'piva'           => '04722030287',
	'descrizione'    => 'Location per eventi aziendali ad Albettone, nel Vicentino.',
	// piede delle pagine legali
	'societa'        => 'EGO ITALY srl',
);
