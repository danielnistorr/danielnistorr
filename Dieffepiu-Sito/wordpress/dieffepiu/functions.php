<?php
/**
 * Tema Dieffepiu.
 *
 * - Stili, caratteri e immagini sono nel tema (assets/): il sito non dipende da servizi esterni.
 * - Testata e piede sono in parti/*.html; il menu della testata si puo' cambiare da Aspetto > Menu.
 * - Nei contenuti delle pagine {{casa}} e {{tema}} diventano l'indirizzo del sito e quello del tema:
 *   il sito funziona anche se cambia dominio o cartella.
 * - Moduli: shortcode [dieffepiu_modulo tipo="contatti"] e [dieffepiu_modulo tipo="accesso"],
 *   inviati per email con wp_mail all'indirizzo scelto in Aspetto > Installa Dieffepiu.
 *
 * @package dieffepiu
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'DFP_VERSIONE', '1.0.0' );

require get_template_directory() . '/inc/installa.php';

add_action(
	'after_setup_theme',
	function () {
		add_theme_support( 'title-tag' );
		add_theme_support( 'post-thumbnails' );
		add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
		register_nav_menus( array( 'principale' => 'Menu della testata' ) );
	}
);

add_action(
	'wp_enqueue_scripts',
	function () {
		$t = get_template_directory_uri();
		wp_enqueue_style( 'dieffepiu', $t . '/assets/sito.css', array(), DFP_VERSIONE );
		wp_enqueue_script( 'dieffepiu', $t . '/assets/sito.js', array(), DFP_VERSIONE, array( 'in_footer' => true ) );
		// il sito usa solo il suo foglio di stile: via quelli dei blocchi, che non servono
		foreach ( array( 'wp-block-library', 'wp-block-library-theme', 'global-styles', 'classic-theme-styles' ) as $h ) {
			wp_dequeue_style( $h );
		}
	},
	20
);

remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_enqueue_scripts', 'wp_enqueue_global_styles' );
remove_action( 'wp_footer', 'wp_enqueue_global_styles', 1 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
add_filter( 'run_wptexturize', '__return_false' );
remove_filter( 'the_content', 'convert_smilies', 20 );

/**
 * Sostituisce i segnaposto dei contenuti.
 *
 * @param string $html HTML con {{casa}} e {{tema}}.
 * @return string
 */
function dfp_token( $html ) {
	return strtr(
		(string) $html,
		array(
			'{{casa}}' => untrailingslashit( home_url() ),
			'{{tema}}' => get_template_directory_uri(),
		)
	);
}
add_filter( 'the_content', 'dfp_token', 8 );

/**
 * Una parte del tema (parti/<nome>.html), con i segnaposto sostituiti.
 *
 * @param string $nome Nome del file senza estensione.
 * @return string
 */
function dfp_parte( $nome ) {
	$f = get_template_directory() . '/parti/' . sanitize_file_name( $nome ) . '.html';
	if ( ! file_exists( $f ) ) {
		return '';
	}
	return dfp_token( file_get_contents( $f ) ); // phpcs:ignore WordPress.WP.AlternativeFunctions.file_get_contents_file_get_contents
}

/**
 * Indirizzo della pagina corrente, per segnare la voce del menu.
 *
 * @return string
 */
function dfp_qui() {
	global $wp;
	$r = isset( $wp->request ) ? $wp->request : '';
	return trailingslashit( home_url( $r ? '/' . $r : '/' ) );
}

/**
 * La testata, con il menu di Aspetto > Menu se c'e' e la voce della pagina corrente segnata.
 *
 * @return string
 */
function dfp_testata() {
	$h      = dfp_parte( 'testata' );
	$luoghi = get_nav_menu_locations();
	if ( ! empty( $luoghi['principale'] ) ) {
		$voci = wp_get_nav_menu_items( $luoghi['principale'] );
		if ( $voci ) {
			$righe = '';
			foreach ( $voci as $v ) {
				if ( (int) $v->menu_item_parent ) {
					continue;
				}
				$righe .= '      <a href="' . esc_url( $v->url ) . '">' . esc_html( $v->title ) . "</a>\n";
			}
			$h = preg_replace( '#<!--voci-->.*?<!--/voci-->#s', $righe, $h );
		}
	}
	$qui  = dfp_qui();
	$casa = trailingslashit( home_url( '/' ) );
	$i    = strpos( $h, '<nav class="menu"' );
	$j    = strpos( $h, '</nav>', (int) $i );
	if ( false !== $i && false !== $j ) {
		$nav = substr( $h, $i, $j - $i );
		$nav = preg_replace_callback(
			'#<a href="([^"]+)">#',
			function ( $m ) use ( $qui, $casa ) {
				$u = trailingslashit( html_entity_decode( $m[1] ) );
				if ( $u !== $casa && 0 === strpos( $qui, $u ) ) {
					return '<a href="' . $m[1] . '" aria-current="page">';
				}
				return $m[0];
			},
			$nav
		);
		$h = substr( $h, 0, $i ) . $nav . substr( $h, $j );
	}
	return $h;
}

/**
 * Briciole di pane: Home / ... / pagina corrente.
 *
 * @param array $voci Ogni voce e' array( url, nome ) oppure il solo nome (ultima voce, senza link).
 * @return string
 */
function dfp_briciole( $voci ) {
	$pezzi = array( '<a href="' . esc_url( home_url( '/' ) ) . '">Home</a>' );
	foreach ( $voci as $v ) {
		if ( is_array( $v ) ) {
			$pezzi[] = '<a href="' . esc_url( $v[0] ) . '">' . esc_html( $v[1] ) . '</a>';
		} else {
			$pezzi[] = '<span aria-current="page">' . esc_html( $v ) . '</span>';
		}
	}
	return '<nav class="briciole" aria-label="Sei qui">' . implode( '<span class="sep" aria-hidden="true">/</span>', $pezzi ) . '</nav>';
}

/**
 * Indirizzo della pagina delle notizie.
 *
 * @return string
 */
function dfp_url_notizie() {
	$id = (int) get_option( 'page_for_posts' );
	return $id ? get_permalink( $id ) : home_url( '/news/' );
}

/**
 * Data in italiano senza dipendere dalla lingua installata.
 *
 * @param int  $ts       Timestamp.
 * @param bool $articolo Con l'articolo ("il 13 ottobre 2025", "l'8 settembre 2026").
 * @return string
 */
function dfp_data( $ts, $articolo = false ) {
	$mesi = array( 1 => 'gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre' );
	$g    = (int) wp_date( 'j', $ts );
	$s    = $g . ' ' . $mesi[ (int) wp_date( 'n', $ts ) ] . ' ' . wp_date( 'Y', $ts );
	if ( ! $articolo ) {
		return $s;
	}
	return ( in_array( $g, array( 8, 11 ), true ) ? "l\u{2019}" : 'il ' ) . $s;
}

// Titolo e descrizione delle pagine scritti dall'installatore (campi _dfp_titolo_seo e _dfp_descrizione).
add_filter(
	'pre_get_document_title',
	function ( $t ) {
		$id = dfp_id_corrente();
		if ( $id ) {
			$s = get_post_meta( $id, '_dfp_titolo_seo', true );
			if ( $s ) {
				return $s;
			}
		}
		return $t;
	}
);

/**
 * ID della pagina o dell'articolo che si sta guardando (anche la pagina delle notizie).
 *
 * @return int
 */
function dfp_id_corrente() {
	if ( is_home() && ! is_front_page() ) {
		return (int) get_option( 'page_for_posts' );
	}
	if ( is_singular() ) {
		return (int) get_queried_object_id();
	}
	return 0;
}

add_action(
	'wp_head',
	function () {
		$t = get_template_directory_uri();
		echo '<link rel="preload" href="' . esc_url( $t . '/assets/fonts/pathway-latin.woff2' ) . '" as="font" type="font/woff2" crossorigin>' . "\n";
		if ( ! has_site_icon() ) {
			echo '<link rel="icon" type="image/png" href="' . esc_url( $t . '/assets/img/icona-180.png' ) . '">' . "\n";
		}
		$id = dfp_id_corrente();
		$d  = $id ? get_post_meta( $id, '_dfp_descrizione', true ) : '';
		if ( ! $d && is_singular( 'post' ) ) {
			$d = get_the_excerpt( $id );
		}
		if ( $d ) {
			echo '<meta name="description" content="' . esc_attr( wp_strip_all_tags( $d ) ) . '">' . "\n";
		}
	},
	1
);

// ------------------------------------------------------------------ moduli

/**
 * Campi dei due moduli: nome => etichetta, e quali sono obbligatori.
 *
 * @param string $tipo contatti | accesso.
 * @return array
 */
function dfp_campi( $tipo ) {
	if ( 'accesso' === $tipo ) {
		return array(
			array(
				'azienda'   => 'Azienda',
				'piva'      => 'Partita IVA',
				'nome'      => 'Nome e cognome',
				'email'     => 'Email',
				'telefono'  => 'Telefono',
				'attivita'  => 'Attività',
				'messaggio' => 'Note',
			),
			array( 'azienda', 'piva', 'nome', 'email' ),
		);
	}
	return array(
		array(
			'nome'      => 'Nome e cognome',
			'azienda'   => 'Azienda',
			'email'     => 'Email',
			'telefono'  => 'Telefono',
			'paese'     => 'Paese',
			'argomento' => 'Argomento',
			'messaggio' => 'Messaggio',
		),
		array( 'nome', 'azienda', 'email', 'messaggio' ),
	);
}

add_shortcode(
	'dieffepiu_modulo',
	function ( $a ) {
		$a    = shortcode_atts( array( 'tipo' => 'contatti' ), $a );
		$tipo = 'accesso' === $a['tipo'] ? 'accesso' : 'contatti';
		$html = dfp_parte( 'modulo-' . $tipo );
		$stato = isset( $_GET['modulo'] ) ? sanitize_key( wp_unslash( $_GET['modulo'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification
		$esito = '';
		if ( 'inviato' === $stato ) {
			$esito = 'Grazie: il messaggio è partito.';
			$html  = str_replace( 'class="esito-m"', 'class="esito-m ok"', $html );
		} elseif ( 'errore' === $stato ) {
			$esito = 'Il messaggio non è partito: controllate i campi con l’asterisco e il consenso, poi riprovate. Oppure chiamate il +39 049 8791175.';
			$html  = str_replace( 'class="esito-m"', 'class="esito-m errore"', $html );
		}
		$campi = '<input type="hidden" name="action" value="dfp_modulo">'
			. '<input type="hidden" name="tipo" value="' . esc_attr( $tipo ) . '">'
			. '<input type="hidden" name="ritorno" value="' . esc_url( get_permalink() ) . '">'
			. wp_nonce_field( 'dfp_modulo_' . $tipo, '_dfp', false, false );
		return strtr(
			$html,
			array(
				'{{azione}}'   => esc_url( admin_url( 'admin-post.php' ) ),
				'{{campi_wp}}' => $campi,
				'{{esito}}'    => esc_html( $esito ),
			)
		);
	}
);

/**
 * Riceve un modulo, lo controlla e lo manda per email. Poi torna alla pagina con ?modulo=inviato o =errore.
 */
function dfp_modulo_invia() {
	// phpcs:disable WordPress.Security.NonceVerification.Missing -- il nonce si controlla qui sotto
	$tipo    = ( isset( $_POST['tipo'] ) && 'accesso' === $_POST['tipo'] ) ? 'accesso' : 'contatti';
	$ritorno = isset( $_POST['ritorno'] ) ? esc_url_raw( wp_unslash( $_POST['ritorno'] ) ) : home_url( '/' );
	$ritorno = wp_validate_redirect( $ritorno, home_url( '/' ) );
	$ok      = isset( $_POST['_dfp'] ) && wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST['_dfp'] ) ), 'dfp_modulo_' . $tipo );
	if ( ! empty( $_POST['sito_web'] ) ) {
		$ok = false; // trappola per i programmi automatici
	}
	list( $campi, $obbligatori ) = dfp_campi( $tipo );
	$v = array();
	foreach ( $campi as $k => $etichetta ) {
		$grezzo  = isset( $_POST[ $k ] ) ? wp_unslash( $_POST[ $k ] ) : ''; // phpcs:ignore WordPress.Security.ValidatedSanitizedInput.InputNotSanitized
		$v[ $k ] = 'messaggio' === $k ? sanitize_textarea_field( $grezzo ) : sanitize_text_field( $grezzo );
	}
	foreach ( $obbligatori as $k ) {
		if ( '' === $v[ $k ] ) {
			$ok = false;
		}
	}
	if ( ! is_email( $v['email'] ) || empty( $_POST['consenso'] ) ) {
		$ok = false;
	}
	// phpcs:enable
	$ip     = isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( wp_unslash( $_SERVER['REMOTE_ADDR'] ) ) : '';
	$freno  = 'dfp_m_' . md5( $ip );
	if ( $ok && get_transient( $freno ) ) {
		$ok = false; // un invio ogni 30 secondi dallo stesso indirizzo
	}
	if ( $ok ) {
		$corpo = '';
		foreach ( $campi as $k => $etichetta ) {
			$corpo .= $etichetta . ': ' . $v[ $k ] . "\n";
		}
		$corpo  .= "\nConsenso privacy: sì\nPagina: " . $ritorno . "\nData: " . wp_date( 'j/m/Y H:i' ) . "\n";
		$a       = get_option( 'dfp_email_moduli', get_option( 'admin_email' ) );
		$oggetto = ( 'accesso' === $tipo ? 'Richiesta di accesso all’area riservata: ' : 'Richiesta dal sito: ' ) . $v['azienda'];
		$nome    = str_replace( array( '"', '<', '>' ), '', $v['nome'] );
		$ok      = wp_mail( $a, $oggetto, $corpo, array( 'Reply-To: "' . $nome . '" <' . $v['email'] . '>' ) );
		set_transient( $freno, 1, 30 );
	}
	wp_safe_redirect( add_query_arg( 'modulo', $ok ? 'inviato' : 'errore', $ritorno ) . '#modulo' );
	exit;
}
add_action( 'admin_post_nopriv_dfp_modulo', 'dfp_modulo_invia' );
add_action( 'admin_post_dfp_modulo', 'dfp_modulo_invia' );
