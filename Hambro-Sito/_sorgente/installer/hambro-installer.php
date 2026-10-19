<?php
/**
 * Plugin Name: Hambro: installazione della home
 * Description: Installa e configura la home di Hambro (tema Hello Elementor, Elementor, Ultimate Addons, impostazioni, template Elementor, pagina Home, header e footer, menu). Da disattivare ed eliminare dopo l'uso.
 * Version: 1.0
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

add_action( 'admin_menu', function () {
	add_management_page( 'Installa Hambro', 'Installa Hambro', 'manage_options', 'hbr-installa', 'hbr_pagina' );
} );

function hbr_passi() {
	$passi = [ 'plugin' => 'Plugin e tema', 'attivazione' => 'Prima attivazione dei plugin', 'impostazioni' => 'Impostazioni del sito' ];
	foreach ( glob( __DIR__ . '/template/*.json' ) as $f ) { $passi[ 'import:' . basename( $f ) ] = 'Importa ' . basename( $f ); }
	return $passi + [ 'pagine' => 'Pagina Home', 'hf' => 'Header, footer e menu', 'verifica' => 'Verifica' ];
}

function hbr_pagina() {
	echo '<div class="wrap"><h1>Installa Hambro</h1><p>Apri i passi uno alla volta, nell\'ordine. Ogni passo scrive cosa ha fatto.</p><ol>';
	foreach ( hbr_passi() as $k => $t ) {
		$u = wp_nonce_url( admin_url( 'admin-post.php?action=hbr_passo&passo=' . rawurlencode( $k ) ), 'hbr_passo' );
		echo '<li><a class="hbr-passo" data-passo="' . esc_attr( $k ) . '" href="' . esc_url( $u ) . '">' . esc_html( $t ) . '</a></li>';
	}
	echo '</ol></div>';
}

add_action( 'admin_post_hbr_passo', function () {
	if ( ! current_user_can( 'manage_options' ) ) { wp_die( 'permesso negato' ); }
	check_admin_referer( 'hbr_passo' );
	@set_time_limit( 600 );
	header( 'Content-Type: text/plain; charset=utf-8' );
	$passo = sanitize_text_field( wp_unslash( $_GET['passo'] ?? '' ) );
	try {
		if ( 0 === strpos( $passo, 'import:' ) ) { hbr_import( substr( $passo, 7 ) ); }
		elseif ( in_array( $passo, [ 'plugin', 'attivazione', 'impostazioni', 'pagine', 'hf', 'verifica' ], true ) ) { call_user_func( 'hbr_' . $passo ); }
		else { echo "passo sconosciuto\n"; }
	} catch ( Throwable $e ) {
		echo 'ERRORE: ' . $e->getMessage() . ' (' . basename( $e->getFile() ) . ':' . $e->getLine() . ")\n";
	}
	echo "FINE\n";
	exit;
} );

// Elementor (contenitori), Ultimate Addons (header, footer e menu globali). Contact Form 7 non serve: la home non ha moduli.
function hbr_elenco_plugin() {
	return [ 'elementor' => 'elementor/elementor.php', 'header-footer-elementor' => 'header-footer-elementor/header-footer-elementor.php' ];
}

function hbr_plugin() {
	require_once ABSPATH . 'wp-admin/includes/plugin.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/misc.php';
	require_once ABSPATH . 'wp-admin/includes/plugin-install.php';
	require_once ABSPATH . 'wp-admin/includes/theme.php';
	require_once ABSPATH . 'wp-admin/includes/class-wp-upgrader.php';
	echo 'metodo file system: ' . get_filesystem_method() . "\n";
	if ( ! wp_get_theme( 'hello-elementor' )->exists() ) {
		$api = themes_api( 'theme_information', [ 'slug' => 'hello-elementor', 'fields' => [ 'sections' => false ] ] );
		if ( is_wp_error( $api ) ) { echo 'tema: ' . $api->get_error_message() . "\n"; }
		else { $r = ( new Theme_Upgrader( new Automatic_Upgrader_Skin() ) )->install( $api->download_link ); echo 'tema hello-elementor ' . $api->version . ': ' . ( is_wp_error( $r ) ? $r->get_error_message() : ( $r ? 'installato' : 'non installato' ) ) . "\n"; }
	} else { echo "tema hello-elementor: già installato\n"; }
	if ( wp_get_theme( 'hello-elementor' )->exists() ) { switch_theme( 'hello-elementor' ); echo "tema attivo: hello-elementor\n"; }
	foreach ( hbr_elenco_plugin() as $slug => $file ) {
		if ( ! file_exists( WP_PLUGIN_DIR . '/' . $file ) ) {
			$api = plugins_api( 'plugin_information', [ 'slug' => $slug, 'fields' => [ 'sections' => false ] ] );
			if ( is_wp_error( $api ) ) { echo "$slug: " . $api->get_error_message() . "\n"; continue; }
			$r = ( new Plugin_Upgrader( new Automatic_Upgrader_Skin() ) )->install( $api->download_link );
			echo "$slug {$api->version}: " . ( is_wp_error( $r ) ? $r->get_error_message() : ( $r ? 'installato' : 'non installato' ) ) . "\n";
		} else { echo "$slug: già installato\n"; }
		if ( file_exists( WP_PLUGIN_DIR . '/' . $file ) && ! is_plugin_active( $file ) ) {
			$a = activate_plugin( $file, '', false, true );
			echo "$slug: " . ( is_wp_error( $a ) ? 'attivazione fallita ' . $a->get_error_message() : 'attivato' ) . "\n";
		}
	}
	delete_transient( 'elementor_activation_redirect' );
	foreach ( get_plugins() as $f => $d ) { echo '  ' . $f . ' ' . $d['Version'] . ( is_plugin_active( $f ) ? ' (attivo)' : '' ) . "\n"; }
}

// le attivazioni del passo "plugin" sono silenziose: qui eseguo le routine di prima attivazione
// (Elementor crea il kit con le impostazioni globali e le opzioni predefinite)
function hbr_attivazione() {
	foreach ( hbr_elenco_plugin() as $f ) {
		do_action( 'activate_' . $f, false );
		echo "attivazione eseguita: $f\n";
	}
	delete_transient( 'elementor_activation_redirect' );
	if ( class_exists( '\Elementor\Plugin' ) ) {
		$kit = \Elementor\Plugin::$instance->kits_manager->get_active_id();
		if ( ! $kit ) { \Elementor\Core\Kits\Manager::create_default_kit(); $kit = get_option( 'elementor_active_kit' ); }
		echo 'kit Elementor attivo: ' . $kit . "\n";
	} else { echo "Elementor non attivo: ripeti il passo Plugin e tema\n"; }
}

function hbr_impostazioni() {
	update_option( 'blogname', 'Hambro' );
	update_option( 'blogdescription', 'Fibbie, lacci e rinforzi' );
	update_option( 'blog_public', 0 );                 // sito di prova: i motori di ricerca non lo indicizzano
	update_option( 'timezone_string', 'Europe/Rome' );
	update_option( 'date_format', 'j F Y' );
	update_option( 'default_comment_status', 'closed' );
	update_option( 'permalink_structure', '/%postname%/' );
	// Mona Sans arriva dal link nel widget HTML dell'header: i Google Fonts di Elementor (Roboto e Roboto Slab del kit) non servono
	update_option( 'elementor_google_font', '0' );
	flush_rewrite_rules( true );
	echo "impostazioni: nome, descrizione, non indicizzabile, fuso Europe/Rome, permalink /%postname%/, Google Fonts di Elementor spenti\n";
	require_once ABSPATH . 'wp-admin/includes/translation-install.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	$l = wp_download_language_pack( 'it_IT' );
	if ( $l ) { update_option( 'WPLANG', $l ); echo "lingua: $l\n"; } else { echo "lingua italiana non scaricata (resta l'inglese per l'area admin)\n"; }
	foreach ( [ 'hello-world' => 'post', 'sample-page' => 'page', 'pagina-di-esempio' => 'page', 'ciao-mondo' => 'post' ] as $slug => $tipo ) {
		$p = get_page_by_path( $slug, OBJECT, $tipo );
		if ( $p ) { wp_delete_post( $p->ID, true ); echo "eliminato contenuto di esempio: $slug\n"; }
	}
	if ( defined( 'ELEMENTOR_VERSION' ) ) {
		echo 'Elementor ' . ELEMENTOR_VERSION . ', contenitori: ' . ( \Elementor\Plugin::$instance->experiments->is_feature_active( 'container' ) ? 'attivi' : 'NON attivi' ) . "\n";
	}
	echo 'unfiltered_html: ' . ( current_user_can( 'unfiltered_html' ) ? 'si' : 'NO (gli script dei widget HTML, cioè righello e banco di misura, verrebbero tolti)' ) . "\n";
}

function hbr_conta( $els ) { $n = 0; foreach ( $els as $e ) { $n += 1 + hbr_conta( $e['elements'] ?? [] ); } return $n; }

function hbr_import( $nome ) {
	if ( ! class_exists( '\Elementor\Plugin' ) ) { echo "Elementor non attivo\n"; return; }
	$f = __DIR__ . '/template/' . basename( $nome );
	if ( ! file_exists( $f ) ) { echo "manca $nome\n"; return; }
	$src = json_decode( file_get_contents( $f ), true );
	// se il template esiste già (passo ripetuto) lo sostituisco
	foreach ( get_posts( [ 'post_type' => 'elementor_library', 'numberposts' => -1, 'title' => $src['title'], 'post_status' => 'any' ] ) as $vecchio ) { wp_delete_post( $vecchio->ID, true ); }
	$tmp = wp_tempnam( basename( $f ) ); copy( $f, $tmp );
	$res = \Elementor\Plugin::$instance->templates_manager->get_source( 'local' )->import_template( basename( $f ), $tmp );
	if ( is_wp_error( $res ) ) { echo 'errore: ' . $res->get_error_message() . "\n"; return; }
	$tid = $res[0]['template_id'];
	$salvati = \Elementor\Plugin::$instance->documents->get( $tid )->get_elements_data();
	$json = wp_json_encode( $salvati );
	preg_match_all( '#"url":"([^"]+\.(?:jpe?g|png|webp))"#i', str_replace( '\/', '/', $json ), $m );
	$locali = count( array_filter( $m[1], function ( $u ) { return false !== strpos( $u, '/wp-content/uploads/' ); } ) );
	$segnaposto = count( array_filter( $m[1], function ( $u ) { return false !== strpos( $u, 'placeholder' ); } ) );
	$script = substr_count( $json, '<script' );
	echo "{$src['title']}: template $tid, elementi " . hbr_conta( $salvati ) . ' su ' . hbr_conta( $src['content'] ) . ', immagini ' . count( $m[1] ) . " (nella libreria $locali, segnaposto $segnaposto), script $script\n";
	// Elementor non importa il testo alternativo: lo scrivo nella libreria media (testi di testi-alternativi.txt)
	$alt = hbr_testi_alternativi();
	$fatti = hbr_scrivi_alt( $src['content'], $salvati, $alt );
	if ( $fatti ) { echo 'testo alternativo scritto nella libreria media: ' . implode( ', ', $fatti ) . "\n"; }
}

function hbr_testi_alternativi() {
	$out = [];
	$f = __DIR__ . '/testi-alternativi.txt';
	if ( ! file_exists( $f ) ) { return $out; }
	foreach ( file( $f, FILE_IGNORE_NEW_LINES ) as $riga ) {
		if ( preg_match( '#^([a-z0-9._-]+\.(?:jpe?g|png|webp)): (.+)$#i', $riga, $mm ) ) { $out[ $mm[1] ] = $mm[2]; }
	}
	return $out;
}

// il file importato e il template salvato hanno gli stessi elementi nello stesso ordine: per ogni widget Immagine
// il nome del file d'origine dice quale testo, l'id salvato quale allegato della libreria
function hbr_scrivi_alt( $src, $salvati, $alt ) {
	$fatti = [];
	foreach ( $src as $i => $e ) {
		$s = $salvati[ $i ] ?? null;
		if ( ! $s ) { continue; }
		if ( 'image' === ( $e['widgetType'] ?? '' ) ) {
			$nome = basename( (string) wp_parse_url( $e['settings']['image']['url'] ?? '', PHP_URL_PATH ) );
			$id = (int) ( $s['settings']['image']['id'] ?? 0 );
			if ( $id && isset( $alt[ $nome ] ) ) { update_post_meta( $id, '_wp_attachment_image_alt', $alt[ $nome ] ); $fatti[] = "$nome ($id)"; }
		}
		$fatti = array_merge( $fatti, hbr_scrivi_alt( $e['elements'] ?? [], $s['elements'] ?? [], $alt ) );
	}
	return $fatti;
}

function hbr_ultimi_template() {
	$out = [];
	foreach ( get_posts( [ 'post_type' => 'elementor_library', 'numberposts' => -1, 'orderby' => 'ID', 'order' => 'DESC' ] ) as $p ) {
		if ( 0 === strpos( $p->post_title, 'Hambro' ) && ! isset( $out[ $p->post_title ] ) ) { $out[ $p->post_title ] = $p->ID; }
	}
	return $out;
}

function hbr_pagine() {
	if ( ! class_exists( '\Elementor\Plugin' ) ) { echo "Elementor non attivo\n"; return; }
	foreach ( hbr_ultimi_template() as $titolo => $id ) {
		if ( false !== stripos( $titolo, 'header' ) || false !== stripos( $titolo, 'footer' ) || false !== stripos( $titolo, 'complet' ) ) { continue; }
		$t = trim( str_replace( 'Hambro:', '', $titolo ) );
		$slug = sanitize_title( $t );
		$es = get_page_by_path( $slug );
		$pid = $es ? $es->ID : wp_insert_post( [ 'post_type' => 'page', 'post_status' => 'publish', 'post_title' => $t, 'post_name' => $slug ] );
		$doc = \Elementor\Plugin::$instance->documents->get( $pid );
		$doc->set_is_built_with_elementor( true );
		$doc->save( [ 'elements' => \Elementor\Plugin::$instance->documents->get( $id )->get_elements_data(), 'settings' => [ 'template' => 'elementor_header_footer', 'hide_title' => 'yes' ] ] );
		if ( 'Home' === $t ) { update_option( 'show_on_front', 'page' ); update_option( 'page_on_front', $pid ); }
		echo "pagina $t ($pid) " . get_permalink( $pid ) . "\n";
	}
	\Elementor\Plugin::$instance->files_manager->clear_cache();
}

function hbr_rigenera_id( $els ) { foreach ( $els as &$e ) { $e['id'] = substr( md5( uniqid( '', true ) ), 0, 7 ); $e['elements'] = hbr_rigenera_id( $e['elements'] ?? [] ); } return $els; }

// voci del menu: ancore della home, come nella pagina statica
function hbr_voci_menu() {
	return [
		[ 'Lacci e nastri', '/#lacci', '' ], [ 'Minuteria', '/#minuteria', '' ], [ 'Ricopertura', '/#ricopertura', '' ],
		[ 'Misure per settore', '/#misure', '' ], [ 'Contatti', '/#contatti', '' ],
	];
}

function hbr_hf() {
	if ( ! class_exists( '\Elementor\Plugin' ) ) { echo "Elementor non attivo\n"; return; }
	if ( ! post_type_exists( 'elementor-hf' ) ) { echo "Ultimate Addons non attivo: ripeti il passo Plugin e tema\n"; }
	$tpl = hbr_ultimi_template();
	foreach ( [ 'Hambro: Header' => 'type_header', 'Hambro: Footer' => 'type_footer' ] as $titolo => $tipo ) {
		if ( empty( $tpl[ $titolo ] ) ) { echo "manca $titolo\n"; continue; }
		$nome = 'type_header' === $tipo ? 'Header Hambro' : 'Footer Hambro';
		$es = get_posts( [ 'post_type' => 'elementor-hf', 'title' => $nome, 'numberposts' => 1, 'post_status' => 'any' ] );
		$pid = $es ? $es[0]->ID : wp_insert_post( [ 'post_type' => 'elementor-hf', 'post_status' => 'publish', 'post_title' => $nome ] );
		update_post_meta( $pid, 'ehf_template_type', $tipo );
		update_post_meta( $pid, 'ehf_target_include_locations', [ 'rule' => [ 'basic-global' ], 'specific' => [] ] );
		update_post_meta( $pid, 'ehf_target_exclude_locations', [] );
		update_post_meta( $pid, 'ehf_target_user_roles', [] );
		$doc = \Elementor\Plugin::$instance->documents->get( $pid );
		$doc->set_is_built_with_elementor( true );
		$doc->save( [ 'elements' => hbr_rigenera_id( \Elementor\Plugin::$instance->documents->get( $tpl[ $titolo ] )->get_elements_data() ) ] );
		echo "$tipo -> $pid\n";
	}
	$menu = wp_get_nav_menu_object( 'menu-hambro' );
	$mid = $menu ? $menu->term_id : wp_create_nav_menu( 'Menu Hambro' );
	foreach ( wp_get_nav_menu_items( $mid ) ?: [] as $it ) { wp_delete_post( $it->ID, true ); }
	foreach ( hbr_voci_menu() as $i => $v ) {
		wp_update_nav_menu_item( $mid, 0, [ 'menu-item-title' => $v[0], 'menu-item-url' => $v[1], 'menu-item-type' => 'custom',
			'menu-item-status' => 'publish', 'menu-item-classes' => $v[2], 'menu-item-position' => $i + 1 ] );
	}
	echo 'menu ' . wp_get_nav_menu_object( $mid )->slug . ': ' . count( wp_get_nav_menu_items( $mid ) ) . " voci\n";
	\Elementor\Plugin::$instance->files_manager->clear_cache();
}

function hbr_verifica() {
	$pg = get_post( get_option( 'page_on_front' ) );
	echo 'home: ' . ( $pg ? get_permalink( $pg ) . ' (' . get_post_meta( $pg->ID, '_wp_page_template', true ) . ')' : 'MANCA' ) . "\n";
	echo 'tema: ' . get_stylesheet() . ', indicizzabile: ' . ( get_option( 'blog_public' ) ? 'si' : 'no' ) . ', permalink: ' . get_option( 'permalink_structure' ) . "\n";
	foreach ( [ 'type_header', 'type_footer' ] as $t ) {
		$q = get_posts( [ 'post_type' => 'elementor-hf', 'numberposts' => 1, 'meta_key' => 'ehf_template_type', 'meta_value' => $t ] );
		echo "$t: " . ( $q ? $q[0]->post_title . ' (' . $q[0]->ID . ')' : 'MANCA' ) . "\n";
	}
	$m = wp_get_nav_menu_object( 'menu-hambro' );
	echo 'menu: ' . ( $m ? count( wp_get_nav_menu_items( $m->term_id ) ) . ' voci' : 'MANCA' ) . "\n";
	$ids = get_posts( [ 'post_type' => 'attachment', 'numberposts' => -1, 'fields' => 'ids' ] );
	$con_alt = count( array_filter( $ids, function ( $id ) { return '' !== (string) get_post_meta( $id, '_wp_attachment_image_alt', true ); } ) );
	echo 'immagini nella libreria media: ' . count( $ids ) . ", con testo alternativo: $con_alt\n";
}
