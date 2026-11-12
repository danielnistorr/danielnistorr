<?php
/**
 * Disinstallazione: toglie le regole salvate. Pagine e contenuti non sono mai stati toccati.
 *
 * @package edera-preventivo
 */

if ( ! defined( 'WP_UNINSTALL_PLUGIN' ) ) {
	exit;
}

delete_option( 'edera_preventivo_regole' );
global $wpdb;
$wpdb->query( "DELETE FROM {$wpdb->options} WHERE option_name LIKE '\_transient\_edera\_preventivo\_esito\_%' OR option_name LIKE '\_transient\_timeout\_edera\_preventivo\_esito\_%'" ); // phpcs:ignore WordPress.DB.DirectDatabaseQuery
