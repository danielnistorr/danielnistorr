<?php
/**
 * Testata e menu del telefono: lo stesso HTML del sito originale.
 * Le voci portano alle sezioni della home (ancore: #location, #eventi ...).
 *
 * @package edera
 */

$edera_mappa = edera_dato( 'mappa' );
?>
<header class="testa">
  <div class="wrap">
    <a href="<?php echo esc_url( edera_ancora( '#' ) ); ?>" class="marchio" aria-label="Edera Country House, inizio pagina"><b>EDERA</b><small>COUNTRY HOUSE</small></a>
    <nav class="voci" aria-label="Sezioni">
      <a href="<?php echo esc_url( edera_ancora( '#location' ) ); ?>">La location</a>
      <a href="<?php echo esc_url( edera_ancora( '#eventi' ) ); ?>">Eventi</a>
      <a href="<?php echo esc_url( edera_ancora( '#gallery' ) ); ?>">Gallery</a>
      <a href="<?php echo esc_url( edera_ancora( '#contatti' ) ); ?>">Contatti</a>
      <a class="btn btn-chiaro" href="<?php echo esc_url( edera_ancora( '#preventivo' ) ); ?>">Preventivo flash <span class="freccia" aria-hidden="true">↗</span></a>
    </nav>
    <button class="apri-menu" type="button" aria-expanded="false" aria-controls="pannello">Menu</button>
  </div>
</header>

<div class="pannello" id="pannello" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="riga">
    <span class="marchio"><b>EDERA</b><small>COUNTRY HOUSE</small></span>
    <button class="apri-menu chiudi" type="button" style="display:inline-flex">Chiudi</button>
  </div>
  <nav aria-label="Sezioni">
    <a href="<?php echo esc_url( edera_ancora( '#location' ) ); ?>">La location</a>
    <a href="<?php echo esc_url( edera_ancora( '#eventi' ) ); ?>">Eventi</a>
    <a href="<?php echo esc_url( edera_ancora( '#gallery' ) ); ?>">Gallery</a>
    <a href="<?php echo esc_url( edera_ancora( '#preventivo' ) ); ?>">Preventivo flash</a>
    <a href="<?php echo esc_url( edera_ancora( '#contatti' ) ); ?>">Contatti</a>
  </nav>
  <p class="fine"><a href="<?php echo esc_url( $edera_mappa ); ?>" target="_blank" rel="noopener" title="Apri in Google Maps"><?php echo esc_html( edera_dato( 'via' ) ); ?> · <?php echo esc_html( edera_dato( 'comune' ) ); ?></a><br><a href="mailto:<?php echo esc_attr( edera_dato( 'email' ) ); ?>"><?php echo esc_html( edera_dato( 'email' ) ); ?></a> · <a href="tel:<?php echo esc_attr( edera_dato( 'telefono_link' ) ); ?>"><?php echo esc_html( edera_dato( 'telefono' ) ); ?></a></p>
</div>
