# -*- coding: utf-8 -*-
"""
Estrae dal crawl del sito attuale (catalog_it.json) e dal manifest delle immagini un file catalogo.json
con famiglie, sottocategorie, conteggi e articoli (codice, nome, foto locale se esiste).
Uso: python3 estrai_catalogo.py <percorso catalog_it.json>
"""
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(os.path.dirname(QUI), 'assets', 'originali')

# nomi puliti delle 10 voci del menu PRODOTTI del sito attuale, nell'ordine del sito
FAMIGLIE = {
    'cat/it_8.html': ('utensili', 'Utensili'),
    'cat/it_10.html': ('filati-elastici', 'Filati ed elastici'),
    'cat/it_16.html': ('igiene-sicurezza', 'Igiene e sicurezza'),
    'cat/it_19.html': ('prodotti-chimici', 'Prodotti chimici'),
    'cat/it_20.html': ('modelleria-riparazione', 'Modelleria e riparazione'),
    'cat/it_21.html': ('imballaggio', 'Imballaggio'),
    'cat/it_22.html': ('esposizione-cura', 'Esposizione e cura'),
    'cat/it_40_1.html': ('vibram-lastre', 'Lastre Vibram'),
    'cat/it_40_2.html': ('vibram-suole', 'Suole Vibram'),
    'cat/it_40_3.html': ('vibram-mezzesuole-tacchi', 'Mezzesuole e tacchi Vibram'),
}


def pulisci(s):
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s


def main(src):
    data = json.load(open(src, encoding='utf-8'))
    manifest = json.load(open(os.path.join(ASSET, 'manifest.json'), encoding='utf-8'))
    foto = {}
    for x in manifest:
        if x.get('file', '') and x['file'].startswith('prodotti/') and x.get('page'):
            m = re.search(r'productid=(\d+)', x['page'])
            if m:
                foto[m.group(1)] = {'file': x['file'], 'w': x['width'], 'h': x['height']}
    out = []
    for d in data:
        slug, nome = FAMIGLIE[d['file']]
        titoli = {i['anchor']: pulisci(i['title']) for i in d.get('subcat_icons', [])}
        sub = []
        for g in d['groups']:
            arts = []
            for p in g['products']:
                f = foto.get(p.get('productid') or '')
                arts.append({'id': p.get('productid'), 'codice': p.get('code'), 'nome': pulisci(p.get('name')),
                             'foto': f['file'] if f else None, 'foto_w': f['w'] if f else None})
            nome_sub = titoli.get(g['anchor']) or pulisci(g.get('heading')) or g['anchor']
            sub.append({'nome': nome_sub, 'n': len(arts), 'articoli': arts})
        out.append({'slug': slug, 'nome': nome, 'n': sum(s['n'] for s in sub), 'sottocategorie': sub})
    tot = sum(f['n'] for f in out)
    json.dump({'fonte': 'crawl di www.benvegnusrl.it del 4 ottobre 2026', 'totale': tot, 'famiglie': out},
              open(os.path.join(QUI, 'catalogo.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for f in out:
        print(f"{f['nome']}: {f['n']} | " + ', '.join(f"{s['nome']} {s['n']}" for s in f['sottocategorie']))
    print('totale', tot)


if __name__ == '__main__':
    main(sys.argv[1])
