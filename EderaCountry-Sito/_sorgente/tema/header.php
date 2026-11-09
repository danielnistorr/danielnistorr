<?php
/**
 * Inizio pagina: testata e menu del telefono, come nel sito originale (parti/testata.php).
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
<a class="salta" href="#contenuto">Vai al contenuto</a>

<?php get_template_part( 'parti/testata' ); ?>

<main id="contenuto">
