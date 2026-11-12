<?php
/**
 * Plugin Name:       Edera Preventivo
 * Description:       Il calcolatore "Preventivo flash" di Edera Country House con prezzi e regole che si cambiano dal pannello (menu Preventivo): spazi, durate, giorni esclusi, tariffe e supplementi, sconti e minimi, servizi aggiuntivi, testi della mail. Disegna lo shortcode [edera_preventivo] al posto del tema.
 * Version:           1.0.1
 * Requires at least: 6.4
 * Requires PHP:      7.4
 * Author:            Edera Country House
 * License:           GPLv2 or later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:       edera-preventivo
 * Domain Path:       /languages
 *
 * @package edera-preventivo
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'EDERA_PREVENTIVO_VERSIONE', '1.0.1' );
define( 'EDERA_PREVENTIVO_FILE', __FILE__ );

require __DIR__ . '/includes/regole.php';
require __DIR__ . '/includes/sito.php';
if ( is_admin() ) {
	require __DIR__ . '/includes/admin.php';
}

add_action(
	'init',
	function () {
		load_plugin_textdomain( 'edera-preventivo', false, dirname( plugin_basename( __FILE__ ) ) . '/languages' );
	}
);

// All'attivazione: se le regole non ci sono ancora, prende i prezzi di config/preventivo.php del tema attivo
// (con le modifiche fatte dal committente) o i valori iniziali. Non tocca pagine, contenuti o dati di Elementor.
register_activation_hook(
	__FILE__,
	function () {
		if ( false === get_option( EDERA_PREVENTIVO_OPZIONE, false ) ) {
			add_option( EDERA_PREVENTIVO_OPZIONE, edera_preventivo_dal_tema(), '', false );
		}
	}
);

add_filter(
	'plugin_action_links_' . plugin_basename( __FILE__ ),
	function ( $link ) {
		array_unshift( $link, '<a href="' . esc_url( admin_url( 'admin.php?page=edera-preventivo' ) ) . '">' . esc_html__( 'Prezzi e regole', 'edera-preventivo' ) . '</a>' );
		return $link;
	}
);
