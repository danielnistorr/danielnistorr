<?php
/**
 * Plugin Name: Benvegnù: installazione del sito
 * Description: Installa e configura il sito Benvegnù (plugin, impostazioni, template Elementor, pagine, header e footer, menu, modulo). Da disattivare ed eliminare dopo l'uso.
 * Version: 1.0
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

add_action( 'admin_menu', function () {
	add_management_page( 'Installa Benvegnù', 'Installa Benvegnù', 'manage_options', 'bvg-installa', 'bvg_pagina' );
} );

function bvg_passi() {
	$passi = [ 'plugin' => 'Plugin e tema', 'attivazione' => 'Prima attivazione dei plugin', 'impostazioni' => 'Impostazioni del sito' ];
	foreach ( glob( __DIR__ . '/template/*.json' ) as $f ) { $passi[ 'import:' . basename( $f ) ] = 'Importa ' . basename( $f ); }
	return $passi + [ 'pagine' => 'Pagine', 'hf' => 'Header, footer e menu', 'cf7' => 'Modulo Contact Form 7', 'novita' => 'Articoli di esempio per Novità', 'verifica' => 'Verifica' ];
}

function bvg_pagina() {
	echo '<div class="wrap"><h1>Installa Benvegnù</h1><ol>';
	foreach ( bvg_passi() as $k => $t ) {
		$u = wp_nonce_url( admin_url( 'admin-post.php?action=bvg_passo&passo=' . rawurlencode( $k ) ), 'bvg_passo' );
		echo '<li><a class="bvg-passo" data-passo="' . esc_attr( $k ) . '" href="' . esc_url( $u ) . '">' . esc_html( $t ) . '</a></li>';
	}
	echo '</ol></div>';
}

add_action( 'admin_post_bvg_passo', function () {
	if ( ! current_user_can( 'manage_options' ) ) { wp_die( 'permesso negato' ); }
	check_admin_referer( 'bvg_passo' );
	@set_time_limit( 600 );
	header( 'Content-Type: text/plain; charset=utf-8' );
	$passo = sanitize_text_field( wp_unslash( $_GET['passo'] ?? '' ) );
	try {
		if ( 0 === strpos( $passo, 'import:' ) ) { bvg_import( substr( $passo, 7 ) ); }
		elseif ( function_exists( 'bvg_' . $passo ) ) { call_user_func( 'bvg_' . $passo ); }
		else { echo "passo sconosciuto\n"; }
	} catch ( Throwable $e ) {
		echo 'ERRORE: ' . $e->getMessage() . ' (' . basename( $e->getFile() ) . ':' . $e->getLine() . ")\n";
	}
	echo "FINE\n";
	exit;
} );

function bvg_plugin() {
	require_once ABSPATH . 'wp-admin/includes/plugin.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/misc.php';
	require_once ABSPATH . 'wp-admin/includes/plugin-install.php';
	require_once ABSPATH . 'wp-admin/includes/theme.php';
	require_once ABSPATH . 'wp-admin/includes/class-wp-upgrader.php';
	echo 'metodo file system: ' . get_filesystem_method() . "\n";
	// tema Hello Elementor
	if ( ! wp_get_theme( 'hello-elementor' )->exists() ) {
		$api = themes_api( 'theme_information', [ 'slug' => 'hello-elementor', 'fields' => [ 'sections' => false ] ] );
		if ( is_wp_error( $api ) ) { echo 'tema: ' . $api->get_error_message() . "\n"; }
		else { $r = ( new Theme_Upgrader( new Automatic_Upgrader_Skin() ) )->install( $api->download_link ); echo 'tema hello-elementor ' . $api->version . ': ' . ( is_wp_error( $r ) ? $r->get_error_message() : ( $r ? 'installato' : 'non installato' ) ) . "\n"; }
	}
	if ( wp_get_theme( 'hello-elementor' )->exists() ) { switch_theme( 'hello-elementor' ); echo "tema attivo: hello-elementor\n"; }
	$plugin = [ 'elementor' => 'elementor/elementor.php', 'header-footer-elementor' => 'header-footer-elementor/header-footer-elementor.php', 'contact-form-7' => 'contact-form-7/wp-contact-form-7.php' ];
	foreach ( $plugin as $slug => $file ) {
		if ( ! file_exists( WP_PLUGIN_DIR . '/' . $file ) ) {
			$api = plugins_api( 'plugin_information', [ 'slug' => $slug, 'fields' => [ 'sections' => false ] ] );
			if ( is_wp_error( $api ) ) { echo "$slug: " . $api->get_error_message() . "\n"; continue; }
			$r = ( new Plugin_Upgrader( new Automatic_Upgrader_Skin() ) )->install( $api->download_link );
			echo "$slug {$api->version}: " . ( is_wp_error( $r ) ? $r->get_error_message() : ( $r ? 'installato' : 'non installato' ) ) . "\n";
		}
		if ( file_exists( WP_PLUGIN_DIR . '/' . $file ) && ! is_plugin_active( $file ) ) {
			$a = activate_plugin( $file, '', false, true );
			echo "$slug: " . ( is_wp_error( $a ) ? 'attivazione fallita ' . $a->get_error_message() : 'attivo' ) . "\n";
		}
	}
	delete_transient( 'elementor_activation_redirect' );
	foreach ( get_plugins() as $f => $d ) { echo '  ' . $f . ' ' . $d['Version'] . ( is_plugin_active( $f ) ? ' (attivo)' : '' ) . "\n"; }
}

// le attivazioni del passo "plugin" sono silenziose: qui eseguo le routine di prima attivazione
// (Elementor crea il kit con le impostazioni globali e le opzioni predefinite)
function bvg_attivazione() {
	foreach ( [ 'elementor/elementor.php', 'header-footer-elementor/header-footer-elementor.php', 'contact-form-7/wp-contact-form-7.php' ] as $f ) {
		do_action( 'activate_' . $f, false );
		echo "attivazione eseguita: $f\n";
	}
	delete_transient( 'elementor_activation_redirect' );
	if ( class_exists( '\Elementor\Plugin' ) ) {
		$kit = \Elementor\Plugin::$instance->kits_manager->get_active_id();
		if ( ! $kit ) { \Elementor\Core\Kits\Manager::create_default_kit(); $kit = get_option( 'elementor_active_kit' ); }
		echo 'kit Elementor attivo: ' . $kit . "\n";
	}
}

function bvg_impostazioni() {
	update_option( 'blogname', 'Benvegnù S.r.l.' );
	update_option( 'blogdescription', 'Forniture per calzaturifici, pelletterie e calzolai a Vigonovo' );
	update_option( 'blog_public', 0 );                 // sito di prova: i motori di ricerca non lo indicizzano
	update_option( 'timezone_string', 'Europe/Rome' );
	update_option( 'date_format', 'j F Y' );
	update_option( 'default_comment_status', 'closed' );
	update_option( 'permalink_structure', '/%postname%/' );
	flush_rewrite_rules( true );
	echo "impostazioni: nome, descrizione, non indicizzabile, fuso Europe/Rome, permalink /%postname%/\n";
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
	echo 'unfiltered_html: ' . ( current_user_can( 'unfiltered_html' ) ? 'si' : 'NO (gli script nei widget HTML verrebbero tolti)' ) . "\n";
}

function bvg_conta( $els ) { $n = 0; foreach ( $els as $e ) { $n += 1 + bvg_conta( $e['elements'] ?? [] ); } return $n; }

function bvg_import( $nome ) {
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
	preg_match_all( '#"url":"([^"]+\.(?:jpe?g|png))"#i', str_replace( '\/', '/', $json ), $m );
	$locali = count( array_filter( $m[1], function ( $u ) { return false !== strpos( $u, '/wp-content/uploads/' ); } ) );
	$segnaposto = count( array_filter( $m[1], function ( $u ) { return false !== strpos( $u, 'placeholder' ); } ) );
	echo "{$src['title']}: template $tid, elementi " . bvg_conta( $salvati ) . ' su ' . bvg_conta( $src['content'] ) . ', immagini ' . count( $m[1] ) . " (locali $locali, segnaposto $segnaposto)\n";
}

function bvg_ultimi_template() {
	$out = [];
	foreach ( get_posts( [ 'post_type' => 'elementor_library', 'numberposts' => -1, 'orderby' => 'ID', 'order' => 'DESC' ] ) as $p ) {
		if ( 0 === strpos( $p->post_title, 'Benvegnù' ) && ! isset( $out[ $p->post_title ] ) ) { $out[ $p->post_title ] = $p->ID; }
	}
	return $out;
}

function bvg_pagine() {
	foreach ( bvg_ultimi_template() as $titolo => $id ) {
		if ( false !== stripos( $titolo, 'header' ) || false !== stripos( $titolo, 'footer' ) || false !== stripos( $titolo, 'complet' ) ) { continue; }
		$t = trim( str_replace( 'Benvegnù:', '', $titolo ) );
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

function bvg_rigenera_id( $els ) { foreach ( $els as &$e ) { $e['id'] = substr( md5( uniqid( '', true ) ), 0, 7 ); $e['elements'] = bvg_rigenera_id( $e['elements'] ?? [] ); } return $els; }

function bvg_hf() {
	$tpl = bvg_ultimi_template();
	foreach ( [ 'Benvegnù: Header' => 'type_header', 'Benvegnù: Footer' => 'type_footer' ] as $titolo => $tipo ) {
		if ( empty( $tpl[ $titolo ] ) ) { echo "manca $titolo\n"; continue; }
		$nome = 'type_header' === $tipo ? 'Header Benvegnù' : 'Footer Benvegnù';
		$es = get_posts( [ 'post_type' => 'elementor-hf', 'title' => $nome, 'numberposts' => 1, 'post_status' => 'any' ] );
		$pid = $es ? $es[0]->ID : wp_insert_post( [ 'post_type' => 'elementor-hf', 'post_status' => 'publish', 'post_title' => $nome ] );
		update_post_meta( $pid, 'ehf_template_type', $tipo );
		update_post_meta( $pid, 'ehf_target_include_locations', [ 'rule' => [ 'basic-global' ], 'specific' => [] ] );
		update_post_meta( $pid, 'ehf_target_exclude_locations', [] );
		update_post_meta( $pid, 'ehf_target_user_roles', [] );
		$doc = \Elementor\Plugin::$instance->documents->get( $pid );
		$doc->set_is_built_with_elementor( true );
		$doc->save( [ 'elements' => bvg_rigenera_id( \Elementor\Plugin::$instance->documents->get( $tpl[ $titolo ] )->get_elements_data() ) ] );
		echo "$tipo -> $pid\n";
	}
	$menu = wp_get_nav_menu_object( 'menu-principale' );
	$mid = $menu ? $menu->term_id : wp_create_nav_menu( 'Menu principale' );
	foreach ( wp_get_nav_menu_items( $mid ) ?: [] as $it ) { wp_delete_post( $it->ID, true ); }
	foreach ( [ 'catalogo', 'vibram', 'marchi', 'azienda', 'novita', 'contatti' ] as $slug ) {
		$pg = get_page_by_path( $slug );
		if ( $pg ) { wp_update_nav_menu_item( $mid, 0, [ 'menu-item-object-id' => $pg->ID, 'menu-item-object' => 'page', 'menu-item-type' => 'post_type', 'menu-item-status' => 'publish', 'menu-item-title' => get_the_title( $pg ) ] ); }
	}
	echo 'menu ' . wp_get_nav_menu_object( $mid )->slug . ': ' . count( wp_get_nav_menu_items( $mid ) ) . " voci\n";
	\Elementor\Plugin::$instance->files_manager->clear_cache();
}

function bvg_cf7() {
	if ( ! class_exists( 'WPCF7_ContactForm' ) ) { echo "Contact Form 7 non attivo\n"; return; }
	$es = wpcf7_get_contact_form_by_title( 'Richiesta disponibilità' );
	$cf = $es ? $es : WPCF7_ContactForm::get_template( [ 'title' => 'Richiesta disponibilità' ] );
	$p = $cf->get_properties();
	$p['form'] = file_get_contents( __DIR__ . '/modulo-cf7.txt' );
	$p['mail']['recipient'] = 'commerciale@benvegnusrl.it';
	$p['mail']['subject'] = 'Richiesta disponibilità: [articolo]';
	$p['mail']['additional_headers'] = 'Reply-To: [email]';
	$p['mail']['body'] = "Nome: [nome]\nAzienda: [azienda]\nEmail: [email]\nTelefono: [telefono]\nArticolo: [articolo]\nVarianti: [varianti]\nQuantità: [quantita]\nConsegna: [consegna]\nNote: [note]";
	$cf->set_properties( $p );
	$cf->set_title( 'Richiesta disponibilità' );
	echo 'modulo ' . $cf->save() . ': ' . ( do_shortcode( '[contact-form-7 title="Richiesta disponibilità"]' ) ? 'shortcode ok' : 'shortcode vuoto' ) . "\n";
}

function bvg_novita() {
	foreach ( [ 'Il catalogo online: 874 articoli in 10 famiglie' => 'Il catalogo online raccoglie 874 articoli in 10 famiglie, con le suole e le lastre Vibram, gli utensili, i filati e i prodotti per la cura della scarpa.', 'Il nuovo sito di Benvegnù è online' => 'Il nuovo sito di Benvegnù è online: catalogo, pagina Vibram, marchi e contatti del banco di Vigonovo.' ] as $titolo => $testo ) {
		$es = get_posts( [ 'post_type' => 'post', 'title' => $titolo, 'numberposts' => 1 ] );
		if ( ! $es ) { $id = wp_insert_post( [ 'post_type' => 'post', 'post_status' => 'publish', 'post_title' => $titolo, 'post_content' => $testo ] ); echo "articolo $id: $titolo\n"; }
		else { echo "articolo già presente: $titolo\n"; }
	}
}

function bvg_verifica() {
	foreach ( [ '', 'catalogo', 'vibram', 'marchi', 'azienda', 'novita', 'contatti' ] as $slug ) {
		$pg = $slug ? get_page_by_path( $slug ) : get_post( get_option( 'page_on_front' ) );
		echo ( $slug ?: 'home' ) . ': ' . ( $pg ? get_permalink( $pg ) . ' (' . get_post_meta( $pg->ID, '_wp_page_template', true ) . ')' : 'MANCA' ) . "\n";
	}
	echo 'tema: ' . get_stylesheet() . ', indicizzabile: ' . ( get_option( 'blog_public' ) ? 'si' : 'no' ) . ', permalink: ' . get_option( 'permalink_structure' ) . "\n";
	$a = 0; foreach ( get_posts( [ 'post_type' => 'attachment', 'numberposts' => -1 ] ) as $x ) { $a++; }
	echo "immagini nella libreria media: $a\n";
}
