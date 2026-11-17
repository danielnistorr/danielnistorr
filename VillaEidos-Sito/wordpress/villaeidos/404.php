<?php
/**
 * Pagina non trovata.
 *
 * @package villaeidos
 */

get_header();
?>
<section class="testo-semplice">
	<h1>Pagina non trovata</h1>
	<p>L'indirizzo non esiste o è cambiato. <a href="<?php echo esc_url( home_url( '/' ) ); ?>">Torna alla pagina principale</a>.</p>
</section>
<?php
get_footer();
