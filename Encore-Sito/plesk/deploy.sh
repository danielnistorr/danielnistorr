#!/bin/bash
# Mette online la landing di Encore su encore.evoxconsulting.it (server Plesk), dal tuo terminale.
# Uso:  bash deploy.sh <percorso di encore-statico.zip> [email per il certificato HTTPS]
# Esempio: bash deploy.sh ~/Downloads/encore-statico.zip nome@dominio.it
# Chiede la password di root due volte (copia del file, poi comandi sul server).
set -e
ZIP=${1:?indica il percorso di encore-statico.zip}
EMAIL=${2:-}
HOST=root@195.20.235.104

scp "$ZIP" "$HOST:/root/encore-statico.zip"

ssh "$HOST" "EMAIL='$EMAIL' bash -s" <<'SUL_SERVER'
set -e
DOM=encore.evoxconsulting.it
BASE=/var/www/vhosts/evoxconsulting.it
# 1. il sito in Plesk, se non c'è ancora (cartella: evoxconsulting.it/encore.evoxconsulting.it)
if ! plesk bin site --info "$DOM" >/dev/null 2>&1; then
  plesk bin site --create "$DOM" -webspace-name evoxconsulting.it -www-root "$DOM"
fi
D="$BASE/$DOM"
[ -d "$D" ] || { echo "Cartella $D non trovata: guarda in Plesk qual è la cartella del sito e cambia D in questo script"; exit 1; }
# 2. i file, con lo stesso proprietario del sito principale
U=$(stat -c %U "$BASE/httpdocs")
unzip -oq /root/encore-statico.zip -d "$D"
chown -R "$U":psacln "$D"
chown "$U":psaserv "$D"
# 3. HTTPS con Let's Encrypt (se hai passato l'email)
if [ -n "$EMAIL" ]; then
  plesk bin extension --exec letsencrypt cli.php -d "$DOM" -m "$EMAIL" || echo "HTTPS non riuscito: attivalo da Plesk, SSL/TLS > Let's Encrypt"
fi
rm -f /root/encore-statico.zip
echo "Fatto: http://$DOM"
curl -sI "http://$DOM" | head -1
# il modulo: una richiesta vuota deve rispondere {"ok":false} (422), segno che PHP gira sul sottodominio
echo "Modulo: $(curl -s -X POST "http://$DOM/contatto.php")"
SUL_SERVER
