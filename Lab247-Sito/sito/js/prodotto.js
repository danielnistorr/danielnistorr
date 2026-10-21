// 247LAB, scheda prodotto: sul telefono le foto si scorrono di lato. Qui il contatore "1 / 3" e le frecce.
(function(){
  var tel=matchMedia('(max-width:600px)');
  var ferma=matchMedia('(prefers-reduced-motion:reduce)');
  document.querySelectorAll('.scheda-galleria').forEach(function(g){
    var s=g.querySelector('.scheda-scorri'),c=g.querySelector('.scheda-conta span');
    if(!s)return;
    var foto=[].slice.call(s.querySelectorAll('.scheda-foto'));
    var qui=function(){
      var x=s.scrollLeft,m=0,d=Infinity;
      foto.forEach(function(f,i){var v=Math.abs(f.offsetLeft-s.offsetLeft-x);if(v<d){d=v;m=i;}});
      return m;
    };
    var aggiorna=function(){if(c)c.textContent=String(qui()+1);};
    var modo=function(){
      if(tel.matches){s.setAttribute('tabindex','0');}else{s.removeAttribute('tabindex');}
      aggiorna();
    };
    s.addEventListener('scroll',function(){window.requestAnimationFrame(aggiorna);},{passive:true});
    s.addEventListener('keydown',function(e){
      if(!tel.matches||(e.key!=='ArrowRight'&&e.key!=='ArrowLeft'))return;
      e.preventDefault();
      var i=Math.max(0,Math.min(foto.length-1,qui()+(e.key==='ArrowRight'?1:-1)));
      s.scrollTo({left:foto[i].offsetLeft-s.offsetLeft,behavior:ferma.matches?'auto':'smooth'});
    });
    tel.addEventListener('change',modo);
    modo();
  });
})();
