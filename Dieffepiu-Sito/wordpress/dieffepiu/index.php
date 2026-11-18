<?php
/**
 * Elenco delle notizie (pagina "Fiere e novita'", archivi, ricerca).
 *
 * @package dieffepiu
 */

get_header();
?>
<main id="top" class="interna">
<?php echo dfp_parte( 'news-testa' ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
<section class="wrap" aria-label="Elenco delle notizie">
	<div class="notizie-elenco">
<?php
while ( have_posts() ) :
	the_post();
	$dfp_quando = get_post_meta( get_the_ID(), '_dfp_quando', true );
	?>
	<article class="notizia">
		<time datetime="<?php echo esc_attr( get_the_date( 'Y-m-d' ) ); ?>"><?php echo esc_html( $dfp_quando ? $dfp_quando : dfp_data( get_the_date( 'U' ) ) ); ?></time>
		<div class="corpo-n">
			<h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
			<p><?php echo esc_html( get_the_excerpt() ); ?></p>
		</div>
	</article>
	<?php
endwhile;
?>
	</div>
	<?php
	$dfp_prima = get_previous_posts_link( 'Notizie più recenti' );
	$dfp_dopo  = get_next_posts_link( 'Notizie precedenti' );
	if ( $dfp_prima || $dfp_dopo ) {
		echo '<p class="vai">' . wp_kses_post( trim( $dfp_prima . ' &emsp; ' . $dfp_dopo, ' &emsp;' ) ) . '</p>';
	}
	?>
</section>
<?php echo dfp_parte( 'richiesta' ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
</main>
<?php
get_footer();
