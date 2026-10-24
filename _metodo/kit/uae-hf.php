<?php
// Header e footer globali con Ultimate Addons (come farebbe un utente) dai template "<prefisso>: Header" e "<prefisso>: Footer",
// e menu WordPress "Menu principale" con le pagine indicate.
// Uso: wp eval-file uae-hf.php "<prefisso>" "slug1,slug2,slug3"
use Elementor\Plugin;
wp_set_current_user( 1 );
$prefix = $args[0] ?? '';
$slugs = array_filter( array_map( 'trim', explode( ',', $args[1] ?? '' ) ) );
$latest = function ( $needle ) use ( $prefix ) {
	foreach ( get_posts( [ 'post_type' => 'elementor_library', 'numberposts' => -1, 'orderby' => 'ID', 'order' => 'DESC' ] ) as $p ) {
		if ( 0 === strpos( $p->post_title, $prefix ) && false !== stripos( $p->post_title, $needle ) && false === stripos( $p->post_title, 'complet' ) ) { return $p->ID; }
	}
	return 0;
};
$regen = function ( $els ) use ( &$regen ) { foreach ( $els as &$e ) { $e['id'] = substr( md5( uniqid( '', true ) ), 0, 7 ); $e['elements'] = $regen( $e['elements'] ?? [] ); } return $els; };
foreach ( [ 'header' => 'type_header', 'footer' => 'type_footer' ] as $needle => $type ) {
	$tid = $latest( $needle );
	if ( ! $tid ) { echo "manca template $needle\n"; continue; }
	$title = ucfirst( $needle ) . ' ' . $prefix;
	$ex = get_posts( [ 'post_type' => 'elementor-hf', 'title' => $title, 'numberposts' => 1, 'post_status' => 'any' ] );
	$pid = $ex ? $ex[0]->ID : wp_insert_post( [ 'post_type' => 'elementor-hf', 'post_status' => 'publish', 'post_title' => $title ] );
	update_post_meta( $pid, 'ehf_template_type', $type );
	update_post_meta( $pid, 'ehf_target_include_locations', [ 'rule' => [ 'basic-global' ], 'specific' => [] ] );
	update_post_meta( $pid, 'ehf_target_exclude_locations', [] );
	update_post_meta( $pid, 'ehf_target_user_roles', [] );
	$doc = Plugin::$instance->documents->get( $pid );
	$doc->set_is_built_with_elementor( true );
	$doc->save( [ 'elements' => $regen( Plugin::$instance->documents->get( $tid )->get_elements_data() ) ] );
	echo "$type -> $pid (da template $tid)\n";
}
$menu = wp_get_nav_menu_object( 'menu-principale' );
$mid = $menu ? $menu->term_id : wp_create_nav_menu( 'Menu principale' );
foreach ( wp_get_nav_menu_items( $mid ) ?: [] as $it ) { wp_delete_post( $it->ID, true ); }
foreach ( $slugs as $slug ) {
	$pg = get_page_by_path( $slug );
	if ( $pg ) { wp_update_nav_menu_item( $mid, 0, [ 'menu-item-object-id' => $pg->ID, 'menu-item-object' => 'page', 'menu-item-type' => 'post_type', 'menu-item-status' => 'publish', 'menu-item-title' => get_the_title( $pg ) ] ); }
	else { echo "pagina non trovata per il menu: $slug\n"; }
}
echo 'menu ' . wp_get_nav_menu_object( $mid )->slug . ' voci ' . count( wp_get_nav_menu_items( $mid ) ?: [] ) . "\n";
