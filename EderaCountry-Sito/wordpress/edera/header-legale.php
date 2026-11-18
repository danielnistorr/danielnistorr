<?php
/**
 * Inizio delle pagine legali (Informativa privacy, Cookie): la testata semplice dell'originale.
 *
 * @package edera
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
<header class="testa"><a class="logo" href="<?php echo esc_url( home_url( '/' ) ); ?>" aria-label="Edera Country House, pagina principale"><b>EDERA</b><i>COUNTRY HOUSE</i></a><a class="eti" href="<?php echo esc_url( home_url( '/' ) ); ?>">Tornare al sito</a></header>
<main>
