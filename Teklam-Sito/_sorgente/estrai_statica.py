# -*- coding: utf-8 -*-
"""
Copia dalla home statica approvata (sito/index.html) le parti che in WordPress restano widget HTML,
così come sono, nei file che contenuti.py legge:
  foglio.html     la tavola della prima schermata: il letto del laser e le tre lastre SVG (larga, media, girata)
  cartellino.html il cartellino del pezzo scelto (stato iniziale: pezzo 01)
  foglio.js       lo script della pagina statica per i sei pezzi (schede, lastra della misura giusta, tastiera)
  spessori.html   l'interruttore Ferro, Inox, Alluminio della riga 01 della distinta
  spessori.js     lo script della pagina statica per l'interruttore
  sagome.json     le sei sagome piene della distinta (SVG)
I percorsi "img/" diventano "%BASE%": contenuti.py li sostituisce con la base delle immagini.
Uso: python3 _sorgente/estrai_statica.py   (solo se la home statica cambia)
"""
import json
import os
import re

QUI = os.path.dirname(os.path.abspath(__file__))
STATICA = os.path.join(os.path.dirname(QUI), 'sito', 'index.html')


def tra(s, a, b, incluso=True):
    i = s.index(a)
    j = s.index(b, i) + (len(b) if incluso else 0)
    return s[i:j]


def base(t):
    return re.sub(r'(["\' ])img/', r'\1%BASE%', t)


def scrivi(nome, testo):
    with open(os.path.join(QUI, nome), 'w', encoding='utf-8') as f:
        f.write(testo.strip() + '\n')
    print(nome, len(testo))


def main():
    s = open(STATICA, encoding='utf-8').read()
    tavola = tra(s, '<div class="tavola">', '</svg>\n    </div>')
    # il titolo h1 inciso sulla lastra in WordPress è un widget Titolo nativo: lo tolgo dalla tavola
    h1 = re.search(r'\s*<h1 class="incisione"[^>]*>.*?</h1>', tavola).group(0)
    tavola = tavola.replace(h1, '')
    scrivi('foglio.html', base(tavola))
    scrivi('cartellino.html', base(tra(s, '<aside class="cartellino"', '</aside>')))
    script = tra(s, '<script>', '</script>')[len('<script>'):-len('</script>')]
    i = script.index('  // interruttore ferro')
    # lo script dei pezzi e quello dell'interruttore: in WordPress stanno ognuno nel suo widget HTML
    pezzi = script[:i].rstrip() + '\n})();'
    spess = '(function(){\n' + script[i:].strip()
    scrivi('foglio.js', base(pezzi))
    scrivi('spessori.js', spess)
    scrivi('spessori.html', tra(s, '<div class="sp" style="--a:20">', '</p>\n</div>'))
    sagome = re.findall(r'<span class="d-sag">(<svg class="sagoma".*?</svg>)</span>', s)
    assert len(sagome) == 6, len(sagome)
    scrivi('sagome.json', json.dumps(sagome, ensure_ascii=False, indent=0))


if __name__ == '__main__':
    main()
