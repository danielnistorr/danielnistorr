<?php
/**
 * Calcolatore "Preventivo flash": shortcode [edera_preventivo pdf="ID o indirizzo del PDF"].
 * Dal tema 1.2, se il plugin "Edera Preventivo" e' attivo, lo shortcode e' del plugin e questo file non lo registra.
 *
 * L'HTML e il JavaScript (assets/preventivo.js) sono quelli del sito originale; prezzi, capienze e regole
 * stanno in config/preventivo.php. La stima si calcola nel browser e la richiesta parte con un'email
 * (mailto) dal programma di posta di chi scrive: il sito non riceve e non salva dati, come nell'originale.
 *
 * @package edera
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Prezzo di uno spazio, con le stesse regole di preventivo.js (serve per la stima scritta nell'HTML).
 *
 * @param array $s      Spazio da config/preventivo.php.
 * @param float $n      Partecipanti.
 * @param float $durata 1.5 giornata intera, 1 mezza giornata.
 * @return float
 */
function edera_preventivo_costo( $s, $n, $durata ) {
	if ( isset( $s['intera'] ) ) {
		return 1.0 === (float) $durata && isset( $s['mezza'] ) ? (float) $s['mezza'] : (float) $s['intera'];
	}
	$extra = max( 0, min( $n, (float) $s['persone'] ) - (float) $s['incluse'] );
	return (float) $s['base'] + $extra * (float) $s['a_persona'];
}

/**
 * Importo in euro come Intl.NumberFormat('it-IT', {style:'currency', currency:'EUR'}) senza decimali inutili.
 *
 * @param float $v Importo.
 * @return string
 */
function edera_euro( $v ) {
	$dec = ( floor( $v ) == $v ) ? 0 : 2; // phpcs:ignore Universal.Operators.StrictComparisons
	$t   = number_format( $v, $dec, ',', '.' );
	if ( $dec ) {
		$t = rtrim( rtrim( $t, '0' ), ',' );
	}
	return $t . "\u{00A0}€";
}

/**
 * Indirizzo del PDF dei servizi aggiuntivi: un numero e' l'ID nella libreria media, altrimenti un indirizzo.
 *
 * @param string $pdf Valore dello shortcode.
 * @return string
 */
function edera_preventivo_pdf( $pdf ) {
	$pdf = trim( (string) $pdf );
	if ( '' === $pdf ) {
		$pdf = (string) get_option( 'edera_pdf_servizi', '' );
	}
	if ( ctype_digit( $pdf ) ) {
		$u = wp_get_attachment_url( (int) $pdf );
		return $u ? $u : '';
	}
	return $pdf;
}

// Tema 1.2: con il plugin "Edera Preventivo" attivo lo shortcode lo disegna il plugin (prezzi e regole dal
// pannello): il tema non registra il suo e non carica il suo script. Senza il plugin vale questo, come prima.
if ( ! defined( 'EDERA_PREVENTIVO_VERSIONE' ) ) :
add_shortcode(
	'edera_preventivo',
	function ( $a ) {
		$a      = shortcode_atts( array( 'pdf' => '' ), $a, 'edera_preventivo' );
		$c      = edera_config( 'preventivo' );
		$spazi  = isset( $c['spazi'] ) ? $c['spazi'] : array();
		$email  = isset( $c['email'] ) ? $c['email'] : '';
		$pdf    = edera_preventivo_pdf( $a['pdf'] );
		$esempio = isset( $c['partecipanti_esempio'] ) ? (float) $c['partecipanti_esempio'] : 20;

		// stato iniziale, come lo scrive lo script appena parte
		$scelti = array();
		foreach ( $spazi as $k => $s ) {
			if ( ! empty( $s['scelto'] ) ) {
				$scelti[] = $k;
			}
		}
		if ( ! $scelti && $spazi ) {
			$scelti[] = array_key_first( $spazi );
		}
		$massimo = 0;
		$mezza   = false;
		$totale  = 0;
		foreach ( $scelti as $k ) {
			$massimo += (int) $spazi[ $k ]['persone'];
			$mezza    = $mezza || isset( $spazi[ $k ]['mezza'] );
		}
		$n = min( $esempio, $massimo );
		foreach ( $scelti as $k ) {
			$totale += edera_preventivo_costo( $spazi[ $k ], $n, 1.5 );
		}

		wp_enqueue_script( 'edera-preventivo', get_template_directory_uri() . '/assets/preventivo.js', array(), EDERA_VERSIONE, array( 'in_footer' => true ) );
		wp_localize_script(
			'edera-preventivo',
			'EDERA_PREVENTIVO',
			array(
				'email'     => $email,
				'spazi'     => $spazi,
				'esempio'   => $esempio,
				'stagione'  => isset( $c['stagione'] ) ? $c['stagione'] : array( 'mesi' => array(), 'supplemento' => 0 ),
				'notaSi'    => isset( $c['nota_mezza_si'] ) ? $c['nota_mezza_si'] : '',
				'notaNo'    => isset( $c['nota_mezza_no'] ) ? $c['nota_mezza_no'] : '',
			)
		);

		ob_start();
		?>
<div class="calcolo">
        <form class="modulo" id="calcolo" novalidate>
          <fieldset class="passo">
            <legend><span>01</span>Gli spazi</legend>
            <div class="spazi" role="group" aria-label="Scegli uno o più spazi">
		<?php foreach ( $spazi as $k => $s ) : ?>
              <div class="spazio"><input type="checkbox" id="s-<?php echo esc_attr( $k ); ?>" name="spazi" value="<?php echo esc_attr( $k ); ?>"<?php echo in_array( $k, $scelti, true ) ? ' checked' : ''; ?>><label for="s-<?php echo esc_attr( $k ); ?>"><b><?php echo esc_html( $s['nome'] ); ?></b><small>fino a <?php echo (int) $s['persone']; ?> persone</small></label></div>
		<?php endforeach; ?>
            </div>
		<?php if ( $pdf ) : ?>
            <a class="servizi" href="<?php echo esc_url( $pdf ); ?>" target="_blank" rel="noopener">Servizi aggiuntivi, in PDF <span class="freccia" aria-hidden="true">↗</span></a>
		<?php endif; ?>
          </fieldset>

          <fieldset class="passo">
            <legend><span>02</span>Partecipanti e durata</legend>
            <div class="campi">
              <label class="campo">Numero partecipanti
                <input id="ospiti" type="number" inputmode="numeric" min="1" max="<?php echo (int) $massimo; ?>" step="1" placeholder="Indica il numero di persone" required>
                <span class="nota" id="ospiti-nota">Con gli spazi scelti, fino a <?php echo (int) $massimo; ?> persone.</span>
              </label>
              <div class="campo">
                <span id="durata-titolo">Durata della giornata</span>
                <div class="durata" role="radiogroup" aria-labelledby="durata-titolo">
                  <label><input type="radio" name="durata" value="1.5" checked><span>Giornata intera</span></label>
                  <label><input type="radio" name="durata" value="1"<?php echo $mezza ? '' : ' disabled'; ?>><span>Mezza giornata</span></label>
                </div>
                <span class="nota" id="durata-nota"><?php echo esc_html( $mezza ? $c['nota_mezza_si'] : $c['nota_mezza_no'] ); ?></span>
              </div>
            </div>
          </fieldset>

          <fieldset class="passo">
            <legend><span>03</span>Il tuo evento</legend>
            <div class="campi">
              <label class="campo">Tipologia di evento<input id="tipo" type="text" placeholder="Es. team building"></label>
              <label class="campo">Data indicativa<input id="data" type="date"></label>
            </div>
          </fieldset>

          <fieldset class="passo">
            <legend><span>04</span>I tuoi recapiti</legend>
            <div class="campi">
              <label class="campo tutta">Nome azienda<input id="azienda" type="text" autocomplete="organization" placeholder="Nome azienda"></label>
              <label class="campo">Email di contatto<input id="email" type="email" autocomplete="email" placeholder="nome@azienda.it"></label>
              <label class="campo">Telefono<input id="telefono" type="tel" autocomplete="tel" placeholder="Es. 333 1234567"></label>
              <label class="consenso campo tutta"><input id="privacy" type="checkbox" required><span>Dichiaro di aver letto l'<a href="<?php echo esc_url( edera_pagina( 'privacy' ) ); ?>" target="_blank" rel="noopener">informativa privacy</a> e di aver compreso il trattamento dei dati personali necessario a gestire la mia richiesta di preventivo.</span></label>
            </div>
          </fieldset>
        </form>

        <aside class="stima" aria-labelledby="stima-titolo">
          <p class="sopra">La tua stima</p>
          <h3 id="stima-titolo">Budget orientativo</h3>
          <p class="prezzo" id="totale" aria-live="polite"><?php echo esc_html( edera_euro( $totale ) ); ?></p>
          <p class="nota">IVA e servizi extra da verificare</p>
          <ul class="voci-stima" id="voci-stima"></ul>
          <button class="btn btn-oro" type="button" id="prepara">Prepara la richiesta</button>
          <p class="avvertenza"><?php echo esc_html( isset( $c['avvertenza'] ) ? $c['avvertenza'] : '' ); ?></p>
          <div class="riepilogo" id="riepilogo" aria-live="polite">
            <pre id="riepilogo-testo"></pre>
            <div class="righe">
              <a class="btn btn-verde" id="invia" href="mailto:<?php echo esc_attr( $email ); ?>">Invia per email</a>
              <button class="btn btn-filo" type="button" id="copia" style="color:var(--green-deep);border-color:var(--green)">Copia il riepilogo</button>
            </div>
            <p class="esito" id="esito">La richiesta parte dal tuo programma di posta, verso <?php echo esc_html( $email ); ?>.</p>
          </div>
        </aside>
      </div>
		<?php
		return ob_get_clean();
	}
);
endif;
