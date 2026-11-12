#!/usr/bin/env bash
# Installa il sito Edera Country House in WordPress, con WP-CLI:
# tema, Elementor, foto e PDF nella libreria media, pagine Home, Informativa privacy e Cookie in Elementor,
# Home come pagina iniziale e indirizzi belli (/privacy/, /cookie/). Dal tema 1.1 anche la planimetria:
# su un sito gia' installato la aggiunge alla Home senza toccare il resto.
#
# Uso, via SSH con l'utente del sito (non root se si puo'):
#
#   curl -sSLO https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/EderaCountry-Sito/wordpress/installa-su-server.sh
#   bash installa-su-server.sh /percorso/cartella/del/sito https://prova.ederacountry.it tua@email.it
#
# Argomenti:
#   1. la cartella del sito (dove c'e' o ci sara' wp-config.php)
#   2. l'indirizzo del sito, con https://
#   3. l'email dell'amministratore (serve solo se WordPress va installato da zero)
#   4. facoltativo: lo zip del tema, come percorso sul server o indirizzo (normalmente si scarica da GitHub)
#
# - Se nella cartella c'e' gia' WordPress, lo usa (non tocca database e utenti).
# - Se la cartella e' vuota, installa WordPress in italiano: chiede i dati del database a video
#   (la password non si vede mentre la scrivi) e crea l'utente "edera-admin" con una password casuale
#   che stampa una volta sola.
# - Sul sottodominio di prova il sito resta nascosto ai motori di ricerca; su ederacountry.it e' visibile.
# - Si puo' rilanciare: non crea doppioni. Le pagine gia' modificate in Elementor restano com'erano;
#   per riscriverle con quelle del tema: EDERA_RISCRIVI=1 bash installa-su-server.sh ...
# Nessuna password viene scritta in questo file o nel registro.
set -euo pipefail

DIR="${1:?Indica la cartella del sito}"
URL="${2:?Indica l indirizzo del sito, con https://}"
EMAIL="${3:-}"
TEMA="${4:-https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/EderaCountry-Sito/wordpress/edera-tema.zip}"
URL="${URL%/}"

cd "$DIR"
if command -v wp >/dev/null 2>&1; then
  WP=(wp)
else
  echo "WP-CLI non c'e': lo scarico in /tmp"
  curl -sSLo /tmp/wp-cli.phar https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
  WP=(php -d memory_limit=512M /tmp/wp-cli.phar)
fi
if [ "$(id -u)" = "0" ]; then
  WP+=(--allow-root)
  echo "Attenzione: stai usando root. Alla fine i file tornano al proprietario della cartella."
fi

if [ ! -f wp-config.php ]; then
  altro=$(ls -A | grep -v -x -E 'cgi-bin|\.well-known|\.htaccess|index\.html|default\.html|favicon\.ico' || true)
  if [ -n "$altro" ]; then
    echo "Nella cartella ci sono gia' dei file ma non WordPress: mi fermo per non cancellare niente."
    echo "$altro"
    exit 1
  fi
  if [ -z "$EMAIL" ]; then
    echo "Per installare WordPress serve l'email dell'amministratore (terzo argomento)."
    exit 1
  fi
  read -rp "Nome del database (creato dal pannello): " DBN
  read -rp "Utente del database: " DBU
  read -rsp "Password del database: " DBP; echo
  read -rp "Server del database [localhost]: " DBH; DBH=${DBH:-localhost}
  "${WP[@]}" core download --locale=it_IT
  "${WP[@]}" config create --dbname="$DBN" --dbuser="$DBU" --dbpass="$DBP" --dbhost="$DBH" --locale=it_IT
  unset DBP
  PASSADMIN=$(openssl rand -base64 18 | tr -d '/+=')
  "${WP[@]}" core install --url="$URL" --title="Edera Country House" --admin_user=edera-admin \
    --admin_password="$PASSADMIN" --admin_email="$EMAIL" --skip-email
  echo
  echo "Accesso a $URL/wp-admin  utente: edera-admin  password: $PASSADMIN"
  echo "Copiala ora in un gestore di password: non viene salvata da nessuna parte."
  echo
  unset PASSADMIN
fi

# sito di prova nascosto ai motori di ricerca, il dominio vero visibile
case "$URL" in
  https://ederacountry.it|https://www.ederacountry.it|http://ederacountry.it|http://www.ederacountry.it) NASCONDI=0 ;;
  *) NASCONDI=1 ;;
esac

ADMIN=$("${WP[@]}" user list --role=administrator --field=user_login | head -n 1)
"${WP[@]}" theme install "$TEMA" --force --activate
"${WP[@]}" plugin install elementor --activate
# pannello ed editor di Elementor in italiano (se le traduzioni si possono scaricare)
"${WP[@]}" language core install it_IT --activate >/dev/null 2>&1 || true
"${WP[@]}" language plugin install elementor it_IT >/dev/null 2>&1 || true
EDERA_NASCONDI="$NASCONDI" EDERA_RISCRIVI="${EDERA_RISCRIVI:-}" "${WP[@]}" eval --user="$ADMIN" '
  $log = edera_installa( array( "riscrivi" => "1" === getenv( "EDERA_RISCRIVI" ), "nascondi" => "1" === getenv( "EDERA_NASCONDI" ) ) );
  foreach ( $log as $r ) { echo $r, PHP_EOL; }
  foreach ( $log as $r ) { if ( 0 === strpos( $r, "ERRORE" ) ) { exit( 1 ); } }
  // tema 1.1: la planimetria nella Home (se la Home è già stata modificata, la aggiunge senza toccare il resto)
  foreach ( edera_aggiungi_planimetria() as $r ) { echo $r, PHP_EOL; }'
"${WP[@]}" rewrite structure '/%postname%/' --hard >/dev/null
"${WP[@]}" rewrite flush --hard || true

if [ "$(id -u)" = "0" ]; then
  chown -R "$(stat -c %U .)":"$(stat -c %G .)" .
fi
echo
echo "Fatto: $URL"
