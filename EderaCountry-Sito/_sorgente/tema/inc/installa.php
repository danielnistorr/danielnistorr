<?php
/**
 * Installatore: Aspetto > Installa Edera (oppure, con WP-CLI: wp eval 'edera_installa();').
 *
 * In un colpo:
 * - carica nella libreria media le foto del sito (con le loro misure gia' pronte) e il PDF dei servizi aggiuntivi;
 * - crea le pagine Home, Informativa privacy (/privacy/) e Cookie (/cookie/) come pagine di Elementor,
 *   fatte di contenitori e widget normali (contenuti/*.json, generati da _sorgente/build.py);
 * - imposta la Home come pagina iniziale, gli indirizzi belli (/%postname%/) e le opzioni di Elementor
 *   che cambierebbero l'aspetto (colori e caratteri globali, Google Fonts).
 *
 * Si puo' rilanciare quando si vuole: trova pagine e immagini gia' create e non fa doppioni.
 * Una pagina modificata nell'editor resta com'e', a meno di chiedere "riscrivi".
 *
 * @package edera
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action(
	'admin_menu',
	function () {
		add_theme_page( 'Installa Edera', 'Installa Edera', 'manage_options', 'edera-installa', 'edera_pagina_installa' );
	}
);

add_action(
	'admin_notices',
	function () {
		if ( get_option( 'edera_installato' ) || ! current_user_can( 'manage_options' ) ) {
			return;
		}
		$s = get_current_screen();
		if ( $s && 'appearance_page_edera-installa' === $s->id ) {
			return;
		}
		echo '<div class="notice notice-info"><p><strong>Tema Edera attivo.</strong> Per creare le pagine e caricare foto e PDF: <a href="' . esc_url( admin_url( 'themes.php?page=edera-installa' ) ) . '">Aspetto &gt; Installa Edera</a>.</p></div>';
	}
);

/**
 * Legge un file JSON di contenuti/.
 *
 * @param string $nome Nome del file.
 * @return array
 */
function edera_leggi( $nome ) {
	$f = get_template_directory() . '/contenuti/' . $nome;
	if ( ! file_exists( $f ) ) {
		return array();
	}
	$d = json_decode( file_get_contents( $f ), true ); // phpcs:ignore WordPress.WP.AlternativeFunctions.file_get_contents_file_get_contents
	return is_array( $d ) ? $d : array();
}

/**
 * Elementor e' caricato?
 *
 * @return bool
 */
function edera_elementor() {
	return did_action( 'elementor/loaded' ) && class_exists( '\Elementor\Plugin' ) && isset( \Elementor\Plugin::$instance->documents );
}

/**
 * L'allegato creato dall'installatore con questa chiave (campo _edera_chiave).
 *
 * @param string $chiave Chiave.
 * @return int
 */
function edera_trova_media( $chiave ) {
	$q = get_posts(
		array(
			'post_type'      => 'attachment',
			'post_status'    => 'any',
			'posts_per_page' => 1,
			'fields'         => 'ids',
			'meta_key'       => '_edera_chiave', // phpcs:ignore WordPress.DB.SlowDBQuery
			'meta_value'     => $chiave, // phpcs:ignore WordPress.DB.SlowDBQuery
		)
	);
	return $q ? (int) $q[0] : 0;
}

/**
 * Copia un file del tema nella cartella uploads/edera/ (se non c'e' gia').
 *
 * @param string $da  File del tema.
 * @param string $dir Cartella di arrivo.
 * @return bool
 */
function edera_copia( $da, $dir ) {
	$a = trailingslashit( $dir ) . basename( $da );
	if ( file_exists( $a ) && filesize( $a ) === filesize( $da ) ) {
		return true;
	}
	return copy( $da, $a );
}

/**
 * Foto e PDF nella libreria media. Ogni foto e' un allegato con le sue misure gia' pronte (le stesse
 * dell'originale), cosi' WordPress scrive lo stesso srcset senza ricalcolare nulla.
 *
 * @param array $log Resoconto.
 * @return array chiave => ID allegato.
 */
function edera_media( &$log ) {
	require_once ABSPATH . 'wp-admin/includes/image.php';
	$m   = edera_leggi( 'media.json' );
	$up  = wp_upload_dir();
	$dir = trailingslashit( $up['basedir'] ) . 'edera';
	$ids = array();
	if ( ! wp_mkdir_p( $dir ) ) {
		$log[] = 'ERRORE: non riesco a creare la cartella ' . $dir . ' (permessi di wp-content/uploads).';
		return $ids;
	}
	$sorg  = get_template_directory() . '/assets/';
	$nuove = 0;
	foreach ( (array) ( isset( $m['immagini'] ) ? $m['immagini'] : array() ) as $im ) {
		$file = array_merge( array( $im['file'] ), $im['varianti'] );
		foreach ( $file as $f ) {
			if ( ! edera_copia( $sorg . 'img/' . $f, $dir ) ) {
				$log[] = 'ERRORE: non riesco a copiare ' . $f . ' in ' . $dir . '.';
				continue 2;
			}
		}
		$percorso = $dir . '/' . $im['file'];
		$id       = edera_trova_media( $im['chiave'] );
		if ( ! $id ) {
			$id = wp_insert_attachment(
				array(
					'post_mime_type' => 'image/webp',
					'post_title'     => $im['titolo'],
					'post_status'    => 'inherit',
					'guid'           => trailingslashit( $up['baseurl'] ) . 'edera/' . $im['file'],
				),
				$percorso,
				0,
				true
			);
			if ( is_wp_error( $id ) ) {
				$log[] = 'ERRORE sulla foto ' . $im['file'] . ': ' . $id->get_error_message();
				continue;
			}
			update_post_meta( $id, '_edera_chiave', $im['chiave'] );
			++$nuove;
		}
		update_attached_file( $id, $percorso );
		$dim   = wp_getimagesize( $percorso );
		$sizes = array();
		foreach ( $im['varianti'] as $f ) {
			$d = wp_getimagesize( $dir . '/' . $f );
			if ( $d ) {
				$sizes[ 'edera-' . $d[0] ] = array(
					'file'      => $f,
					'width'     => (int) $d[0],
					'height'    => (int) $d[1],
					'mime-type' => 'image/webp',
					'filesize'  => (int) filesize( $dir . '/' . $f ),
				);
			}
		}
		wp_update_attachment_metadata(
			$id,
			array(
				'width'      => (int) $dim[0],
				'height'     => (int) $dim[1],
				'file'       => 'edera/' . $im['file'],
				'filesize'   => (int) filesize( $percorso ),
				'sizes'      => $sizes,
				'image_meta' => array(),
			)
		);
		update_post_meta( $id, '_wp_attachment_image_alt', $im['alt'] );
		if ( ! empty( $im['sizes'] ) ) {
			update_post_meta( $id, '_edera_sizes', $im['sizes'] );
		} else {
			delete_post_meta( $id, '_edera_sizes' );
		}
		$ids[ $im['chiave'] ] = $id;
	}
	foreach ( (array) ( isset( $m['immagini'] ) ? $m['immagini'] : array() ) as $im ) {
		if ( ! empty( $im['tel'] ) && isset( $ids[ $im['chiave'] ], $ids[ $im['tel'] ] ) ) {
			update_post_meta( $ids[ $im['chiave'] ], '_edera_tel', $ids[ $im['tel'] ] );
		}
	}
	$log[] = 'Foto nella libreria media: ' . count( $ids ) . ( $nuove ? ' (' . $nuove . ' nuove)' : ' (già presenti)' ) . '.';

	foreach ( (array) ( isset( $m['documenti'] ) ? $m['documenti'] : array() ) as $doc ) {
		if ( ! edera_copia( $sorg . 'doc/' . $doc['file'], $dir ) ) {
			$log[] = 'ERRORE: non riesco a copiare ' . $doc['file'] . '.';
			continue;
		}
		$percorso = $dir . '/' . $doc['file'];
		$id       = edera_trova_media( $doc['chiave'] );
		if ( ! $id ) {
			$id = wp_insert_attachment(
				array(
					'post_mime_type' => 'application/pdf',
					'post_title'     => $doc['titolo'],
					'post_status'    => 'inherit',
					'guid'           => trailingslashit( $up['baseurl'] ) . 'edera/' . $doc['file'],
				),
				$percorso,
				0,
				true
			);
			if ( is_wp_error( $id ) ) {
				$log[] = 'ERRORE sul PDF: ' . $id->get_error_message();
				continue;
			}
			update_post_meta( $id, '_edera_chiave', $doc['chiave'] );
			$log[] = 'PDF caricato nella libreria media: ' . $doc['file'] . '.';
		} else {
			$log[] = 'PDF già nella libreria media: ' . $doc['file'] . '.';
		}
		update_attached_file( $id, $percorso );
		wp_update_attachment_metadata( $id, array( 'filesize' => (int) filesize( $percorso ) ) );
		$ids[ $doc['chiave'] ] = $id;
	}
	return $ids;
}

/**
 * Sostituisce i segnaposto nei contenuti: le foto ({"edera_img": "chiave"}), {{casa}}, {{pagina:...}}, {{media:...}}.
 *
 * @param mixed $x     Dati di Elementor.
 * @param array $media chiave => ID.
 * @param array $pag   chiave => ID pagina.
 * @return mixed
 */
function edera_segnaposti( $x, $media, $pag ) {
	if ( is_array( $x ) ) {
		if ( isset( $x['edera_img'] ) ) {
			$id = isset( $media[ $x['edera_img'] ] ) ? (int) $media[ $x['edera_img'] ] : 0;
			return array(
				'url'    => $id ? wp_get_attachment_url( $id ) : '',
				'id'     => $id,
				'alt'    => '',
				'source' => 'library',
				'size'   => '',
			);
		}
		foreach ( $x as $k => $v ) {
			$x[ $k ] = edera_segnaposti( $v, $media, $pag );
		}
		return $x;
	}
	if ( is_string( $x ) && false !== strpos( $x, '{{' ) ) {
		$x = str_replace( '{{casa}}', home_url( '/' ), $x );
		$x = preg_replace_callback(
			'/\{\{pagina:([a-z0-9-]+)\}\}/',
			function ( $m ) use ( $pag ) {
				return isset( $pag[ $m[1] ] ) ? get_permalink( $pag[ $m[1] ] ) : home_url( '/' . $m[1] . '/' );
			},
			$x
		);
		$x = preg_replace_callback(
			'/\{\{media:([a-z0-9-]+)\}\}/',
			function ( $m ) use ( $media ) {
				return isset( $media[ $m[1] ] ) ? (string) $media[ $m[1] ] : '';
			},
			$x
		);
	}
	return $x;
}

/**
 * Impronta dei dati di Elementor di una pagina: dice se qualcuno l'ha modificata dopo l'installazione.
 *
 * @param int $id Pagina.
 * @return string
 */
function edera_impronta( $id ) {
	$d = get_post_meta( $id, '_elementor_data', true );
	return md5( is_string( $d ) ? $d : wp_json_encode( $d ) );
}

/**
 * Salva una pagina come documento di Elementor.
 *
 * @param int    $id       Pagina.
 * @param array  $elementi Contenitori e widget.
 * @param string $modello  Modello di pagina ('' = predefinito).
 * @return bool
 */
function edera_salva_elementor( $id, $elementi, $modello ) {
	$doc = \Elementor\Plugin::$instance->documents->get( $id, false );
	if ( ! $doc ) {
		return false;
	}
	$doc->set_is_built_with_elementor( true );
	$ok = $doc->save(
		array(
			'elements' => $elementi,
			'settings' => array(
				'hide_title' => 'yes',
				'template'   => $modello ? $modello : 'default',
			),
		)
	);
	update_post_meta( $id, '_wp_page_template', $modello ? $modello : 'default' );
	update_post_meta( $id, '_edera_impronta', edera_impronta( $id ) );
	return (bool) $ok;
}

/**
 * Esegue l'installazione.
 *
 * @param array $opz riscrivi (bool): riscrive anche le pagine modificate nell'editor;
 *                   nascondi (bool|null): sito nascosto ai motori di ricerca (null = non toccare).
 * @return array Righe di resoconto.
 */
function edera_installa( $opz = array() ) {
	$opz = wp_parse_args(
		$opz,
		array(
			'riscrivi' => false,
			'nascondi' => null,
		)
	);
	$log = array();
	if ( ! edera_elementor() ) {
		return array( 'ERRORE: Elementor non è attivo. Installalo e attivalo (Plugin > Aggiungi nuovo > Elementor), poi rilancia.' );
	}
	if ( ! \Elementor\Plugin::$instance->kits_manager->get_active_id() ) {
		\Elementor\Core\Kits\Manager::create_default_kit();
	}

	$media = edera_media( $log );
	update_option( 'edera_pdf_servizi', isset( $media['servizi-aggiuntivi'] ) ? (int) $media['servizi-aggiuntivi'] : '' );

	// le pagine: prima tutte (servono gli indirizzi per i link), poi il contenuto
	$pagine = edera_leggi( 'pagine.json' );
	$ids    = array();
	foreach ( $pagine as $p ) {
		$esiste = get_page_by_path( $p['slug'], OBJECT, 'page' );
		$dati   = array(
			'post_type'      => 'page',
			'post_status'    => 'publish',
			'post_title'     => $p['titolo'],
			'post_name'      => $p['slug'],
			'menu_order'     => (int) $p['ordine'],
			'comment_status' => 'closed',
			'ping_status'    => 'closed',
		);
		if ( $esiste ) {
			$dati['ID'] = $esiste->ID;
			$id         = wp_update_post( $dati, true );
		} else {
			$id = wp_insert_post( $dati, true );
		}
		if ( is_wp_error( $id ) ) {
			$log[] = 'ERRORE sulla pagina ' . $p['titolo'] . ': ' . $id->get_error_message();
			continue;
		}
		$ids[ $p['chiave'] ] = array( (int) $id, (bool) $esiste );
	}
	$pag = array();
	foreach ( $ids as $k => $v ) {
		$pag[ $k ] = $v[0];
	}
	kses_remove_filters();
	foreach ( $pagine as $p ) {
		if ( ! isset( $ids[ $p['chiave'] ] ) ) {
			continue;
		}
		list( $id, $esisteva ) = $ids[ $p['chiave'] ];
		$intatta  = get_post_meta( $id, '_edera_impronta', true ) === edera_impronta( $id );
		$nome     = $p['titolo'] . ' (/' . ( 'home' === $p['chiave'] ? '' : $p['slug'] . '/' ) . ')';
		if ( $esisteva && ! $opz['riscrivi'] && ! $intatta ) {
			$log[] = 'Pagina modificata nell’editor, lasciata com’era: ' . $nome . '.';
		} else {
			$el    = edera_segnaposti( edera_leggi( $p['file'] ), $media, $pag );
			$fatto = edera_salva_elementor( $id, $el, $p['modello'] );
			$log[] = ( $fatto ? ( $esisteva ? 'Pagina aggiornata in Elementor: ' : 'Pagina creata in Elementor: ' ) : 'ERRORE: Elementor non ha salvato ' ) . $nome . '.';
		}
		update_post_meta( $id, '_edera_chiave', $p['chiave'] );
		update_post_meta( $id, '_edera_titolo', $p['titolo_seo'] );
		update_post_meta( $id, '_edera_descrizione', $p['descrizione'] );
		if ( ! empty( $p['noindex'] ) ) {
			update_post_meta( $id, '_edera_noindex', 1 );
		} else {
			delete_post_meta( $id, '_edera_noindex' );
		}
	}
	kses_init_filters();

	// Elementor: niente colori, caratteri e Google Fonts globali che cambierebbero l'aspetto
	update_option( 'elementor_disable_color_schemes', 'yes' );
	update_option( 'elementor_disable_typography_schemes', 'yes' );
	update_option( 'elementor_google_font', '0' );
	update_option( 'elementor_onboarded', true );
	delete_transient( 'elementor_activation_redirect' );
	\Elementor\Plugin::$instance->files_manager->clear_cache();
	$log[] = 'Elementor: colori e caratteri globali e Google Fonts spenti (caratteri e colori li dà il tema).';

	// home, indirizzi, impostazioni
	if ( isset( $pag['privacy'] ) ) {
		update_option( 'wp_page_for_privacy_policy', $pag['privacy'] );
	}
	if ( isset( $pag['home'] ) ) {
		update_option( 'show_on_front', 'page' );
		update_option( 'page_on_front', $pag['home'] );
		$log[] = 'La pagina "Home" è la pagina iniziale del sito.';
	}
	update_option( 'permalink_structure', '/%postname%/' );
	flush_rewrite_rules();
	$log[] = 'Indirizzi belli: /privacy/ e /cookie/.';
	foreach ( array( 'hello-world', 'ciao-mondo' ) as $s ) {
		$x = get_page_by_path( $s, OBJECT, 'post' );
		if ( $x && 'trash' !== $x->post_status ) {
			wp_trash_post( $x->ID );
			$log[] = 'Spostato nel cestino l’articolo di esempio di WordPress.';
		}
	}
	foreach ( array( 'sample-page', 'pagina-di-esempio' ) as $s ) {
		$x = get_page_by_path( $s, OBJECT, 'page' );
		if ( $x && 'trash' !== $x->post_status ) {
			wp_trash_post( $x->ID );
			$log[] = 'Spostata nel cestino la pagina di esempio di WordPress.';
		}
	}
	if ( in_array( get_option( 'blogname' ), array( '', 'Il mio sito', 'Il mio blog', 'My WordPress Website', 'My Blog' ), true ) ) {
		update_option( 'blogname', 'Edera Country House' );
	}
	update_option( 'blogdescription', 'Eventi aziendali ad Albettone, Vicenza' );
	update_option( 'timezone_string', 'Europe/Rome' );
	update_option( 'date_format', 'j F Y' );
	update_option( 'default_comment_status', 'closed' );
	update_option( 'default_ping_status', 'closed' );
	if ( 'it_IT' !== get_locale() ) {
		require_once ABSPATH . 'wp-admin/includes/translation-install.php';
		if ( wp_can_install_language_pack() && wp_download_language_pack( 'it_IT' ) ) {
			update_option( 'WPLANG', 'it_IT' );
			$log[] = 'Lingua del pannello: italiano.';
		}
	}
	if ( null !== $opz['nascondi'] ) {
		update_option( 'blog_public', $opz['nascondi'] ? '0' : '1' );
		$log[] = $opz['nascondi'] ? 'Sito nascosto ai motori di ricerca (sito di prova).' : 'Sito visibile ai motori di ricerca.';
	}
	update_option( 'edera_installato', EDERA_VERSIONE . ' ' . wp_date( 'Y-m-d H:i' ) );
	return $log;
}

/**
 * Scarica, installa e attiva Elementor dal catalogo di WordPress.org.
 *
 * @return array
 */
function edera_installa_elementor() {
	require_once ABSPATH . 'wp-admin/includes/plugin.php';
	require_once ABSPATH . 'wp-admin/includes/plugin-install.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/misc.php';
	require_once ABSPATH . 'wp-admin/includes/class-wp-upgrader.php';
	$log  = array();
	$file = 'elementor/elementor.php';
	if ( ! file_exists( WP_PLUGIN_DIR . '/' . $file ) ) {
		$api = plugins_api(
			'plugin_information',
			array(
				'slug'   => 'elementor',
				'fields' => array( 'sections' => false ),
			)
		);
		if ( is_wp_error( $api ) ) {
			return array( 'Elementor non scaricato: ' . $api->get_error_message() . ' Installalo da Plugin > Aggiungi nuovo.' );
		}
		$r     = ( new Plugin_Upgrader( new Automatic_Upgrader_Skin() ) )->install( $api->download_link );
		$log[] = ( $r && ! is_wp_error( $r ) ) ? 'Elementor ' . $api->version . ' installato.' : 'Elementor non installato: il server non lo permette da qui. Installalo da Plugin > Aggiungi nuovo, poi torna qui.';
	}
	if ( file_exists( WP_PLUGIN_DIR . '/' . $file ) && ! is_plugin_active( $file ) ) {
		$a     = activate_plugin( $file );
		$log[] = is_wp_error( $a ) ? 'Elementor non attivato: ' . $a->get_error_message() : 'Elementor attivo.';
	}
	delete_transient( 'elementor_activation_redirect' );
	return $log;
}

// i bottoni della pagina: si eseguono prima della pagina, poi si torna con il resoconto
add_action(
	'admin_init',
	function () {
		if ( empty( $_POST['edera_passo'] ) || ! current_user_can( 'manage_options' ) ) {
			return;
		}
		check_admin_referer( 'edera_installa' );
		$passo = sanitize_key( wp_unslash( $_POST['edera_passo'] ) );
		if ( 'elementor' === $passo ) {
			$log = edera_installa_elementor();
		} else {
			$log   = edera_installa(
				array(
					'riscrivi' => ! empty( $_POST['edera_riscrivi'] ),
					'nascondi' => ! empty( $_POST['edera_nascondi'] ),
				)
			);
			$log[] = '__fatto__';
		}
		set_transient( 'edera_log_' . get_current_user_id(), $log, 600 );
		wp_safe_redirect( admin_url( 'themes.php?page=edera-installa' ) );
		exit;
	}
);

/**
 * La pagina Aspetto > Installa Edera.
 */
function edera_pagina_installa() {
	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}
	$log = get_transient( 'edera_log_' . get_current_user_id() );
	delete_transient( 'edera_log_' . get_current_user_id() );
	$log      = is_array( $log ) ? $log : array();
	$completo = in_array( '__fatto__', $log, true );
	$log      = array_diff( $log, array( '__fatto__' ) );
	$el       = edera_elementor();
	$fatto    = get_option( 'edera_installato' );
	?>
	<div class="wrap">
		<h1>Installa Edera</h1>
		<p>Carica foto e PDF nella libreria media, crea le pagine Home, Informativa privacy e Cookie in Elementor e imposta la Home come pagina iniziale.</p>
		<?php if ( $fatto ) : ?>
			<p><strong>Ultima installazione:</strong> <?php echo esc_html( $fatto ); ?>.</p>
		<?php endif; ?>
		<?php if ( $log ) : ?>
			<div class="notice notice-success"><p><strong><?php echo $completo ? 'Fatto.' : 'Elementor:'; ?></strong>
			<?php if ( $completo ) : ?>
				<a href="<?php echo esc_url( home_url( '/' ) ); ?>">Apri il sito</a>
			<?php endif; ?></p>
			<ul style="list-style:disc;margin-left:20px">
			<?php foreach ( $log as $r ) : ?>
				<li><?php echo esc_html( $r ); ?></li>
			<?php endforeach; ?>
			</ul></div>
		<?php endif; ?>
		<?php if ( ! $el ) : ?>
			<form method="post" style="margin:16px 0 24px;padding:12px 16px;background:#fff;border:1px solid #c3c4c7">
				<?php wp_nonce_field( 'edera_installa' ); ?>
				<input type="hidden" name="edera_passo" value="elementor">
				<p><strong>Passo 1: Elementor.</strong> Elementor non è attivo: le pagine del sito sono fatte con Elementor (la versione gratuita basta).</p>
				<?php submit_button( 'Installa e attiva Elementor', 'secondary', 'edera_el', false ); ?>
			</form>
		<?php endif; ?>
		<form method="post">
			<?php wp_nonce_field( 'edera_installa' ); ?>
			<input type="hidden" name="edera_passo" value="sito">
			<table class="form-table" role="presentation">
				<tr><th scope="row">Pagine già modificate</th>
					<td><label><input name="edera_riscrivi" type="checkbox" value="1"> Riscrivi anche le pagine cambiate nell’editor</label>
					<p class="description">Senza la spunta, una pagina che hai già modificato in Elementor resta com’è.</p></td></tr>
				<tr><th scope="row">Motori di ricerca</th>
					<td><label><input name="edera_nascondi" type="checkbox" value="1"<?php checked( '0' === get_option( 'blog_public' ) || ! $fatto ); ?>> Nascondi il sito ai motori di ricerca (sito di prova)</label></td></tr>
			</table>
			<?php submit_button( $fatto ? 'Aggiorna il sito' : 'Installa il sito', 'primary', 'edera_vai', true, $el ? array() : array( 'disabled' => 'disabled' ) ); ?>
		</form>
	</div>
	<?php
}
