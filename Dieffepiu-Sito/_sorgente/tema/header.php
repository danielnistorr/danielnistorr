<?php
/**
 * Testata del sito: la stessa della home, da parti/testata.html.
 *
 * @package dieffepiu
 */

?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<?php echo dfp_testata(); // phpcs:ignore WordPress.Security.EscapeOutput -- HTML del tema, link gia' puliti ?>

