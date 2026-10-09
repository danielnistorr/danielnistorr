# -*- coding: utf-8 -*-
"""
Scrive plugin/redirect-301.csv (plugin Redirection, Strumenti > Redirection > Import/Export): dagli indirizzi del sito
attuale (www.gardenspav.it, elenco in 01-analisi-sito-attuale.md) alle pagine nuove. Formato: regex,destinazione,1,301.

Controlli: nessuna regola colpisce un indirizzo del sito nuovo (sarebbe un redirect in loop); se c'è l'elenco degli URL
vecchi (_prova/url-vecchi.tsv, fuori dal repository) stampa quelli italiani che non trovano una regola.
Uso: python3 redirect.py
"""
import json
import os
import re

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
P = '^/piattaforme_per_autolavaggi/'
M = '^/manufatti_per_la_depurazione_it/'

REGOLE = [
    ('^/home/?$', '/'),
    ('^/l-_azienda', '/azienda/'),
    ('^/prodotti', '/'),
    ('^/vasche_prefabbricate_monoblocco', '/vasche/'),
    (M + r'vasche_rettangolari\.php', '/vasche/#rettangolari'),
    (M + r'vasche_circolari\.php', '/vasche/#circolari'),
    (M + r'vasche_trattate_con_resine_epossidiche\.php', '/vasche/#resine'),
    ('^/depurazione$', '/depurazione/'),
    (M + r'dissabbiatore_statico\.php', '/depurazione/#dissabbiatore'),
    (M + r'separatore_grassi\.php', '/depurazione/#separatore-grassi'),
    (M + r'vasca_imhoff\.php', '/depurazione/#imhoff'),
    (M + r'separatore_oli_in_continuo\.php', '/depurazione/#separatore-oli'),
    (M + r'separatore_oli_ce_con_filtro_a_coalescenza_per_aut\.php', '/depurazione/#separatore-oli-autorimesse'),
    (M + r'impianti_trattamento_per_acque_di_prima_pioggia\.php', '/depurazione/#prima-pioggia'),
    (M + r'depuratori_biologici_ossidazione_totale_fanghi_att\.php', '/depurazione/#depuratori-biologici'),
    ('^/piattaforme_per_autolavaggi/?$', '/piattaforme-autolavaggi/'),
    (P + r'caratteristiche_e_vantaggi\.php', '/piattaforme-autolavaggi/#caratteristiche'),
    (P + r'piattaforma_per_pista_self_mod_450\.php', '/piattaforme-autolavaggi/#mod-450'),
    (P + r'piattaforma_per_pista_self_mod_500\.php', '/piattaforme-autolavaggi/#mod-500'),
    (P + r'piattaforma_per_pista_self_mod_500_doppia_griglia\.php', '/piattaforme-autolavaggi/#mod-500-doppia-griglia'),
    (P + r'piattaforma_per_portale_mod_1\.php', '/piattaforme-autolavaggi/#mod-1'),
    (P + r'piattaforma_per_portale_mod_2\.php', '/piattaforme-autolavaggi/#mod-2'),
    (P + r'piattaforma_per_portale_mod3_sistema_lavaggio\.php', '/piattaforme-autolavaggi/#mod-3'),
    (P + r'piattaforma_per_portale_mod_4_con_area_prelavaggio\.php', '/piattaforme-autolavaggi/#mod-4'),
    (P + r'piattaforma_per_portale_mod_5\.php', '/piattaforme-autolavaggi/#mod-5'),
    (P + r'esempio_di_posa\.php', '/piattaforme-autolavaggi/#posa'),
    (P + r'isola_di_aspirazione\.php', '/piattaforme-autolavaggi/#accessori'),
    (P + r'(personalizzazione|piattaforme_in_calcestruzzo_colorato|piattaforme_con_riscaldamento_integrato|'
     r'installazione_con_travi_di_rialzo.*)\.php', '/piattaforme-autolavaggi/#personalizzazione'),
    (P + r'realizzazioni\.php', '/realizzazioni/'),
]
CODA = [
    (P + 'poprad_.*', '/realizzazioni/'),
    ('^/piattaforme_per_autolavaggi_5/.*', '/realizzazioni/'),
    ('^/dove_siamo', '/contatti/'),
    ('^/news', '/'),
    ('^/privacy$', '/privacy/'),
    ('^/cookie_info', '/cookie/'),
    ('^/web-agency/.*', '/'),
    (r'^/UserFiles/files/politica_qualita\.pdf', '/azienda/'),
    (r'^/UserFiles/files/ISO-9001-.*\.pdf', '/azienda/'),
]
NUOVI = ['/', '/vasche/', '/depurazione/', '/piattaforme-autolavaggi/', '/realizzazioni/', '/azienda/', '/contatti/',
         '/privacy/', '/cookie/']


def regola_cantiere(url):
    return '^' + url.replace('.', r'\.')


def main():
    cantieri = json.load(open(os.path.join(QUI, 'dati', 'cantieri.json'), encoding='utf-8'))
    regole = REGOLE + [(regola_cantiere(c['url_vecchio']), f'/realizzazioni/#{c["id"]}') for c in cantieri] + CODA
    for sorgente, dest in regole:
        assert ',' not in sorgente + dest, sorgente
        for n in NUOVI:
            assert not re.search(sorgente, n), f'{sorgente} colpisce {n}: redirect in loop'
    with open(os.path.join(RADICE, 'plugin', 'redirect-301.csv'), 'w', encoding='utf-8') as f:
        f.write(''.join(f'{s},{d},1,301\n' for s, d in regole))
    elenco = os.path.join(RADICE, '_prova', 'url-vecchi.tsv')
    if os.path.exists(elenco):
        vecchi = [r.split('\t')[0].replace('http://www.gardenspav.it', '') for r in open(elenco, encoding='utf-8')
                  if r.startswith('http://www.gardenspav.it')]
        senza = [v for v in vecchi if not any(re.search(s, v) for s, _ in regole)]
        print(f'{len(vecchi)} URL italiani, senza regola: {senza} (restano uguali nel sito nuovo)')
    print(f'{len(regole)} regole in plugin/redirect-301.csv')


if __name__ == '__main__':
    main()
