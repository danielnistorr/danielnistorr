<?php
/**
 * Elementor: i piccoli aggiustamenti che rendono i widget normali uguali all'HTML dell'originale.
 *
 * - Foto d'apertura (classe apertura-foto): si carica subito e con priorita' alta; se la foto ha la versione
 *   per il telefono (campo _edera_tel, scritto dall'installatore) diventa un <picture> con le due versioni.
 * - Immagini della libreria: "sizes" come nell'originale (campo _edera_sizes), cosi' il browser sceglie
 *   la stessa misura.
 * - Bottoni: la freccia finale (↗ ↓ →) diventa <span class="freccia">, come nell'originale.
 * - Elenchi fatti di contenitori (spazi, formati, domande): ruolo "list" per i lettori di schermo;
 *   numeri decorativi (classe n-sez e numeri delle domande) nascosti ai lettori di schermo.
 * - Niente Google Fonts di Elementor: i caratteri sono nel tema.
 *
 * @package edera
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
function edera_classi( $el ) {
	$s = $el->get_settings();
	$c = isset( $s['_css_classes'] ) ? $s['_css_classes'] : ( isset( $s['css_classes'] ) ? $s['css_classes'] : '' );
	return preg_split( '/\s+/', trim( (string) $c ) );
}

add_filter(
	'elementor/widget/render_content',
	function ( $html, $widget ) {
		$tipo   = $widget->get_name();
		$classi = edera_classi( $widget );
		if ( 'image' === $tipo && in_array( 'apertura-foto', $classi, true ) ) {
			$html = preg_replace( '/\sloading="lazy"/', '', $html );
			$html = preg_replace( '/\sfetchpriority="[^"]*"/', '', $html );
			$html = preg_replace( '/<img /', '<img loading="eager" fetchpriority="high" ', $html, 1 );
			$s    = $widget->get_settings_for_display();
			$id   = isset( $s['image']['id'] ) ? (int) $s['image']['id'] : 0;
			$tel  = $id ? (int) get_post_meta( $id, '_edera_tel', true ) : 0;
			if ( $tel ) {
				$srcset = wp_get_attachment_image_srcset( $tel, 'full' );
				if ( ! $srcset ) {
					$srcset = wp_get_attachment_image_url( $tel, 'full' );
				}
				$sorgente = '<source media="(max-width: 760px)" srcset="' . esc_attr( $srcset ) . '" sizes="100vw">';
				$html     = preg_replace( '/<img [^>]*>/', '<picture>' . $sorgente . '$0</picture>', $html, 1 );
			}
		}
		if ( 'button' === $tipo ) {
			$html = preg_replace( '/\s*([↗↓→↘])\s*(<\/span>)/u', ' <span class="freccia" aria-hidden="true">$1</span>$2', $html, 1 );
		}
		return $html;
	},
	10,
	2
);

// ruoli e attributi che l'HTML originale aveva su elenchi e numeri decorativi
$edera_attributi = function ( $el ) {
	$classi = edera_classi( $el );
	$elenchi = array(
		'spazi-elenco' => 'Gli spazi',
		'formati'      => '',
		'faq-elenco'   => '',
	);
	foreach ( $elenchi as $c => $nome ) {
		if ( in_array( $c, $classi, true ) ) {
			$el->add_render_attribute( '_wrapper', 'role', 'list' );
			if ( $nome ) {
				$el->add_render_attribute( '_wrapper', 'aria-label', $nome );
			}
		}
	}
	if ( array_intersect( array( 'spazio-voce', 'formato', 'faq-voce' ), $classi ) ) {
		$el->add_render_attribute( '_wrapper', 'role', 'listitem' );
	}
	if ( in_array( 'n-sez', $classi, true ) || in_array( 'nascosto-lettori', $classi, true ) ) {
		$el->add_render_attribute( '_wrapper', 'aria-hidden', 'true' );
	}
};
add_action( 'elementor/frontend/container/before_render', $edera_attributi );
add_action( 'elementor/frontend/widget/before_render', $edera_attributi );

// Immagini: "sizes" scritto dall'installatore (lo stesso dell'originale); niente priorita' alta automatica
// (la da' solo la foto d'apertura, sopra).
add_filter(
	'wp_calculate_image_sizes',
	function ( $sizes, $size, $src, $meta, $id ) {
		if ( $id ) {
			$s = get_post_meta( $id, '_edera_sizes', true );
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
		$attr['loading'] = 'lazy'; // come nell'originale: tutte pigre, tranne la foto d'apertura (vedi sopra)
		return $attr;
	}
);

// L'ottimizzazione delle immagini di Elementor e quella di WordPress possono ripetere un attributo gia' scritto
// (fetchpriority sulla foto d'apertura): nel tag finale resta solo il primo.
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
