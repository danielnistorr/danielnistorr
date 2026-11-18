<?php
/**
 * Elenco generico (articoli, archivi, ricerca): il sito non ha un blog, ma WordPress lo richiede.
 *
 * @package edera
 */

get_header();
?>
<section class="sezione bianca testo-semplice">
	<div class="wrap">
		<?php if ( have_posts() ) : ?>
			<?php
			while ( have_posts() ) :
				the_post();
				?>
				<article>
					<h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
					<?php the_excerpt(); ?>
				</article>
			<?php endwhile; ?>
		<?php else : ?>
			<h1>Nessun contenuto</h1>
			<p><a href="<?php echo esc_url( home_url( '/' ) ); ?>">Torna alla pagina principale</a></p>
		<?php endif; ?>
	</div>
</section>
<?php
get_footer();
