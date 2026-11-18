(function(){
  // il gesto della home: scegliere la macchina, la barra gialla prende la sua lunghezza sugli 8,2 m
  var M={
    basic:{nome:"Saldatrice manuale Basic",codice:"ATT001-B",l:3000,barra:"piano 3.000 mm",
      righe:[["Piano","3.000 mm"],["Barra saldante","1.560 mm"],["Peso","150 kg"],["Fettuccia","10 e 50 mm"]],
      nota:"Saldatura termica a impulsi."},
    att007:{nome:"Banco elettronico di taglio e saldatura",codice:"ATT007",l:4000,barra:"banco 4.000 mm",
      righe:[["Lunghezza","4.000 mm"],["Peso","400 kg"]],
      nota:"Taglia e salda la rete sullo stesso banco."},
    tubi:{nome:"Banco e saldatrice automatica per tubi rete da 6 m",codice:"",l:6000,barra:"tubi rete 6.000 mm",
      righe:[["Tubi rete","6.000 mm"],["Saldatura","automatica"]],
      nota:"Brevetto depositato."},
    att030:{nome:"Banco elettronico per sistemi a misura e in kit",codice:"ATT030",l:8200,barra:"banco 8.200 mm",
      righe:[["Lunghezza","8.200 mm"],["Peso e potenza","1.200 kg","4 kW"],["Produttività","40 pezzi l’ora","a misura; 30 in kit"],["Taglio della rete","± 1,5 mm"]],
      nota:"Rumorosità inferiore a 70 dB(A)."}
  };
  var bott=document.querySelectorAll(".selettore button");
  if(bott.length){
    var nome=document.getElementById("m-nome"),cod=document.getElementById("m-codice"),
        barra=document.getElementById("m-barra"),barraT=document.getElementById("m-barra-t"),
        dati=document.getElementById("m-dati"),nota=document.getElementById("m-nota");
    var mostra=function(k){
      var d=M[k];if(!d)return;
      bott.forEach(function(b){b.setAttribute("aria-pressed",b.getAttribute("data-m")===k?"true":"false")});
      nome.textContent=d.nome;cod.textContent=d.codice;
      barra.style.setProperty("--l",(d.l/8200*100).toFixed(3)+"%");
      barraT.textContent=d.barra.replace(/ (?=mm)/," ");
      barra.classList.toggle("fuori",d.l<6000);
      dati.innerHTML="";
      for(var i=0;i<4;i++){
        var div=document.createElement("div"),r=d.righe[i];
        if(r){
          var dt=document.createElement("dt");dt.textContent=r[0];
          var dd=document.createElement("dd");dd.textContent=r[1].replace(/ (?=(mm|kg|kW)\b)/g," ");
          if(r[2]){var s=document.createElement("small");s.textContent=r[2].replace(/ (?=(mm|kg|kW)\b)/g," ");dd.appendChild(s)}
          div.appendChild(dt);div.appendChild(dd);
        }
        dati.appendChild(div);
      }
      nota.textContent=d.nota;
    };
    bott.forEach(function(b,i){
      b.addEventListener("click",function(){mostra(b.getAttribute("data-m"))});
      b.addEventListener("keydown",function(e){
        var j=null;
        if(e.key==="ArrowRight")j=(i+1)%bott.length;
        if(e.key==="ArrowLeft")j=(i-1+bott.length)%bott.length;
        if(j!==null){e.preventDefault();bott[j].focus();mostra(bott[j].getAttribute("data-m"))}
      });
    });
  }
  // menu del telefono
  var apri=document.querySelector(".apri-menu"),menu=document.getElementById("menu");
  if(apri&&menu){
    apri.addEventListener("click",function(){
      var o=apri.getAttribute("aria-expanded")!=="true";
      apri.setAttribute("aria-expanded",String(o));menu.classList.toggle("aperto",o);apri.textContent=o?"Chiudi":"Menu";
    });
    menu.addEventListener("click",function(e){if(e.target.tagName==="A"){apri.setAttribute("aria-expanded","false");menu.classList.remove("aperto");apri.textContent="Menu"}});
  }
  // piede a fisarmonica sotto i 600 px, con bottoni veri
  var mq=window.matchMedia("(max-width:600px)");
  var fb=document.querySelectorAll(".fisarmonica-btn");
  function imposta(){fb.forEach(function(b){var ul=document.getElementById(b.getAttribute("aria-controls"));
    if(ul)ul.hidden=mq.matches?b.getAttribute("aria-expanded")!=="true":false})}
  fb.forEach(function(b){b.addEventListener("click",function(){
    var o=b.getAttribute("aria-expanded")!=="true";b.setAttribute("aria-expanded",String(o));
    b.querySelector("span").textContent=o?"−":"+";imposta()})});
  if(mq.addEventListener){mq.addEventListener("change",imposta)}imposta();
  // newsletter: finche' non e' collegata a un servizio di invio, lo dice
  var form=document.querySelector(".notizie"),esito=document.getElementById("esito-notizie");
  if(form&&esito){form.addEventListener("submit",function(e){e.preventDefault();
    esito.textContent="Grazie. L’iscrizione non è ancora attiva: il modulo va collegato al servizio di invio."})}
  // esito dell'invio (WordPress torna alla pagina con ?modulo=inviato o ?modulo=errore)
  var stato=(location.search.match(/[?&]modulo=(inviato|errore)/)||[])[1];
  if(stato){document.querySelectorAll("form.modulo:not([data-anteprima]) .esito-m").forEach(function(es){
    if(stato==="inviato"){es.className="esito-m ok";es.textContent="Grazie: il messaggio è partito."}
    else{es.className="esito-m errore";es.textContent="Il messaggio non è partito: controllate i campi con l’asterisco e il consenso, poi riprovate. Oppure chiamate il +39 049 8791175."}
  })}
  // moduli di contatto: nell'anteprima HTML non c'e' un server, quindi lo dicono invece di fingere un invio
  document.querySelectorAll("form.modulo[data-anteprima]").forEach(function(f){
    f.addEventListener("submit",function(e){
      e.preventDefault();
      var es=f.querySelector(".esito-m");
      if(es){es.className="esito-m ok";es.textContent="Questa è l’anteprima: il modulo non invia nulla. Sul sito WordPress il messaggio arriva per email."}
    });
  });
})();
