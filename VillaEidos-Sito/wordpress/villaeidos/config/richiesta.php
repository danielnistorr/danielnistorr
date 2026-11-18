<?php
/**
 * Modulo "Richiesta di disponibilita'" (shortcode [villaeidos_richiesta]).
 *
 * Il modulo non manda dati al sito: prepara una mail nel programma di posta di chi lo compila, verso "email".
 * Le etichette dei campi si cambiano in parti/richiesta.html.
 *
 * @package villaeidos
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

return array(
	// A chi arriva la richiesta.
	'email' => 'eidos@eco-management.it',
	// Oggetto della mail (dopo si aggiungono il tipo di spazio e l'azienda).
	'oggetto' => 'Richiesta di disponibilità',
	// I tipi di spazio fra cui scegliere, nell'ordine.
	'tipi'  => array( 'Ufficio o sede', 'Sala riunioni', 'Sala conferenze' ),
);
