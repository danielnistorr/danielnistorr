#!/bin/bash
# wp-cli su un'istanza: wpc.sh <cartella-wp> <comandi...>
D=$1; shift
cd "$D" && php -d memory_limit=1024M /tmp/claude-0/-home-user-danielnistorr/89486122-32ef-5f21-add5-5cbe6108c543/scratchpad/wpdl/wp-cli.phar --allow-root "$@"
