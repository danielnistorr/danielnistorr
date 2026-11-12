# -*- coding: utf-8 -*-
"""
Redirect 301 dal sito attuale (ASP.NET) alle pagine nuove, per non perdere le visite e le posizioni su Google.
Scrive plugin/redirect-301.csv nel formato di importazione del plugin gratuito Redirection
(Strumenti > Redirection > Import/Export): sorgente, destinazione, regex (1 o 0), codice HTTP.
Le regole con regex coprono tutte le 1067 pagine trovate nel crawl del 4 ottobre 2026.
Uso: python3 redirect.py [elenco-url-vecchi.csv]   (il secondo argomento serve solo per verificare la copertura)
"""
import csv
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(QUI), 'plugin', 'redirect-301.csv')

REGOLE = [
    # (sorgente, destinazione, regex)
    ('^/index\\.aspx.*', '/', 1),
    ('^/(IT/Azienda|EN/Company|about\\.aspx).*', '/azienda/', 1),
    ('^/(IT|EN)/News.*', '/novita/', 1),
    ('^/(IT/Contatti|EN/Contacts|contact\\.aspx).*', '/contatti/', 1),
    ('^/IT/Condizioni-di-vendita.*', '/azienda/#condizioni', 1),
    ('^/IT/Prodotti/VIBRAM.*', '/vibram/', 1),
    ('^/IT/Prodotti/UTENSILI.*', '/catalogo/#utensili', 1),
    ('^/IT/Prodotti/FILATI_ED_ELASTICI.*', '/catalogo/#filati-elastici', 1),
    ('^/IT/Prodotti/IGIENE_E_SICUREZZA.*', '/catalogo/#igiene-sicurezza', 1),
    ('^/IT/Prodotti/PRODOTTI_CHIMICI.*', '/catalogo/#prodotti-chimici', 1),
    ('^/IT/Prodotti/MODELLERIA_E_RIPARAZIONE.*', '/catalogo/#modelleria-riparazione', 1),
    ('^/IT/Prodotti/IMBALLAGGIO.*', '/catalogo/#imballaggio', 1),
    ('^/IT/Prodotti/ESPOSIZIONE_E_CURA.*', '/catalogo/#esposizione-cura', 1),
    ('^/(IT/Prodotti|EN/Products|product\\.aspx|newpage\\.aspx|download\\.aspx|invitefriend\\.aspx).*', '/catalogo/', 1),
]


def destinazione(path):
    for src, dst, rx in REGOLE:
        if re.match(src, path):
            return dst
    return None


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        for src, dst, rx in REGOLE:
            w.writerow([src, dst, rx, 301])
    print('scritto', OUT, len(REGOLE), 'regole')
    if len(sys.argv) > 1:
        rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8')))
        scoperti = []
        for r in rows:
            u = re.sub(r'^https?://[^/]+', '', r['url'])
            if u in ('/', ''):
                continue
            if u.endswith('.pdf'):
                continue    # il PDF delle condizioni va ricaricato nella libreria media: vedi LEGGIMI
            if not destinazione(u):
                scoperti.append(u)
        print(f'copertura: {len(rows) - len(scoperti)} di {len(rows)} indirizzi; scoperti: {scoperti[:10]}')


if __name__ == '__main__':
    main()
