"""I due moduli (contatti e richiesta di accesso): lo stesso HTML per l'anteprima e per il tema.

Nel tema il file sta in parti/modulo-<tipo>.html e lo shortcode [dieffepiu_modulo tipo="..."] sostituisce
{{azione}}, {{campi_wp}} e {{esito}}. Nell'anteprima il modulo non invia nulla e lo dice.
"""
from comune import PRIVACY

ARGOMENTI = ["Sistemi e componenti", "Macchine", "Ricambi", "Listini e area riservata", "Altro"]
ATTIVITA = ["Produttore di zanzariere", "Assemblatore", "Installatore", "Rivenditore", "Altro"]


def _campo(id_, nome, etichetta, tipo="text", obbl=False, auto=None, pieno=False):
    req = " required" if obbl else ""
    ac = f' autocomplete="{auto}"' if auto else ""
    stella = " *" if obbl else ""
    cl = ' class="pieno"' if pieno else ""
    return (f'      <div{cl}><label class="l" for="{id_}">{etichetta}{stella}</label>'
            f'<input id="{id_}" name="{nome}" type="{tipo}"{ac}{req}></div>')


def _scelta(id_, nome, etichetta, voci):
    opz = "".join(f"<option>{v}</option>" for v in voci)
    return (f'      <div><label class="l" for="{id_}">{etichetta}</label>'
            f'<select id="{id_}" name="{nome}">{opz}</select></div>')


def _testo(id_, nome, etichetta, obbl):
    req = " required" if obbl else ""
    stella = " *" if obbl else ""
    return (f'      <div class="pieno"><label class="l" for="{id_}">{etichetta}{stella}</label>'
            f'<textarea id="{id_}" name="{nome}" rows="6"{req}></textarea></div>')


def html(tipo, anteprima):
    if tipo == "contatti":
        titolo, guida, bottone = ("Scriveteci", "I campi con l’asterisco sono obbligatori.", "Invia la richiesta")
        campi = [
            _campo("f-nome", "nome", "Nome e cognome", obbl=True, auto="name"),
            _campo("f-azienda", "azienda", "Azienda", obbl=True, auto="organization"),
            _campo("f-email", "email", "Email", "email", obbl=True, auto="email"),
            _campo("f-tel", "telefono", "Telefono", "tel", auto="tel"),
            _campo("f-paese", "paese", "Paese", auto="country-name"),
            _scelta("f-argomento", "argomento", "Argomento", ARGOMENTI),
            _testo("f-messaggio", "messaggio", "Messaggio", True),
        ]
        consenso = "acconsento al trattamento dei dati per ricevere una risposta"
    else:
        titolo, guida, bottone = ("Richiesta di accesso", "Per le aziende del settore. I campi con l’asterisco sono obbligatori.", "Chiedi l’accesso")
        campi = [
            _campo("f-azienda", "azienda", "Azienda", obbl=True, auto="organization"),
            _campo("f-piva", "piva", "Partita IVA", obbl=True),
            _campo("f-nome", "nome", "Nome e cognome", obbl=True, auto="name"),
            _campo("f-email", "email", "Email", "email", obbl=True, auto="email"),
            _campo("f-tel", "telefono", "Telefono", "tel", auto="tel"),
            _scelta("f-attivita", "attivita", "Attività", ATTIVITA),
            _testo("f-messaggio", "messaggio", "Note", False),
        ]
        consenso = "acconsento al trattamento dei dati per la gestione della richiesta"
    ante = ' data-anteprima="1"' if anteprima else ""
    azione = "#" if anteprima else "{{azione}}"
    esito = "" if anteprima else "{{esito}}"
    wp = "" if anteprima else "\n  {{campi_wp}}"
    righe = "\n".join(campi)
    return f'''<form class="modulo" id="modulo" method="post" action="{azione}"{ante}>
  <h2>{titolo}</h2>
  <p class="guida-m">{guida}</p>
  <div class="campi">
{righe}
  </div>
  <div class="miele" aria-hidden="true"><label for="f-sito">Lasciate vuoto questo campo</label><input id="f-sito" name="sito_web" type="text" tabindex="-1" autocomplete="off"></div>
  <label class="consenso"><input type="checkbox" name="consenso" value="1" required> <span>Ho letto l’<a href="{PRIVACY}">informativa privacy</a> e {consenso}.</span></label>
  <div class="invia"><button class="bottone" type="submit">{bottone}</button><p class="esito-m" role="status" aria-live="polite">{esito}</p></div>{wp}
</form>'''


def blocco(c, tipo):
    """Nell'anteprima il modulo intero; in WordPress lo shortcode del tema."""
    if c.modo == "wp":
        return f'[dieffepiu_modulo tipo="{tipo}"]'
    return html(tipo, anteprima=True)
