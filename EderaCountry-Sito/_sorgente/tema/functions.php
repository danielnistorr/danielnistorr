<?php
/**
 * Tema Edera Country House.
 *
 * - Le pagine (Home, Informativa privacy, Cookie) sono fatte in Elementor con widget normali
 *   (Titolo, Editor di testo, Immagine, Pulsante, Elenco icone) dentro contenitori con classi CSS.
 *   Il tema da' l'aspetto: assets/sito.css aggancia quelle classi; testata, menu del telefono e piede
 *   sono in parti/ (HTML uguale a quello del sito originale).
 * - Il calcolatore "Preventivo flash" e' lo shortcode [edera_preventivo]: prezzi e regole in config/preventivo.php.
 * - La planimetria (tema 1.1) e' tutta in Elementor: foto dall'alto, pallini (Pulsanti in posizione assoluta),
 *   legenda, galleria del Rustico con il lightbox di Elementor. Il tema ne da' solo l'aspetto (sito.css).
 * - Caratteri e immagini sono nel tema e nella libreria media: il sito non chiama servizi esterni
 *   e non usa cookie (per questo non c'e' il banner, come nell'originale).
 * - Movimenti (titolo d'apertura, foto della galleria, testata): si spengono da
 *   Aspetto > Personalizza > Movimenti, vedi inc/movimento.php.
 * - Installazione: Aspetto > Installa Edera, oppure installa-su-server.sh con WP-CLI (inc/installa.php).
 *
 * @package edera
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'EDERA_VERSIONE', '1.1.0' );

require get_template_directory() . '/inc/installa.php';
require get_template_directory() . '/inc/elementor.php';
require get_template_directory() . '/inc/preventivo.php';
require get_template_directory() . '/inc/movimento.php';

/**
 * Un file di config/ (array PHP), letto una volta sola.
 *
 * @param string $nome Nome del file senza estensione.
 * @return array
 */
function edera_config( $nome ) {
	static $cache = array();
	if ( ! isset( $cache[ $nome ] ) ) {
		$f              = get_template_directory() . '/config/' . sanitize_file_name( $nome ) . '.php';
		$cache[ $nome ] = file_exists( $f ) ? (array) include $f : array();
	}
	return $cache[ $nome ];
}

/**
 * Un recapito di config/contatti.php.
 *
 * @param string $k Chiave.
 * @return string
 */
function edera_dato( $k ) {
	$c = edera_config( 'contatti' );
	return isset( $c[ $k ] ) ? (string) $c[ $k ] : '';
}

/**
 * La pagina corrente usa il modello "Pagina legale"?
 *
 * @return bool
 */
function edera_legale() {
	return is_page_template( 'modelli/legale.php' );
}

/**
 * Link a una sezione della home: sulla home resta un'ancora (#location), altrove porta alla home.
 *
 * @param string $ancora Ancora con il cancelletto.
 * @return string
 */
function edera_ancora( $ancora ) {
	if ( is_front_page() ) {
		return $ancora;
	}
	return home_url( '/' ) . ( '#' === $ancora ? '' : $ancora );
}

/**
 * Indirizzo di una pagina del sito per percorso (privacy, cookie), anche se non e' ancora stata creata.
 *
 * @param string $percorso Percorso della pagina.
 * @return string
 */
function edera_pagina( $percorso ) {
	$p = get_page_by_path( $percorso );
	return $p ? get_permalink( $p ) : home_url( '/' . $percorso . '/' );
}

add_action(
	'after_setup_theme',
	function () {
		add_theme_support( 'title-tag' );
		add_theme_support( 'post-thumbnails' );
		add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
	}
);

// lingua della pagina come nell'originale (lang="it")
add_filter(
	'language_attributes',
	function ( $a ) {
		return preg_replace( '/lang="[^"]*"/', 'lang="it"', $a );
	}
);

add_filter(
	'body_class',
	function ( $c ) {
		$c[] = edera_legale() ? 'edera-legale' : 'edera';
		return $c;
	}
);

add_action(
	'wp_enqueue_scripts',
	function () {
		$t   = get_template_directory_uri();
		$dip = wp_style_is( 'elementor-frontend', 'registered' ) ? array( 'elementor-frontend' ) : array();
		if ( edera_legale() ) {
			wp_enqueue_style( 'edera-legale', $t . '/assets/legale.css', $dip, EDERA_VERSIONE );
		} else {
			wp_enqueue_style( 'edera', $t . '/assets/sito.css', $dip, EDERA_VERSIONE );
			wp_enqueue_script( 'edera', $t . '/assets/sito.js', array(), EDERA_VERSIONE, array( 'in_footer' => true ) );
		}
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
// apostrofi e virgolette restano quelli scritti (l'originale usa l'apostrofo dritto)
add_filter( 'run_wptexturize', '__return_false' );
remove_filter( 'the_content', 'convert_smilies', 20 );
// le immagini scelgono la misura con "sizes", come nell'originale (niente "sizes=auto")
add_filter( 'wp_img_tag_add_auto_sizes', '__return_false' );

// Titolo e descrizione delle pagine, scritti dall'installatore (campi _edera_titolo e _edera_descrizione).
add_filter(
	'pre_get_document_title',
	function ( $t ) {
		if ( is_singular() ) {
			$s = get_post_meta( get_queried_object_id(), '_edera_titolo', true );
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
		if ( ! is_singular() ) {
			return;
		}
		$id = get_queried_object_id();
		$d  = get_post_meta( $id, '_edera_descrizione', true );
		if ( $d ) {
			echo '<meta name="description" content="' . esc_attr( $d ) . '">' . "\n";
		}
		if ( is_front_page() ) {
			$u = edera_url_apertura( $id );
			if ( $u ) {
				echo '<link rel="preload" href="' . esc_url( $u ) . '" as="image" media="(min-width: 761px)">' . "\n";
			}
		}
	},
	1
);

// Le pagine legali non vanno nei motori di ricerca (come nell'originale).
add_filter(
	'wp_robots',
	function ( $r ) {
		if ( is_singular() && get_post_meta( get_queried_object_id(), '_edera_noindex', true ) ) {
			$r['noindex'] = true;
			unset( $r['max-image-preview'] );
		}
		return $r;
	}
);

/**
 * Indirizzo della foto d'apertura della home (la prima immagine con la classe apertura-foto), per il preload.
 *
 * @param int $id Pagina.
 * @return string
 */
function edera_url_apertura( $id ) {
	$dati = get_post_meta( $id, '_elementor_data', true );
	if ( ! $dati ) {
		return '';
	}
	$el = is_array( $dati ) ? $dati : json_decode( $dati, true );
	$trova = function ( $els ) use ( &$trova ) {
		foreach ( (array) $els as $e ) {
			$s = isset( $e['settings'] ) ? $e['settings'] : array();
			if ( isset( $e['widgetType'] ) && 'image' === $e['widgetType'] && isset( $s['_css_classes'] ) && false !== strpos( $s['_css_classes'], 'apertura-foto' ) ) {
				return isset( $s['image'] ) ? $s['image'] : null;
			}
			if ( ! empty( $e['elements'] ) ) {
				$r = $trova( $e['elements'] );
				if ( $r ) {
					return $r;
				}
			}
		}
		return null;
	};
	$img = $trova( $el );
	if ( ! $img ) {
		return '';
	}
	if ( ! empty( $img['id'] ) ) {
		$u = wp_get_attachment_image_url( (int) $img['id'], 'full' );
		if ( $u ) {
			return $u;
		}
	}
	return isset( $img['url'] ) ? $img['url'] : '';
}
