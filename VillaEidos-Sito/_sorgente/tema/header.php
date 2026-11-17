<?php
/**
 * Inizio pagina: testata e menu del telefono (parti/testata.html, lo stesso HTML dell'anteprima).
 *
 * @package villaeidos
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
<?php echo villaeidos_parte( 'testata' ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- segnaposti gia' con escape ?>
<main id="contenuto">
