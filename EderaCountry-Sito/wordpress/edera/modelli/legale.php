<?php
/**
 * Template Name: Pagina legale
 *
 * Informativa privacy e Cookie: testata e piede semplici, testo su una colonna (assets/legale.css).
 *
 * @package edera
 */

get_header( 'legale' );
while ( have_posts() ) :
	the_post();
	the_content();
endwhile;
get_footer( 'legale' );
