<?php
/**
 * Movimenti: tre tocchi fatti con il kit HE (GSAP, ScrollTrigger, SplitText) in assets/he/.
 *
 * Si accendono con classi CSS scritte in Elementor (scheda Avanzate > Classi CSS):
 *   moto-righe    su un Titolo: il titolo sale riga per riga (subito, se e' nella prima schermata)
 *   moto-taglio   su un'Immagine: la foto si scopre con un taglio netto dal basso quando entra
 *                 (moto-taglio-sinistra / moto-taglio-destra per gli altri versi)
 *   moto-testata  su un contenitore: da 900 px in su la testata si nasconde scendendo, torna salendo
 *                 e dopo quel contenitore prende il fondo chiaro (sul telefono resta com'e')
 * assets/moto.js traduce le classi negli attributi data-he-* del kit prima che il kit parta.
 *
 * Tutti i movimenti si spengono con un clic: Aspetto > Personalizza > Movimenti, oppure con
 * define( 'EDERA_SENZA_MOVIMENTI', true ); in wp-config.php. Spenti, la pagina e' identica all'originale.
 * Con "riduci movimento" del sistema e senza JavaScript la pagina resta completa e ferma.
 *
 * @package edera
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action(
	'customize_register',
	function ( $wpc ) {
		$wpc->add_section(
			'edera_movimenti',
			array(
				'title'       => 'Movimenti',
				'priority'    => 160,
				'description' => 'Tre movimenti discreti: il titolo d’apertura che sale riga per riga, le foto della galleria che si scoprono con un taglio netto, la testata che si nasconde scendendo (solo sugli schermi da 900 px). Senza la spunta la pagina è ferma, identica al sito originale.',
			)
		);
		$wpc->add_setting(
			'edera_movimenti',
			array(
				'type'              => 'theme_mod',
				'default'           => true,
				'sanitize_callback' => function ( $v ) {
					return (bool) $v;
				},
			)
		);
		$wpc->add_control(
			'edera_movimenti',
			array(
				'section' => 'edera_movimenti',
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
function edera_movimenti_attivi() {
	if ( defined( 'EDERA_SENZA_MOVIMENTI' ) && EDERA_SENZA_MOVIMENTI ) {
		return false;
	}
	if ( ! get_theme_mod( 'edera_movimenti', true ) || edera_legale() || is_admin() ) {
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
		if ( ! edera_movimenti_attivi() ) {
			return;
		}
		$t = get_template_directory_uri() . '/assets/he/';
		$v = EDERA_VERSIONE;
		wp_enqueue_style( 'edera-he', $t . 'he.css', array( 'edera' ), $v );
		wp_enqueue_style( 'edera-moto', get_template_directory_uri() . '/assets/moto.css', array( 'edera-he' ), $v );
		wp_register_script( 'gsap', $t . 'vendor/gsap.min.js', array(), '3', array( 'in_footer' => true ) );
		wp_register_script( 'gsap-scrolltrigger', $t . 'vendor/ScrollTrigger.min.js', array( 'gsap' ), '3', array( 'in_footer' => true ) );
		wp_register_script( 'gsap-splittext', $t . 'vendor/SplitText.min.js', array( 'gsap' ), '3', array( 'in_footer' => true ) );
		wp_register_script( 'edera-moto', get_template_directory_uri() . '/assets/moto.js', array( 'gsap-scrolltrigger', 'gsap-splittext' ), $v, array( 'in_footer' => true ) );
		wp_enqueue_script( 'edera-he', $t . 'he.js', array( 'edera-moto' ), $v, array( 'in_footer' => true ) );
	},
	30
);
