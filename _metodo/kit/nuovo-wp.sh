#!/bin/bash
# Crea un WordPress di prova separato per un cliente e lo avvia.
# Uso: nuovo-wp.sh <slug> <porta> <cartella-assets-web-del-cliente>
# Risultato: http://127.0.0.1:<porta>/ con Elementor 4.3.3, Hello, Ultimate Addons, Contact Form 7, senza contenuti;
# le immagini del cliente sono servite da http://127.0.0.1:<porta>/assets/
set -e
S=/tmp/claude-0/-home-user-danielnistorr/89486122-32ef-5f21-add5-5cbe6108c543/scratchpad; K=$S/kit
SLUG=$1; PORT=$2; ASSETS=$3; D=$S/wp-$SLUG
if [ ! -d "$D" ]; then
  cp -a $S/wp "$D"
  find "$D/wp-content/uploads" -mindepth 1 -delete 2>/dev/null || true
  for x in anteprima bvg-assets; do [ -e "$D/$x" ] && find "$D/$x" -delete 2>/dev/null; rm -f "$D/$x" 2>/dev/null || true; done
fi
sed -i "s#define( 'WP_HOME', '[^']*' );#define( 'WP_HOME', 'http://127.0.0.1:$PORT' );#; s#define( 'WP_SITEURL', '[^']*' );#define( 'WP_SITEURL', 'http://127.0.0.1:$PORT' );#" $D/wp-config.php
sed -i "/WP_PROXY_HOST\|WP_PROXY_PORT\|WP_PROXY_BYPASS_HOSTS/d" $D/wp-config.php
ln -sfn "$ASSETS" $D/assets
pkill -f "php.*-S 127.0.0.1:$PORT " 2>/dev/null || true
cd $D && setsid env WPROOT=$D PHP_CLI_SERVER_WORKERS=4 nohup php -d memory_limit=1024M -S 127.0.0.1:$PORT -t $D $K/router.php > $S/php-$SLUG.log 2>&1 < /dev/null &
disown || true
cd - >/dev/null
sleep 2
W="$K/wpc.sh $D"
$W search-replace 'http://127.0.0.1:8899' "http://127.0.0.1:$PORT" --all-tables --quiet 2>/dev/null || true
# contenuti di partenza vuoti: niente pagine, articoli, template, immagini, header/footer, menu del cliente precedente
for T in elementor_library page post attachment elementor-hf; do
  IDS=$($W post list --post_type=$T --post_status=any --format=ids 2>/dev/null); [ -n "$IDS" ] && $W post delete $IDS --force >/dev/null 2>&1 || true
done
for M in $($W menu list --format=ids 2>/dev/null); do $W menu delete $M >/dev/null 2>&1 || true; done
for F in $($W post list --post_type=wpcf7_contact_form --format=ids 2>/dev/null); do $W post delete $F --force >/dev/null 2>&1 || true; done
$W option update blogname "$SLUG (prova)" >/dev/null 2>&1
echo "WordPress di prova: http://127.0.0.1:$PORT/  cartella: $D  wp-cli: $W"
curl -s -o /dev/null -w "risposta: %{http_code}\n" --max-time 60 http://127.0.0.1:$PORT/
