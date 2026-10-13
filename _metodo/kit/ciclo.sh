#!/bin/bash
# Ciclo completo di prova per un cliente: build -> import in WordPress -> pagine -> header/footer/menu -> screenshot.
# Variabili (tutte obbligatorie tranne VIEWS e HTMLTOO):
#   SLUG     nome breve (es. rossi)           PORT   porta del WordPress di prova (es. 8901)
#   SRC      cartella _sorgente del cliente   PREFIX prefisso dei titoli dei template (es. "Rossi")
#   MENU     slug delle pagine del menu, separati da virgola (es. "chi-siamo,prodotti,contatti")
#   PAGINE   coppie percorso:nome-file separate da spazio (es. "/:01-home /chi-siamo/:02-chi-siamo")
#   VIEWS    "desktop tablet mobile" (predefinito: desktop)    HTMLTOO=1 anche gli screenshot del fallback
# Screenshot in $SRC/../_prova/shots/el-<nome>-<vista>.png (e ht-...); build di prova in $SRC/../_prova/build
S=/tmp/claude-0/-home-user-danielnistorr/89486122-32ef-5f21-add5-5cbe6108c543/scratchpad; K=$S/kit
D=$S/wp-$SLUG; W="$K/wpc.sh $D"; P=$(cd $SRC/.. && pwd)/_prova; TB=$P/build; SH=$P/shots
VIEWS=${VIEWS:-desktop}
mkdir -p $SH
set -e
python3 $SRC/build.py --base http://127.0.0.1:$PORT/assets/ --out $TB
IDS=$($W post list --post_type=elementor_library --format=ids 2>/dev/null); [ -n "$IDS" ] && $W post delete $IDS --force >/dev/null 2>&1 || true
AIDS=$($W post list --post_type=attachment --format=ids 2>/dev/null); [ -n "$AIDS" ] && $W post delete $AIDS --force >/dev/null 2>&1 || true
$W eval-file $K/import-test.php $TB/elementor-json 2>/dev/null | python3 -c "
import json,sys; raw=sys.stdin.read(); d,_=json.JSONDecoder().raw_decode(raw[raw.find('['):])
bad=[r for r in d if not r['ok'] or r['elements_src']!=r['elements_saved'] or r['images_placeholder']]
print('import:', len(d), 'file,', sum(r['elements_saved'] for r in d), 'elementi,', sum(r['images_local'] for r in d), 'immagini locali,', 'PROBLEMI: '+str(bad) if bad else 'nessun problema')"
$W eval-file $K/make-pages.php "$PREFIX" elementor_header_footer senza-hf 2>/dev/null | tail -20
$W eval-file $K/uae-hf.php "$PREFIX" "$MENU" 2>/dev/null
$W rewrite structure '/%postname%/' --hard >/dev/null 2>&1 || true
rm -rf $D/anteprima && cp -r $TB/anteprima $D/anteprima
set +e
for coppia in $PAGINE; do
  pth=${coppia%%:*}; n=${coppia##*:}
  for v in $VIEWS; do
    case $v in desktop) Wd=1440; H=900; M="";; tablet) Wd=1024; H=1366; M=mobile;; mobile) Wd=390; H=844; M=mobile;; esac
    node $K/shoot.mjs "http://127.0.0.1:$PORT$pth" $SH/el-$n-$v.png $Wd $H $M
    [ -n "$HTMLTOO" ] && node $K/shoot.mjs "http://127.0.0.1:$PORT/anteprima/$n.html" $SH/ht-$n-$v.png $Wd $H $M
  done
done
echo "screenshot in $SH"
