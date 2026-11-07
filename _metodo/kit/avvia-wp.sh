#!/bin/bash
# Riavvia il server di un WordPress di prova già creato (dopo un riavvio del container). Uso: avvia-wp.sh <slug> <porta>
S=/tmp/claude-0/-home-user-danielnistorr/89486122-32ef-5f21-add5-5cbe6108c543/scratchpad; K=$S/kit; D=$S/wp-$1
pkill -f "php.*-S 127.0.0.1:$2 " 2>/dev/null || true
cd $D && setsid env WPROOT=$D PHP_CLI_SERVER_WORKERS=4 nohup php -d memory_limit=1024M -S 127.0.0.1:$2 -t $D $K/router.php > $S/php-$1.log 2>&1 < /dev/null &
disown || true
sleep 2; curl -s -o /dev/null -w "http://127.0.0.1:$2/ risposta %{http_code}\n" --max-time 60 http://127.0.0.1:$2/
