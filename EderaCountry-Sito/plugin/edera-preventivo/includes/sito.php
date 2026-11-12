<?php
/**
 * Il calcolatore sul sito: shortcode [edera_preventivo pdf="ID o indirizzo del PDF"].
 *
 * Prende il posto dello shortcode del tema Edera (si registra dopo il tema, su "init"), con lo stesso HTML e le
 * stesse classi: l'aspetto lo da' il foglio di stile del tema. Le regole arrivano al browser in JSON e i conti
 * li fa assets/calcolo.js; la richiesta resta una mail precompilata.
 *
 * @package edera-preventivo
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action(
	'init',
	function () {
		remove_shortcode( 'edera_preventivo' ); // quello del tema, se il tema e' ancora la 1.1
		add_shortcode( 'edera_preventivo', 'edera_preventivo_shortcode' );
	},
	20
);

/**
 * Importo in euro come Intl.NumberFormat('it-IT') del browser (senza decimali inutili, spazio unificatore).
 *
 * @param float $v Importo.
 * @return string
 */
function edera_preventivo_euro( $v ) {
	$dec = ( floor( $v ) == $v ) ? 0 : 2; // phpcs:ignore Universal.Operators.StrictComparisons
	$t   = number_format( $v, $dec, ',', abs( $v ) >= 10000 ? '.' : '' );
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
function edera_preventivo_link_pdf( $pdf ) {
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

/**
 * La nota sotto il prezzo (IVA).
 *
 * @param array $r Regole.
 * @return string
 */
function edera_preventivo_nota_iva( $r ) {
	switch ( $r['testi']['iva'] ) {
		case 'inclusa':
			return __( 'IVA inclusa', 'edera-preventivo' );
		case 'esclusa':
			return __( 'IVA esclusa', 'edera-preventivo' );
		case 'nessuna':
			return '';
	}
	return $r['testi']['nota_prezzo'];
}

/**
 * Prezzo e testo di un servizio aggiuntivo.
 *
 * @param array $x Servizio.
 * @return string
 */
function edera_preventivo_prezzo_servizio( $x ) {
	$p = edera_preventivo_euro( (float) $x['prezzo'] );
	/* translators: %s: price */
	return 'persona' === $x['modo'] ? sprintf( __( '%s a persona', 'edera-preventivo' ), $p ) : $p;
}

/**
 * Carica script e stili del calcolatore (una volta sola) e passa le regole al browser.
 *
 * @param array $r Regole.
 */
function edera_preventivo_risorse( $r ) {
	$u   = plugin_dir_url( EDERA_PREVENTIVO_FILE ) . 'assets/';
	$v   = EDERA_PREVENTIVO_VERSIONE;
	$cal = edera_preventivo_calendario_attivo( $r );
	$dip = array( 'edera-preventivo-calcolo' );
	wp_enqueue_script( 'edera-preventivo-calcolo', $u . 'calcolo.js', array(), $v, array( 'in_footer' => true ) );
	wp_localize_script( 'edera-preventivo-calcolo', 'EDERA_PREVENTIVO_TESTI', edera_preventivo_testi_js() );
	if ( $cal ) {
		wp_enqueue_style( 'edera-flatpickr', $u . 'vendor/flatpickr/flatpickr.min.css', array(), '4.6.13' );
		wp_enqueue_script( 'edera-flatpickr', $u . 'vendor/flatpickr/flatpickr.min.js', array(), '4.6.13', array( 'in_footer' => true ) );
		wp_enqueue_script( 'edera-flatpickr-it', $u . 'vendor/flatpickr/it.js', array( 'edera-flatpickr' ), '4.6.13', array( 'in_footer' => true ) );
		$dip[] = 'edera-flatpickr-it';
	}
	if ( $cal || array_filter( wp_list_pluck( $r['servizi'], 'attivo' ) ) || (int) $r['sconti']['minimo_persone'] > 1 ) {
		wp_enqueue_style( 'edera-preventivo', $u . 'preventivo.css', $cal ? array( 'edera-flatpickr' ) : array(), $v );
	}
	wp_enqueue_script( 'edera-preventivo', $u . 'preventivo.js', $dip, $v, array( 'in_footer' => true ) );
	wp_localize_script(
		'edera-preventivo',
		'EDERA_PREVENTIVO',
		array(
			'regole' => $r,
			'testi'  => edera_preventivo_testi_js(),
		)
	);
}

/**
 * Testi che servono agli script.
 *
 * @return array
 */
function edera_preventivo_testi_js() {
	return array(
		'daA'            => __( 'Con gli spazi scelti, da {min} a {max} persone.', 'edera-preventivo' ),
		'scegliData'     => __( 'Scegli la data', 'edera-preventivo' ),
		'spesaMinima'    => __( 'Spesa minima', 'edera-preventivo' ),
		'arrotondamento' => __( 'Arrotondamento', 'edera-preventivo' ),
	);
}

/**
 * Lo shortcode [edera_preventivo].
 *
 * @param array $a Attributi.
 * @return string
 */
function edera_preventivo_shortcode( $a ) {
	$a      = shortcode_atts( array( 'pdf' => '' ), $a, 'edera_preventivo' );
	$r      = edera_preventivo_regole();
	$pdf    = edera_preventivo_link_pdf( $a['pdf'] );
	$email  = $r['testi']['email'];
	$spazi  = array_values(
		array_filter(
			$r['spazi'],
			function ( $s ) {
				return $s['attivo'];
			}
		)
	);
	$scelti = array();
	foreach ( $spazi as $s ) {
		if ( $s['scelto'] ) {
			$scelti[] = $s['chiave'];
		}
	}
	if ( ! $scelti && $spazi ) {
		$scelti[] = $spazi[0]['chiave'];
	}
	// stato iniziale, come lo scrive lo script appena parte (serve solo senza JavaScript)
	$massimo = 0;
	$con     = 0;
	foreach ( $spazi as $s ) {
		if ( in_array( $s['chiave'], $scelti, true ) ) {
			$massimo += (int) $s['persone'];
			$con     += $s['mezza'] ? 1 : 0;
		}
	}
	$mezza  = $r['durate']['mezza_attiva'] && ( 'tutti' === $r['durate']['regola_mezza'] ? count( $scelti ) === $con : $con > 0 );
	$minimo = max( 1, (int) $r['sconti']['minimo_persone'] );
	$n      = max( min( $minimo, $massimo ), min( (int) $r['generali']['partecipanti_esempio'], $massimo ) );
	$totale = 0;
	foreach ( $spazi as $s ) {
		if ( in_array( $s['chiave'], $scelti, true ) ) {
			$totale += 'fisso' === $s['modo'] ? (float) $s['prezzo_intera'] : (float) $s['base'] + max( 0, min( $n, (int) $s['persone'] ) - (int) $s['incluse'] ) * (float) $s['a_persona'];
		}
	}
	$servizi = array_filter(
		$r['servizi'],
		function ( $x ) {
			return $x['attivo'];
		}
	);
	$cal     = edera_preventivo_calendario_attivo( $r );
	$iva     = edera_preventivo_nota_iva( $r );
	$privacy = get_privacy_policy_url();
	$privacy = $privacy ? $privacy : home_url( '/privacy/' );
	$nota_os = $minimo > 1
		/* translators: 1: minimum, 2: maximum participants */
		? sprintf( __( 'Con gli spazi scelti, da %1$d a %2$d persone.', 'edera-preventivo' ), $minimo, $massimo )
		: 'Con gli spazi scelti, fino a ' . (int) $massimo . ' persone.';

	edera_preventivo_risorse( $r );
	ob_start();
	?>
<div class="calcolo">
        <form class="modulo" id="calcolo" novalidate>
          <fieldset class="passo">
            <legend><span>01</span>Gli spazi</legend>
            <div class="spazi" role="group" aria-label="Scegli uno o più spazi">
	<?php foreach ( $spazi as $s ) : ?>
              <div class="spazio"><input type="checkbox" id="s-<?php echo esc_attr( $s['chiave'] ); ?>" name="spazi" value="<?php echo esc_attr( $s['chiave'] ); ?>"<?php echo in_array( $s['chiave'], $scelti, true ) ? ' checked' : ''; ?>><label for="s-<?php echo esc_attr( $s['chiave'] ); ?>"><b><?php echo esc_html( $s['nome'] ); ?></b><small>fino a <?php echo (int) $s['persone']; ?> persone</small><?php echo '' !== $s['nota'] ? '<small class="edp-nota-spazio">' . esc_html( $s['nota'] ) . '</small>' : ''; ?></label></div>
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
                <input id="ospiti" type="number" inputmode="numeric" min="<?php echo (int) $minimo; ?>" max="<?php echo (int) $massimo; ?>" step="1" placeholder="Indica il numero di persone" required>
                <span class="nota" id="ospiti-nota"><?php echo esc_html( $nota_os ); ?></span>
              </label>
              <div class="campo">
                <span id="durata-titolo">Durata della giornata</span>
                <div class="durata" role="radiogroup" aria-labelledby="durata-titolo">
                  <label><input type="radio" name="durata" value="1.5" checked><span><?php echo esc_html( $r['durate']['intera'] ); ?></span></label>
                  <label><input type="radio" name="durata" value="1"<?php echo $mezza ? '' : ' disabled'; ?>><span><?php echo esc_html( $r['durate']['mezza'] ); ?></span></label>
                </div>
                <span class="nota" id="durata-nota"><?php echo esc_html( $mezza ? $r['durate']['nota_mezza_si'] : $r['durate']['nota_mezza_no'] ); ?></span>
              </div>
            </div>
          </fieldset>

          <fieldset class="passo">
            <legend><span>03</span>Il tuo evento</legend>
            <div class="campi">
              <label class="campo">Tipologia di evento<input id="tipo" type="text" placeholder="Es. team building"></label>
	<?php if ( $cal ) : ?>
              <label class="campo edp-campo-data"><?php esc_html_e( 'Data dell’evento', 'edera-preventivo' ); ?><input id="data" type="text" inputmode="none" placeholder="<?php esc_attr_e( 'Scegli la data', 'edera-preventivo' ); ?>" autocomplete="off"><span class="nota" id="data-nota" hidden></span></label>
	<?php else : ?>
              <label class="campo">Data indicativa<input id="data" type="date"></label>
	<?php endif; ?>
	<?php if ( $servizi ) : ?>
              <div class="campo tutta edp-servizi">
                <span id="servizi-titolo"><?php esc_html_e( 'Servizi aggiuntivi', 'edera-preventivo' ); ?></span>
                <div class="spazi" role="group" aria-labelledby="servizi-titolo">
		<?php foreach ( $servizi as $i => $x ) : ?>
                  <div class="spazio"><input type="checkbox" id="servizio-<?php echo (int) $i; ?>" name="servizi" value="<?php echo (int) $i; ?>"><label for="servizio-<?php echo (int) $i; ?>"><b><?php echo esc_html( $x['nome'] ); ?></b><small><?php echo esc_html( edera_preventivo_prezzo_servizio( $x ) ); ?></small><?php echo '' !== $x['nota'] ? '<small class="edp-nota-spazio">' . esc_html( $x['nota'] ) . '</small>' : ''; ?></label></div>
		<?php endforeach; ?>
                </div>
              </div>
	<?php endif; ?>
            </div>
          </fieldset>

          <fieldset class="passo">
            <legend><span>04</span>I tuoi recapiti</legend>
            <div class="campi">
              <label class="campo tutta">Nome azienda<input id="azienda" type="text" autocomplete="organization" placeholder="Nome azienda"></label>
              <label class="campo">Email di contatto<input id="email" type="email" autocomplete="email" placeholder="nome@azienda.it"></label>
              <label class="campo">Telefono<input id="telefono" type="tel" autocomplete="tel" placeholder="Es. 333 1234567"></label>
              <label class="consenso campo tutta"><input id="privacy" type="checkbox" required><span>Dichiaro di aver letto l'<a href="<?php echo esc_url( $privacy ); ?>" target="_blank" rel="noopener">informativa privacy</a> e di aver compreso il trattamento dei dati personali necessario a gestire la mia richiesta di preventivo.</span></label>
            </div>
          </fieldset>
        </form>

        <aside class="stima" aria-labelledby="stima-titolo">
          <p class="sopra">La tua stima</p>
          <h3 id="stima-titolo">Budget orientativo</h3>
          <p class="prezzo" id="totale" aria-live="polite"><?php echo esc_html( edera_preventivo_euro( $totale ) ); ?></p>
	<?php if ( '' !== $iva ) : ?>
          <p class="nota"><?php echo esc_html( $iva ); ?></p>
	<?php endif; ?>
          <ul class="voci-stima" id="voci-stima"></ul>
          <button class="btn btn-oro" type="button" id="prepara">Prepara la richiesta</button>
          <p class="avvertenza"><?php echo esc_html( $r['testi']['avvertenza'] ); ?></p>
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
