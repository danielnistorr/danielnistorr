(function(){
// interruttore ferro, inox, alluminio nella riga 01 della distinta
  var sp = document.querySelector('.sp');
  function metallo(b, fuoco){
    [].forEach.call(sp.querySelectorAll('[role=radio]'), function(x){ var on = x === b; x.setAttribute('aria-checked', on ? 'true' : 'false'); x.tabIndex = on ? 0 : -1; });
    sp.style.setProperty('--a', b.dataset.a);
    sp.querySelector('.sp-out').innerHTML = b.textContent.toLowerCase() + ' fino a <span class="num">' + b.dataset.a + '</span>\u00a0mm';
    if (fuoco) b.focus();
  }
  sp.addEventListener('click', function(e){
    var b = e.target.closest('[role=radio]');
    if (b) metallo(b, false);
  });
  sp.addEventListener('keydown', function(e){
    var b = e.target.closest('[role=radio]');
    if (!b) return;
    var tutti = [].slice.call(b.parentNode.children), i = tutti.indexOf(b), j = null;
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') j = (i + 1) % tutti.length;
    else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') j = (i + tutti.length - 1) % tutti.length;
    else if (e.key === 'Home') j = 0;
    else if (e.key === 'End') j = tutti.length - 1;
    if (j !== null) { e.preventDefault(); metallo(tutti[j], true); }
  });
})();
