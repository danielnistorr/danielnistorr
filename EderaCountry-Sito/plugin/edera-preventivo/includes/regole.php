<?php
/**
 * Le regole del Preventivo flash: valori iniziali, lettura, controllo e salvataggio.
 *
 * Tutte le regole stanno in una sola opzione di WordPress ("edera_preventivo_regole"), un array con le sezioni
 * spazi, durate, calendario, tariffe, sconti, servizi, testi e generali. I conti li fa il browser
 * (assets/calcolo.js) con queste regole: il server non riceve e non salva le richieste.
 *
 * @package edera-preventivo
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const EDERA_PREVENTIVO_OPZIONE = 'edera_preventivo_regole';

/**
 * Testo della mail iniziale: lo stesso del calcolatore del sito originale.
 *
 * @return string
 */
function edera_preventivo_corpo_iniziale() {
	return "Richiesta di preventivo, Edera Country House\n\n"
		. "Azienda: {azienda}\nEmail: {email}\nTelefono: {telefono}\nTipologia di evento: {tipo}\n"
		. "Spazi: {spazi}\nData: {data}\nPartecipanti: {persone}\nDurata: {durata}\n{servizi_riga}"
		. "Stima location: {totale}\n\nImporto indicativo, da confermare con la struttura.";
}

/**
 * Le regole di oggi (le stesse del calcolatore di ederacountry.it e di config/preventivo.php del tema Edera).
 *
 * @return array
 */
function edera_preventivo_iniziali() {
	return array(
		'versione'   => 1,
		'spazi'      => array(
			array( 'chiave' => 'rustico', 'nome' => 'Rustico', 'persone' => 50, 'modo' => 'persone', 'base' => 400, 'incluse' => 20, 'a_persona' => 15, 'prezzo_intera' => 0, 'prezzo_mezza' => 0, 'mezza' => false, 'attivo' => true, 'scelto' => true, 'nota' => '' ),
			array( 'chiave' => 'serra', 'nome' => 'Serra', 'persone' => 70, 'modo' => 'persone', 'base' => 250, 'incluse' => 20, 'a_persona' => 5, 'prezzo_intera' => 0, 'prezzo_mezza' => 0, 'mezza' => false, 'attivo' => true, 'scelto' => false, 'nota' => '' ),
			array( 'chiave' => 'piscina', 'nome' => 'Piscina', 'persone' => 30, 'modo' => 'fisso', 'base' => 0, 'incluse' => 0, 'a_persona' => 0, 'prezzo_intera' => 400, 'prezzo_mezza' => 300, 'mezza' => true, 'attivo' => true, 'scelto' => false, 'nota' => '' ),
			array( 'chiave' => 'esterno', 'nome' => 'Spazio esterno', 'persone' => 120, 'modo' => 'persone', 'base' => 350, 'incluse' => 20, 'a_persona' => 2.5, 'prezzo_intera' => 0, 'prezzo_mezza' => 0, 'mezza' => false, 'attivo' => true, 'scelto' => false, 'nota' => '' ),
		),
		'durate'     => array(
			'intera'        => 'Giornata intera',
			'mezza'         => 'Mezza giornata',
			'mezza_attiva'  => true,
			'regola_mezza'  => 'almeno_uno',
			'nota_mezza_si' => 'Per la piscina puoi scegliere mezza giornata o giornata intera.',
			'nota_mezza_no' => 'Per gli spazi selezionati è prevista la giornata intera.',
		),
		'calendario' => array(
			'date_escluse'   => array(),
			'periodi_chiusi' => array(),
			'giorni_chiusi'  => array(),
			'preavviso'      => 0,
			'finestra_mesi'  => 0,
		),
		'tariffe'    => array(
			array( 'nome' => 'Tariffa stagionale', 'attiva' => true, 'tipo' => 'mesi', 'mesi' => array( 10, 11, 12, 1, 2, 3 ), 'giorni' => array(), 'dal' => '', 'al' => '', 'modo' => 'importo', 'valore' => 125, 'applica' => 'primo_spazio' ),
		),
		'sconti'     => array(
			'piu_spazi'      => array( 'attivo' => false, 'da' => 2, 'modo' => 'percentuale', 'valore' => 0, 'nome' => 'Sconto per più spazi' ),
			'persone'        => array( 'attivo' => false, 'oltre' => 50, 'modo' => 'percentuale', 'valore' => 0, 'nome' => 'Sconto per gruppi numerosi' ),
			'minimo_persone' => 0,
			'spesa_minima'   => 0,
			'arrotonda'      => array( 'modo' => 'nessuno', 'passo' => 10 ),
		),
		'servizi'    => array(),
		'testi'      => array(
			'email'        => 'edera@ederacountry.it',
			'oggetto'      => 'Richiesta di preventivo, {azienda}',
			'corpo'        => edera_preventivo_corpo_iniziale(),
			'avvertenza'   => 'Il prezzo indicato è orientativo e non definitivo: il preventivo finale può variare in base alla tipologia di evento, ai servizi richiesti e alle esigenze organizzative. Valori da confermare con la struttura.',
			'iva'          => 'personalizzata',
			'nota_prezzo'  => 'IVA e servizi extra da verificare',
			'msg_data'     => 'Questa data non è disponibile: scegline un’altra.',
			'msg_capienza' => 'Con gli spazi scelti si arriva al massimo a {max} persone: la stima è calcolata su {max}.',
		),
		'generali'   => array(
			'partecipanti_esempio' => 20,
		),
	);
}

/**
 * Le regole di config/preventivo.php del tema Edera, se il tema attivo ce l'ha (quelle che il committente
 * poteva aver gia' cambiato), portate nella forma del plugin. Altrimenti i valori iniziali.
 *
 * @return array
 */
function edera_preventivo_dal_tema() {
	$r = edera_preventivo_iniziali();
	$f = get_template_directory() . '/config/preventivo.php';
	if ( ! file_exists( $f ) ) {
		return $r;
	}
	$c = include $f;
	if ( ! is_array( $c ) || empty( $c['spazi'] ) || ! is_array( $c['spazi'] ) ) {
		return $r;
	}
	$spazi = array();
	foreach ( $c['spazi'] as $k => $s ) {
		$fisso   = isset( $s['intera'] );
		$spazi[] = array(
			'chiave'        => sanitize_key( $k ),
			'nome'          => isset( $s['nome'] ) ? (string) $s['nome'] : (string) $k,
			'persone'       => isset( $s['persone'] ) ? (int) $s['persone'] : 1,
			'modo'          => $fisso ? 'fisso' : 'persone',
			'base'          => isset( $s['base'] ) ? (float) $s['base'] : 0,
			'incluse'       => isset( $s['incluse'] ) ? (int) $s['incluse'] : 0,
			'a_persona'     => isset( $s['a_persona'] ) ? (float) $s['a_persona'] : 0,
			'prezzo_intera' => $fisso ? (float) $s['intera'] : 0,
			'prezzo_mezza'  => isset( $s['mezza'] ) ? (float) $s['mezza'] : 0,
			'mezza'         => isset( $s['mezza'] ),
			'attivo'        => true,
			'scelto'        => ! empty( $s['scelto'] ),
			'nota'          => '',
		);
	}
	$r['spazi'] = $spazi;
	if ( isset( $c['email'] ) ) {
		$r['testi']['email'] = (string) $c['email'];
	}
	if ( isset( $c['partecipanti_esempio'] ) ) {
		$r['generali']['partecipanti_esempio'] = (int) $c['partecipanti_esempio'];
	}
	if ( isset( $c['stagione']['mesi'], $c['stagione']['supplemento'] ) ) {
		$r['tariffe'][0]['mesi']   = array_map( 'intval', (array) $c['stagione']['mesi'] );
		$r['tariffe'][0]['valore'] = (float) $c['stagione']['supplemento'];
	}
	foreach ( array( 'nota_mezza_si', 'nota_mezza_no' ) as $k ) {
		if ( isset( $c[ $k ] ) ) {
			$r['durate'][ $k ] = (string) $c[ $k ];
		}
	}
	if ( isset( $c['avvertenza'] ) ) {
		$r['testi']['avvertenza'] = (string) $c['avvertenza'];
	}
	$v = edera_preventivo_controlla( $r );
	return $v['errori'] ? edera_preventivo_iniziali() : $v['regole'];
}

/**
 * Le regole salvate (o quelle iniziali, se non ce ne sono ancora).
 *
 * @return array
 */
function edera_preventivo_regole() {
	$r = get_option( EDERA_PREVENTIVO_OPZIONE );
	if ( ! is_array( $r ) || empty( $r['spazi'] ) ) {
		return edera_preventivo_iniziali();
	}
	// una sezione che manca (aggiunta in una versione successiva del plugin) prende i valori iniziali
	return array_replace( edera_preventivo_iniziali(), array_intersect_key( $r, edera_preventivo_iniziali() ) );
}

/**
 * Il calendario ha regole (giorni esclusi, chiusure, preavviso, finestra)?
 *
 * @param array $r Regole.
 * @return bool
 */
function edera_preventivo_calendario_attivo( $r ) {
	$c = $r['calendario'];
	return ! empty( $c['date_escluse'] ) || ! empty( $c['periodi_chiusi'] ) || ! empty( $c['giorni_chiusi'] ) || (int) $c['preavviso'] > 0 || (int) $c['finestra_mesi'] > 0;
}

/**
 * Una data Y-m-d valida?
 *
 * @param string $d Data.
 * @return bool
 */
function edera_preventivo_data_valida( $d ) {
	if ( ! is_string( $d ) || ! preg_match( '/^(\d{4})-(\d{2})-(\d{2})$/', $d, $m ) ) {
		return false;
	}
	return checkdate( (int) $m[2], (int) $m[3], (int) $m[1] );
}

/**
 * Pulisce e controlla le regole (dal modulo di amministrazione o da un file JSON importato).
 * Niente prezzi negativi, percentuali fra 0 e 100, date nel formato AAAA-MM-GG, numeri interi dove servono.
 *
 * @param mixed $in Dati grezzi.
 * @return array array( 'regole' => regole pulite, 'errori' => messaggi ).
 */
function edera_preventivo_controlla( $in ) {
	$e   = array();
	$ini = edera_preventivo_iniziali();
	$in  = is_array( $in ) ? $in : array();
	$num = function ( $v ) {
		$v = is_string( $v ) ? str_replace( ',', '.', trim( $v ) ) : $v;
		return is_numeric( $v ) ? (float) $v : null;
	};
	$intero = function ( $v ) use ( $num ) {
		$n = $num( $v );
		return null === $n ? null : (int) round( $n );
	};
	$si     = function ( $v ) {
		return ! empty( $v ) && '0' !== $v && 'false' !== $v;
	};
	$testo  = function ( $v, $righe = false ) {
		$v = is_scalar( $v ) ? (string) $v : '';
		return $righe ? sanitize_textarea_field( $v ) : sanitize_text_field( $v );
	};
	$prezzo = function ( $v, $dove ) use ( $num, &$e ) {
		if ( '' === $v || null === $v ) {
			return 0.0;
		}
		$n = $num( $v );
		if ( null === $n ) {
			/* translators: %s: where the wrong value is */
			$e[] = sprintf( __( 'Numero non valido: %s.', 'edera-preventivo' ), $dove );
			return 0.0;
		}
		if ( $n < 0 ) {
			/* translators: %s: where the wrong value is */
			$e[] = sprintf( __( 'I prezzi non possono essere negativi: %s.', 'edera-preventivo' ), $dove );
			return 0.0;
		}
		return round( $n, 2 );
	};
	$quota  = function ( $modo, $v, $dove ) use ( $prezzo, &$e ) {
		$n = $prezzo( $v, $dove );
		if ( 'percentuale' === $modo && $n > 100 ) {
			/* translators: %s: where the wrong value is */
			$e[] = sprintf( __( 'Le percentuali vanno da 0 a 100: %s.', 'edera-preventivo' ), $dove );
			$n = 100.0;
		}
		return $n;
	};
	$lista_num = function ( $v, $min, $max ) {
		$out = array();
		foreach ( (array) $v as $x ) {
			if ( is_numeric( $x ) && (int) $x >= $min && (int) $x <= $max && ! in_array( (int) $x, $out, true ) ) {
				$out[] = (int) $x;
			}
		}
		return $out;
	};
	$r = array( 'versione' => 1 );

	// spazi
	$r['spazi'] = array();
	$chiavi     = array();
	foreach ( array_values( isset( $in['spazi'] ) ? (array) $in['spazi'] : array() ) as $i => $s ) {
		$s    = (array) $s;
		$nome = $testo( isset( $s['nome'] ) ? $s['nome'] : '' );
		if ( '' === $nome ) {
			continue; // riga vuota
		}
		/* translators: %s: space name */
		$dove   = sprintf( __( 'spazio "%s"', 'edera-preventivo' ), $nome );
		$chiave = sanitize_key( isset( $s['chiave'] ) && '' !== $s['chiave'] ? $s['chiave'] : remove_accents( $nome ) );
		$chiave = '' === $chiave ? 'spazio' : $chiave;
		$base_k = $chiave;
		for ( $n = 2; in_array( $chiave, $chiavi, true ); $n++ ) {
			$chiave = $base_k . '-' . $n;
		}
		$chiavi[] = $chiave;
		$persone  = $intero( isset( $s['persone'] ) ? $s['persone'] : '' );
		if ( null === $persone || $persone < 1 ) {
			/* translators: %s: where the wrong value is */
			$e[]     = sprintf( __( 'La capienza deve essere almeno 1 persona: %s.', 'edera-preventivo' ), $dove );
			$persone = 1;
		}
		$incluse = $intero( isset( $s['incluse'] ) ? $s['incluse'] : 0 );
		if ( null === $incluse || $incluse < 0 ) {
			/* translators: %s: where the wrong value is */
			$e[]     = sprintf( __( 'Le persone comprese nel prezzo base non possono essere negative: %s.', 'edera-preventivo' ), $dove );
			$incluse = 0;
		}
		$modo         = isset( $s['modo'] ) && 'fisso' === $s['modo'] ? 'fisso' : 'persone';
		$r['spazi'][] = array(
			'chiave'        => $chiave,
			'nome'          => $nome,
			'persone'       => $persone,
			'modo'          => $modo,
			'base'          => $prezzo( isset( $s['base'] ) ? $s['base'] : 0, $dove ),
			'incluse'       => $incluse,
			'a_persona'     => $prezzo( isset( $s['a_persona'] ) ? $s['a_persona'] : 0, $dove ),
			'prezzo_intera' => $prezzo( isset( $s['prezzo_intera'] ) ? $s['prezzo_intera'] : 0, $dove ),
			'prezzo_mezza'  => $prezzo( isset( $s['prezzo_mezza'] ) ? $s['prezzo_mezza'] : 0, $dove ),
			'mezza'         => $si( isset( $s['mezza'] ) ? $s['mezza'] : false ),
			'attivo'        => $si( isset( $s['attivo'] ) ? $s['attivo'] : false ),
			'scelto'        => $si( isset( $s['scelto'] ) ? $s['scelto'] : false ),
			'nota'          => $testo( isset( $s['nota'] ) ? $s['nota'] : '' ),
		);
	}
	$attivi = array_filter(
		$r['spazi'],
		function ( $s ) {
			return $s['attivo'];
		}
	);
	if ( ! $attivi ) {
		$e[] = __( 'Serve almeno uno spazio attivo.', 'edera-preventivo' );
	}

	// durate
	$d           = isset( $in['durate'] ) ? (array) $in['durate'] : array();
	$r['durate'] = array(
		'intera'        => $testo( isset( $d['intera'] ) ? $d['intera'] : '' ),
		'mezza'         => $testo( isset( $d['mezza'] ) ? $d['mezza'] : '' ),
		'mezza_attiva'  => $si( isset( $d['mezza_attiva'] ) ? $d['mezza_attiva'] : false ),
		'regola_mezza'  => isset( $d['regola_mezza'] ) && 'tutti' === $d['regola_mezza'] ? 'tutti' : 'almeno_uno',
		'nota_mezza_si' => $testo( isset( $d['nota_mezza_si'] ) ? $d['nota_mezza_si'] : '' ),
		'nota_mezza_no' => $testo( isset( $d['nota_mezza_no'] ) ? $d['nota_mezza_no'] : '' ),
	);
	foreach ( array( 'intera', 'mezza' ) as $k ) {
		if ( '' === $r['durate'][ $k ] ) {
			$r['durate'][ $k ] = $ini['durate'][ $k ];
		}
	}

	// calendario
	$c    = isset( $in['calendario'] ) ? (array) $in['calendario'] : array();
	$cal  = array(
		'date_escluse'   => array(),
		'periodi_chiusi' => array(),
		'giorni_chiusi'  => $lista_num( isset( $c['giorni_chiusi'] ) ? $c['giorni_chiusi'] : array(), 1, 7 ),
		'preavviso'      => 0,
		'finestra_mesi'  => 0,
	);
	foreach ( array_values( isset( $c['date_escluse'] ) ? (array) $c['date_escluse'] : array() ) as $x ) {
		$x    = (array) $x;
		$data = trim( isset( $x['data'] ) ? (string) $x['data'] : '' );
		if ( '' === $data ) {
			continue;
		}
		if ( ! edera_preventivo_data_valida( $data ) ) {
			/* translators: %s: date */
			$e[] = sprintf( __( 'Data esclusa non valida (si scrive AAAA-MM-GG): %s.', 'edera-preventivo' ), $data );
			continue;
		}
		$cal['date_escluse'][] = array(
			'data' => $data,
			'nota' => $testo( isset( $x['nota'] ) ? $x['nota'] : '' ),
		);
	}
	foreach ( array_values( isset( $c['periodi_chiusi'] ) ? (array) $c['periodi_chiusi'] : array() ) as $x ) {
		$x   = (array) $x;
		$dal = trim( isset( $x['dal'] ) ? (string) $x['dal'] : '' );
		$al  = trim( isset( $x['al'] ) ? (string) $x['al'] : '' );
		if ( '' === $dal && '' === $al ) {
			continue;
		}
		if ( ! edera_preventivo_data_valida( $dal ) || ! edera_preventivo_data_valida( $al ) || $dal > $al ) {
			/* translators: 1: start date, 2: end date */
			$e[] = sprintf( __( 'Periodo di chiusura non valido (date AAAA-MM-GG, "dal" prima di "al"): %1$s, %2$s.', 'edera-preventivo' ), $dal, $al );
			continue;
		}
		$cal['periodi_chiusi'][] = array(
			'dal'  => $dal,
			'al'   => $al,
			'nota' => $testo( isset( $x['nota'] ) ? $x['nota'] : '' ),
		);
	}
	$pre = $intero( isset( $c['preavviso'] ) && '' !== $c['preavviso'] ? $c['preavviso'] : 0 );
	if ( null === $pre || $pre < 0 || $pre > 365 ) {
		$e[] = __( 'Il preavviso va da 0 a 365 giorni.', 'edera-preventivo' );
		$pre = 0;
	}
	$fin = $intero( isset( $c['finestra_mesi'] ) && '' !== $c['finestra_mesi'] ? $c['finestra_mesi'] : 0 );
	if ( null === $fin || $fin < 0 || $fin > 60 ) {
		$e[] = __( 'La finestra di prenotazione va da 0 a 60 mesi.', 'edera-preventivo' );
		$fin = 0;
	}
	$cal['preavviso']     = $pre;
	$cal['finestra_mesi'] = $fin;
	$r['calendario']      = $cal;

	// tariffe e supplementi
	$r['tariffe'] = array();
	foreach ( array_values( isset( $in['tariffe'] ) ? (array) $in['tariffe'] : array() ) as $t ) {
		$t    = (array) $t;
		$nome = $testo( isset( $t['nome'] ) ? $t['nome'] : '' );
		if ( '' === $nome ) {
			continue;
		}
		/* translators: %s: surcharge name */
		$dove = sprintf( __( 'tariffa "%s"', 'edera-preventivo' ), $nome );
		$tipo = isset( $t['tipo'] ) && in_array( $t['tipo'], array( 'mesi', 'giorni', 'periodo' ), true ) ? $t['tipo'] : 'mesi';
		$modo = isset( $t['modo'] ) && 'percentuale' === $t['modo'] ? 'percentuale' : 'importo';
		$riga = array(
			'nome'    => $nome,
			'attiva'  => $si( isset( $t['attiva'] ) ? $t['attiva'] : false ),
			'tipo'    => $tipo,
			'mesi'    => $lista_num( isset( $t['mesi'] ) ? $t['mesi'] : array(), 1, 12 ),
			'giorni'  => $lista_num( isset( $t['giorni'] ) ? $t['giorni'] : array(), 1, 7 ),
			'dal'     => trim( isset( $t['dal'] ) ? (string) $t['dal'] : '' ),
			'al'      => trim( isset( $t['al'] ) ? (string) $t['al'] : '' ),
			'modo'    => $modo,
			'valore'  => $quota( $modo, isset( $t['valore'] ) ? $t['valore'] : 0, $dove ),
			'applica' => isset( $t['applica'] ) && in_array( $t['applica'], array( 'primo_spazio', 'ogni_spazio', 'totale' ), true ) ? $t['applica'] : 'totale',
		);
		if ( 'mesi' === $tipo && ! $riga['mesi'] ) {
			/* translators: %s: where */
			$e[] = sprintf( __( 'Scegli almeno un mese: %s.', 'edera-preventivo' ), $dove );
		}
		if ( 'giorni' === $tipo && ! $riga['giorni'] ) {
			/* translators: %s: where */
			$e[] = sprintf( __( 'Scegli almeno un giorno della settimana: %s.', 'edera-preventivo' ), $dove );
		}
		if ( 'periodo' === $tipo && ( ! edera_preventivo_data_valida( $riga['dal'] ) || ! edera_preventivo_data_valida( $riga['al'] ) || $riga['dal'] > $riga['al'] ) ) {
			/* translators: %s: where */
			$e[] = sprintf( __( 'Periodo non valido (date AAAA-MM-GG, "dal" prima di "al"): %s.', 'edera-preventivo' ), $dove );
		}
		$r['tariffe'][] = $riga;
	}

	// sconti e minimi
	$s  = isset( $in['sconti'] ) ? (array) $in['sconti'] : array();
	$ps = isset( $s['piu_spazi'] ) ? (array) $s['piu_spazi'] : array();
	$pp = isset( $s['persone'] ) ? (array) $s['persone'] : array();
	$ar = isset( $s['arrotonda'] ) ? (array) $s['arrotonda'] : array();
	$sc = array(
		'piu_spazi'      => array(
			'attivo' => $si( isset( $ps['attivo'] ) ? $ps['attivo'] : false ),
			'da'     => max( 2, (int) $intero( isset( $ps['da'] ) ? $ps['da'] : 2 ) ),
			'modo'   => isset( $ps['modo'] ) && 'importo' === $ps['modo'] ? 'importo' : 'percentuale',
			'valore' => 0,
			'nome'   => $testo( isset( $ps['nome'] ) && '' !== $ps['nome'] ? $ps['nome'] : $ini['sconti']['piu_spazi']['nome'] ),
		),
		'persone'        => array(
			'attivo' => $si( isset( $pp['attivo'] ) ? $pp['attivo'] : false ),
			'oltre'  => max( 1, (int) $intero( isset( $pp['oltre'] ) ? $pp['oltre'] : 1 ) ),
			'modo'   => isset( $pp['modo'] ) && 'importo' === $pp['modo'] ? 'importo' : 'percentuale',
			'valore' => 0,
			'nome'   => $testo( isset( $pp['nome'] ) && '' !== $pp['nome'] ? $pp['nome'] : $ini['sconti']['persone']['nome'] ),
		),
		'minimo_persone' => max( 0, (int) $intero( isset( $s['minimo_persone'] ) && '' !== $s['minimo_persone'] ? $s['minimo_persone'] : 0 ) ),
		'spesa_minima'   => $prezzo( isset( $s['spesa_minima'] ) ? $s['spesa_minima'] : 0, __( 'spesa minima', 'edera-preventivo' ) ),
		'arrotonda'      => array(
			'modo'  => isset( $ar['modo'] ) && in_array( $ar['modo'], array( 'nessuno', 'eccesso', 'difetto', 'vicino' ), true ) ? $ar['modo'] : 'nessuno',
			'passo' => $prezzo( isset( $ar['passo'] ) ? $ar['passo'] : 10, __( 'arrotondamento', 'edera-preventivo' ) ),
		),
	);
	$sc['piu_spazi']['valore'] = $quota( $sc['piu_spazi']['modo'], isset( $ps['valore'] ) ? $ps['valore'] : 0, $sc['piu_spazi']['nome'] );
	$sc['persone']['valore']   = $quota( $sc['persone']['modo'], isset( $pp['valore'] ) ? $pp['valore'] : 0, $sc['persone']['nome'] );
	if ( 'nessuno' !== $sc['arrotonda']['modo'] && $sc['arrotonda']['passo'] <= 0 ) {
		$e[] = __( 'Per arrotondare serve un passo maggiore di zero (per esempio 10 euro).', 'edera-preventivo' );
	}
	$r['sconti'] = $sc;

	// servizi aggiuntivi
	$r['servizi'] = array();
	foreach ( array_values( isset( $in['servizi'] ) ? (array) $in['servizi'] : array() ) as $x ) {
		$x    = (array) $x;
		$nome = $testo( isset( $x['nome'] ) ? $x['nome'] : '' );
		if ( '' === $nome ) {
			continue;
		}
		/* translators: %s: service name */
		$dove           = sprintf( __( 'servizio "%s"', 'edera-preventivo' ), $nome );
		$r['servizi'][] = array(
			'nome'   => $nome,
			'prezzo' => $prezzo( isset( $x['prezzo'] ) ? $x['prezzo'] : 0, $dove ),
			'modo'   => isset( $x['modo'] ) && 'persona' === $x['modo'] ? 'persona' : 'fisso',
			'attivo' => $si( isset( $x['attivo'] ) ? $x['attivo'] : false ),
			'nota'   => $testo( isset( $x['nota'] ) ? $x['nota'] : '' ),
		);
	}

	// testi e invio
	$t          = isset( $in['testi'] ) ? (array) $in['testi'] : array();
	$r['testi'] = array();
	foreach ( array( 'oggetto', 'avvertenza', 'nota_prezzo', 'msg_data', 'msg_capienza' ) as $k ) {
		$r['testi'][ $k ] = $testo( isset( $t[ $k ] ) ? $t[ $k ] : '' );
	}
	// a capo come nella mail di oggi ("\n"): il modulo del pannello manda "\r\n"
	$r['testi']['corpo'] = str_replace( array( "\r\n", "\r" ), "\n", $testo( isset( $t['corpo'] ) ? $t['corpo'] : '', true ) );
	$r['testi']['iva']   = isset( $t['iva'] ) && in_array( $t['iva'], array( 'personalizzata', 'inclusa', 'esclusa', 'nessuna' ), true ) ? $t['iva'] : 'personalizzata';
	$email               = sanitize_email( isset( $t['email'] ) ? $t['email'] : '' );
	if ( ! is_email( $email ) ) {
		$e[]   = __( 'L’email che riceve le richieste non è valida.', 'edera-preventivo' );
		$email = $ini['testi']['email'];
	}
	$r['testi']['email'] = $email;
	foreach ( array( 'oggetto', 'corpo' ) as $k ) {
		if ( '' === trim( $r['testi'][ $k ] ) ) {
			$r['testi'][ $k ] = $ini['testi'][ $k ];
		}
	}

	// generali
	$g     = isset( $in['generali'] ) ? (array) $in['generali'] : array();
	$esemp = $intero( isset( $g['partecipanti_esempio'] ) ? $g['partecipanti_esempio'] : 20 );
	if ( null === $esemp || $esemp < 1 ) {
		$e[]   = __( 'I partecipanti d’esempio devono essere almeno 1.', 'edera-preventivo' );
		$esemp = 20;
	}
	$r['generali'] = array( 'partecipanti_esempio' => $esemp );

	return array(
		'regole' => $r,
		'errori' => array_values( array_unique( $e ) ),
	);
}
