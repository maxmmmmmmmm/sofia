/* ==========================================================================
   SOFIA FILATOVA — behaviour
   Vanilla, no dependencies, no build step. Every feature is optional: each
   one bails out quietly if its markup is not on the page, so you can paste
   individual blocks into Tilda in any combination.
   ========================================================================== */

(function () {
  "use strict";

  var $  = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  // The standalone site has one .sf-root wrapping the page. On Tilda every
  // pasted block is its own .sf-root, so anything that reads or writes root
  // state has to cope with a list.
  var roots = $$(".sf-root");
  if (!roots.length) return;
  var root = roots[0];

  /* ------------------------------------------------------------------
     Language — RU / EN, remembered between visits
     ------------------------------------------------------------------ */

  var LANG_KEY = "sf-lang";

  function applyLang(lang) {
    roots.forEach(function (r) { r.setAttribute("data-lang", lang); });
    document.documentElement.setAttribute("lang", lang);
    $$(".sf-lang__btn").forEach(function (btn) {
      btn.classList.toggle("is-active", btn.dataset.lang === lang);
      btn.setAttribute("aria-pressed", String(btn.dataset.lang === lang));
    });
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* private mode */ }

    // Язык выбирает город в прайсе: русскому посетителю показываем Москву,
    // англоязычному — Лиссабон. Ручной выбор вкладки живёт до следующей
    // смены языка.
    showCity(lang === "ru" ? "moscow" : "lisbon");
  }

  function showCity(city) {
    var tabs = $$(".sf-tab");
    if (!tabs.length) return;
    tabs.forEach(function (t) {
      var on = t.dataset.city === city;
      t.classList.toggle("is-active", on);
      t.setAttribute("aria-selected", String(on));
    });
    $$(".sf-pricelist").forEach(function (list) {
      list.hidden = list.dataset.city !== city;
    });
  }

  (function initLang() {
    var saved;
    try { saved = localStorage.getItem(LANG_KEY); } catch (e) { saved = null; }

    var start;
    if (saved === "ru" || saved === "en") {
      start = saved;
    } else {
      start = (navigator.language || "").toLowerCase().indexOf("ru") === 0 ? "ru" : "en";
    }
    applyLang(start);

    $$(".sf-lang__btn").forEach(function (btn) {
      btn.addEventListener("click", function () { applyLang(btn.dataset.lang); });
    });
  })();

  /* ------------------------------------------------------------------
     Header: shadow once scrolled, mobile drawer
     ------------------------------------------------------------------ */

  (function initHeader() {
    var header = $(".sf-header");
    if (header) {
      var onScroll = function () {
        header.classList.toggle("is-stuck", window.scrollY > 8);
      };
      onScroll();
      window.addEventListener("scroll", onScroll, { passive: true });
    }

    var burger = $(".sf-burger");
    var drawer = $(".sf-drawer");
    if (!burger || !drawer) return;

    var setOpen = function (open) {
      burger.classList.toggle("is-open", open);
      drawer.classList.toggle("is-open", open);
      burger.setAttribute("aria-expanded", String(open));
      document.body.classList.toggle("sf-noscroll", open);
    };

    burger.addEventListener("click", function () {
      setOpen(!drawer.classList.contains("is-open"));
    });
    $$(".sf-drawer__link", drawer).forEach(function (a) {
      a.addEventListener("click", function () { setOpen(false); });
    });
    window.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });
    // A resize past the desktop breakpoint should not leave the body locked.
    window.addEventListener("resize", function () {
      if (window.innerWidth > 980) setOpen(false);
    });
  })();

  /* ------------------------------------------------------------------
     Price: city / currency tabs
     ------------------------------------------------------------------ */

  (function initPriceTabs() {
    var tabs = $$(".sf-tab");
    if (!tabs.length) return;

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () { showCity(tab.dataset.city); });
    });
  })();

  /* ------------------------------------------------------------------
     Сетка на главной заканчивается полным рядом
     ------------------------------------------------------------------ */

  (function initGridTrim() {
    var grid = $(".sf-homegrid .sf-mosaic");
    if (!grid) return;
    var items = $$(".sf-mosaic__item", grid);
    if (items.length < 4) return;

    function trim() {
      items.forEach(function (i) { i.hidden = false; });

      // Ряды не заданы разметкой — их складывает флексбокс, и на разной
      // ширине они разные. Границу ряда определяем по offsetTop.
      var rows = [], prev = null;
      items.forEach(function (i) {
        if (prev === null || i.offsetTop !== prev) { rows.push([]); prev = i.offsetTop; }
        rows[rows.length - 1].push(i);
      });
      if (rows.length < 2) return;

      var heights = rows.map(function (r) { return r[0].getBoundingClientRect().height; });
      var rest = heights.slice(0, -1).sort(function (a, b) { return a - b; });
      var median = rest[Math.floor(rest.length / 2)];

      // Неполный ряд флексбокс растягивает по ширине, и он выходит заметно
      // выше остальных. Это и есть признак хвоста.
      if (heights[heights.length - 1] > median * 1.25) {
        rows[rows.length - 1].forEach(function (i) { i.hidden = true; });
      }
    }

    trim();
    window.addEventListener("resize", trim);
  })();

  /* ------------------------------------------------------------------
     Lightbox
     ------------------------------------------------------------------ */

  (function initLightbox() {
    var triggers = $$(".sf-mosaic__btn");
    var box = $(".sf-lightbox");
    if (!triggers.length || !box) return;

    var stageImg = $(".sf-lightbox__stage img", box);
    var counter  = $(".sf-lightbox__count", box);
    var index    = 0;
    var lastFocus = null;
    var timer = null;          // показ серии по очереди

    var SLIDE_MS = 3600;

    function stopShow() {
      if (timer) { window.clearInterval(timer); timer = null; }
      box.classList.remove("is-playing");
    }

    function startShow() {
      stopShow();
      box.classList.add("is-playing");
      timer = window.setInterval(function () { show(index + 1); }, SLIDE_MS);
    }

    function show(i) {
      index = (i + triggers.length) % triggers.length;
      var trigger = triggers[index];
      stageImg.src = trigger.dataset.full || $("img", trigger).src;
      stageImg.alt = trigger.dataset.alt || "";
      if (counter) counter.textContent = (index + 1) + " / " + triggers.length;
      if (timer) {                     // перезапуск полосы отсчёта
        var bar = $(".sf-lightbox__bar", box);
        if (bar) { bar.style.animation = "none"; void bar.offsetWidth; bar.style.animation = ""; }
      }
      preload(index + 1);
      preload(index - 1);
    }

    function preload(i) {
      var t = triggers[(i + triggers.length) % triggers.length];
      if (!t) return;
      var pre = new Image();
      pre.src = t.dataset.full || "";
    }

    function open(i, play) {
      lastFocus = document.activeElement;
      show(i);
      box.classList.add("is-open");
      box.setAttribute("aria-hidden", "false");
      document.body.classList.add("sf-noscroll");
      var closeBtn = $(".sf-lightbox__close", box);
      if (closeBtn) closeBtn.focus();
      if (play) startShow();
    }

    function close() {
      stopShow();
      box.classList.remove("is-open");
      box.setAttribute("aria-hidden", "true");
      document.body.classList.remove("sf-noscroll");
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }

    triggers.forEach(function (t, i) {
      t.addEventListener("click", function () { open(i); });
    });



    var closeBtn = $(".sf-lightbox__close", box);
    var prevBtn  = $(".sf-lightbox__prev", box);
    var nextBtn  = $(".sf-lightbox__next", box);
    if (closeBtn) closeBtn.addEventListener("click", close);
    if (prevBtn)  prevBtn.addEventListener("click", function () { stopShow(); show(index - 1); });
    if (nextBtn)  nextBtn.addEventListener("click", function () { stopShow(); show(index + 1); });

    // Click the backdrop (but not the photo or the controls) to dismiss
    box.addEventListener("click", function (e) {
      if (e.target === box || e.target.classList.contains("sf-lightbox__stage")) close();
    });

    window.addEventListener("keydown", function (e) {
      if (!box.classList.contains("is-open")) return;
      if (e.key === "Escape")     { close(); }
      if (e.key === "ArrowLeft")  { stopShow(); show(index - 1); }
      if (e.key === "ArrowRight") { stopShow(); show(index + 1); }
    });

    // Swipe on touch
    var startX = null;
    box.addEventListener("touchstart", function (e) {
      startX = e.changedTouches[0].clientX;
    }, { passive: true });
    box.addEventListener("touchend", function (e) {
      if (startX === null) return;
      var dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) > 48) { stopShow(); show(index + (dx < 0 ? 1 : -1)); }
      startX = null;
    }, { passive: true });
  })();

  /* ------------------------------------------------------------------
     Booking dialog — three ways to get in touch
     ------------------------------------------------------------------ */

  (function initBooking() {
    var box = $(".sf-booking");
    var triggers = $$("[data-booking]");
    if (!box || !triggers.length) return;

    var lastFocus = null;

    function open() {
      lastFocus = document.activeElement;
      box.classList.add("is-open");
      box.setAttribute("aria-hidden", "false");
      document.body.classList.add("sf-noscroll");
      var first = $(".sf-booking__row", box);
      if (first) first.focus();
    }

    function close() {
      stopShow();
      box.classList.remove("is-open");
      box.setAttribute("aria-hidden", "true");
      document.body.classList.remove("sf-noscroll");
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }

    triggers.forEach(function (btn) {
      btn.addEventListener("click", open);
    });

    var closeBtn = $(".sf-booking__close", box);
    if (closeBtn) closeBtn.addEventListener("click", close);

    // Backdrop only — a click on the panel itself must not dismiss it.
    box.addEventListener("click", function (e) {
      if (e.target === box) close();
    });

    window.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && box.classList.contains("is-open")) close();
    });

    // Picking a messenger leaves the page; drop the lock so returning via the
    // back button does not land on a frozen page.
    $$(".sf-booking__row", box).forEach(function (a) {
      a.addEventListener("click", close);
    });
  })();

  /* ------------------------------------------------------------------
     Смена экранов: гасим страницу перед переходом
     ------------------------------------------------------------------ */

  (function initExitFade() {
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    var FADE_MS = 260;

    $$("a[href]").forEach(function (a) {
      var url = a.getAttribute("href");
      if (!url) return;
      // Якоря, внешние ссылки и мессенджеры уводят со страницы сами —
      // гасить её под ними незачем.
      if (url.charAt(0) === "#") return;
      if (a.target === "_blank") return;
      if (/^[a-z][a-z0-9+.-]*:/i.test(url)) return;

      a.addEventListener("click", function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
        e.preventDefault();
        document.body.classList.add("sf-leaving");
        window.setTimeout(function () { window.location.href = url; }, FADE_MS);
      });
    });

    // Возврат «назад» может отдать страницу из кеша уже погашенной.
    window.addEventListener("pageshow", function () {
      document.body.classList.remove("sf-leaving");
    });
  })();

  /* ------------------------------------------------------------------
     Контакты: кнопка раскрывает три канала
     ------------------------------------------------------------------ */

  (function initReach() {
    $$(".sf-reach").forEach(function (box) {
      var btn = $(".sf-reach__open", box);
      var list = $(".sf-reach__list", box);
      if (!btn || !list) return;

      btn.addEventListener("click", function () {
        list.hidden = false;
        // hidden снимаем раньше класса, иначе переход не проиграет: элемент
        // появляется уже в конечном состоянии. Начальное состояние закрепляем
        // принудительным пересчётом, а не requestAnimationFrame: в фоновой
        // вкладке кадр может не наступить, и ссылки застряли бы на opacity 0.
        void list.offsetWidth;
        box.classList.add("is-open");
        btn.setAttribute("aria-expanded", "true");
      });
    });
  })();

})();
