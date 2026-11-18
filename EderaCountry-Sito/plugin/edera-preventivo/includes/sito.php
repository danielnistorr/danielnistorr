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
 * Riempie i segnaposti {nome} di un testo, come riempi() di calcolo.js.
 *
 * @param string $t Testo.
 * @param array  $m Segnaposto => valore.
 * @return string
 */
function edera_preventivo_riempi( $t, $m ) {
	return preg_replace_callback(
		'/\{([a-z_]+)\}/',
		function ( $x ) use ( $m ) {
			return array_key_exists( $x[1], $m ) ? (string) $m[ $x[1] ] : $x[0];
		},
		(string) $t
	);
}

/**
 * Prezzo di una voce in un modo (fisso, a persona, a pezzo), come prezzoBase() di calcolo.js.
 *
 * @param string $modo     Modo.
 * @param float  $importo  Importo.
 * @param array  $x        Voce.
 * @param bool   $comprese Scrivere i pezzi compresi nell'affitto.
 * @return string
 */
function edera_preventivo_prezzo_base( $modo, $importo, $x, $comprese ) {
	$t = edera_preventivo_testi_js();
	$p = edera_preventivo_euro( (float) $importo );
	$u = '' !== (string) $x['unita'] ? $x['unita'] : $t['pezzo'];
	if ( 'persona' === $modo ) {
		return edera_preventivo_riempi( $t['aPersona'], array( 'prezzo' => $p ) );
	}
	if ( 'pezzo' === $modo ) {
		return $comprese && (int) $x['comprese'] > 0
			? edera_preventivo_riempi( $t['pezzoComprese'], array( 'comprese' => (int) $x['comprese'], 'prezzo' => $p, 'unita' => $u ) )
			: edera_preventivo_riempi( $t['aPezzo'], array( 'prezzo' => $p, 'unita' => $u ) );
	}
	return $p;
}

/**
 * Prezzo e testo di una voce dei servizi e dotazioni: "80 €", "2 € a persona", "1 € a sedia", "da 80 €" (con le
 * fasce: il prezzo della prima). Come prezzoTesto() di calcolo.js.
 *
 * @param array $x Voce.
 * @return string
 */
function edera_preventivo_prezzo_servizio( $x ) {
	$x = $x + edera_preventivo_servizio_nuove();
	if ( 'incluso' !== $x['modo'] && ! empty( $x['fasce'] ) ) {
		$f = reset( $x['fasce'] );
		return edera_preventivo_riempi( edera_preventivo_testi_js()['da'], array( 'prezzo' => edera_preventivo_prezzo_base( $f['modo'], $f['importo'], $x, false ) ) );
	}
	return edera_preventivo_prezzo_base( $x['modo'], $x['prezzo'], $x, true );
}

/**
 * Una voce c'e' con gli spazi scelti (attiva e senza spazi, o con almeno uno dei suoi spazi)? Come
 * voceDisponibile() di calcolo.js.
 *
 * @param array $x      Voce.
 * @param array $chiavi Chiavi degli spazi scelti.
 * @return bool
 */
function edera_preventivo_voce_disponibile( $x, $chiavi ) {
	return ! empty( $x['attivo'] ) && ( empty( $x['spazi'] ) || array_intersect( (array) $x['spazi'], $chiavi ) );
}

/**
 * La voce ha una quantita' (prezzo a pezzo, o una fascia a pezzo)?
 *
 * @param array $x Voce.
 * @return bool
 */
function edera_preventivo_con_quantita( $x ) {
	return 'pezzo' === $x['modo'] || in_array( 'pezzo', wp_list_pluck( (array) $x['fasce'], 'modo' ), true );
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
	if ( $cal || array_filter( wp_list_pluck( $r['servizi'], 'attivo' ) ) || (int) $r['sconti']['minimo_persone'] > 1 || edera_preventivo_con_note( $r ) ) {
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
 * La stima puo' avere delle note (capienza superabile, almeno uno spazio attivo con le fasce, o una voce dei
 * servizi e dotazioni con le fasce o con pezzi che possono non bastare)?
 *
 * @param array $r Regole.
 * @return bool
 */
function edera_preventivo_con_note( $r ) {
	if ( 'rigido' !== $r['generali']['oltre_capienza'] ) {
		return true;
	}
	foreach ( $r['spazi'] as $s ) {
		if ( $s['attivo'] && ! empty( $s['fasce'] ) ) {
			return true;
		}
	}
	// servizi e dotazioni: fasce (numero fuori dalle fasce) o quantita' automatica con un massimo (pezzi che non bastano)
	foreach ( $r['servizi'] as $x ) {
		if ( $x['attivo'] && 'incluso' !== $x['modo'] && ( ! empty( $x['fasce'] ) || ( 'automatica' === $x['quantita'] && (int) $x['massimo'] > 0 && edera_preventivo_con_quantita( $x ) ) ) ) {
			return true;
		}
	}
	return false;
}

/**
 * Prezzo di uno spazio per lo stato iniziale del calcolatore (giornata intera), come prezzoSpazio() di calcolo.js.
 *
 * @param array $s     Spazio.
 * @param int   $n     Partecipanti.
 * @param int   $extra Persone oltre la capienza contate in piu' (con la stima).
 * @return float|null  Null = da valutare (oltre la capienza, nessuna fascia).
 */
function edera_preventivo_prezzo_iniziale( $s, $n, $extra ) {
	$p = min( $n, (int) $s['persone'] + $extra );
	if ( ! empty( $s['fasce'] ) ) {
		$f      = null;
		$aperta = null;
		foreach ( $s['fasce'] as $x ) {
			if ( ! $f && $p >= (int) $x['da'] && ( ! (int) $x['a'] || $p <= (int) $x['a'] ) ) {
				$f = $x;
			}
			if ( ! (int) $x['a'] ) {
				$aperta = $x;
			}
		}
		if ( ! $f && $p > (int) $s['persone'] ) {
			if ( ! $aperta ) {
				return null;
			}
			$f = $aperta;
		}
		if ( $f ) {
			return 'persona' === $f['modo'] ? (float) $f['importo'] * $p : (float) $f['importo'];
		}
	}
	return 'fisso' === $s['modo'] ? (float) $s['prezzo_intera'] : (float) $s['base'] + max( 0, $p - (int) $s['incluse'] ) * (float) $s['a_persona'];
}

/**
 * Testi che servono agli script.
 *
 * @return array
 */
function edera_preventivo_testi_js() {
	return array(
		'daA'             => __( 'Con gli spazi scelti, da {min} a {max} persone.', 'edera-preventivo' ),
		'scegliData'      => __( 'Scegli la data', 'edera-preventivo' ),
		'spesaMinima'     => __( 'Spesa minima', 'edera-preventivo' ),
		'arrotondamento'  => __( 'Arrotondamento', 'edera-preventivo' ),
		// tariffe solo su certi spazi, con la riga a parte (dalla 1.1.0): "Riscaldamento (Rustico, Serra)"
		'tariffaRiga'     => __( '{nome} ({spazi})', 'edera-preventivo' ),
		// servizi e dotazioni (dalla 1.1.0): righe della stima, prezzi, quantita', note
		'voceDettaglio'   => __( '{voce} ({dettaglio})', 'edera-preventivo' ),
		'voceQuantita'    => __( '{voce} ({quantita})', 'edera-preventivo' ),
		'pezzi'           => __( '{quantita} × {prezzo}', 'edera-preventivo' ),
		'pezziComprese'   => __( '{quantita}, di cui {comprese} nell’affitto: {pagati} × {prezzo}', 'edera-preventivo' ),
		'pezziCompresi'   => __( '{quantita} nell’affitto', 'edera-preventivo' ),
		'aPersona'        => __( '{prezzo} a persona', 'edera-preventivo' ),
		'aPezzo'          => __( '{prezzo} a {unita}', 'edera-preventivo' ),
		'pezzoComprese'   => __( '{comprese} nell’affitto, poi {prezzo} a {unita}', 'edera-preventivo' ),
		'da'              => __( 'da {prezzo}', 'edera-preventivo' ),
		'pezzo'           => __( 'pezzo', 'edera-preventivo' ),
		'pezziNome'       => __( 'pezzi', 'edera-preventivo' ),
		'finoA'           => __( 'fino a {massimo}', 'edera-preventivo' ),
		'auto'            => __( '{quantita} {pezzi} per {persone}', 'edera-preventivo' ),
		'autoMassimo'     => __( '{quantita} {pezzi} per {persone}, il massimo disponibile', 'edera-preventivo' ),
		'persona1'        => __( '1 persona', 'edera-preventivo' ),
		'persone'         => __( '{n} persone', 'edera-preventivo' ),
		'disponibili'     => __( '{voce}: ne servono {servono}, disponibili {massimo}: il resto da concordare con la struttura.', 'edera-preventivo' ),
		'fuoriFasciaVoce' => __( '{voce}: per {persone} persone non c’è una fascia di prezzo, la stima usa il prezzo standard.', 'edera-preventivo' ),
		'compresiRiga'    => __( 'Compresi nell’affitto: {elenco}', 'edera-preventivo' ),
		'dotazioniRiga'   => __( 'Dotazioni: {elenco}', 'edera-preventivo' ),
		'compresoMax'     => __( '{voce} (fino a {massimo})', 'edera-preventivo' ),
		'compresi'        => __( 'Compresi nell’affitto', 'edera-preventivo' ),
		'quantita'        => __( 'Quantità', 'edera-preventivo' ),
		'quantitaMax'     => __( 'Quantità (fino a {massimo})', 'edera-preventivo' ),
		'dotazioni'       => __( 'Dotazioni', 'edera-preventivo' ),
		'serviziExtra'    => __( 'Servizi extra', 'edera-preventivo' ),
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
	// stato iniziale, come lo scrive lo script appena parte (serve solo senza JavaScript); stessi conti di calcolo.js
	$capienza = 0;
	$con      = 0;
	foreach ( $spazi as $s ) {
		if ( in_array( $s['chiave'], $scelti, true ) ) {
			$capienza += (int) $s['persone'];
			$con      += $s['mezza'] ? 1 : 0;
		}
	}
	$mezza    = $r['durate']['mezza_attiva'] && ( 'tutti' === $r['durate']['regola_mezza'] ? count( $scelti ) === $con : $con > 0 );
	$minimo   = max( 1, (int) $r['sconti']['minimo_persone'] );
	$modo     = $r['generali']['oltre_capienza'];
	$assoluto = max( 0, (int) $r['generali']['massimo_assoluto'] );
	$limite   = 'rigido' === $modo ? ( $assoluto > 0 ? min( $capienza, $assoluto ) : $capienza ) : $assoluto; // 0 = nessun limite
	$n        = max( 1, (int) $r['generali']['partecipanti_esempio'] );
	if ( $limite > 0 && $n > $limite ) {
		$n = $limite;
	}
	if ( $minimo > 1 && $n < $minimo ) {
		$n = $limite > 0 ? min( $minimo, $limite ) : $minimo;
	}
	$extra  = ( 'stima' === $modo && $n > $capienza ) ? $n - $capienza : 0;
	$senza  = 'senza' === $modo && $n > $capienza;
	$totale = 0;
	foreach ( $spazi as $s ) {
		if ( in_array( $s['chiave'], $scelti, true ) ) {
			$prezzo = edera_preventivo_prezzo_iniziale( $s, $n, $extra );
			$senza  = $senza || null === $prezzo;
			$totale += (float) $prezzo;
		}
	}
	// servizi e dotazioni attivi (le chiavi sono gli indici nelle regole), in due gruppi: dotazioni, poi servizi extra;
	// in ogni gruppo le voci da scegliere e quelle comprese nell'affitto. Una voce legata a spazi non scelti resta
	// nascosta (lo script la mostra quando si sceglie lo spazio)
	$testi  = edera_preventivo_testi_js();
	$gruppi = array(
		'dotazione' => array( 'titolo' => $testi['dotazioni'], 'id' => 'dotazioni-titolo', 'scelte' => array(), 'compresi' => array(), 'visibili' => 0 ),
		'servizio'  => array( 'titolo' => $testi['serviziExtra'], 'id' => 'servizi-titolo', 'scelte' => array(), 'compresi' => array(), 'visibili' => 0 ),
	);
	foreach ( $r['servizi'] as $i => $x ) {
		if ( ! $x['attivo'] ) {
			continue;
		}
		$g = 'dotazione' === $x['gruppo'] ? 'dotazione' : 'servizio';
		$x['_visibile'] = edera_preventivo_voce_disponibile( $x, $scelti );
		$gruppi[ $g ][ 'incluso' === $x['modo'] ? 'compresi' : 'scelte' ][ $i ] = $x;
		$gruppi[ $g ]['visibili'] += $x['_visibile'] ? 1 : 0;
	}
	$servizi = array_filter(
		$gruppi,
		function ( $gr ) {
			return $gr['scelte'] || $gr['compresi'];
		}
	);
	$cal     = edera_preventivo_calendario_attivo( $r );
	$iva     = edera_preventivo_nota_iva( $r );
	$privacy = get_privacy_policy_url();
	$privacy = $privacy ? $privacy : home_url( '/privacy/' );
	$nota_os = $minimo > 1
		/* translators: 1: minimum, 2: maximum participants */
		? sprintf( __( 'Con gli spazi scelti, da %1$d a %2$d persone.', 'edera-preventivo' ), $minimo, $limite )
		: 'Con gli spazi scelti, fino a ' . (int) $limite . ' persone.';
	if ( 'rigido' !== $modo ) {
		$nota_os = str_replace( '{capienza}', (string) $capienza, $r['testi']['nota_capienza'] );
	}

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
                <input id="ospiti" type="number" inputmode="numeric" min="<?php echo (int) $minimo; ?>"<?php echo $limite > 0 ? ' max="' . (int) $limite . '"' : ''; ?> step="1" placeholder="Indica il numero di persone" required>
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
	<?php foreach ( $servizi as $g => $gr ) : ?>
              <div class="campo tutta edp-servizi edp-gruppo-<?php echo esc_attr( $g ); ?>"<?php echo $gr['visibili'] ? '' : ' hidden'; ?>>
                <span id="<?php echo esc_attr( $gr['id'] ); ?>"><?php echo esc_html( $gr['titolo'] ); ?></span>
		<?php if ( $gr['compresi'] ) : ?>
                <div class="edp-compresi"<?php echo array_filter( wp_list_pluck( $gr['compresi'], '_visibile' ) ) ? '' : ' hidden'; ?>>
                  <span class="edp-compresi-titolo"><?php echo esc_html( $testi['compresi'] ); ?></span>
                  <ul>
			<?php foreach ( $gr['compresi'] as $i => $x ) : ?>
                    <li data-voce="<?php echo (int) $i; ?>"<?php echo $x['_visibile'] ? '' : ' hidden'; ?>><b><?php echo esc_html( $x['nome'] ); ?></b><?php echo (int) $x['massimo'] > 0 ? '<small>' . esc_html( edera_preventivo_riempi( $testi['finoA'], array( 'massimo' => (int) $x['massimo'] ) ) ) . '</small>' : ''; ?><?php echo '' !== $x['nota'] ? '<small>' . esc_html( $x['nota'] ) . '</small>' : ''; ?></li>
			<?php endforeach; ?>
                  </ul>
                </div>
		<?php endif; ?>
		<?php if ( $gr['scelte'] ) : ?>
                <div class="spazi edp-voci" role="group" aria-labelledby="<?php echo esc_attr( $gr['id'] ); ?>">
			<?php
			foreach ( $gr['scelte'] as $i => $x ) :
				$quanti = edera_preventivo_con_quantita( $x );
				$chiede = $quanti && 'cliente' === $x['quantita'];
				?>
                  <div class="spazio<?php echo $chiede ? ' edp-pezzi' : ''; ?>" data-voce="<?php echo (int) $i; ?>"<?php echo $x['_visibile'] ? '' : ' hidden'; ?>><input type="checkbox" id="servizio-<?php echo (int) $i; ?>" name="servizi" value="<?php echo (int) $i; ?>"><label for="servizio-<?php echo (int) $i; ?>"><b><?php echo esc_html( $x['nome'] ); ?></b><small><?php echo esc_html( edera_preventivo_prezzo_servizio( $x ) ); ?></small><?php echo '' !== $x['nota'] ? '<small class="edp-nota-spazio">' . esc_html( $x['nota'] ) . '</small>' : ''; ?><?php echo $quanti && ! $chiede ? '<small class="edp-auto" data-voce="' . (int) $i . '"></small>' : ''; ?></label><?php if ( $chiede ) : ?><span class="edp-quantita"><label for="quantita-<?php echo (int) $i; ?>"><?php echo esc_html( (int) $x['massimo'] > 0 ? edera_preventivo_riempi( $testi['quantitaMax'], array( 'massimo' => (int) $x['massimo'] ) ) : $testi['quantita'] ); ?></label><input id="quantita-<?php echo (int) $i; ?>" class="edp-q" type="number" inputmode="numeric" min="1"<?php echo (int) $x['massimo'] > 0 ? ' max="' . (int) $x['massimo'] . '"' : ''; ?> step="1" value="1" data-voce="<?php echo (int) $i; ?>"></span><?php endif; ?></div>
			<?php endforeach; ?>
                </div>
		<?php endif; ?>
              </div>
	<?php endforeach; ?>
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
	<?php if ( $senza ) : ?>
          <p class="prezzo edp-da-valutare" id="totale" aria-live="polite"><?php echo esc_html( $r['testi']['da_valutare'] ); ?></p>
	<?php else : ?>
          <p class="prezzo" id="totale" aria-live="polite"><?php echo esc_html( edera_preventivo_euro( $totale ) ); ?></p>
	<?php endif; ?>
	<?php if ( '' !== $iva ) : ?>
          <p class="nota"><?php echo esc_html( $iva ); ?></p>
	<?php endif; ?>
	<?php if ( edera_preventivo_con_note( $r ) ) : ?>
          <div class="edp-note-stima" id="stima-note" aria-live="polite" hidden></div>
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
