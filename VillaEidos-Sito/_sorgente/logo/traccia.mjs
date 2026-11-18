// Logo di Villa Eidos: vettorializza le due maschere di maschere.py con potrace (porting JS, pacchetto npm
// "potrace" 2.1.8) e scrive i tracciati assoluti in <lavoro>/tracciati.json, uno per inchiostro.
// Uso: NODE_PATH=<cartella con node_modules/potrace> node traccia.mjs <lavoro>
// Il disegno finale (logo intero, marchio, scritta, versione orizzontale) lo compone logo.py.
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
const require = createRequire(path.join(process.env.NODE_PATH || process.cwd(), 'x.js'));
const potrace = require('potrace');

const lavoro = process.argv[2] || 'logo-lavoro';
const opz = { threshold: 128, turdSize: 20, optTolerance: 0.25, alphaMax: 1.0, optCurve: true, turnPolicy: potrace.Potrace.TURNPOLICY_MINORITY };
const fuori = {};
for (const nome of ['verde', 'acqua']) {
  const svg = await new Promise((ok, ko) => potrace.trace(path.join(lavoro, `maschera-${nome}.png`), opz, (e, s) => (e ? ko(e) : ok(s))));
  const d = svg.match(/ d="([^"]+)"/)[1];
  fuori[nome] = d;
  console.log(nome, d.length, 'caratteri');
}
const dim = fs.readFileSync(path.join(lavoro, 'maschera-verde.png'));
fs.writeFileSync(path.join(lavoro, 'tracciati.json'), JSON.stringify(fuori));
