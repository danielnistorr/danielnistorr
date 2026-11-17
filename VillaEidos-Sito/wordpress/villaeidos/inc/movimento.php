<?php
/**
 * Movimenti: due tocchi del kit HE (GSAP, ScrollTrigger, SplitText) in assets/he/.
 *
 * Si accendono con classi CSS scritte in Elementor (scheda Avanzate > Classi CSS):
 *   moto-righe    su un Titolo: il titolo sale riga per riga (subito, se e' nella prima schermata)
 *   moto-taglio   su un'Immagine: la foto si scopre con un taglio netto dal basso quando entra
 * assets/moto.js traduce le classi negli attributi data-he-* del kit prima che il kit parta.
 * Nessuna dissolvenza, nessuna testata che si nasconde.
 *
 * Si spengono con un clic: Aspetto > Personalizza > Movimenti, oppure con
 * define( 'VILLAEIDOS_SENZA_MOVIMENTI', true ); in wp-config.php. Spenti, la pagina e' la stessa, ferma.
 * Con "riduci movimento" del sistema e senza JavaScript la pagina resta completa e ferma.
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
				'description' => 'Due movimenti discreti: il titolo d’apertura che sale riga per riga, le foto delle sale riunioni e della sala conferenze che si scoprono con un taglio netto. Senza la spunta la pagina è ferma.',
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
 * I movimenti sono attivi su questa pagina?
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

add_action(
	'wp_enqueue_scripts',
	function () {
		if ( ! villaeidos_movimenti_attivi() ) {
			return;
		}
		$t = get_template_directory_uri() . '/assets/';
		$v = VILLAEIDOS_VERSIONE;
		wp_enqueue_style( 'villaeidos-he', $t . 'he/he.css', array( 'villaeidos' ), $v );
		wp_enqueue_style( 'villaeidos-moto', $t . 'moto.css', array( 'villaeidos-he' ), $v );
		wp_register_script( 'gsap', $t . 'he/vendor/gsap.min.js', array(), '3', array( 'in_footer' => true ) );
		wp_register_script( 'gsap-scrolltrigger', $t . 'he/vendor/ScrollTrigger.min.js', array( 'gsap' ), '3', array( 'in_footer' => true ) );
		wp_register_script( 'gsap-splittext', $t . 'he/vendor/SplitText.min.js', array( 'gsap' ), '3', array( 'in_footer' => true ) );
		wp_register_script( 'villaeidos-moto', $t . 'moto.js', array( 'gsap-scrolltrigger', 'gsap-splittext' ), $v, array( 'in_footer' => true ) );
		wp_enqueue_script( 'villaeidos-he', $t . 'he/he.js', array( 'villaeidos-moto' ), $v, array( 'in_footer' => true ) );
	},
	30
);
