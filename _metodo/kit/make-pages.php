<?php
// Crea (o aggiorna) una pagina WordPress per ogni template importato, come farebbe un utente
// con "Inserisci template": copia gli elementi del template nella pagina.
// Header e footer (template di tipo section) vengono messi in cima e in fondo a ogni pagina.
// Uso: wp eval-file make-pages.php <prefisso-titolo> <page_template>
use Elementor\Plugin;
wp_set_current_user( 1 );
$prefix = $args[0] ?? 'Benvegnu';
$tpl = $args[1] ?? 'elementor_canvas';
$con_hf = ( $args[2] ?? 'con-hf' ) === 'con-hf';
$all = get_posts( [ 'post_type' => 'elementor_library', 'numberposts' => -1, 'orderby' => 'ID', 'order' => 'DESC' ] );
$latest = [];
foreach ( $all as $p ) { if ( 0 === strpos( $p->post_title, $prefix ) && ! isset( $latest[ $p->post_title ] ) ) { $latest[ $p->post_title ] = $p->ID; } }
$get = function ( $id ) { return Plugin::$instance->documents->get( $id )->get_elements_data(); };
$header = $footer = [];
foreach ( $latest as $title => $id ) {
	if ( false !== stripos( $title, 'header' ) ) { $header = $get( $id ); }
	if ( false !== stripos( $title, 'footer' ) ) { $footer = $get( $id ); }
}
$regen = function ( $els ) use ( &$regen ) { foreach ( $els as &$e ) { $e['id'] = substr( md5( uniqid( '', true ) ), 0, 7 ); $e['elements'] = $regen( $e['elements'] ?? [] ); } return $els; };
ksort( $latest );
foreach ( $latest as $title => $id ) {
	if ( false !== stripos( $title, 'header' ) || false !== stripos( $title, 'footer' ) || false !== stripos( $title, 'complet' ) ) { continue; }
	$slug = get_post_meta( $id, '_bvg_slug', true );
	$page_title = trim( str_replace( [ $prefix . ':', $prefix ], '', $title ), " -:" );
	$els = $con_hf ? array_merge( $regen( $header ), $get( $id ), $regen( $footer ) ) : $get( $id );
	$existing = get_page_by_path( sanitize_title( $page_title ) );
	$pid = $existing ? $existing->ID : wp_insert_post( [ 'post_type' => 'page', 'post_status' => 'publish', 'post_title' => $page_title, 'post_name' => sanitize_title( $page_title ) ] );
	$doc = Plugin::$instance->documents->get( $pid );
	$doc->set_is_built_with_elementor( true );
	$doc->save( [ 'elements' => $els, 'settings' => [ 'template' => $tpl, 'hide_title' => 'yes' ] ] );
	if ( 'Home' === $page_title ) { update_option( 'show_on_front', 'page' ); update_option( 'page_on_front', $pid ); }
	echo "page $pid <- template $id ($title) " . get_permalink( $pid ) . "\n";
}
