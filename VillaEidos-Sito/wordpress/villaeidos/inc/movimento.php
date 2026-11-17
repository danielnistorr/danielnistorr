<?php
/**
 * Movimento: quasi niente, come chiede la direzione.
 * - La foto d'apertura si scopre dal basso con un taglio netto quando la pagina si apre (CSS, assets/sito.css).
 * - La testata si compatta scorrendo (assets/sito.js): con il movimento acceso il cambio d'altezza e' una transizione
 *   breve, spento e' un cambio secco.
 * I bottoni si invertono di colpo al passaggio, sempre. Nessuna dissolvenza, nessun titolo che sale.
 *
 * Il movimento si accende con la classe ve-moto sul body, solo sulla Home e mai nell'editor di Elementor.
 * Si spegne con un clic: Aspetto > Personalizza > Movimenti, oppure con
 * define( 'VILLAEIDOS_SENZA_MOVIMENTI', true ); in wp-config.php. Con "riduci movimento" del sistema non c'e' comunque.
 *
 * @package villaeidos
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action(
	'customize_register',
	function ( $wpc ) {
		$wpc->add_section(
			'villaeidos_movimenti',
			array(
				'title'       => 'Movimenti',
				'priority'    => 160,
				'description' => 'La foto d’apertura che si scopre quando la pagina si apre e la testata che si compatta con una transizione breve. Senza la spunta la pagina è ferma (la testata si compatta lo stesso, senza transizione).',
			)
		);
		$wpc->add_setting(
			'villaeidos_movimenti',
			array(
				'type'              => 'theme_mod',
				'default'           => true,
				'sanitize_callback' => function ( $v ) {
					return (bool) $v;
				},
			)
		);
		$wpc->add_control(
			'villaeidos_movimenti',
			array(
				'section' => 'villaeidos_movimenti',
				'type'    => 'checkbox',
				'label'   => 'Movimenti attivi',
			)
		);
	}
);

/**
 * Il movimento e' attivo su questa pagina?
 *
 * @return bool
 */
function villaeidos_movimenti_attivi() {
	if ( defined( 'VILLAEIDOS_SENZA_MOVIMENTI' ) && VILLAEIDOS_SENZA_MOVIMENTI ) {
		return false;
	}
	if ( ! get_theme_mod( 'villaeidos_movimenti', true ) || is_admin() || ! is_front_page() ) {
		return false;
	}
	// nell'anteprima dell'editor di Elementor la pagina resta ferma, per modificarla comodamente
	if ( isset( $_GET['elementor-preview'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		return false;
	}
	if ( class_exists( '\Elementor\Plugin' ) && isset( \Elementor\Plugin::$instance->preview ) && \Elementor\Plugin::$instance->preview->is_preview_mode() ) {
		return false;
	}
	return true;
}

add_filter(
	'body_class',
	function ( $c ) {
		if ( villaeidos_movimenti_attivi() ) {
			$c[] = 've-moto';
		}
		return $c;
	}
);
