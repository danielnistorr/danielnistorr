(function(){
  var SCHEDE = ["<figure class=\"c-foto\"><span class=\"c-vano\"><img src=\"%BASE%p-case.jpg\" width=\"360\" height=\"248\" alt=\"Tre case in lamiera bianca per un apparecchio elettromedicale\"><\/span><figcaption class=\"c-cap\">Case per un apparecchio elettromedicale<span class=\"c-fonte\">, da una nostra realizzazione<\/span>.<\/figcaption><\/figure><div class=\"c-testo\"><h2 class=\"c-nome\">Taglio laser<\/h2><p class=\"c-dato\">Bystronic Byspeed 4400 W, campo <span class=\"num\">3000 × 1500<\/span> mm<\/p><a class=\"c-link\" href=\"#l-01\">Macchine e misure<\/a><\/div>", "<figure class=\"c-foto\"><span class=\"c-vano\"><img src=\"%BASE%p-griglia.jpg\" width=\"360\" height=\"248\" alt=\"Griglie punzonate impilate sul bancale, per una macchina movimento terra\"><\/span><figcaption class=\"c-cap\">Griglie per una macchina movimento terra<span class=\"c-fonte\">, da una nostra realizzazione<\/span>.<\/figcaption><\/figure><div class=\"c-testo\"><h2 class=\"c-nome\">Punzonatura<\/h2><p class=\"c-dato\">Finn-Power SG6, punzonatura e cesoia angolare, <span class=\"num\">3000 × 1500<\/span> mm<\/p><a class=\"c-link\" href=\"#l-02\">Macchine e misure<\/a><\/div>", "<figure class=\"c-foto\"><span class=\"c-vano\"><img src=\"%BASE%p-cassetto.jpg\" width=\"360\" height=\"248\" alt=\"Cassetto in lamiera con il frontale verniciato, per un arredo odontoiatrico\"><\/span><figcaption class=\"c-cap\">Cassetto per un arredo odontoiatrico<span class=\"c-fonte\">, da una nostra realizzazione<\/span>.<\/figcaption><\/figure><div class=\"c-testo\"><h2 class=\"c-nome\">Piegatura<\/h2><p class=\"c-dato\">Finn-Power a 8 assi e Warcom a CN, <span class=\"num\">3100<\/span> mm utili<\/p><a class=\"c-link\" href=\"#l-03\">Macchine e misure<\/a><\/div>", "<figure class=\"c-foto\"><span class=\"c-vano\"><img src=\"%BASE%p-telaio-inox.jpg\" width=\"360\" height=\"248\" alt=\"Telaio in inox saldato, con il ripiano inclinato\"><\/span><figcaption class=\"c-cap\">Telaio inox per una macchina<span class=\"c-fonte\">, da una nostra realizzazione<\/span>.<\/figcaption><\/figure><div class=\"c-testo\"><h2 class=\"c-nome\">Saldatura<\/h2><p class=\"c-dato\">A filo continuo, a elettrodo e TIG, su ferro, inox e alluminio<\/p><a class=\"c-link\" href=\"#l-04\">Macchine e misure<\/a><\/div>", "<figure class=\"c-foto\"><span class=\"c-vano\"><img src=\"%BASE%p-telaio-frigo.jpg\" width=\"360\" height=\"248\" alt=\"Telaio in tubolare con un arco calandrato, per un banco frigo\"><\/span><figcaption class=\"c-cap\">Telaio in tubolare per un banco frigo<span class=\"c-fonte\">, da una nostra realizzazione<\/span>.<\/figcaption><\/figure><div class=\"c-testo\"><h2 class=\"c-nome\">Tubi e profili<\/h2><p class=\"c-dato\">Curvatubi Pedrazzoli, calandra Ercolina a CN, troncatrice OMES<\/p><a class=\"c-link\" href=\"#l-05\">Macchine e misure<\/a><\/div>", "<figure class=\"c-foto\"><span class=\"c-vano\"><img src=\"%BASE%p-modello.jpg\" width=\"360\" height=\"248\" alt=\"Modello 3D di un pezzo in lamiera\"><\/span><figcaption class=\"c-cap\">Modello 3D di un pezzo in lamiera<span class=\"c-fonte\">, prima di tagliare il foglio<\/span>.<\/figcaption><\/figure><div class=\"c-testo\"><h2 class=\"c-nome\">Progettazione 3D<\/h2><p class=\"c-dato\">Ufficio tecnico interno, Sandro Volpato: <a href=\"mailto:ufftec@teklam.it\">ufftec@teklam.it<\/a><\/p><a class=\"c-link\" href=\"#l-06\">Macchine e misure<\/a><\/div>"];
  var card = document.querySelector('.cartellino');
  var pezzi = [].slice.call(document.querySelectorAll('.pz'));
  var attuale = 0;

  // la lastra nel motivo SVG: la misura giusta per lo schermo
  var dpr = window.devicePixelRatio || 1;
  var hi = window.innerWidth * dpr;
  [].forEach.call(document.querySelectorAll('.foglio-h .img-lastra, .foglio-m .img-lastra'), function(im){
    im.setAttribute('href', hi > 2200 ? '%BASE%lastra-2730.jpg' : hi > 1500 ? '%BASE%lastra-2160.jpg' : '%BASE%lastra-1440.jpg');
  });
  [].forEach.call(document.querySelectorAll('.foglio-v .img-lastra'), function(im){
    if (hi > 800) im.setAttribute('href', '%BASE%lastra-v-1170.jpg');
  });

  function scegli(i){
    if (i === attuale) return;
    attuale = i;
    pezzi.forEach(function(g){ var on = +g.dataset.i === i; g.classList.toggle('on', on); g.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    card.innerHTML = SCHEDE[i];
  }
  pezzi.forEach(function(g){
    g.addEventListener('click', function(){ scegli(+g.dataset.i); });
    g.addEventListener('keydown', function(e){
      var i = +g.dataset.i, fratelli = [].slice.call(g.ownerSVGElement.querySelectorAll('.pz'));
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); scegli(i); }
      else if (e.key === 'ArrowRight' || e.key === 'ArrowDown') { e.preventDefault(); fratelli[(i + 1) % 6].focus(); }
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { e.preventDefault(); fratelli[(i + 5) % 6].focus(); }
    });
  });
})();
