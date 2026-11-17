<?php
/**
 * Tema Villa Eidos.
 *
 * - Le pagine (Home, Informativa privacy, Cookie) sono fatte in Elementor (anche gratuito) con widget normali
 *   (Titolo, Editor di testo, Immagine, Pulsante, Shortcode) dentro contenitori con classi CSS: testi e foto si
 *   cambiano dal pannello di Elementor. Il tema da' l'aspetto: assets/sito.css aggancia quelle classi.
 * - Testata, menu del telefono, piede e modulo sono in parti/*.html, lo stesso HTML dell'anteprima statica.
 * - La foto d'apertura (classe apertura-foto) oggi e' il fregio con "Villa, Barchessa, Giardino": quando arriva
 *   la foto della villa si cambia con un clic in Elementor (vedi il LEGGIMI).
 * - Il modulo "Richiesta di disponibilita'" e' lo shortcode [villaeidos_richiesta] (inc/richiesta.php): prepara una
 *   mail nel programma di posta di chi scrive, il sito non riceve e non salva dati.
 * - Recapiti: Aspetto > Personalizza > Recapiti, oppure config/contatti.php. Ragione sociale e partita IVA sono
 *   ancora da chiedere al cliente: finche' mancano il piede lo dice e il pannello lo ricorda.
 * - Caratteri e immagini sono nel tema e nella libreria media: il sito non chiama servizi esterni e non usa cookie.
 * - Due movimenti (titolo d'apertura, due foto degli spazi), spenti da Aspetto > Personalizza > Movimenti.
 * - Installazione: Aspetto > Installa Villa Eidos, oppure installa-su-server.sh con WP-CLI (inc/installa.php).
 *
 * @package villaeidos
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'VILLAEIDOS_VERSIONE', '1.0.0' );

require get_template_directory() . '/inc/installa.php';
require get_template_directory() . '/inc/elementor.php';
require get_template_directory() . '/inc/richiesta.php';
require get_template_directory() . '/inc/movimento.php';

/**
 * Un file di config/ (array PHP), letto una volta sola.
 *
 * @param string $nome Nome del file senza estensione.
 * @return array
 */
function villaeidos_config( $nome ) {
	static $cache = array();
	if ( ! isset( $cache[ $nome ] ) ) {
		$f              = get_template_directory() . '/config/' . sanitize_file_name( $nome ) . '.php';
		$cache[ $nome ] = file_exists( $f ) ? (array) include $f : array();
	}
	return $cache[ $nome ];
}

/**
 * Un recapito: prima Aspetto > Personalizza > Recapiti, poi config/contatti.php.
 *
 * @param string $k Chiave.
 * @return string
 */
function villaeidos_dato( $k ) {
	$m = get_theme_mod( 'villaeidos_recapito_' . $k, '' );
	if ( is_string( $m ) && '' !== trim( $m ) ) {
		return trim( $m );
	}
	$c = villaeidos_config( 'contatti' );
	return isset( $c[ $k ] ) ? trim( (string) $c[ $k ] ) : '';
}

/**
 * La riga legale del piede: ragione sociale e partita IVA, oppure il segnaposto se mancano (non si inventano).
 *
 * @return string HTML.
 */
function villaeidos_riga_legale() {
	$societa = villaeidos_dato( 'societa' );
	$piva    = villaeidos_dato( 'piva' );
	if ( '' === $societa || '' === $piva ) {
		return '<span class="da-completare">Ragione sociale e partita IVA da completare</span>';
	}
	return esc_html( $societa . ', P.IVA ' . $piva );
}

add_action(
	'customize_register',
	function ( $wpc ) {
		$wpc->add_section(
			'villaeidos_recapiti',
			array(
				'title'       => 'Recapiti',
				'priority'    => 155,
				'description' => 'Recapiti di testata, menu del telefono, piede e modulo. Un campo vuoto usa il valore del file config/contatti.php del tema. (Quelli dentro le sezioni della Home si cambiano in Elementor.)',
			)
		);
		$campi = array(
			'telefono'      => array( 'Telefono, come si legge (049 0990550)', 'sanitize_text_field' ),
			'telefono_link' => array( 'Telefono, per la chiamata (+390490990550)', 'sanitize_text_field' ),
			'email'         => array( 'Email', 'sanitize_email' ),
			'comune'        => array( 'Comune e provincia', 'sanitize_text_field' ),
			'indirizzi'     => array( 'Indirizzi (separati da virgola)', 'sanitize_text_field' ),
			'mappa'         => array( 'Link a Google Maps', 'esc_url_raw' ),
			'societa'       => array( 'Ragione sociale (da chiedere al cliente)', 'sanitize_text_field' ),
			'piva'          => array( 'Partita IVA (da chiedere al cliente)', 'sanitize_text_field' ),
		);
		$file  = villaeidos_config( 'contatti' );
		foreach ( $campi as $k => $c ) {
			$wpc->add_setting(
				'villaeidos_recapito_' . $k,
				array(
					'type'              => 'theme_mod',
					'default'           => '',
					'sanitize_callback' => $c[1],
				)
			);
			$wpc->add_control(
				'villaeidos_recapito_' . $k,
				array(
					'section'     => 'villaeidos_recapiti',
					'label'       => $c[0],
					'type'        => 'mappa' === $k ? 'url' : 'text',
					'input_attrs' => array( 'placeholder' => isset( $file[ $k ] ) ? $file[ $k ] : '' ),
				)
			);
		}
	}
);

// Promemoria nel pannello finche' mancano ragione sociale e partita IVA.
add_action(
	'admin_notices',
	function () {
		if ( ! current_user_can( 'manage_options' ) || ( '' !== villaeidos_dato( 'societa' ) && '' !== villaeidos_dato( 'piva' ) ) ) {
			return;
		}
		echo '<div class="notice notice-warning"><p><strong>Villa Eidos:</strong> mancano ragione sociale e partita IVA (obbligatorie nel piede del sito). Si scrivono in <a href="' . esc_url( admin_url( 'customize.php?autofocus[section]=villaeidos_recapiti' ) ) . '">Aspetto &gt; Personalizza &gt; Recapiti</a>. Vanno completati anche i segnaposto [DA COMPLETARE] delle pagine Informativa privacy e Cookie.</p></div>';
	}
);

/**
 * Indirizzo di una pagina del sito per percorso (privacy, cookie), anche se non e' ancora stata creata.
 *
 * @param string $percorso Percorso della pagina.
 * @return string
 */
function villaeidos_pagina( $percorso ) {
	$p = get_page_by_path( $percorso );
	return $p ? get_permalink( $p ) : home_url( '/' . $percorso . '/' );
}

/**
 * I segnaposti delle parti in HTML, gia' pronti per l'HTML (testo con escape, indirizzi con esc_url).
 *
 * @return array
 */
function villaeidos_segnaposti_parti() {
	$t         = get_template_directory_uri() . '/assets/';
	$indirizzi = array_map( 'trim', explode( ',', villaeidos_dato( 'indirizzi' ) ) );
	return array(
		'{{home}}'        => is_front_page() ? '' : esc_url( home_url( '/' ) ),
		'{{logo}}'        => esc_url( $t . 'logo/villaeidos-orizzontale.svg' ),
		'{{logo_intero}}' => esc_url( $t . 'logo/villaeidos-logo.svg' ),
		'{{tel}}'         => esc_html( villaeidos_dato( 'telefono' ) ),
		'{{tel_link}}'    => esc_attr( villaeidos_dato( 'telefono_link' ) ),
		'{{email}}'       => esc_html( villaeidos_dato( 'email' ) ),
		'{{comune}}'      => esc_html( villaeidos_dato( 'comune' ) ),
		'{{indirizzi}}'   => implode( '<br>', array_map( 'esc_html', array_filter( $indirizzi ) ) ),
		'{{mappa}}'       => esc_url( villaeidos_dato( 'mappa' ) ),
		'{{privacy}}'     => esc_url( villaeidos_pagina( 'privacy' ) ),
		'{{cookie}}'      => esc_url( villaeidos_pagina( 'cookie' ) ),
		'{{anno}}'        => esc_html( wp_date( 'Y' ) ),
		'{{legale}}'      => villaeidos_riga_legale(),
	);
}

/**
 * Stampa una parte di parti/ (testata, piede) con i segnaposti sostituiti. Il commento iniziale non si stampa.
 *
 * @param string $nome  Nome del file senza estensione.
 * @param array  $altri Altri segnaposti.
 * @return string
 */
function villaeidos_parte( $nome, $altri = array() ) {
	$f = get_template_directory() . '/parti/' . sanitize_file_name( $nome ) . '.html';
	if ( ! file_exists( $f ) ) {
		return '';
	}
	$h = file_get_contents( $f ); // phpcs:ignore WordPress.WP.AlternativeFunctions.file_get_contents_file_get_contents
	$h = preg_replace( '/^\s*<!--.*?-->\s*/s', '', $h );
	return strtr( $h, array_merge( villaeidos_segnaposti_parti(), $altri ) );
}

add_action(
	'after_setup_theme',
	function () {
		add_theme_support( 'title-tag' );
		add_theme_support( 'post-thumbnails' );
		add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
	}
);

add_filter(
	'language_attributes',
	function ( $a ) {
		return preg_replace( '/lang="[^"]*"/', 'lang="it"', $a );
	}
);

add_filter(
	'body_class',
	function ( $c ) {
		$c[] = 've';
		if ( is_singular() && get_post_meta( get_queried_object_id(), '_villaeidos_noindex', true ) ) {
			$c[] = 've-legale';
		}
		return $c;
	}
);

add_action(
	'wp_enqueue_scripts',
	function () {
		$t   = get_template_directory_uri();
		$dip = wp_style_is( 'elementor-frontend', 'registered' ) ? array( 'elementor-frontend' ) : array();
		wp_enqueue_style( 'villaeidos', $t . '/assets/sito.css', $dip, VILLAEIDOS_VERSIONE );
		wp_enqueue_script( 'villaeidos', $t . '/assets/sito.js', array(), VILLAEIDOS_VERSIONE, array( 'in_footer' => true ) );
		// il sito usa solo i suoi fogli di stile: via quelli dei blocchi, che non servono
		foreach ( array( 'wp-block-library', 'wp-block-library-theme', 'global-styles', 'classic-theme-styles' ) as $h ) {
			wp_dequeue_style( $h );
		}
	},
	20
);

remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
remove_action( 'wp_enqueue_scripts', 'wp_enqueue_global_styles' );
remove_action( 'wp_footer', 'wp_enqueue_global_styles', 1 );
remove_action( 'wp_head', 'wp_generator' );
add_filter( 'run_wptexturize', '__return_false' );
remove_filter( 'the_content', 'convert_smilies', 20 );
add_filter( 'wp_img_tag_add_auto_sizes', '__return_false' );

// Titolo e descrizione delle pagine, scritti dall'installatore (campi _villaeidos_titolo e _villaeidos_descrizione).
add_filter(
	'pre_get_document_title',
	function ( $t ) {
		if ( is_singular() ) {
			$s = get_post_meta( get_queried_object_id(), '_villaeidos_titolo', true );
			if ( $s ) {
				return $s;
			}
		}
		return $t;
	}
);

add_action(
	'wp_head',
	function () {
		$t = get_template_directory_uri() . '/assets/';
		// i due caratteri del sito, precaricati (sono nel tema)
		echo '<link rel="preload" href="' . esc_url( $t . 'fonts/brygada-1918-latin.woff2' ) . '" as="font" type="font/woff2" crossorigin>' . "\n";
		echo '<link rel="preload" href="' . esc_url( $t . 'fonts/pontano-sans-latin.woff2' ) . '" as="font" type="font/woff2" crossorigin>' . "\n";
		if ( ! has_site_icon() ) {
			echo '<link rel="icon" href="' . esc_url( $t . 'logo/villaeidos-marchio.svg' ) . '" type="image/svg+xml">' . "\n";
		}
		if ( ! is_singular() ) {
			return;
		}
		$id = get_queried_object_id();
		$d  = get_post_meta( $id, '_villaeidos_descrizione', true );
		if ( $d ) {
			echo '<meta name="description" content="' . esc_attr( $d ) . '">' . "\n";
		}
	},
	1
);

// Le pagine legali non vanno nei motori di ricerca.
add_filter(
	'wp_robots',
	function ( $r ) {
		if ( is_singular() && get_post_meta( get_queried_object_id(), '_villaeidos_noindex', true ) ) {
			$r['noindex'] = true;
			unset( $r['max-image-preview'] );
		}
		return $r;
	}
);
