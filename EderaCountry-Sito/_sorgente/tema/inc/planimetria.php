<?php
/**
 * Planimetria: shortcode [edera_planimetria].
 *
 * La foto dall'alto con i pallini numerati, l'elenco degli spazi accanto (sotto, sul telefono) e la galleria
 * del Rustico. Pallini, testi e foto stanno in config/planimetria.php; le foto sono nella libreria media.
 * Il comportamento e' in assets/planimetria.js; senza JavaScript restano la mappa, i numeri, le etichette
 * e l'elenco. "Scegli nel preventivo" spunta lo spazio nel calcolatore usando il calcolatore stesso
 * (la sua casella e il suo evento "change"): i prezzi restano solo in config/preventivo.php.
 *
 * @package edera
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * ID di una foto: un numero e' gia' l'ID; un nome e' quello dato dall'installatore (campo _edera_chiave).
 *
 * @param mixed $v Valore di config/planimetria.php.
 * @return int 0 se non e' nella libreria media.
 */
function edera_foto_id( $v ) {
	if ( is_int( $v ) || ( is_string( $v ) && ctype_digit( $v ) ) ) {
		return (int) $v;
	}
	if ( is_string( $v ) && '' !== $v && false === strpos( $v, '/' ) ) {
		return edera_trova_media( $v );
	}
	return 0;
}

/**
 * Indirizzi di una foto della galleria: grande (con srcset), miniatura.
 *
 * @param mixed $v Valore di config/planimetria.php.
 * @return array|null
 */
function edera_foto_galleria( $v ) {
	$id = edera_foto_id( $v );
	if ( $id ) {
		$grande = wp_get_attachment_image_url( $id, 'full' );
		if ( ! $grande ) {
			return null;
		}
		$meta = wp_get_attachment_metadata( $id );
		$mini = $grande;
		$min  = PHP_INT_MAX;
		if ( ! empty( $meta['sizes'] ) ) {
			foreach ( $meta['sizes'] as $nome => $s ) {
				if ( (int) $s['width'] >= 160 && (int) $s['width'] < $min ) {
					$min  = (int) $s['width'];
					$mini = wp_get_attachment_image_url( $id, $nome );
				}
			}
		}
		return array(
			'src'    => $grande,
			'srcset' => (string) wp_get_attachment_image_srcset( $id, 'full' ),
			'mini'   => $mini,
		);
	}
	if ( is_string( $v ) && preg_match( '#^https?://#', $v ) ) {
		return array(
			'src'    => $v,
			'srcset' => '',
			'mini'   => $v,
		);
	}
	return null;
}

add_shortcode(
	'edera_planimetria',
	function () {
		$c       = edera_config( 'planimetria' );
		$pallini = isset( $c['pallini'] ) ? (array) $c['pallini'] : array();
		$mappa   = isset( $c['mappa'] ) ? $c['mappa'] : array();
		$alt     = isset( $mappa['alt'] ) ? $mappa['alt'] : '';
		$id      = edera_foto_id( isset( $mappa['foto'] ) ? $mappa['foto'] : '' );
		if ( $id ) {
			$img = wp_get_attachment_image(
				$id,
				'full',
				false,
				array(
					'class' => 'pl-foto-aerea',
					'alt'   => $alt,
				)
			);
		} elseif ( ! empty( $mappa['foto'] ) && preg_match( '#^https?://#', $mappa['foto'] ) ) {
			$img = '<img class="pl-foto-aerea" src="' . esc_url( $mappa['foto'] ) . '" alt="' . esc_attr( $alt ) . '" loading="lazy">';
		} else {
			return current_user_can( 'edit_pages' ) ? '<p>Planimetria: manca la foto dall’alto (config/planimetria.php, Aspetto &gt; Installa Edera).</p>' : '';
		}

		$foto = array();
		foreach ( isset( $c['galleria'] ) ? (array) $c['galleria'] : array() as $g ) {
			$f = edera_foto_galleria( isset( $g['foto'] ) ? $g['foto'] : '' );
			if ( $f ) {
				$f['didascalia'] = isset( $g['didascalia'] ) ? (string) $g['didascalia'] : '';
				$foto[]          = $f;
			}
		}
		$titolo_galleria = '';
		foreach ( $pallini as $p ) {
			if ( ! empty( $p['galleria'] ) ) {
				$titolo_galleria = $p['nome'];
				break;
			}
		}

		wp_enqueue_script( 'edera-planimetria', get_template_directory_uri() . '/assets/planimetria.js', array(), EDERA_VERSIONE, array( 'in_footer' => true ) );

		static $n = 0;
		++$n;
		$pre = 'pl' . $n;
		ob_start();
		?>
<div class="planimetria" data-planimetria>
  <div class="pl-mappa">
    <?php echo $img; // phpcs:ignore WordPress.Security.EscapeOutput -- wp_get_attachment_image ?>
    <ol class="pl-pallini" aria-label="Gli spazi sulla planimetria">
		<?php
		foreach ( $pallini as $i => $p ) :
			$k      = $i + 1;
			$classi = 'pl-pallino ' . ( isset( $p['etichetta'] ) && 'sinistra' === $p['etichetta'] ? 'sinistra' : 'destra' ) . ( (float) $p['y'] > 55 ? ' in-basso' : '' );
			$stile  = '--x:' . (float) $p['x'] . '%;--y:' . (float) $p['y'] . '%';
			?>
      <li class="<?php echo esc_attr( $classi ); ?>" style="<?php echo esc_attr( $stile ); ?>">
        <button type="button" class="pl-punto" aria-expanded="false" aria-controls="<?php echo esc_attr( $pre . '-scheda-' . $k ); ?>" aria-label="<?php echo esc_attr( $k . '. ' . $p['nome'] ); ?>"><span class="pl-num" aria-hidden="true"><?php echo (int) $k; ?></span><span class="pl-nome" aria-hidden="true"><?php echo esc_html( $p['nome'] ); ?></span></button>
        <div class="pl-scheda" id="<?php echo esc_attr( $pre . '-scheda-' . $k ); ?>" hidden>
          <p class="pl-scheda-nome"><?php echo esc_html( $p['nome'] ); ?></p>
			<?php if ( ! empty( $p['capienza'] ) ) : ?>
          <p class="pl-scheda-capienza"><?php echo esc_html( $p['capienza'] ); ?></p>
			<?php endif; ?>
			<?php if ( ( ! empty( $p['galleria'] ) && $foto ) || ! empty( $p['preventivo'] ) ) : ?>
          <div class="pl-azioni">
				<?php if ( ! empty( $p['galleria'] ) && $foto ) : ?>
            <button type="button" class="btn btn-verde pl-apri-foto">Vedi le foto</button>
				<?php endif; ?>
				<?php if ( ! empty( $p['preventivo'] ) ) : ?>
            <a class="pl-scegli" href="#preventivo" data-spazio="<?php echo esc_attr( $p['preventivo'] ); ?>">Scegli nel preventivo <span class="freccia" aria-hidden="true">↓</span></a>
				<?php endif; ?>
          </div>
			<?php endif; ?>
        </div>
      </li>
		<?php endforeach; ?>
    </ol>
  </div>
  <ol class="pl-elenco" aria-label="Legenda della planimetria">
		<?php foreach ( $pallini as $i => $p ) : ?>
    <li><span class="pl-num" aria-hidden="true"><?php echo (int) ( $i + 1 ); ?></span><b><?php echo esc_html( $p['nome'] ); ?></b><?php if ( ! empty( $p['capienza'] ) ) : ?><span class="pl-cap"><?php echo esc_html( $p['capienza'] ); ?></span><?php endif; ?><?php if ( ! empty( $p['galleria'] ) && $foto ) : ?><button type="button" class="pl-link pl-apri-foto" hidden>Vedi le foto</button><?php endif; ?></li>
		<?php endforeach; ?>
  </ol>
		<?php if ( $foto ) : ?>
  <div class="pl-galleria" role="dialog" aria-modal="true" aria-labelledby="<?php echo esc_attr( $pre . '-titolo' ); ?>" hidden>
    <div class="pl-g-barra">
      <h3 id="<?php echo esc_attr( $pre . '-titolo' ); ?>"><?php echo esc_html( $titolo_galleria ); ?></h3>
      <span class="pl-g-conta" aria-live="polite"></span>
      <button type="button" class="pl-chiudi">Chiudi</button>
    </div>
    <div class="pl-g-palco">
      <img class="pl-g-foto" alt="" sizes="(max-width: 760px) 100vw, 1200px">
      <button type="button" class="pl-prec" aria-label="Foto precedente">←</button>
      <button type="button" class="pl-succ" aria-label="Foto successiva">→</button>
    </div>
    <p class="pl-g-didascalia"></p>
    <div class="pl-g-miniature">
			<?php foreach ( $foto as $j => $f ) : ?>
      <button type="button" class="pl-mini" aria-label="<?php echo esc_attr( 'Foto ' . ( $j + 1 ) . ': ' . $f['didascalia'] ); ?>" data-src="<?php echo esc_url( $f['src'] ); ?>" data-srcset="<?php echo esc_attr( $f['srcset'] ); ?>" data-didascalia="<?php echo esc_attr( $f['didascalia'] ); ?>"><img data-src="<?php echo esc_url( $f['mini'] ); ?>" alt="" width="92" height="62"></button>
			<?php endforeach; ?>
    </div>
  </div>
		<?php endif; ?>
</div>
		<?php
		return ob_get_clean();
	}
);
