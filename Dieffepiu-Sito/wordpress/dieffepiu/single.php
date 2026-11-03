<?php
/**
 * Una notizia.
 *
 * @package dieffepiu
 */

get_header();
while ( have_posts() ) :
	the_post();
	$dfp_news = dfp_url_notizie();
	?>
<main id="top" class="interna">
<section class="wrap testa-pagina" aria-labelledby="titolo">
	<?php echo dfp_briciole( array( array( $dfp_news, 'Fiere e novità' ), get_the_title() ) ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
	<h1 class="titolo-pagina" id="titolo"><?php the_title(); ?></h1>
	<p class="data-art"><time datetime="<?php echo esc_attr( get_the_date( 'Y-m-d' ) ); ?>"><?php echo esc_html( 'Pubblicata ' . dfp_data( get_the_date( 'U' ), true ) ); ?></time></p>
	<div class="griglia articolo">
		<div class="testo-art num"><?php the_content(); ?></div>
	</div>
	<p class="vai"><a href="<?php echo esc_url( $dfp_news ); ?>">Tutte le fiere e le novità</a></p>
</section>
	<?php echo dfp_parte( 'richiesta' ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
</main>
	<?php
endwhile;
get_footer();
