#!/usr/bin/env bash
# Installa il sito Dieffepiu (tema, Elementor, pagine, notizie, menu) in una cartella del server, con WP-CLI.
#
# Prima: crea il sottodominio dal pannello dell'hosting (la sua cartella) e, se WordPress non c'e' ancora,
# un database vuoto con il suo utente. Poi, via SSH, con l'utente del sito (non root se si puo'):
#
#   curl -sSLO https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Dieffepiu-Sito/wordpress/installa-su-server.sh
#   bash installa-su-server.sh /percorso/cartella/sottodominio https://dieffepiu.tuodominio.it tua@email.it
#
# - Se nella cartella c'e' gia' WordPress, lo usa (non tocca database e utenti).
# - Se la cartella e' vuota, installa WordPress in italiano: chiede i dati del database a video
#   (la password non si vede mentre la scrivi) e crea l'utente amministratore "dieffepiu-admin"
#   con una password casuale che stampa una volta sola.
# - Il sito resta nascosto ai motori di ricerca; i moduli arrivano all'email indicata.
# Nessuna password viene scritta in questo file o nel registro.
set -euo pipefail

DIR="${1:?Indica la cartella del sottodominio}"
URL="${2:?Indica l indirizzo https del sottodominio}"
EMAIL="${3:?Indica la tua email (amministratore e moduli)}"
TEMA="https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Dieffepiu-Sito/wordpress/dieffepiu-tema.zip"

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
  altro=$(ls -A | grep -v -x -E 'cgi-bin|\.well-known|\.htaccess|index\.html|default\.html' || true)
  if [ -n "$altro" ]; then
    echo "Nella cartella ci sono gia' dei file ma non WordPress: mi fermo per non cancellare niente."
    echo "$altro"
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
  "${WP[@]}" core install --url="$URL" --title="Dieffepiu" --admin_user=dieffepiu-admin \
    --admin_password="$PASSADMIN" --admin_email="$EMAIL" --skip-email
  echo
  echo "Accesso a $URL/wp-admin  utente: dieffepiu-admin  password: $PASSADMIN"
  echo "Copiala ora in un gestore di password: non viene salvata da nessuna parte."
  echo
  unset PASSADMIN
fi

ADMIN=$("${WP[@]}" user list --role=administrator --field=user_login | head -n 1)
"${WP[@]}" theme install "$TEMA" --force --activate
"${WP[@]}" plugin install elementor --activate
DFP_EMAIL="$EMAIL" "${WP[@]}" eval --user="$ADMIN" \
  'foreach ( dfp_installa( true, getenv( "DFP_EMAIL" ), true, true ) as $r ) { echo $r, PHP_EOL; }'
"${WP[@]}" rewrite flush --hard || true

if [ "$(id -u)" = "0" ]; then
  chown -R "$(stat -c %U .)":"$(stat -c %G .)" .
fi
echo
echo "Fatto: $URL"
