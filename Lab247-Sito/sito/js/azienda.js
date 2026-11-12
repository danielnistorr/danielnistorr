// 247LAB, pagine dell'azienda: il modulo contatti prepara una mail (mailto) e la scheda di MINA cambia finitura.
(function(){
  // ---------- contatti: nessun invio, solo una mail pronta nel programma di posta ----------
  var f=document.getElementById('modulo-contatti');
  if(f){
    var esito=document.getElementById('m-esito'),a=f.getAttribute('data-a');
    // l'oggetto puo' arrivare dal link di un'altra pagina (contatti.html?oggetto=Su%20misura)
    try{var q=new URLSearchParams(location.search).get('oggetto');if(q&&!f.oggetto.value)f.oggetto.value=q.slice(0,120);}catch(err){}
    var segna=function(el,male){if(male)el.setAttribute('aria-invalid','true');else el.removeAttribute('aria-invalid');};
    ['nome','cognome','email','messaggio'].forEach(function(n){f[n].addEventListener('input',function(){segna(f[n],false);});});
    f.addEventListener('submit',function(ev){
      ev.preventDefault();
      var manca=null;
      ['nome','cognome','email','messaggio'].forEach(function(n){
        var el=f[n],male=!el.value.trim()||(n==='email'&&!el.checkValidity());
        segna(el,male);if(male&&!manca)manca=el;
      });
      if(manca){esito.textContent=manca===f.email&&f.email.value?'Scrivi un indirizzo email valido.':'Compila i campi Nome, Cognome, Email e Messaggio.';manca.focus();return;}
      if(!f.consenso.checked){esito.textContent='Serve il consenso al trattamento dei dati.';f.consenso.focus();return;}
      var oggetto=f.oggetto.value.trim()||'Richiesta dal sito';
      var corpo=f.messaggio.value.trim()+'\n\n'+f.nome.value.trim()+' '+f.cognome.value.trim()+'\n'+f.email.value.trim();
      location.href='mailto:'+a+'?subject='+encodeURIComponent(oggetto)+'&body='+encodeURIComponent(corpo);
      esito.innerHTML='Si apre il tuo programma di posta con il messaggio pronto: invialo da lì. Se non si apre, scrivici a <a href="mailto:'+a+'">'+a+'</a>.';
    });
  }
  // ---------- MINA: la finitura cambia foto, prezzo, codice e la mail d'ordine ----------
  var s=document.getElementById('mina-scelta');
  if(s){
    var img=document.getElementById('mina-img'),pr=document.getElementById('mina-prezzo'),sku=document.getElementById('mina-sku'),
        nome=document.getElementById('mina-nome'),ord=document.getElementById('mina-ordine');
    var pronte={};
    var precarica=function(i){if(pronte[i.value])return;pronte[i.value]=1;var x=new Image();x.sizes=img.sizes;x.srcset=i.getAttribute('data-srcset');x.src=i.getAttribute('data-src');};
    s.querySelectorAll('input[name=finitura]').forEach(function(i){
      i.parentNode.addEventListener('pointerenter',function(){precarica(i);});
      i.addEventListener('focus',function(){precarica(i);});
      i.addEventListener('change',function(){
        if(!i.checked)return;
        img.srcset=i.getAttribute('data-srcset');img.src=i.getAttribute('data-src');img.alt=i.getAttribute('data-alt');
        pr.textContent=i.getAttribute('data-prezzo');sku.textContent=i.getAttribute('data-sku');
        nome.textContent=i.getAttribute('data-nome');ord.href=i.getAttribute('data-mail');
        document.title=i.getAttribute('data-nome')+' | 247LAB';
      });
    });
    s.addEventListener('submit',function(ev){ev.preventDefault();});
  }
})();
