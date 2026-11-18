<?php
/**
 * Elementor: i piccoli aggiustamenti che rendono i widget normali uguali all'anteprima.
 *
 * - Foto d'apertura (classe apertura-foto): si carica subito e con priorita' alta; se la foto ha la versione per il
 *   telefono (campo _villaeidos_tel dell'allegato) diventa un <picture>. Oggi nessuna foto ce l'ha: la cornice e' 4:5
 *   ovunque e una foto nuova (quella della villa) si ritaglia al centro.
 * - Immagini della libreria: "sizes" scritto dall'installatore (campo _villaeidos_sizes), cosi' il browser sceglie la
 *   misura giusta; tutte pigre tranne l'apertura.
 * - Niente Google Fonts di Elementor: i caratteri sono nel tema.
 *
 * @package villaeidos
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_filter( 'elementor/frontend/print_google_fonts', '__return_false' );

/**
 * Le classi CSS di un elemento di Elementor.
 *
 * @param \Elementor\Element_Base $el Elemento.
 * @return string[]
 */
function villaeidos_classi( $el ) {
	$s = $el->get_settings();
	$c = isset( $s['_css_classes'] ) ? $s['_css_classes'] : ( isset( $s['css_classes'] ) ? $s['css_classes'] : '' );
	return preg_split( '/\s+/', trim( (string) $c ) );
}

add_filter(
	'elementor/widget/render_content',
	function ( $html, $widget ) {
		if ( 'image' !== $widget->get_name() || ! in_array( 'apertura-foto', villaeidos_classi( $widget ), true ) ) {
			return $html;
		}
		$html = preg_replace( '/\sloading="[^"]*"/', '', $html );
		$html = preg_replace( '/\sfetchpriority="[^"]*"/', '', $html );
		$html = preg_replace( '/<img /', '<img loading="eager" fetchpriority="high" ', $html, 1 );
		$s    = $widget->get_settings_for_display();
		$id   = isset( $s['image']['id'] ) ? (int) $s['image']['id'] : 0;
		$tel  = $id ? (int) get_post_meta( $id, '_villaeidos_tel', true ) : 0;
		if ( $tel ) {
			$srcset = wp_get_attachment_image_srcset( $tel, 'full' );
			if ( ! $srcset ) {
				$srcset = wp_get_attachment_image_url( $tel, 'full' );
			}
			$sizes    = get_post_meta( $tel, '_villaeidos_sizes', true );
			$sorgente = '<source media="(max-width: 760px)" srcset="' . esc_attr( $srcset ) . '" sizes="' . esc_attr( $sizes ? $sizes : '100vw' ) . '">';
			$html     = preg_replace( '/<img [^>]*>/', '<picture>' . $sorgente . '$0</picture>', $html, 1 );
		}
		return $html;
	},
	10,
	2
);

add_filter(
	'wp_calculate_image_sizes',
	function ( $sizes, $size, $src, $meta, $id ) {
		if ( $id ) {
			$s = get_post_meta( $id, '_villaeidos_sizes', true );
			if ( $s ) {
				return $s;
			}
		}
		return $sizes;
	},
	10,
	5
);
add_filter(
	'wp_get_attachment_image_attributes',
	function ( $attr ) {
		unset( $attr['fetchpriority'] );
		$attr['loading'] = 'lazy'; // tutte pigre, tranne la foto d'apertura (sopra)
		return $attr;
	}
);

// Elementor e WordPress possono ripetere un attributo gia' scritto: nel tag finale resta solo il primo.
add_filter(
	'wp_content_img_tag',
	function ( $img ) {
		$visti = array();
		return preg_replace_callback(
			'/\s([a-zA-Z-]+)(="[^"]*")?(?=[\s\/>])/',
			function ( $m ) use ( &$visti ) {
				$k = strtolower( $m[1] );
				if ( isset( $visti[ $k ] ) ) {
					return '';
				}
				$visti[ $k ] = true;
				return $m[0];
			},
			$img
		);
	},
	99
);
