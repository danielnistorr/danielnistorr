#!/usr/bin/env bash
# Misura i segnali da IA di una pagina a 1440 px e controlla le soglie del paragrafo f di
# _metodo/CARATTERI-E-SEGNALI-IA.md (dal paragrafo 7 di _metodo/ricerca-caratteri/segnali-ia.md).
# uso: segnali.sh <url> <cartella-uscita> [nome]
#   <url>  https://... oppure file:///percorso/anteprima/01-home.html (un percorso locale va bene: diventa file://)
#   scrive <nome>-1440-info.json, <nome>-1440-soglie.json, <nome>-1440-top.png e <nome>-1440.png in <cartella-uscita>
#   stampa una riga per soglia: OK, DA CORREGGERE (bloccante) o DA GUARDARE (indicativa)
#   esce con 0 se nessuna soglia bloccante fallisce, 1 se almeno una fallisce,
#   2 se la pagina non si apre, risponde con un errore o non ha testo
set -u
if [ $# -lt 2 ]; then echo "uso: $0 <url> <cartella-uscita> [nome]" >&2; exit 2; fi
URL="$1"; OUT="$2"; NOME="${3:-pagina}"
QUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
case "$URL" in
  http://*|https://*|file://*) ;;
  /*) URL="file://$URL" ;;
  *) URL="file://$(cd "$(dirname "$URL")" && pwd)/$(basename "$URL")" ;;
esac
case "$URL" in
  file://*) if [ ! -f "${URL#file://}" ]; then echo "file inesistente: ${URL#file://}" >&2; exit 2; fi ;;
esac
mkdir -p "$OUT"
rm -f "$OUT/$NOME-1440-info.json" "$OUT/$NOME-1440-soglie.json"
node "$QUI/misura-segnali.cjs" "$OUT" "$NOME" "$URL" 1440 > "$OUT/$NOME-1440-misura.log" 2>&1
RC=$?
if [ $RC -ne 0 ] || [ ! -f "$OUT/$NOME-1440-info.json" ]; then cat "$OUT/$NOME-1440-misura.log" >&2; echo "misura non riuscita" >&2; exit 2; fi
node "$QUI/segnali-soglie.cjs" "$OUT" "$NOME" "$URL" 1440
