<?php
// Crea o aggiorna un modulo Contact Form 7. Uso: wp eval-file cf7.php "<titolo>" <file-modulo.txt> <destinatario>
wp_set_current_user( 1 );
list( $titolo, $file, $dest ) = $args;
$es = wpcf7_get_contact_form_by_title( $titolo );
$cf = $es ? $es : WPCF7_ContactForm::get_template( [ 'title' => $titolo ] );
$p = $cf->get_properties();
$p['form'] = file_get_contents( $file );
$p['mail']['recipient'] = $dest;
$p['mail']['subject'] = $titolo;
$p['mail']['additional_headers'] = 'Reply-To: [your-email]';
$cf->set_properties( $p ); $cf->set_title( $titolo );
echo 'modulo ' . $cf->save() . ': ' . ( do_shortcode( '[contact-form-7 title="' . $titolo . '"]' ) ? 'ok' : 'vuoto' ) . "\n";
