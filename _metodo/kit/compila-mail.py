# uso: python3 compila-mail.py <cartella-invio> --nome "Nome Cognome" --paese "Paese" --telefono "333 1234567" --email "tu@dominio.it" [--dopo-visita 01,05]
# Per ogni <cartella-invio>/NN-azienda/email.md:
#   - sostituisce [NOME], [PAESE], [TELEFONO] nella mail (e nella variante, se l'azienda è in --dopo-visita)
#   - rifà il PDF con il mittente in fondo alla pagina 3
#   - scrive pronta.txt (A, oggetto, testo) e una bozza .eml con l'allegato, che Outlook apre come mail da inviare
import argparse, email.policy, json, os, re, subprocess, sys
from email.message import EmailMessage
from email.utils import formataddr

p = argparse.ArgumentParser()
p.add_argument('cartella')
p.add_argument('--nome', required=True)
p.add_argument('--paese', required=True)
p.add_argument('--telefono', required=True)
p.add_argument('--email', required=True)
p.add_argument('--dopo-visita', default='')
a = p.parse_args()
KIT = os.path.dirname(os.path.abspath(__file__))
dopo = {x.strip() for x in a.dopo_visita.split(',') if x.strip()}


def blocchi(md):
    # i blocchi ```text ... ``` nell'ordine: mail, variante, richiamo
    return re.findall(r'```text\n(.*?)\n```', md, re.S)


def campo(md, nome):
    m = re.search(r'^\*\*' + nome + r':\*\*\s*(.+)$', md, re.M)
    return m.group(1).strip() if m else ''


def riempi(t):
    return t.replace('[NOME]', a.nome).replace('[PAESE]', a.paese).replace('[TELEFONO]', a.telefono)


for d in sorted(os.listdir(a.cartella)):
    md_path = os.path.join(a.cartella, d, 'email.md')
    if not re.match(r'\d\d-', d) or not os.path.exists(md_path):
        continue
    md = open(md_path, encoding='utf-8').read()
    b = blocchi(md)
    if len(b) < 2:
        sys.exit(f'{md_path}: mancano i blocchi della mail')
    testo = b[0]
    if d[:2] in dopo:
        # la variante sostituisce il primo paragrafo dopo il saluto
        par = testo.split('\n\n')
        par[1] = b[1].strip()
        testo = '\n\n'.join(par)
    testo = riempi(testo)
    rimasti = re.findall(r'\[[A-Z]+\]', testo)
    if rimasti:
        sys.exit(f'{d}: segnaposto rimasti: {rimasti}')
    a_ = re.split(r'\s+·\s+', campo(md, 'A'))[0].strip()
    oggetto = campo(md, 'Oggetto')
    cart = os.path.join(a.cartella, d)
    spec = os.path.join(cart, 'spec.json')
    mitt = f'{a.nome}  ·  {a.telefono}  ·  {a.email}'
    subprocess.run(['node', os.path.join(KIT, 'allegato.mjs'), spec, cart, '--mittente', mitt], check=True)
    pdf = os.path.join(cart, json.load(open(spec, encoding='utf-8'))['file'])
    subprocess.run(['rm', '-rf', os.path.join(cart, '_lavoro')])
    open(os.path.join(cart, 'pronta.txt'), 'w', encoding='utf-8').write(f'A: {a_}\nOggetto: {oggetto}\nAllegato: {os.path.basename(pdf)}\n\n{testo}\n')
    m = EmailMessage(policy=email.policy.SMTP)
    m['From'] = formataddr((a.nome, a.email))
    m['To'] = a_
    m['Subject'] = oggetto
    m['X-Unsent'] = '1'
    m.set_content(testo)
    m.add_attachment(open(pdf, 'rb').read(), maintype='application', subtype='pdf', filename=os.path.basename(pdf))
    open(os.path.join(cart, f'{d}.eml'), 'wb').write(m.as_bytes())
    print(f'{d}: {a_}  |  {oggetto}')
