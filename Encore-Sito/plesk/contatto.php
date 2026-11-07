<?php
// Modulo "Book a pilot" della landing di Encore: riceve la richiesta e la manda per email.
// Va nella stessa cartella di index.html. Cambia $DESTINATARIO se le richieste devono arrivare altrove.
header('Content-Type: application/json; charset=utf-8');

$DESTINATARIO = 'info@evoxconsulting.it';
$MITTENTE = 'noreply@encore.evoxconsulting.it';

function rispondi($ok, $codice = 200) {
    http_response_code($codice);
    echo json_encode(['ok' => $ok]);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    rispondi(false, 405);
}
// campo trappola: le persone non lo vedono, i bot lo compilano
if (!empty($_POST['website'])) {
    rispondi(true);
}

// una riga sola, niente a capo (evita intestazioni email iniettate), lunghezza massima
function riga($valore, $max) {
    $valore = str_replace(["\r", "\n"], ' ', (string) $valore);
    return trim(mb_substr($valore, 0, $max));
}

$nome = riga($_POST['name'] ?? '', 120);
$marchio = riga($_POST['brand'] ?? '', 120);
$email = filter_var(riga($_POST['email'] ?? '', 200), FILTER_VALIDATE_EMAIL);
$messaggio = trim(mb_substr((string) ($_POST['message'] ?? ''), 0, 4000));

if ($nome === '' || $marchio === '' || !$email) {
    rispondi(false, 422);
}

$oggetto = 'Encore, richiesta pilota: ' . $marchio;
$corpo = "Nome: $nome\nMarchio: $marchio\nEmail: $email\n\n$messaggio\n";
$intestazioni = implode("\r\n", [
    'From: Encore <' . $MITTENTE . '>',
    'Reply-To: ' . $email,
    'Content-Type: text/plain; charset=UTF-8',
]);

$inviata = mail($DESTINATARIO, '=?UTF-8?B?' . base64_encode($oggetto) . '?=', $corpo, $intestazioni);
rispondi($inviata, $inviata ? 200 : 500);
