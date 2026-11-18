<?php
/**
 * Pagine. Una pagina fatta con Elementor (come la Home) si stampa cosi' com'e', a tutta larghezza.
 * Una pagina scritta nell'editor di WordPress riceve titolo e colonna di testo nello stile del sito.
 *
 * @package edera
 */

get_header();
while ( have_posts() ) :
	the_post();
	if ( 'builder' === get_post_meta( get_the_ID(), '_elementor_edit_mode', true ) ) :
		the_content();
	else :
		?>
<section class="sezione bianca testo-semplice">
	<div class="wrap">
		<h1><?php the_title(); ?></h1>
		<?php the_content(); ?>
	</div>
</section>
		<?php
	endif;
endwhile;
get_footer();
