<?php
/**
 * Barra fissa del telefono e piede: lo stesso HTML del sito originale.
 *
 * @package edera
 */

$edera_mappa = edera_dato( 'mappa' );
$edera_tel   = edera_dato( 'telefono_link' );
$edera_email = edera_dato( 'email' );
?>
<div class="barra" id="barra" aria-label="Azioni rapide">
  <a class="btn btn-oro" href="<?php echo esc_url( edera_ancora( '#preventivo' ) ); ?>">Preventivo flash</a>
  <a class="btn btn-filo" href="tel:<?php echo esc_attr( $edera_tel ); ?>">Chiama</a>
</div>

<footer class="piede">
  <div class="wrap">
    <div class="alto">
      <div>
        <span class="marchio"><b>EDERA</b><small>COUNTRY HOUSE</small></span>
        <p><?php echo esc_html( edera_dato( 'descrizione' ) ); ?></p>
        <p class="indirizzo"><a href="<?php echo esc_url( $edera_mappa ); ?>" target="_blank" rel="noopener" title="Apri in Google Maps"><?php echo esc_html( edera_dato( 'via' ) ); ?><br><?php echo esc_html( edera_dato( 'comune' ) ); ?></a></p>
      </div>
      <div>
        <h4>La location</h4>
        <ul><li><a href="<?php echo esc_url( edera_ancora( '#location' ) ); ?>">Gli spazi</a></li><li><a href="<?php echo esc_url( edera_ancora( '#gallery' ) ); ?>">Gallery</a></li><li><a href="<?php echo esc_url( edera_ancora( '#contatti' ) ); ?>">Contatti</a></li></ul>
      </div>
      <div>
        <h4>Eventi</h4>
        <ul><li><a href="<?php echo esc_url( edera_ancora( '#eventi' ) ); ?>">Meeting e convention</a></li><li><a href="<?php echo esc_url( edera_ancora( '#eventi' ) ); ?>">Celebrazioni</a></li><li><a href="<?php echo esc_url( edera_ancora( '#eventi' ) ); ?>">Team building</a></li></ul>
      </div>
      <div>
        <h4>Contatti</h4>
        <ul><li><a href="mailto:<?php echo esc_attr( $edera_email ); ?>"><?php echo esc_html( $edera_email ); ?></a></li><li><a href="tel:<?php echo esc_attr( $edera_tel ); ?>">Cell. <?php echo esc_html( edera_dato( 'telefono' ) ); ?></a></li><li><a href="<?php echo esc_url( edera_ancora( '#preventivo' ) ); ?>">Preventivo flash</a></li></ul>
      </div>
    </div>
    <div class="basso">
      <span>© <span id="anno"><?php echo esc_html( wp_date( 'Y' ) ); ?></span> Edera Country House · <?php echo esc_html( edera_dato( 'via' ) ); ?> · <?php echo esc_html( edera_dato( 'comune' ) ); ?> · C.F. e P.IVA <?php echo esc_html( edera_dato( 'piva' ) ); ?></span>
      <span><a href="<?php echo esc_url( edera_pagina( 'privacy' ) ); ?>">Informativa privacy</a> · <a href="<?php echo esc_url( edera_pagina( 'cookie' ) ); ?>">Cookie</a></span>
    </div>
  </div>
</footer>
