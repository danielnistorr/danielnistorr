<?php
/**
 * Pagina non trovata.
 *
 * @package edera
 */

get_header();
?>
<section class="sezione bianca testo-semplice">
	<div class="wrap">
		<h1>Pagina non trovata.</h1>
		<p>L'indirizzo non esiste o è cambiato. <a href="<?php echo esc_url( home_url( '/' ) ); ?>">Torna alla pagina principale</a>.</p>
	</div>
</section>
<?php
get_footer();
