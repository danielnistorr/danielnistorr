/* Kit HE: il movimento curato delle home di fascia alta.
   Si compone con attributi nell'HTML (data-he-*), senza scrivere JavaScript nelle pagine.
   Richiede vendor/gsap.min.js, vendor/ScrollTrigger.min.js, vendor/SplitText.min.js e vendor/lenis.min.js,
   caricati prima di questo file. Con "riduci movimento" o senza le librerie la pagina resta ferma e completa:
   restano attivi solo i comandi d'uso (prima e dopo, indice, galleria nativa).

   Attributi:
   data-he-split          titolo che sale riga per riga (al massimo 3 per pagina); data-he-subito = all'apertura
   data-he-scale          sezione .he-scala: la foto parte incorniciata e si allarga a tutta pagina scorrendo;
                          data-he-scale-zoom="1" toglie l'ingrandimento iniziale (da usare con foto piccole o morbide)
   data-he-parallax="0.12" contenitore .he-parallax: la foto scorre piu' lenta della pagina
   data-he-wipe="su|sinistra|destra"  la foto si scopre con un taglio netto quando entra
   data-he-horizontal     sezione .he-oriz con .he-oriz-binario: galleria orizzontale fissata
   data-he-story          sezione .he-storia con .he-storia-media e .he-passo: la foto cambia passo per passo
   data-he-compare        .he-confronto con img.prima, img.dopo e un input range
   data-he-index          .he-indice: righe [data-img] che cambiano la foto di .he-indice-anteprima
   data-he-header         la testata si nasconde scendendo (solo da 900 px in su: sul telefono resta, col numero); data-he-chiara-dopo="#id" cambia tema dopo una sezione
   data-he-intro          .he-intro: sipario d'ingresso, una volta per visita
   data-he-conta          numero che sale fino al suo valore quando entra (solo per dati veri, al massimo uno)
*/
(function () {
  "use strict";
  var html = document.documentElement;
  var riduci = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var librerie = window.gsap && window.ScrollTrigger;
  var moto = !riduci && librerie;
  html.classList.add(moto ? "he-moto" : "he-fermo");

  function tutti(sel, base) { return Array.prototype.slice.call((base || document).querySelectorAll(sel)); }

  /* ---------- comandi d'uso: funzionano sempre ---------- */
  tutti("[data-he-compare]").forEach(function (box) {
    var r = box.querySelector("input[type=range]");
    if (!r) return;
    var metti = function () { box.style.setProperty("--pos", r.value + "%"); };
    r.addEventListener("input", metti);
    metti();
  });

  tutti("[data-he-index]").forEach(function (box) {
    var ante = box.querySelector(".he-indice-anteprima");
    if (!ante) return;
    var righe = tutti("[data-img]", box);
    var immagini = righe.map(function (riga, i) {
      var im = new Image();
      im.alt = "";
      im.decoding = "async";
      im.src = riga.getAttribute("data-img");
      if (i === 0) im.className = "attiva";
      ante.appendChild(im);
      return im;
    });
    righe.forEach(function (riga, i) {
      var vai = function () { immagini.forEach(function (im, j) { im.classList.toggle("attiva", j === i); }); };
      riga.addEventListener("mouseenter", vai);
      riga.addEventListener("focusin", vai);
    });
  });

  if (!moto) return;

  gsap.registerPlugin(ScrollTrigger);
  if (window.SplitText) gsap.registerPlugin(SplitText);

  /* ---------- scorrimento morbido ---------- */
  var lenis = null;
  if (window.Lenis && !html.hasAttribute("data-he-senza-lenis")) {
    lenis = new Lenis({ lerp: 0.09, wheelMultiplier: 0.9, smoothWheel: true });
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
    gsap.ticker.lagSmoothing(0);
    window.heLenis = lenis;
    tutti('a[href^="#"]').forEach(function (a) {
      a.addEventListener("click", function (e) {
        var id = a.getAttribute("href");
        if (id.length < 2) return;
        var el = document.querySelector(id);
        if (!el) return;
        e.preventDefault();
        var off = parseInt(getComputedStyle(html).getPropertyValue("--he-offset"), 10) || 0;
        lenis.scrollTo(el, { offset: -off, duration: 1.4 });
      });
    });
  }

  var mm = gsap.matchMedia();

  /* ---------- sipario d'ingresso ---------- */
  var intro = document.querySelector("[data-he-intro]");
  var ritardo = 0;
  if (intro) {
    var visto = false;
    try { visto = sessionStorage.getItem("he-intro") === "1"; sessionStorage.setItem("he-intro", "1"); } catch (e) {}
    if (!visto) {
      intro.classList.add("vai");
      ritardo = 1.15;
      var tl = gsap.timeline();
      var marchio = intro.querySelector(".he-intro-marchio");
      if (marchio) tl.from(marchio, { yPercent: 120, duration: 0.7, ease: "expo.out" });
      tl.to(intro, { clipPath: "inset(0 0 100% 0)", duration: 0.85, ease: "expo.inOut" }, "+=0.15")
        .set(intro, { display: "none" });
    }
  }

  /* ---------- titoli riga per riga ---------- */
  var titoli = function () {
    if (!window.SplitText) return;
    tutti("[data-he-split]").forEach(function (el) {
      var subito = el.hasAttribute("data-he-subito");
      SplitText.create(el, {
        type: "lines", mask: "lines", linesClass: "he-riga", autoSplit: true,
        onSplit: function (self) {
          return gsap.from(self.lines, {
            yPercent: 112, duration: 1.15, ease: "expo.out", stagger: 0.085,
            delay: subito ? ritardo + parseFloat(el.getAttribute("data-he-ritardo") || "0.1") : 0,
            scrollTrigger: subito ? null : { trigger: el, start: "top 86%", once: true }
          });
        }
      });
    });
  };
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(titoli); else titoli();

  /* ---------- apertura che si allarga ---------- */
  tutti("[data-he-scale]").forEach(function (sec) {
    var media = sec.querySelector(".he-scala-media");
    if (!media) return;
    var img = media.querySelector("img,video");
    var cornice = sec.getAttribute("data-he-scale") || "inset(14% 20% 14% 20% round 2px)";
    mm.add("(min-width: 900px)", function () {
      var tl = gsap.timeline({ scrollTrigger: { trigger: sec, start: "top top", end: "+=110%", scrub: 0.6, pin: true, anticipatePin: 1 } });
      tl.fromTo(media, { clipPath: cornice }, { clipPath: "inset(0% 0% 0% 0% round 0px)", ease: "none" }, 0);
      var zoom = parseFloat(sec.getAttribute("data-he-scale-zoom") || "1.28");
      if (img && zoom !== 1) tl.fromTo(img, { scale: zoom }, { scale: 1, ease: "none" }, 0);
      var via = sec.querySelectorAll("[data-he-scale-via]");
      if (via.length) tl.to(via, { yPercent: -40, opacity: 0, ease: "none" }, 0);
      var entra = sec.querySelectorAll("[data-he-scale-entra]");
      if (entra.length) tl.fromTo(entra, { yPercent: 40, opacity: 0 }, { yPercent: 0, opacity: 1, ease: "none" }, 0.45);
    });
    mm.add("(max-width: 899px)", function () {
      var zoomT = Math.min(1.18, parseFloat(sec.getAttribute("data-he-scale-zoom") || "1.18"));
      if (img && zoomT !== 1) gsap.fromTo(img, { scale: zoomT }, { scale: 1, ease: "none", scrollTrigger: { trigger: sec, start: "top top", end: "bottom top", scrub: true } });
    });
  });

  /* ---------- parallasse leggera ---------- */
  tutti("[data-he-parallax]").forEach(function (box) {
    var v = parseFloat(box.getAttribute("data-he-parallax")) || 0.1;
    var el = box.querySelector("img,video") || box;
    gsap.fromTo(el, { yPercent: -v * 100 }, { yPercent: v * 100, ease: "none",
      scrollTrigger: { trigger: box, start: "top bottom", end: "bottom top", scrub: true } });
  });

  /* ---------- foto che si scopre con un taglio ---------- */
  var tagli = { su: "inset(100% 0% 0% 0%)", sinistra: "inset(0% 100% 0% 0%)", destra: "inset(0% 0% 0% 100%)", giu: "inset(0% 0% 100% 0%)" };
  tutti("[data-he-wipe]").forEach(function (box) {
    var da = tagli[box.getAttribute("data-he-wipe")] || tagli.su;
    var img = box.querySelector("img,video");
    var tl = gsap.timeline({ scrollTrigger: { trigger: box, start: "top 82%", once: true } });
    tl.fromTo(box, { clipPath: da }, { clipPath: "inset(0% 0% 0% 0%)", duration: 1.35, ease: "expo.inOut" });
    if (img && !box.hasAttribute("data-he-parallax")) tl.fromTo(img, { scale: 1.18 }, { scale: 1, duration: 1.8, ease: "expo.out" }, 0);
  });

  /* ---------- galleria orizzontale ---------- */
  tutti("[data-he-horizontal]").forEach(function (sec) {
    var binario = sec.querySelector(".he-oriz-binario");
    if (!binario) return;
    var barra = sec.querySelector(".he-oriz-progresso i");
    mm.add("(min-width: 900px)", function () {
      var dist = function () { return Math.max(0, binario.scrollWidth - window.innerWidth); };
      gsap.to(binario, { x: function () { return -dist(); }, ease: "none",
        scrollTrigger: { trigger: sec, start: "top top", end: function () { return "+=" + dist(); }, pin: true, scrub: 0.7,
          invalidateOnRefresh: true, anticipatePin: 1,
          onUpdate: function (self) { if (barra) barra.style.transform = "scaleX(" + self.progress.toFixed(4) + ")"; } } });
    });
  });

  /* ---------- racconto con immagine ferma ---------- */
  tutti("[data-he-story]").forEach(function (sec) {
    var media = tutti(".he-storia-media > *", sec);
    var passi = tutti(".he-passo", sec);
    var attiva = function (i) {
      media.forEach(function (m, j) { m.classList.toggle("attivo", j === i); m.classList.toggle("spento", j !== i); });
      passi.forEach(function (p, j) { p.classList.toggle("attivo", j === i); });
    };
    passi.forEach(function (p, i) {
      ScrollTrigger.create({ trigger: p, start: "top 55%", end: "bottom 55%",
        onEnter: function () { attiva(i); }, onEnterBack: function () { attiva(i); } });
    });
  });

  /* ---------- un numero vero che sale ---------- */
  tutti("[data-he-conta]").forEach(function (el) {
    var fine = parseFloat(el.getAttribute("data-he-conta"));
    if (isNaN(fine)) return;
    var o = { v: 0 };
    var fmt = new Intl.NumberFormat("it-IT");
    gsap.to(o, { v: fine, duration: 1.6, ease: "power3.out", scrollTrigger: { trigger: el, start: "top 85%", once: true },
      onUpdate: function () { el.textContent = fmt.format(Math.round(o.v)); } });
  });

  /* ---------- testata ---------- */
  var testa = document.querySelector("[data-he-header]");
  if (testa) {
    ScrollTrigger.create({ start: 0, end: "max", onUpdate: function (self) {
      var y = self.scroll();
      // sul telefono la testata resta sempre visibile: e' quella che porta il numero
      testa.classList.toggle("nascosta", self.direction === 1 && y > 240 && window.innerWidth >= 900);
      testa.classList.toggle("scorsa", y > 40);
    } });
    var dopo = testa.getAttribute("data-he-chiara-dopo");
    if (dopo && document.querySelector(dopo)) {
      ScrollTrigger.create({ trigger: dopo, start: "bottom top", onEnter: function () { testa.classList.add("chiara"); },
        onLeaveBack: function () { testa.classList.remove("chiara"); } });
    }
  }

  window.addEventListener("load", function () { ScrollTrigger.refresh(); });
})();
