<?php
/**
 * Modulo "Richiesta di disponibilita'": shortcode [villaeidos_richiesta].
 *
 * L'HTML e' parti/richiesta.html (lo stesso dell'anteprima), lo script assets/richiesta.js; indirizzo, oggetto e tipi
 * di spazio in config/richiesta.php. Il modulo prepara una mail (mailto) nel programma di posta di chi scrive:
 * il sito non riceve e non salva dati, quindi non serve un plugin per i moduli.
 *
 * @package villaeidos
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_shortcode(
	'villaeidos_richiesta',
	function () {
		$c     = villaeidos_config( 'richiesta' );
		$email = isset( $c['email'] ) ? $c['email'] : villaeidos_dato( 'email' );
		$tipi  = '';
		foreach ( (array) ( isset( $c['tipi'] ) ? $c['tipi'] : array() ) as $i => $t ) {
			$tipi .= '<label><input type="radio" name="tipo" value="' . esc_attr( $t ) . '"' . ( 0 === $i ? ' required' : '' ) . '><span>' . esc_html( $t ) . '</span></label>';
		}
		wp_enqueue_script( 'villaeidos-richiesta', get_template_directory_uri() . '/assets/richiesta.js', array(), VILLAEIDOS_VERSIONE, array( 'in_footer' => true ) );
		wp_localize_script( 'villaeidos-richiesta', 'VILLAEIDOS_RICHIESTA', array( 'oggetto' => isset( $c['oggetto'] ) ? $c['oggetto'] : 'Richiesta di disponibilità' ) );
		return villaeidos_parte(
			'richiesta',
			array(
				'{{email}}' => esc_html( $email ),
				'{{tipi}}'  => $tipi,
			)
		);
	}
);
