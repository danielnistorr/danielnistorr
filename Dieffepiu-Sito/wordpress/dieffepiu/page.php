<?php
/**
 * Pagine. Le pagine create dall'installatore contengono gia' le loro sezioni (titolo compreso):
 * si stampano cosi' come sono. Una pagina nuova scritta nell'editor riceve titolo e colonna di testo.
 * Una pagina fatta con Elementor viene lasciata a Elementor, a tutta larghezza.
 *
 * @package dieffepiu
 */

get_header();
while ( have_posts() ) :
	the_post();
	$dfp_contenuto = get_the_content();
	$dfp_elementor = 'builder' === get_post_meta( get_the_ID(), '_elementor_edit_mode', true );
	if ( $dfp_elementor || false !== strpos( $dfp_contenuto, '<h1' ) ) :
		?>
<main id="top"<?php echo is_front_page() ? '' : ' class="interna"'; ?>>
		<?php the_content(); ?>
</main>
		<?php
	else :
		?>
<main id="top" class="interna">
<section class="wrap testa-pagina" aria-labelledby="titolo">
	<?php echo dfp_briciole( array( get_the_title() ) ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
	<h1 class="titolo-pagina" id="titolo"><?php the_title(); ?></h1>
	<div class="griglia articolo"><div class="testo-art"><?php the_content(); ?></div></div>
</section>
		<?php echo dfp_parte( 'richiesta' ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
</main>
		<?php
	endif;
endwhile;
get_footer();
