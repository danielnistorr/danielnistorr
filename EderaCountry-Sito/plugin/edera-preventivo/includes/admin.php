<?php
/**
 * La pagina "Preventivo" nel pannello di WordPress: tutte le regole del calcolatore, una prova, la copia
 * delle regole (esporta e importa in JSON) e il ripristino dei valori iniziali. Solo per chi ha manage_options.
 *
 * @package edera-preventivo
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action(
	'admin_menu',
	function () {
		add_menu_page( __( 'Preventivo flash', 'edera-preventivo' ), __( 'Preventivo', 'edera-preventivo' ), 'manage_options', 'edera-preventivo', 'edera_preventivo_pagina', 'dashicons-calculator', 58 );
	}
);

add_action(
	'admin_enqueue_scripts',
	function ( $hook ) {
		if ( 'toplevel_page_edera-preventivo' !== $hook ) {
			return;
		}
		$u = plugin_dir_url( EDERA_PREVENTIVO_FILE ) . 'assets/';
		wp_enqueue_style( 'edera-preventivo-admin', $u . 'admin.css', array(), EDERA_PREVENTIVO_VERSIONE );
		wp_enqueue_script( 'edera-preventivo-calcolo', $u . 'calcolo.js', array(), EDERA_PREVENTIVO_VERSIONE, true );
		wp_localize_script( 'edera-preventivo-calcolo', 'EDERA_PREVENTIVO_TESTI', edera_preventivo_testi_js() );
		wp_enqueue_script( 'edera-preventivo-admin', $u . 'admin.js', array( 'edera-preventivo-calcolo' ), EDERA_PREVENTIVO_VERSIONE, true );
		wp_localize_script( 'edera-preventivo-admin', 'EDERA_PREVENTIVO', array( 'regole' => edera_preventivo_regole() ) );
	}
);

/**
 * Controllo comune alle azioni: permesso e nonce.
 *
 * @param string $azione Nome del nonce.
 */
function edera_preventivo_permesso( $azione ) {
	if ( ! current_user_can( 'manage_options' ) ) {
		wp_die( esc_html__( 'Non hai il permesso di cambiare il preventivo.', 'edera-preventivo' ), 403 );
	}
	check_admin_referer( $azione );
}

/**
 * Torna alla pagina con un messaggio (e, se c'e', la bozza non salvata con gli errori).
 *
 * @param string $msg    Messaggio.
 * @param array  $errori Errori.
 * @param array  $bozza  Regole scritte ma non salvate.
 */
function edera_preventivo_torna( $msg, $errori = array(), $bozza = null ) {
	set_transient(
		'edera_preventivo_esito_' . get_current_user_id(),
		array(
			'msg'    => $msg,
			'errori' => $errori,
			'bozza'  => $bozza,
		),
		600
	);
	wp_safe_redirect( admin_url( 'admin.php?page=edera-preventivo' ) );
	exit;
}

add_action(
	'admin_post_edera_preventivo_salva',
	function () {
		edera_preventivo_permesso( 'edera_preventivo_salva' );
		$in = isset( $_POST['regole'] ) ? wp_unslash( $_POST['regole'] ) : array(); // phpcs:ignore WordPress.Security.ValidatedSanitizedInput.InputNotSanitized -- pulito in edera_preventivo_controlla()
		$v  = edera_preventivo_controlla( $in );
		if ( $v['errori'] ) {
			edera_preventivo_torna( __( 'Regole non salvate: correggi gli errori qui sotto.', 'edera-preventivo' ), $v['errori'], $v['regole'] );
		}
		update_option( EDERA_PREVENTIVO_OPZIONE, $v['regole'], false );
		edera_preventivo_torna( __( 'Regole salvate. Il calcolatore sul sito le usa già.', 'edera-preventivo' ) );
	}
);

add_action(
	'admin_post_edera_preventivo_esporta',
	function () {
		edera_preventivo_permesso( 'edera_preventivo_esporta' );
		nocache_headers();
		header( 'Content-Type: application/json; charset=utf-8' );
		header( 'Content-Disposition: attachment; filename="edera-preventivo-' . wp_date( 'Y-m-d' ) . '.json"' );
		echo wp_json_encode( edera_preventivo_regole(), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
		exit;
	}
);

add_action(
	'admin_post_edera_preventivo_importa',
	function () {
		edera_preventivo_permesso( 'edera_preventivo_importa' );
		$f = isset( $_FILES['file'] ) ? $_FILES['file'] : null; // phpcs:ignore WordPress.Security.ValidatedSanitizedInput
		if ( ! $f || ! empty( $f['error'] ) || empty( $f['tmp_name'] ) || ! is_uploaded_file( $f['tmp_name'] ) || $f['size'] > 500000 ) {
			edera_preventivo_torna( __( 'File non ricevuto: scegli il file JSON esportato da questa pagina (al massimo 500 KB).', 'edera-preventivo' ) );
		}
		$dati = json_decode( (string) file_get_contents( $f['tmp_name'] ), true ); // phpcs:ignore WordPress.WP.AlternativeFunctions.file_get_contents_file_get_contents
		if ( ! is_array( $dati ) || empty( $dati['spazi'] ) ) {
			edera_preventivo_torna( __( 'Il file non contiene regole del preventivo.', 'edera-preventivo' ) );
		}
		$v = edera_preventivo_controlla( $dati );
		if ( $v['errori'] ) {
			edera_preventivo_torna( __( 'Regole del file non importate: ci sono errori.', 'edera-preventivo' ), $v['errori'] );
		}
		update_option( EDERA_PREVENTIVO_OPZIONE, $v['regole'], false );
		edera_preventivo_torna( __( 'Regole importate dal file.', 'edera-preventivo' ) );
	}
);

add_action(
	'admin_post_edera_preventivo_ripristina',
	function () {
		edera_preventivo_permesso( 'edera_preventivo_ripristina' );
		update_option( EDERA_PREVENTIVO_OPZIONE, edera_preventivo_dal_tema(), false );
		edera_preventivo_torna( __( 'Valori iniziali ripristinati: sono le regole del calcolatore del sito originale.', 'edera-preventivo' ) );
	}
);

/**
 * Nome di un campo: regole[sezione][...].
 *
 * @param string ...$parti Parti del nome.
 * @return string
 */
function edera_preventivo_nome( ...$parti ) {
	return 'regole[' . implode( '][', $parti ) . ']';
}

/**
 * Un campo di testo o numero con etichetta.
 *
 * @param string $etichetta Etichetta.
 * @param string $nome      Nome.
 * @param mixed  $valore    Valore.
 * @param string $tipo      text | number | email | date.
 * @param string $extra     Attributi in piu'.
 */
function edera_preventivo_campo( $etichetta, $nome, $valore, $tipo = 'text', $extra = '' ) {
	printf(
		'<label class="edp-campo"><span>%1$s</span><input type="%2$s" name="%3$s" value="%4$s"%5$s></label>',
		esc_html( $etichetta ),
		esc_attr( $tipo ),
		esc_attr( $nome ),
		esc_attr( is_bool( $valore ) ? (int) $valore : (string) $valore ),
		$extra // phpcs:ignore WordPress.Security.EscapeOutput -- attributi fissi scritti qui sotto
	);
}

/**
 * Una casella si/no (con il valore 0 nascosto, cosi' arriva anche quando non e' spuntata).
 *
 * @param string $etichetta Etichetta.
 * @param string $nome      Nome.
 * @param bool   $valore    Spuntata?
 */
function edera_preventivo_si( $etichetta, $nome, $valore ) {
	printf(
		'<label class="edp-si"><input type="hidden" name="%1$s" value="0"><input type="checkbox" name="%1$s" value="1"%2$s> %3$s</label>',
		esc_attr( $nome ),
		checked( (bool) $valore, true, false ),
		esc_html( $etichetta )
	);
}

/**
 * Un menu a tendina.
 *
 * @param string $etichetta Etichetta.
 * @param string $nome      Nome.
 * @param string $valore    Valore scelto.
 * @param array  $scelte    valore => testo.
 */
function edera_preventivo_scelta( $etichetta, $nome, $valore, $scelte ) {
	echo '<label class="edp-campo"><span>' . esc_html( $etichetta ) . '</span><select name="' . esc_attr( $nome ) . '">';
	foreach ( $scelte as $k => $t ) {
		echo '<option value="' . esc_attr( $k ) . '"' . selected( (string) $valore, (string) $k, false ) . '>' . esc_html( $t ) . '</option>';
	}
	echo '</select></label>';
}

/**
 * Caselle multiple (giorni della settimana, mesi).
 *
 * @param string $etichetta Etichetta.
 * @param string $nome      Nome (senza []).
 * @param array  $valori    Valori scelti.
 * @param array  $scelte    valore => testo.
 */
function edera_preventivo_multi( $etichetta, $nome, $valori, $scelte ) {
	echo '<fieldset class="edp-multi"><legend>' . esc_html( $etichetta ) . '</legend>';
	foreach ( $scelte as $k => $t ) {
		printf(
			'<label><input type="checkbox" name="%1$s[]" value="%2$s"%3$s> %4$s</label>',
			esc_attr( $nome ),
			esc_attr( $k ),
			checked( in_array( (int) $k, array_map( 'intval', (array) $valori ), true ), true, false ),
			esc_html( $t )
		);
	}
	echo '</fieldset>';
}

/**
 * Comandi di una riga ripetibile.
 */
function edera_preventivo_comandi() {
	echo '<div class="edp-comandi"><button type="button" class="button edp-su" aria-label="' . esc_attr__( 'Sposta su', 'edera-preventivo' ) . '">↑</button>'
		. '<button type="button" class="button edp-giu" aria-label="' . esc_attr__( 'Sposta giù', 'edera-preventivo' ) . '">↓</button>'
		. '<button type="button" class="button edp-togli">' . esc_html__( 'Togli', 'edera-preventivo' ) . '</button></div>';
}

/**
 * Giorni della settimana e mesi.
 *
 * @return array
 */
function edera_preventivo_giorni() {
	return array( 1 => __( 'lun', 'edera-preventivo' ), __( 'mar', 'edera-preventivo' ), __( 'mer', 'edera-preventivo' ), __( 'gio', 'edera-preventivo' ), __( 'ven', 'edera-preventivo' ), __( 'sab', 'edera-preventivo' ), __( 'dom', 'edera-preventivo' ) );
}

/**
 * Mesi.
 *
 * @return array
 */
function edera_preventivo_mesi() {
	return array( 1 => __( 'gen', 'edera-preventivo' ), __( 'feb', 'edera-preventivo' ), __( 'mar', 'edera-preventivo' ), __( 'apr', 'edera-preventivo' ), __( 'mag', 'edera-preventivo' ), __( 'giu', 'edera-preventivo' ), __( 'lug', 'edera-preventivo' ), __( 'ago', 'edera-preventivo' ), __( 'set', 'edera-preventivo' ), __( 'ott', 'edera-preventivo' ), __( 'nov', 'edera-preventivo' ), __( 'dic', 'edera-preventivo' ) );
}

/**
 * Le righe ripetibili: una funzione per tipo, usata per le righe salvate e per il modello delle righe nuove.
 *
 * @param string $tipo spazio | data | periodo | tariffa | servizio.
 * @param mixed  $i    Indice (o __i__ nel modello).
 * @param array  $v    Valori.
 */
function edera_preventivo_riga( $tipo, $i, $v ) {
	echo '<div class="edp-riga">';
	if ( 'spazio' === $tipo ) {
		$n = function ( $k ) use ( $i ) {
			return edera_preventivo_nome( 'spazi', $i, $k );
		};
		echo '<div class="edp-griglia">';
		edera_preventivo_campo( __( 'Nome', 'edera-preventivo' ), $n( 'nome' ), $v['nome'] );
		edera_preventivo_campo( __( 'Capienza massima (persone)', 'edera-preventivo' ), $n( 'persone' ), $v['persone'], 'number', ' min="1" step="1"' );
		edera_preventivo_scelta(
			__( 'Prezzo', 'edera-preventivo' ),
			$n( 'modo' ),
			$v['modo'],
			array(
				'persone' => __( 'base + persone in più', 'edera-preventivo' ),
				'fisso'   => __( 'fisso per durata (come la piscina)', 'edera-preventivo' ),
			)
		);
		edera_preventivo_campo( __( 'Prezzo base (€)', 'edera-preventivo' ), $n( 'base' ), $v['base'], 'number', ' min="0" step="0.01"' );
		edera_preventivo_campo( __( 'Persone comprese nel base', 'edera-preventivo' ), $n( 'incluse' ), $v['incluse'], 'number', ' min="0" step="1"' );
		edera_preventivo_campo( __( 'Per ogni persona in più (€)', 'edera-preventivo' ), $n( 'a_persona' ), $v['a_persona'], 'number', ' min="0" step="0.01"' );
		edera_preventivo_campo( __( 'Fisso, giornata intera (€)', 'edera-preventivo' ), $n( 'prezzo_intera' ), $v['prezzo_intera'], 'number', ' min="0" step="0.01"' );
		edera_preventivo_campo( __( 'Fisso, mezza giornata (€)', 'edera-preventivo' ), $n( 'prezzo_mezza' ), $v['prezzo_mezza'], 'number', ' min="0" step="0.01"' );
		edera_preventivo_campo( __( 'Nota (facoltativa, sotto la capienza)', 'edera-preventivo' ), $n( 'nota' ), $v['nota'] );
		echo '</div><div class="edp-caselle">';
		edera_preventivo_si( __( 'Attivo', 'edera-preventivo' ), $n( 'attivo' ), $v['attivo'] );
		edera_preventivo_si( __( 'Già scelto quando si apre la pagina', 'edera-preventivo' ), $n( 'scelto' ), $v['scelto'] );
		edera_preventivo_si( __( 'Ammette la mezza giornata', 'edera-preventivo' ), $n( 'mezza' ), $v['mezza'] );
		echo '<input type="hidden" name="' . esc_attr( $n( 'chiave' ) ) . '" value="' . esc_attr( $v['chiave'] ) . '">';
		echo '</div>';
	} elseif ( 'data' === $tipo ) {
		echo '<div class="edp-griglia">';
		edera_preventivo_campo( __( 'Data', 'edera-preventivo' ), edera_preventivo_nome( 'calendario', 'date_escluse', $i, 'data' ), $v['data'], 'date' );
		edera_preventivo_campo( __( 'Perché (solo per voi)', 'edera-preventivo' ), edera_preventivo_nome( 'calendario', 'date_escluse', $i, 'nota' ), $v['nota'] );
		echo '</div>';
	} elseif ( 'periodo' === $tipo ) {
		echo '<div class="edp-griglia">';
		edera_preventivo_campo( __( 'Dal', 'edera-preventivo' ), edera_preventivo_nome( 'calendario', 'periodi_chiusi', $i, 'dal' ), $v['dal'], 'date' );
		edera_preventivo_campo( __( 'Al (compreso)', 'edera-preventivo' ), edera_preventivo_nome( 'calendario', 'periodi_chiusi', $i, 'al' ), $v['al'], 'date' );
		edera_preventivo_campo( __( 'Perché (solo per voi)', 'edera-preventivo' ), edera_preventivo_nome( 'calendario', 'periodi_chiusi', $i, 'nota' ), $v['nota'] );
		echo '</div>';
	} elseif ( 'tariffa' === $tipo ) {
		$n = function ( $k ) use ( $i ) {
			return edera_preventivo_nome( 'tariffe', $i, $k );
		};
		echo '<div class="edp-griglia">';
		edera_preventivo_campo( __( 'Nome (compare nella stima)', 'edera-preventivo' ), $n( 'nome' ), $v['nome'] );
		edera_preventivo_scelta(
			__( 'Quando vale', 'edera-preventivo' ),
			$n( 'tipo' ),
			$v['tipo'],
			array(
				'mesi'    => __( 'in certi mesi', 'edera-preventivo' ),
				'giorni'  => __( 'in certi giorni della settimana', 'edera-preventivo' ),
				'periodo' => __( 'in un periodo (dal ... al ...)', 'edera-preventivo' ),
			)
		);
		edera_preventivo_scelta(
			__( 'Come', 'edera-preventivo' ),
			$n( 'modo' ),
			$v['modo'],
			array(
				'importo'     => __( 'importo fisso (€)', 'edera-preventivo' ),
				'percentuale' => __( 'percentuale (%)', 'edera-preventivo' ),
			)
		);
		edera_preventivo_campo( __( 'Valore', 'edera-preventivo' ), $n( 'valore' ), $v['valore'], 'number', ' min="0" step="0.01"' );
		edera_preventivo_scelta(
			__( 'Su che cosa', 'edera-preventivo' ),
			$n( 'applica' ),
			$v['applica'],
			array(
				'primo_spazio' => __( 'sul primo spazio scelto', 'edera-preventivo' ),
				'ogni_spazio'  => __( 'su ogni spazio scelto', 'edera-preventivo' ),
				'totale'       => __( 'sul totale degli spazi (riga a parte)', 'edera-preventivo' ),
			)
		);
		edera_preventivo_campo( __( 'Dal (per "periodo")', 'edera-preventivo' ), $n( 'dal' ), $v['dal'], 'date' );
		edera_preventivo_campo( __( 'Al (per "periodo")', 'edera-preventivo' ), $n( 'al' ), $v['al'], 'date' );
		echo '</div>';
		edera_preventivo_multi( __( 'Mesi (per "in certi mesi")', 'edera-preventivo' ), $n( 'mesi' ), $v['mesi'], edera_preventivo_mesi() );
		edera_preventivo_multi( __( 'Giorni (per "giorni della settimana")', 'edera-preventivo' ), $n( 'giorni' ), $v['giorni'], edera_preventivo_giorni() );
		echo '<div class="edp-caselle">';
		edera_preventivo_si( __( 'Attiva', 'edera-preventivo' ), $n( 'attiva' ), $v['attiva'] );
		echo '</div>';
	} elseif ( 'servizio' === $tipo ) {
		$n = function ( $k ) use ( $i ) {
			return edera_preventivo_nome( 'servizi', $i, $k );
		};
		echo '<div class="edp-griglia">';
		edera_preventivo_campo( __( 'Nome', 'edera-preventivo' ), $n( 'nome' ), $v['nome'] );
		edera_preventivo_campo( __( 'Prezzo (€)', 'edera-preventivo' ), $n( 'prezzo' ), $v['prezzo'], 'number', ' min="0" step="0.01"' );
		edera_preventivo_scelta(
			__( 'Come', 'edera-preventivo' ),
			$n( 'modo' ),
			$v['modo'],
			array(
				'fisso'   => __( 'prezzo fisso', 'edera-preventivo' ),
				'persona' => __( 'a persona', 'edera-preventivo' ),
			)
		);
		edera_preventivo_campo( __( 'Nota (facoltativa)', 'edera-preventivo' ), $n( 'nota' ), $v['nota'] );
		echo '</div><div class="edp-caselle">';
		edera_preventivo_si( __( 'Attivo (compare nel preventivo)', 'edera-preventivo' ), $n( 'attivo' ), $v['attivo'] );
		echo '</div>';
	}
	edera_preventivo_comandi();
	echo '</div>';
}

/**
 * Un elenco di righe ripetibili con il suo modello e il bottone "Aggiungi".
 *
 * @param string $tipo   Tipo di riga.
 * @param array  $righe  Righe salvate.
 * @param array  $vuota  Valori di una riga nuova.
 * @param string $testo  Testo del bottone.
 */
function edera_preventivo_righe( $tipo, $righe, $vuota, $testo ) {
	echo '<div class="edp-righe" data-tipo="' . esc_attr( $tipo ) . '">';
	foreach ( array_values( $righe ) as $i => $v ) {
		edera_preventivo_riga( $tipo, $i, array_merge( $vuota, $v ) );
	}
	echo '</div><template class="edp-modello" data-tipo="' . esc_attr( $tipo ) . '">';
	edera_preventivo_riga( $tipo, '__i__', $vuota );
	echo '</template><p><button type="button" class="button edp-aggiungi" data-tipo="' . esc_attr( $tipo ) . '">' . esc_html( $testo ) . '</button></p>';
}

/**
 * La pagina.
 */
function edera_preventivo_pagina() {
	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}
	$esito = get_transient( 'edera_preventivo_esito_' . get_current_user_id() );
	delete_transient( 'edera_preventivo_esito_' . get_current_user_id() );
	$r = ( is_array( $esito ) && ! empty( $esito['bozza'] ) ) ? $esito['bozza'] : edera_preventivo_regole();
	$c = $r['calendario'];
	$s = $r['sconti'];
	$t = $r['testi'];
	?>
	<div class="wrap edp">
		<h1><?php esc_html_e( 'Preventivo flash', 'edera-preventivo' ); ?></h1>
		<p class="edp-intro"><?php esc_html_e( 'Qui si cambiano prezzi e regole del calcolatore sul sito (shortcode [edera_preventivo]). I conti li fa il browser di chi compila: il sito non riceve e non salva le richieste, che partono come mail dal programma di posta del cliente.', 'edera-preventivo' ); ?></p>
		<?php if ( is_array( $esito ) && ! empty( $esito['msg'] ) ) : ?>
			<div class="notice <?php echo $esito['errori'] ? 'notice-error' : 'notice-success'; ?>"><p><strong><?php echo esc_html( $esito['msg'] ); ?></strong></p>
			<?php if ( $esito['errori'] ) : ?>
				<ul class="edp-errori">
				<?php foreach ( $esito['errori'] as $e ) : ?>
					<li><?php echo esc_html( $e ); ?></li>
				<?php endforeach; ?>
				</ul>
			<?php endif; ?>
			</div>
		<?php endif; ?>
		<nav class="edp-indice" aria-label="<?php esc_attr_e( 'Sezioni', 'edera-preventivo' ); ?>">
			<a href="#edp-spazi"><?php esc_html_e( 'Spazi', 'edera-preventivo' ); ?></a>
			<a href="#edp-durate"><?php esc_html_e( 'Durate', 'edera-preventivo' ); ?></a>
			<a href="#edp-calendario"><?php esc_html_e( 'Calendario', 'edera-preventivo' ); ?></a>
			<a href="#edp-tariffe"><?php esc_html_e( 'Tariffe e supplementi', 'edera-preventivo' ); ?></a>
			<a href="#edp-sconti"><?php esc_html_e( 'Sconti e minimi', 'edera-preventivo' ); ?></a>
			<a href="#edp-servizi"><?php esc_html_e( 'Servizi aggiuntivi', 'edera-preventivo' ); ?></a>
			<a href="#edp-testi"><?php esc_html_e( 'Testi e invio', 'edera-preventivo' ); ?></a>
			<a href="#edp-prova"><?php esc_html_e( 'Prova', 'edera-preventivo' ); ?></a>
			<a href="#edp-copia"><?php esc_html_e( 'Copia delle regole', 'edera-preventivo' ); ?></a>
		</nav>

		<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>" class="edp-modulo">
			<?php wp_nonce_field( 'edera_preventivo_salva' ); ?>
			<input type="hidden" name="action" value="edera_preventivo_salva">

			<section class="edp-sezione" id="edp-spazi">
				<h2><?php esc_html_e( 'Spazi', 'edera-preventivo' ); ?></h2>
				<p class="description"><?php esc_html_e( 'Prezzo "base + persone in più": prezzo base fino alle persone comprese, poi il prezzo per ogni persona in più, fino alla capienza. Prezzo "fisso per durata": un prezzo per la giornata intera e uno per la mezza. L’ordine è quello del calcolatore; il primo spazio scelto è quello su cui va la tariffa "sul primo spazio".', 'edera-preventivo' ); ?></p>
				<?php
				edera_preventivo_righe(
					'spazio',
					$r['spazi'],
					array( 'chiave' => '', 'nome' => '', 'persone' => 10, 'modo' => 'persone', 'base' => 0, 'incluse' => 0, 'a_persona' => 0, 'prezzo_intera' => 0, 'prezzo_mezza' => 0, 'mezza' => false, 'attivo' => true, 'scelto' => false, 'nota' => '' ),
					__( 'Aggiungi uno spazio', 'edera-preventivo' )
				);
				?>
				<?php edera_preventivo_campo( __( 'Partecipanti usati per la stima finché il campo è vuoto', 'edera-preventivo' ), edera_preventivo_nome( 'generali', 'partecipanti_esempio' ), $r['generali']['partecipanti_esempio'], 'number', ' min="1" step="1"' ); ?>
			</section>

			<section class="edp-sezione" id="edp-durate">
				<h2><?php esc_html_e( 'Durate', 'edera-preventivo' ); ?></h2>
				<div class="edp-griglia">
					<?php
					edera_preventivo_campo( __( 'Etichetta della giornata intera', 'edera-preventivo' ), edera_preventivo_nome( 'durate', 'intera' ), $r['durate']['intera'] );
					edera_preventivo_campo( __( 'Etichetta della mezza giornata', 'edera-preventivo' ), edera_preventivo_nome( 'durate', 'mezza' ), $r['durate']['mezza'] );
					edera_preventivo_scelta(
						__( 'La mezza giornata si può scegliere se', 'edera-preventivo' ),
						edera_preventivo_nome( 'durate', 'regola_mezza' ),
						$r['durate']['regola_mezza'],
						array(
							'almeno_uno' => __( 'almeno uno degli spazi scelti la ammette', 'edera-preventivo' ),
							'tutti'      => __( 'tutti gli spazi scelti la ammettono', 'edera-preventivo' ),
						)
					);
					edera_preventivo_campo( __( 'Nota quando la mezza giornata si può scegliere', 'edera-preventivo' ), edera_preventivo_nome( 'durate', 'nota_mezza_si' ), $r['durate']['nota_mezza_si'] );
					edera_preventivo_campo( __( 'Nota quando non si può', 'edera-preventivo' ), edera_preventivo_nome( 'durate', 'nota_mezza_no' ), $r['durate']['nota_mezza_no'] );
					?>
				</div>
				<div class="edp-caselle"><?php edera_preventivo_si( __( 'Mezza giornata attiva', 'edera-preventivo' ), edera_preventivo_nome( 'durate', 'mezza_attiva' ), $r['durate']['mezza_attiva'] ); ?></div>
				<p class="description"><?php esc_html_e( 'Quali spazi ammettono la mezza giornata si sceglie in ogni spazio. Gli spazi con prezzo "base + persone in più" costano uguale anche a mezza giornata.', 'edera-preventivo' ); ?></p>
			</section>

			<section class="edp-sezione" id="edp-calendario">
				<h2><?php esc_html_e( 'Calendario e giorni esclusi', 'edera-preventivo' ); ?></h2>
				<p class="description"><?php esc_html_e( 'Con almeno una di queste regole, nel calcolatore compare il campo "Data dell’evento" con un calendario che non lascia scegliere i giorni esclusi, i giorni chiusi, quelli prima del preavviso e quelli oltre la finestra. Senza regole resta il campo "Data indicativa" di oggi.', 'edera-preventivo' ); ?></p>
				<h3><?php esc_html_e( 'Date escluse (festività, giorni già prenotati)', 'edera-preventivo' ); ?></h3>
				<?php edera_preventivo_righe( 'data', $c['date_escluse'], array( 'data' => '', 'nota' => '' ), __( 'Aggiungi una data', 'edera-preventivo' ) ); ?>
				<h3><?php esc_html_e( 'Periodi di chiusura', 'edera-preventivo' ); ?></h3>
				<?php edera_preventivo_righe( 'periodo', $c['periodi_chiusi'], array( 'dal' => '', 'al' => '', 'nota' => '' ), __( 'Aggiungi un periodo', 'edera-preventivo' ) ); ?>
				<?php edera_preventivo_multi( __( 'Giorni della settimana chiusi', 'edera-preventivo' ), edera_preventivo_nome( 'calendario', 'giorni_chiusi' ), $c['giorni_chiusi'], edera_preventivo_giorni() ); ?>
				<div class="edp-griglia">
					<?php
					edera_preventivo_campo( __( 'Preavviso minimo (giorni, 0 = da oggi)', 'edera-preventivo' ), edera_preventivo_nome( 'calendario', 'preavviso' ), $c['preavviso'], 'number', ' min="0" max="365" step="1"' );
					edera_preventivo_campo( __( 'Finestra massima (mesi da oggi, 0 = nessun limite)', 'edera-preventivo' ), edera_preventivo_nome( 'calendario', 'finestra_mesi' ), $c['finestra_mesi'], 'number', ' min="0" max="60" step="1"' );
					?>
				</div>
			</section>

			<section class="edp-sezione" id="edp-tariffe">
				<h2><?php esc_html_e( 'Tariffe e supplementi', 'edera-preventivo' ); ?></h2>
				<p class="description"><?php esc_html_e( 'Valgono per la data scelta nel calcolatore (senza data, nessun supplemento). Oggi c’è la tariffa stagionale: 125 € in più sul primo spazio scelto, da ottobre a marzo.', 'edera-preventivo' ); ?></p>
				<?php
				edera_preventivo_righe(
					'tariffa',
					$r['tariffe'],
					array( 'nome' => '', 'attiva' => true, 'tipo' => 'giorni', 'mesi' => array(), 'giorni' => array(), 'dal' => '', 'al' => '', 'modo' => 'percentuale', 'valore' => 0, 'applica' => 'totale' ),
					__( 'Aggiungi una tariffa o un supplemento', 'edera-preventivo' )
				);
				?>
			</section>

			<section class="edp-sezione" id="edp-sconti">
				<h2><?php esc_html_e( 'Sconti e minimi', 'edera-preventivo' ); ?></h2>
				<h3><?php esc_html_e( 'Sconto per più spazi insieme', 'edera-preventivo' ); ?></h3>
				<div class="edp-griglia">
					<?php
					edera_preventivo_campo( __( 'Nome (compare nella stima)', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'piu_spazi', 'nome' ), $s['piu_spazi']['nome'] );
					edera_preventivo_campo( __( 'Da quanti spazi', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'piu_spazi', 'da' ), $s['piu_spazi']['da'], 'number', ' min="2" step="1"' );
					edera_preventivo_scelta( __( 'Come', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'piu_spazi', 'modo' ), $s['piu_spazi']['modo'], array( 'percentuale' => __( 'percentuale (%)', 'edera-preventivo' ), 'importo' => __( 'importo fisso (€)', 'edera-preventivo' ) ) );
					edera_preventivo_campo( __( 'Valore', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'piu_spazi', 'valore' ), $s['piu_spazi']['valore'], 'number', ' min="0" step="0.01"' );
					?>
				</div>
				<div class="edp-caselle"><?php edera_preventivo_si( __( 'Attivo', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'piu_spazi', 'attivo' ), $s['piu_spazi']['attivo'] ); ?></div>
				<h3><?php esc_html_e( 'Sconto oltre un numero di partecipanti', 'edera-preventivo' ); ?></h3>
				<div class="edp-griglia">
					<?php
					edera_preventivo_campo( __( 'Nome (compare nella stima)', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'persone', 'nome' ), $s['persone']['nome'] );
					edera_preventivo_campo( __( 'Oltre quante persone', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'persone', 'oltre' ), $s['persone']['oltre'], 'number', ' min="1" step="1"' );
					edera_preventivo_scelta( __( 'Come', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'persone', 'modo' ), $s['persone']['modo'], array( 'percentuale' => __( 'percentuale (%)', 'edera-preventivo' ), 'importo' => __( 'importo fisso (€)', 'edera-preventivo' ) ) );
					edera_preventivo_campo( __( 'Valore', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'persone', 'valore' ), $s['persone']['valore'], 'number', ' min="0" step="0.01"' );
					?>
				</div>
				<div class="edp-caselle"><?php edera_preventivo_si( __( 'Attivo', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'persone', 'attivo' ), $s['persone']['attivo'] ); ?></div>
				<h3><?php esc_html_e( 'Minimi e arrotondamento', 'edera-preventivo' ); ?></h3>
				<div class="edp-griglia">
					<?php
					edera_preventivo_campo( __( 'Minimo di partecipanti (0 = nessuno)', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'minimo_persone' ), $s['minimo_persone'], 'number', ' min="0" step="1"' );
					edera_preventivo_campo( __( 'Spesa minima (€, 0 = nessuna)', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'spesa_minima' ), $s['spesa_minima'], 'number', ' min="0" step="0.01"' );
					edera_preventivo_scelta(
						__( 'Arrotondamento del totale', 'edera-preventivo' ),
						edera_preventivo_nome( 'sconti', 'arrotonda', 'modo' ),
						$s['arrotonda']['modo'],
						array(
							'nessuno' => __( 'nessuno', 'edera-preventivo' ),
							'eccesso' => __( 'per eccesso', 'edera-preventivo' ),
							'vicino'  => __( 'al più vicino', 'edera-preventivo' ),
							'difetto' => __( 'per difetto', 'edera-preventivo' ),
						)
					);
					edera_preventivo_campo( __( 'Arrotonda a multipli di (€)', 'edera-preventivo' ), edera_preventivo_nome( 'sconti', 'arrotonda', 'passo' ), $s['arrotonda']['passo'], 'number', ' min="0" step="0.01"' );
					?>
				</div>
			</section>

			<section class="edp-sezione" id="edp-servizi">
				<h2><?php esc_html_e( 'Servizi aggiuntivi', 'edera-preventivo' ); ?></h2>
				<p class="description"><?php esc_html_e( 'I servizi attivi diventano caselle da spuntare nel calcolatore, con il prezzo nella stima. Oggi l’elenco è vuoto: i servizi sono nel PDF.', 'edera-preventivo' ); ?></p>
				<?php edera_preventivo_righe( 'servizio', $r['servizi'], array( 'nome' => '', 'prezzo' => 0, 'modo' => 'fisso', 'attivo' => true, 'nota' => '' ), __( 'Aggiungi un servizio', 'edera-preventivo' ) ); ?>
			</section>

			<section class="edp-sezione" id="edp-testi">
				<h2><?php esc_html_e( 'Testi e invio', 'edera-preventivo' ); ?></h2>
				<div class="edp-griglia">
					<?php
					edera_preventivo_campo( __( 'Email che riceve la richiesta', 'edera-preventivo' ), edera_preventivo_nome( 'testi', 'email' ), $t['email'], 'email' );
					edera_preventivo_campo( __( 'Oggetto della mail', 'edera-preventivo' ), edera_preventivo_nome( 'testi', 'oggetto' ), $t['oggetto'] );
					edera_preventivo_scelta(
						__( 'Nota sotto il prezzo', 'edera-preventivo' ),
						edera_preventivo_nome( 'testi', 'iva' ),
						$t['iva'],
						array(
							'personalizzata' => __( 'il testo qui accanto', 'edera-preventivo' ),
							'inclusa'        => __( 'IVA inclusa', 'edera-preventivo' ),
							'esclusa'        => __( 'IVA esclusa', 'edera-preventivo' ),
							'nessuna'        => __( 'nessuna nota', 'edera-preventivo' ),
						)
					);
					edera_preventivo_campo( __( 'Testo della nota sotto il prezzo', 'edera-preventivo' ), edera_preventivo_nome( 'testi', 'nota_prezzo' ), $t['nota_prezzo'] );
					edera_preventivo_campo( __( 'Messaggio per una data non disponibile', 'edera-preventivo' ), edera_preventivo_nome( 'testi', 'msg_data' ), $t['msg_data'] );
					edera_preventivo_campo( __( 'Messaggio oltre la capienza ({max} = massimo)', 'edera-preventivo' ), edera_preventivo_nome( 'testi', 'msg_capienza' ), $t['msg_capienza'] );
					?>
				</div>
				<label class="edp-campo edp-largo"><span><?php esc_html_e( 'Testo della mail', 'edera-preventivo' ); ?></span><textarea name="<?php echo esc_attr( edera_preventivo_nome( 'testi', 'corpo' ) ); ?>" rows="13"><?php echo esc_textarea( $t['corpo'] ); ?></textarea></label>
				<p class="description"><?php esc_html_e( 'Segnaposti: {azienda} {email} {telefono} {tipo} {spazi} {data} {persone} {durata} {totale} {servizi} {servizi_riga} (la riga "Servizi aggiuntivi: ..." solo se ce ne sono) {dettaglio} (tutte le voci della stima).', 'edera-preventivo' ); ?></p>
				<label class="edp-campo edp-largo"><span><?php esc_html_e( 'Avvertenza sotto la stima', 'edera-preventivo' ); ?></span><textarea name="<?php echo esc_attr( edera_preventivo_nome( 'testi', 'avvertenza' ) ); ?>" rows="3"><?php echo esc_textarea( $t['avvertenza'] ); ?></textarea></label>
			</section>

			<p class="edp-salva"><?php submit_button( __( 'Salva le regole', 'edera-preventivo' ), 'primary', 'edp_salva', false ); ?></p>
		</form>

		<section class="edp-sezione" id="edp-prova">
			<h2><?php esc_html_e( 'Prova', 'edera-preventivo' ); ?></h2>
			<p class="description"><?php esc_html_e( 'Un calcolatore con le regole salvate (dopo una modifica, prima salva): dà gli stessi numeri del sito.', 'edera-preventivo' ); ?></p>
			<div class="edp-prova" id="edp-prova-box"></div>
		</section>

		<section class="edp-sezione" id="edp-copia">
			<h2><?php esc_html_e( 'Copia delle regole', 'edera-preventivo' ); ?></h2>
			<p><a class="button" href="<?php echo esc_url( wp_nonce_url( admin_url( 'admin-post.php?action=edera_preventivo_esporta' ), 'edera_preventivo_esporta' ) ); ?>"><?php esc_html_e( 'Esporta le regole (file JSON)', 'edera-preventivo' ); ?></a></p>
			<form method="post" enctype="multipart/form-data" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>" class="edp-riga-azione">
				<?php wp_nonce_field( 'edera_preventivo_importa' ); ?>
				<input type="hidden" name="action" value="edera_preventivo_importa">
				<label><?php esc_html_e( 'Importa da un file esportato:', 'edera-preventivo' ); ?> <input type="file" name="file" accept="application/json,.json" required></label>
				<?php submit_button( __( 'Importa', 'edera-preventivo' ), 'secondary', 'edp_importa', false ); ?>
			</form>
			<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>" class="edp-riga-azione" onsubmit="return confirm('<?php echo esc_js( __( 'Tornare ai valori iniziali? Le regole di adesso si perdono (esportale prima, se vuoi tenerle).', 'edera-preventivo' ) ); ?>');">
				<?php wp_nonce_field( 'edera_preventivo_ripristina' ); ?>
				<input type="hidden" name="action" value="edera_preventivo_ripristina">
				<?php submit_button( __( 'Ripristina i valori iniziali', 'edera-preventivo' ), 'delete', 'edp_ripristina', false ); ?>
			</form>
		</section>
	</div>
	<?php
}
