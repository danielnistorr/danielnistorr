<?php
/**
 * Preventivo flash: prezzi e regole del calcolatore.
 *
 * Questo e' l'unico file da cambiare per aggiornare i prezzi. Si apre da
 * Aspetto > Editor dei file del tema > config/preventivo.php, oppure via FTP in
 * wp-content/themes/edera/config/preventivo.php.
 *
 * Regole (le stesse del sito originale):
 * - Si sceglie uno o piu' spazi. Il prezzo di ogni spazio e':
 *     base + (partecipanti - incluse) x a_persona
 *   dove i partecipanti contati per quello spazio non superano la sua capienza ("persone").
 *   Esempio, Rustico con 30 persone: 400 + (30 - 20) x 15 = 550 euro.
 * - Uno spazio con "mezza" e "intera" ha un prezzo fisso per durata (oggi la piscina):
 *   la mezza giornata si puo' scegliere solo se fra gli spazi scelti ce n'e' uno cosi'.
 * - I partecipanti non possono superare la somma delle capienze degli spazi scelti.
 *   Se il campo e' vuoto, la stima usa "partecipanti_esempio" (scritto "esempio" nella stima).
 * - Con una data nei mesi di "stagione" il primo spazio scelto (nell'ordine qui sotto) costa
 *   "supplemento" euro in piu'.
 *
 * Scrivere i numeri senza virgolette, con il punto per i decimali (2.5, non 2,5).
 * Dopo una modifica basta ricaricare la pagina: non serve rifare l'installazione.
 *
 * @package edera
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

return array(

	// A chi arriva la richiesta (il bottone "Invia per email" apre il programma di posta di chi scrive).
	'email'                => 'edera@ederacountry.it',

	// Gli spazi, nell'ordine in cui compaiono. La chiave a sinistra (rustico, serra...) non va cambiata.
	'spazi'                => array(
		'rustico' => array(
			'nome'      => 'Rustico',
			'persone'   => 50,     // capienza massima
			'base'      => 400,    // euro, fino a "incluse" persone
			'incluse'   => 20,     // persone comprese nel prezzo base
			'a_persona' => 15,     // euro per ogni persona oltre le incluse
			'scelto'    => true,   // gia' selezionato quando si apre la pagina
		),
		'serra'   => array(
			'nome'      => 'Serra',
			'persone'   => 70,
			'base'      => 250,
			'incluse'   => 20,
			'a_persona' => 5,
		),
		'piscina' => array(
			'nome'    => 'Piscina',
			'persone' => 30,
			'intera'  => 400,      // euro, giornata intera
			'mezza'   => 300,      // euro, mezza giornata
		),
		'esterno' => array(
			'nome'      => 'Spazio esterno',
			'persone'   => 120,
			'base'      => 350,
			'incluse'   => 20,
			'a_persona' => 2.5,
		),
	),

	// Partecipanti usati per la stima finche' il campo e' vuoto.
	'partecipanti_esempio' => 20,

	// Tariffa stagionale: dal 1 ottobre al 31 marzo (mesi da 1 a 12).
	'stagione'             => array(
		'mesi'        => array( 10, 11, 12, 1, 2, 3 ),
		'supplemento' => 125,  // euro, sul primo spazio scelto
	),

	// Testi che cambiano con la durata.
	'nota_mezza_si'        => 'Per la piscina puoi scegliere mezza giornata o giornata intera.',
	'nota_mezza_no'        => 'Per gli spazi selezionati è prevista la giornata intera.',

	// Avvertenza sotto la stima.
	'avvertenza'           => 'Il prezzo indicato è orientativo e non definitivo: il preventivo finale può variare in base alla tipologia di evento, ai servizi richiesti e alle esigenze organizzative. Valori da confermare con la struttura.',
);
