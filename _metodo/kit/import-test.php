<?php
// Importa ogni .json di una cartella con la stessa funzione del pulsante "Importa template"
// (Source_Local::import_template) e confronta gli elementi del file con quelli salvati.
// Uso: wp eval-file import-test.php <cartella>
use Elementor\Plugin;
wp_set_current_user( 1 );
list( $dir ) = $args;
$source = Plugin::$instance->templates_manager->get_source( 'local' );
$count = function ( $els ) use ( &$count ) { $n = 0; foreach ( $els as $e ) { $n += 1 + $count( $e['elements'] ?? [] ); } return $n; };
$imgs = function ( $els, &$out ) use ( &$imgs ) { foreach ( $els as $e ) { array_walk_recursive( $e['settings'], function ( $v, $k ) use ( &$out ) { if ( 'url' === $k && preg_match( '/\.(jpe?g|png|webp|svg|gif)$/i', $v ) ) { $out[] = $v; } } ); $imgs( $e['elements'] ?? [], $out ); } };
$report = [];
foreach ( glob( "$dir/*.json" ) as $f ) {
	$src = json_decode( file_get_contents( $f ), true );
	// copia temporanea: l'import può spostare o cancellare il file caricato
	$tmp = wp_tempnam( basename( $f ) ); copy( $f, $tmp );
	$res = $source->import_template( basename( $f ), $tmp );
	$row = [ 'file' => basename( $f ), 'ok' => ! is_wp_error( $res ) ];
	if ( is_wp_error( $res ) ) { $row['error'] = $res->get_error_message(); $report[] = $row; continue; }
	$tid = $res[0]['template_id'];
	$doc = Plugin::$instance->documents->get( $tid );
	$saved = $doc->get_elements_data();
	$u = []; $imgs( $saved, $u );
	$s = []; $imgs( $src['content'], $s );
	$ph = count( array_filter( $u, function ( $x ) { return false !== strpos( $x, 'placeholder' ); } ) );
	$row += [ 'template_id' => $tid, 'title' => get_the_title( $tid ), 'type' => $res[0]['type'],
		'elements_src' => $count( $src['content'] ), 'elements_saved' => $count( $saved ),
		'images_src' => count( $s ), 'images_saved' => count( $u ), 'images_placeholder' => $ph,
		'images_local' => count( array_filter( $u, function ( $x ) { return false !== strpos( $x, '/wp-content/uploads/' ); } ) ) ];
	$report[] = $row;
}
echo wp_json_encode( $report, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES ), "\n";
