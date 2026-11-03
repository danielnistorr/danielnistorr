<?php
/**
 * Installatore: Aspetto > Installa Dieffepiu.
 *
 * Crea (o aggiorna) le pagine dai file in contenuti/, le notizie delle fiere, il menu della testata,
 * la home statica, la pagina delle notizie e gli indirizzi /sistemi/, /macchine/, /news/<notizia>/ ...
 * Si puo' lanciare piu' volte: trova le pagine per indirizzo e non crea doppioni.
 *
 * @package dieffepiu
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action(
	'admin_menu',
	function () {
		add_theme_page( 'Installa Dieffepiu', 'Installa Dieffepiu', 'manage_options', 'dfp-installa', 'dfp_pagina_installa' );
	}
);

add_action(
	'admin_notices',
	function () {
		if ( get_option( 'dfp_installato' ) || ! current_user_can( 'manage_options' ) ) {
			return;
		}
		$s = get_current_screen();
		if ( $s && 'appearance_page_dfp-installa' === $s->id ) {
			return;
		}
		echo '<div class="notice notice-info"><p><strong>Tema Dieffepiu attivo.</strong> Per creare pagine, menu e notizie: <a href="' . esc_url( admin_url( 'themes.php?page=dfp-installa' ) ) . '">Aspetto &gt; Installa Dieffepiu</a>.</p></div>';
	}
);

/**
 * Legge un file JSON del tema.
 *
 * @param string $nome File in contenuti/.
 * @return array
 */
function dfp_leggi( $nome ) {
	$f = get_template_directory() . '/contenuti/' . $nome;
	if ( ! file_exists( $f ) ) {
		return array();
	}
	$d = json_decode( file_get_contents( $f ), true ); // phpcs:ignore WordPress.WP.AlternativeFunctions.file_get_contents_file_get_contents
	return is_array( $d ) ? $d : array();
}

/**
 * Esegue l'installazione.
 *
 * @param bool   $sovrascrivi Riscrive il contenuto delle pagine gia' presenti.
 * @param string $email       Destinatario dei moduli.
 * @param bool   $nascondi    Sito non indicizzabile (prova).
 * @param bool   $elementor   Costruisce le pagine come documenti Elementor (se Elementor e' attivo).
 * @return array Righe di resoconto.
 */
function dfp_installa( $sovrascrivi, $email, $nascondi, $elementor = false ) {
	$log   = array();
	$dir   = get_template_directory() . '/contenuti/';
	$ids   = array();
	$pag   = dfp_leggi( 'pagine.json' );
	usort(
		$pag,
		function ( $a, $b ) {
			return ( '' === $a['genitore'] ? 0 : 1 ) - ( '' === $b['genitore'] ? 0 : 1 );
		}
	);
	update_option( 'permalink_structure', '/news/%postname%/' );
	$elementor = $elementor && dfp_elementor();
	kses_remove_filters(); // i contenuti sono HTML del tema: niente filtri che tolgano attributi
	foreach ( $pag as $p ) {
		$percorso  = ( $p['genitore'] ? $p['genitore'] . '/' : '' ) . $p['slug'];
		$contenuto = file_get_contents( $dir . $p['file'] ); // phpcs:ignore WordPress.WP.AlternativeFunctions.file_get_contents_file_get_contents
		$esiste    = get_page_by_path( $percorso, OBJECT, 'page' );
		$dati      = array(
			'post_type'    => 'page',
			'post_status'  => 'publish',
			'post_title'   => $p['titolo'],
			'post_name'    => $p['slug'],
			'menu_order'   => (int) $p['ordine'],
			'post_parent'  => $p['genitore'] && isset( $ids[ $p['genitore'] ] ) ? $ids[ $p['genitore'] ] : 0,
			'comment_status' => 'closed',
			'ping_status'  => 'closed',
		);
		if ( $esiste ) {
			$dati['ID'] = $esiste->ID;
			if ( $sovrascrivi ) {
				$dati['post_content'] = wp_slash( $contenuto );
			}
			$id    = wp_update_post( $dati, true );
			$log[] = ( $sovrascrivi ? 'Aggiornata' : 'Già presente (contenuto lasciato com’era)' ) . ': ' . $p['titolo'] . ' /' . $percorso . '/';
		} else {
			$dati['post_content'] = wp_slash( $contenuto );
			$id                   = wp_insert_post( $dati, true );
			$log[]                = 'Creata: ' . $p['titolo'] . ' /' . $percorso . '/';
		}
		if ( is_wp_error( $id ) ) {
			$log[] = 'ERRORE su ' . $p['titolo'] . ': ' . $id->get_error_message();
			continue;
		}
		$ids[ $p['slug'] ] = $id;
		// la pagina delle notizie la disegna il tema (index.php): Elementor non apre la pagina degli articoli
		if ( $elementor && 'news' !== $p['slug'] && ( $sovrascrivi || ! $esiste || 'builder' !== get_post_meta( $id, '_elementor_edit_mode', true ) ) ) {
			$fatto = dfp_elementor_pagina( $id, $contenuto );
			$log[] = $fatto ? '  costruita con Elementor (' . $p['titolo'] . ')' : '  ERRORE: Elementor non ha salvato ' . $p['titolo'];
		}
		update_post_meta( $id, '_dfp_chiave', $p['chiave'] );
		update_post_meta( $id, '_dfp_titolo_seo', $p['titolo_seo'] );
		update_post_meta( $id, '_dfp_descrizione', $p['descrizione'] );
	}
	kses_init_filters();
	if ( $elementor ) {
		update_option( 'elementor_disable_color_schemes', 'yes' );
		update_option( 'elementor_disable_typography_schemes', 'yes' );
		update_option( 'elementor_google_font', '0' );
		\Elementor\Plugin::$instance->files_manager->clear_cache();
		$log[] = 'Elementor: le pagine si aprono con "Modifica con Elementor", una sezione per contenitore.';
	}

	// home statica e pagina delle notizie
	if ( isset( $ids['home'] ) ) {
		update_option( 'show_on_front', 'page' );
		update_option( 'page_on_front', $ids['home'] );
		$log[] = 'Home: la pagina "Home" è la prima pagina del sito.';
	}
	if ( isset( $ids['news'] ) ) {
		update_option( 'page_for_posts', $ids['news'] );
		$log[] = 'Notizie: la pagina "Fiere e novità" mostra gli articoli.';
	}

	// notizie delle fiere
	$cat = term_exists( 'Fiere', 'category' );
	if ( ! $cat ) {
		$cat = wp_insert_term( 'Fiere', 'category', array( 'slug' => 'fiere' ) );
	}
	$cat_id = is_array( $cat ) ? (int) $cat['term_id'] : (int) $cat;
	foreach ( dfp_leggi( 'articoli.json' ) as $a ) {
		$esiste = get_page_by_path( $a['slug'], OBJECT, 'post' );
		if ( $esiste ) {
			$log[] = 'Notizia già presente: ' . $a['titolo'];
			continue;
		}
		$id = wp_insert_post(
			array(
				'post_type'     => 'post',
				'post_status'   => 'publish',
				'post_title'    => $a['titolo'],
				'post_name'     => $a['slug'],
				'post_date'     => $a['data'],
				'post_content'  => wp_slash( $a['testo'] ),
				'post_excerpt'  => wp_slash( $a['estratto'] ),
				'post_category' => array( $cat_id ),
				'comment_status' => 'closed',
			),
			true
		);
		if ( ! is_wp_error( $id ) ) {
			$log[] = 'Notizia creata: ' . $a['titolo'];
		}
	}
	// articolo e pagina di esempio di WordPress, solo se sono ancora quelli dell'installazione
	foreach ( array( 'hello-world', 'ciao-mondo' ) as $s ) {
		$x = get_page_by_path( $s, OBJECT, 'post' );
		if ( $x ) {
			wp_trash_post( $x->ID );
			$log[] = 'Spostato nel cestino l’articolo di esempio di WordPress.';
		}
	}
	foreach ( array( 'sample-page', 'pagina-di-esempio' ) as $s ) {
		$x = get_page_by_path( $s, OBJECT, 'page' );
		if ( $x ) {
			wp_trash_post( $x->ID );
			$log[] = 'Spostata nel cestino la pagina di esempio di WordPress.';
		}
	}

	// menu della testata: Sistemi, Macchine, Azienda, Contatti
	$menu = wp_get_nav_menu_object( 'Menu della testata' );
	if ( ! $menu ) {
		$menu_id = wp_create_nav_menu( 'Menu della testata' );
		foreach ( array( 'sistemi', 'macchine', 'azienda', 'contatti' ) as $i => $s ) {
			if ( isset( $ids[ $s ] ) ) {
				wp_update_nav_menu_item(
					$menu_id,
					0,
					array(
						'menu-item-object-id' => $ids[ $s ],
						'menu-item-object'    => 'page',
						'menu-item-type'      => 'post_type',
						'menu-item-status'    => 'publish',
						'menu-item-position'  => $i + 1,
					)
				);
			}
		}
		$log[] = 'Menu creato: Menu della testata (Sistemi, Macchine, Azienda, Contatti).';
	} else {
		$menu_id = $menu->term_id;
		$log[]   = 'Menu già presente: Menu della testata.';
	}
	$luoghi               = get_nav_menu_locations();
	$luoghi['principale'] = $menu_id;
	set_theme_mod( 'nav_menu_locations', $luoghi );

	// impostazioni
	flush_rewrite_rules();
	$log[] = 'Indirizzi: /sistemi/, /macchine/ ... e le notizie in /news/<titolo>/.';
	if ( 'Il mio blog' === get_option( 'blogname' ) || 'My WordPress Website' === get_option( 'blogname' ) || '' === get_option( 'blogname' ) ) {
		update_option( 'blogname', 'Dieffepiu' );
	}
	update_option( 'blogdescription', 'Sistemi e macchine per zanzariere' );
	update_option( 'timezone_string', 'Europe/Rome' );
	// italiano per il pannello e per le date, se il pacchetto della lingua si puo' scaricare
	if ( 'it_IT' !== get_locale() ) {
		require_once ABSPATH . 'wp-admin/includes/translation-install.php';
		if ( wp_can_install_language_pack() && wp_download_language_pack( 'it_IT' ) ) {
			update_option( 'WPLANG', 'it_IT' );
			$log[] = 'Lingua del sito: italiano.';
		}
	}
	update_option( 'date_format', 'j F Y' );
	update_option( 'default_comment_status', 'closed' );
	update_option( 'dfp_email_moduli', $email );
	$log[] = 'Moduli: i messaggi arrivano a ' . $email . '.';
	update_option( 'blog_public', $nascondi ? '0' : '1' );
	$log[] = $nascondi ? 'Sito nascosto ai motori di ricerca (sito di prova).' : 'Sito visibile ai motori di ricerca.';
	update_option( 'dfp_installato', DFP_VERSIONE . ' ' . wp_date( 'Y-m-d H:i' ) );
	return $log;
}

/**
 * Elementor e' caricato?
 *
 * @return bool
 */
function dfp_elementor() {
	return did_action( 'elementor/loaded' ) && class_exists( 'Elementor\\Plugin' ) && isset( \Elementor\Plugin::$instance->documents );
}

/**
 * Sette caratteri esadecimali, come gli ID degli elementi di Elementor.
 *
 * @return string
 */
function dfp_id7() {
	return substr( md5( uniqid( '', true ) . wp_rand() ), 0, 7 );
}

/**
 * Salva una pagina come documento Elementor: un contenitore a tutta larghezza per sezione, con dentro un widget HTML.
 * Gli indirizzi sono scritti per esteso (se cambia dominio: Elementor > Strumenti > Sostituisci URL) e i moduli
 * sono gia' dentro l'HTML, cosi' anche l'anteprima dell'editor di Elementor mostra la pagina com'e'.
 *
 * @param int    $id        Pagina.
 * @param string $contenuto Contenuto a blocchi del tema.
 * @return bool
 */
function dfp_elementor_pagina( $id, $contenuto ) {
	preg_match_all( '#<!-- wp:html -->\s*(.*?)\s*<!-- /wp:html -->#s', $contenuto, $m );
	$sezioni = $m[1] ? $m[1] : array( $contenuto );
	$els     = array();
	foreach ( $sezioni as $html ) {
		$html  = dfp_token( $html );
		$html  = preg_replace_callback(
			'#\[dieffepiu_modulo tipo="(\w+)"\]#',
			function ( $x ) use ( $id ) {
				return dfp_modulo_html( $x[1], get_permalink( $id ) );
			},
			$html
		);
		$els[] = array(
			'id'       => dfp_id7(),
			'elType'   => 'container',
			'isInner'  => false,
			'settings' => array(
				'content_width'  => 'full',
				'flex_direction' => 'column',
				'css_classes'    => 'dfp-sez',
				'padding'        => array( 'unit' => 'px', 'top' => '0', 'right' => '0', 'bottom' => '0', 'left' => '0', 'isLinked' => true ),
				'flex_gap'       => array( 'unit' => 'px', 'size' => 0, 'column' => '0', 'row' => '0', 'isLinked' => true ),
			),
			'elements' => array(
				array(
					'id'         => dfp_id7(),
					'elType'     => 'widget',
					'widgetType' => 'html',
					'isInner'    => false,
					'settings'   => array( 'html' => $html ),
					'elements'   => array(),
				),
			),
		);
	}
	if ( ! \Elementor\Plugin::$instance->kits_manager->get_active_id() ) {
		\Elementor\Core\Kits\Manager::create_default_kit();
	}
	$doc = \Elementor\Plugin::$instance->documents->get( $id, false );
	if ( ! $doc ) {
		return false;
	}
	$doc->set_is_built_with_elementor( true );
	return (bool) $doc->save( array( 'elements' => $els, 'settings' => array( 'hide_title' => 'yes' ) ) );
}

/**
 * Scarica, installa e attiva Elementor dal catalogo di WordPress.org.
 *
 * @return array
 */
function dfp_installa_elementor() {
	require_once ABSPATH . 'wp-admin/includes/plugin.php';
	require_once ABSPATH . 'wp-admin/includes/plugin-install.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/misc.php';
	require_once ABSPATH . 'wp-admin/includes/class-wp-upgrader.php';
	$log  = array();
	$file = 'elementor/elementor.php';
	if ( ! file_exists( WP_PLUGIN_DIR . '/' . $file ) ) {
		$api = plugins_api( 'plugin_information', array( 'slug' => 'elementor', 'fields' => array( 'sections' => false ) ) );
		if ( is_wp_error( $api ) ) {
			return array( 'Elementor non scaricato: ' . $api->get_error_message() . ' Installatelo da Plugin > Aggiungi nuovo.' );
		}
		$r     = ( new Plugin_Upgrader( new Automatic_Upgrader_Skin() ) )->install( $api->download_link );
		$log[] = ( $r && ! is_wp_error( $r ) ) ? 'Elementor ' . $api->version . ' installato.' : 'Elementor non installato: il server non lo permette da qui. Installatelo da Plugin > Aggiungi nuovo, poi tornate qui.';
	}
	if ( file_exists( WP_PLUGIN_DIR . '/' . $file ) && ! is_plugin_active( $file ) ) {
		$a     = activate_plugin( $file );
		$log[] = is_wp_error( $a ) ? 'Elementor non attivato: ' . $a->get_error_message() : 'Elementor attivo.';
	}
	delete_transient( 'elementor_activation_redirect' );
	return $log;
}

// i due bottoni dell'installatore: si eseguono prima della pagina, poi si torna alla pagina con il resoconto
add_action(
	'admin_init',
	function () {
		if ( empty( $_POST['dfp_passo'] ) || ! current_user_can( 'manage_options' ) ) {
			return;
		}
		check_admin_referer( 'dfp_installa' );
		$passo = sanitize_key( wp_unslash( $_POST['dfp_passo'] ) );
		if ( 'elementor' === $passo ) {
			$log = dfp_installa_elementor();
		} else {
			$email = isset( $_POST['dfp_email'] ) ? sanitize_email( wp_unslash( $_POST['dfp_email'] ) ) : '';
			if ( ! is_email( $email ) ) {
				$email = get_option( 'admin_email' );
			}
			$log = dfp_installa( ! empty( $_POST['dfp_sovrascrivi'] ), $email, ! empty( $_POST['dfp_nascondi'] ), ! empty( $_POST['dfp_elementor'] ) );
			$log[] = '__fatto__';
		}
		set_transient( 'dfp_log_' . get_current_user_id(), $log, 600 );
		wp_safe_redirect( admin_url( 'themes.php?page=dfp-installa' ) );
		exit;
	}
);

/**
 * La pagina dell'installatore.
 */
function dfp_pagina_installa() {
	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}
	$log = get_transient( 'dfp_log_' . get_current_user_id() );
	delete_transient( 'dfp_log_' . get_current_user_id() );
	$log      = is_array( $log ) ? $log : array();
	$completo = in_array( '__fatto__', $log, true );
	$log      = array_diff( $log, array( '__fatto__' ) );
	$el       = dfp_elementor();
	$email = get_option( 'dfp_email_moduli', get_option( 'admin_email' ) );
	$fatto = get_option( 'dfp_installato' );
	?>
	<div class="wrap">
		<h1>Installa Dieffepiu</h1>
		<p>Crea le 13 pagine del sito (home, sistemi con le sei famiglie, macchine, azienda, fiere e novità, contatti, area riservata), le cinque notizie delle fiere e il menu della testata, imposta la home e gli indirizzi.</p>
		<?php if ( $fatto ) : ?>
			<p><strong>Ultima installazione:</strong> <?php echo esc_html( $fatto ); ?>.</p>
		<?php endif; ?>
		<?php if ( $log ) : ?>
			<div class="notice notice-success"><p><strong><?php echo $completo ? 'Fatto.' : 'Elementor:'; ?></strong> <?php if ( $completo ) : ?><a href="<?php echo esc_url( home_url( '/' ) ); ?>">Apri il sito</a><?php endif; ?></p><ul style="list-style:disc;margin-left:20px">
			<?php foreach ( $log as $r ) : ?>
				<li><?php echo esc_html( $r ); ?></li>
			<?php endforeach; ?>
			</ul></div>
		<?php endif; ?>
		<?php if ( ! $el ) : ?>
			<form method="post" style="margin:16px 0 24px;padding:12px 16px;background:#fff;border:1px solid #c3c4c7">
				<?php wp_nonce_field( 'dfp_installa' ); ?>
				<input type="hidden" name="dfp_passo" value="elementor">
				<p><strong>Passo 1: Elementor.</strong> Elementor non è attivo. Con Elementor ogni pagina si apre in "Modifica con Elementor"; senza, le pagine si modificano nell’editor di WordPress. La grafica è la stessa.</p>
				<?php submit_button( 'Installa e attiva Elementor', 'secondary', 'dfp_el', false ); ?>
			</form>
		<?php endif; ?>
		<form method="post">
			<?php wp_nonce_field( 'dfp_installa' ); ?>
			<input type="hidden" name="dfp_passo" value="sito">
			<table class="form-table" role="presentation">
				<tr><th scope="row">Elementor</th>
					<td><label><input name="dfp_elementor" type="checkbox" value="1"<?php checked( $el ); ?><?php disabled( ! $el ); ?>> Costruisci le pagine con Elementor</label>
					<p class="description"><?php echo $el ? 'Ogni sezione diventa un contenitore di Elementor con dentro il suo HTML: la pagina si apre, si riordina e si allarga in Elementor senza cambiare grafica.' : 'Disponibile quando Elementor è attivo (passo 1).'; ?></p></td></tr>
				<tr><th scope="row"><label for="dfp_email">I moduli arrivano a</label></th>
					<td><input name="dfp_email" id="dfp_email" type="email" class="regular-text" value="<?php echo esc_attr( $email ); ?>">
					<p class="description">Sul sito di prova lasciate il vostro indirizzo. Al passaggio online mettete info@dieffepiu.it (o quello che sceglie l’azienda).</p></td></tr>
				<tr><th scope="row">Pagine già presenti</th>
					<td><label><input name="dfp_sovrascrivi" type="checkbox" value="1"<?php checked( ! $fatto ); ?>> Riscrivi il contenuto delle pagine del sito con quello del tema</label>
					<p class="description">Toglietela se avete già modificato i testi nell’editor e volete tenerli.</p></td></tr>
				<tr><th scope="row">Motori di ricerca</th>
					<td><label><input name="dfp_nascondi" type="checkbox" value="1"<?php checked( '0' === get_option( 'blog_public' ) || ! $fatto ); ?>> Nascondi il sito ai motori di ricerca (sito di prova)</label></td></tr>
			</table>
			<?php submit_button( $fatto ? 'Aggiorna il sito' : 'Installa il sito', 'primary', 'dfp_vai' ); ?>
		</form>
	</div>
	<?php
}
