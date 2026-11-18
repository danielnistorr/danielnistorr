<?php
/**
 * Pagine. Una pagina fatta con Elementor (Home, Informativa privacy, Cookie) si stampa cosi' com'e'.
 * Una pagina scritta nell'editor di WordPress riceve titolo e colonna di testo nello stile del sito.
 *
 * @package villaeidos
 */

get_header();
while ( have_posts() ) :
	the_post();
	if ( 'builder' === get_post_meta( get_the_ID(), '_elementor_edit_mode', true ) ) :
		the_content();
	else :
		?>
<section class="testo-semplice">
	<h1><?php the_title(); ?></h1>
	<?php the_content(); ?>
</section>
		<?php
	endif;
endwhile;
get_footer();
