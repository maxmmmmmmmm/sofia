#!/usr/bin/env python3
"""
BUILD
=====
    python3 src/build.py

Reads content.py + photos.py and writes:

  • the standalone site  → *.html in the project root
  • the Tilda paste-kit  → tilda/*.html

Both come from the same source, so what you preview locally is exactly what
you paste into Tilda. Standard library only — nothing to install.
"""

import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import content as C          # noqa: E402
import photos as P           # noqa: E402

SITE, UI, PAGES, NAV_ORDER = C.SITE, C.UI, C.PAGES, C.NAV_ORDER


# --------------------------------------------------------------- helpers

def t(v):
    """Bilingual inline text. Plain strings pass straight through."""
    if isinstance(v, str):
        return v
    return '<span data-l="en">%s</span><span data-l="ru">%s</span>' % (v["en"], v["ru"])


def tb(v, tag="div", cls=""):
    """
    Bilingual block-level text: ONE element carrying both languages as inline
    spans, rather than one element per language. That keeps a page to a single
    <h1> — duplicating the element would give every page two, one of them
    hidden, which is exactly the shape search engines dislike.
    """
    attr = ' class="%s"' % cls if cls else ""
    return "<%s%s>%s</%s>" % (tag, attr, t(v), tag)


def a(v):
    """Bilingual value for an HTML attribute — English is the SEO default."""
    return v if isinstance(v, str) else v["en"]


def indent(html, pad):
    return "\n".join(pad + line if line.strip() else line for line in html.split("\n"))


def asset_version(rel):
    """?v=<mtime> on the local CSS and JS. Without it a browser keeps serving
    the stylesheet it cached, and an edit looks like it did nothing — which is
    confusing enough to waste an afternoon. Irrelevant on Tilda, where the CSS
    lives inline in HEAD."""
    full = os.path.join(ROOT, rel)
    try:
        return "%s?v=%d" % (rel, int(os.path.getmtime(full)))
    except OSError:
        return rel


def sm(path):
    """Grid-sized variant beside the full one: love/03.jpg → love/03@sm.jpg.
    Written by tools/fetch_photos.py."""
    stem, ext = os.path.splitext(path)
    return stem + "@sm" + ext


# ------------------------------------------------------------ components

def mosaic(items, alt_text, eager=0):
    """
    Justified gallery. Each figure carries --ar (width/height); the CSS turns
    that into equal-height rows with no JavaScript layout pass.
    """
    figures = []
    for i, entry in enumerate(items):
        path, ar = entry[0], entry[1]
        full = P.BASE + path              # lightbox
        thumb = P.BASE + sm(path)         # grid
        w = 800
        h = round(w / ar)
        loading = "eager" if i < eager else "lazy"
        priority = ' fetchpriority="high"' if i < eager else ""
        figures.append(
            '  <figure class="sf-mosaic__item" style="--ar:%s">\n'
            '    <button class="sf-mosaic__btn" type="button" data-full="%s" data-alt="%s">\n'
            '      <img src="%s" alt="%s" width="%d" height="%d" loading="%s" decoding="async"%s>\n'
            "    </button>\n"
            "  </figure>" % (ar, full, alt_text, thumb, alt_text, w, h, loading, priority)
        )

    # Invisible tail items so the final row keeps roughly the target height
    # instead of blowing two photos up across the whole viewport.
    fillers = "\n" + "\n".join(
        '  <i class="sf-mosaic__fill" style="--ar:%s" aria-hidden="true"></i>' % ar
        for ar in (0.75, 0.67, 0.8, 1.33, 0.7)
    )

    return '<div class="sf-mosaic">\n%s%s\n</div>' % ("\n".join(figures), fillers)


def lightbox():
    return """<div class="sf-lightbox" role="dialog" aria-modal="true" aria-hidden="true">
  <button class="sf-lightbox__btn sf-lightbox__close" type="button" aria-label="%s">
    <svg viewBox="0 0 24 24"><path d="M5 5l14 14M19 5L5 19"/></svg>
  </button>
  <button class="sf-lightbox__btn sf-lightbox__prev" type="button" aria-label="%s">
    <svg viewBox="0 0 24 24"><path d="M15 4L7 12l8 8"/></svg>
  </button>
  <div class="sf-lightbox__stage"><img alt=""></div>
  <button class="sf-lightbox__btn sf-lightbox__next" type="button" aria-label="%s">
    <svg viewBox="0 0 24 24"><path d="M9 4l8 8-8 8"/></svg>
  </button>
  <div class="sf-lightbox__count"></div>
  <div class="sf-lightbox__bar"></div>
</div>""" % (a(UI["close"]), a(UI["prev"]), a(UI["next"]))


def header(current):
    def link(key, cls):
        p = PAGES[key]
        active = " is-active" if key == current else ""
        return '<a class="%s%s" href="%s">%s</a>' % (cls, active, p["file"], t(p["nav"]))

    nav_links = "\n".join("    " + link(k, "sf-header__link") for k in NAV_ORDER)
    drawer_links = "\n".join("  " + link(k, "sf-drawer__link") for k in NAV_ORDER)

    return """<header class="sf-header">
  <nav class="sf-header__nav" aria-label="%s">
%s
  </nav>

  <button class="sf-burger" type="button" aria-label="%s" aria-expanded="false">
    <span></span><span></span>
  </button>

  <div class="sf-header__side">
    <div class="sf-lang">
      <button class="sf-lang__btn" type="button" data-lang="en">EN</button>
      <span class="sf-lang__sep">/</span>
      <button class="sf-lang__btn" type="button" data-lang="ru">RU</button>
    </div>
    <a class="sf-logo" href="%s">%s</a>
  </div>
</header>

<div class="sf-drawer">
%s
</div>""" % (
        a(UI["menu"]), nav_links, a(UI["menu"]),
        PAGES["home"]["file"], SITE["wordmark"], drawer_links,
    )


ICONS = {
    "instagram": '<path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.2.05 1.8.25 2.2.42.6.22 1 .48 1.4.9.43.43.7.83.92 1.4.17.42.37 1.06.42 2.25.06 1.28.07 1.66.07 4.9s0 3.6-.07 4.9c-.05 1.2-.25 1.8-.42 2.2-.22.6-.5 1-.92 1.4-.42.43-.82.7-1.4.92-.42.17-1.06.37-2.25.42-1.28.06-1.66.07-4.9.07s-3.6 0-4.9-.07c-1.2-.05-1.8-.25-2.2-.42-.6-.22-1-.5-1.4-.92-.43-.42-.7-.82-.92-1.4-.17-.42-.37-1.06-.42-2.25C2.2 15.6 2.2 15.2 2.2 12s0-3.6.07-4.9c.05-1.2.25-1.8.42-2.2.22-.6.5-1 .92-1.4.42-.43.82-.7 1.4-.92.42-.17 1.06-.37 2.25-.42C8.4 2.2 8.8 2.2 12 2.2Z"/><circle cx="12" cy="12" r="3.8"/><circle cx="17.4" cy="6.6" r="1"/>',
    "telegram": '<path d="M21.5 4.3 2.9 11.4c-.9.35-.9.86-.16 1.08l4.7 1.47 1.8 5.5c.22.6.4.83.86.83.36 0 .52-.16.72-.36l2.2-2.14 4.6 3.4c.84.46 1.44.22 1.65-.78l3-14.1c.3-1.22-.48-1.78-1.28-1.42Z"/>',
    "whatsapp": '<path d="M20.5 11.7a8.4 8.4 0 0 1-12.4 7.4L3.5 20.5l1.4-4.5A8.4 8.4 0 1 1 20.5 11.7Z"/><path d="M8.9 8.2c.2-.5.4-.5.6-.5h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2 0 .4-.1.6l-.4.5c-.1.2-.3.4-.1.7a6 6 0 0 0 2.8 2.5c.3.1.5 0 .7-.1l.6-.7c.2-.2.4-.2.6-.1l1.8.9c.2.1.4.2.4.4v.5c0 .8-.7 1.5-1.5 1.6-1 .1-2-.2-4-1.4a9.4 9.4 0 0 1-3.5-4.1c-.4-1.1-.3-2.2.2-2.7Z"/>',
    "phone": '<path d="M6.2 3.5h3l1.5 3.7-1.9 1.4a12 12 0 0 0 5.6 5.6l1.4-1.9 3.7 1.5v3a1.7 1.7 0 0 1-1.9 1.7A16.5 16.5 0 0 1 4.5 5.4 1.7 1.7 0 0 1 6.2 3.5Z"/>',
    "email": '<rect x="2.6" y="5" width="18.8" height="14" rx="1.6"/><path d="m3.4 6.4 8.6 6.2 8.6-6.2"/>',
}


def social_row(extra=""):
    """Icon links, matching the reference's small glyph row. `extra` adds a
    modifier class — it must not replace sf-social, which carries the layout."""
    links = [
        ("instagram", SITE["instagram"]["href"], "Instagram"),
        ("telegram", SITE["telegram"]["href"], "Telegram"),
        ("whatsapp", SITE["whatsapp"]["href"], "WhatsApp"),
    ]
    out = ['<div class="sf-social%s">' % ((" " + extra) if extra else "")]
    for key, href, label in links:
        blank = "" if key == "email" else ' target="_blank" rel="noopener"'
        out.append(
            '  <a href="%s"%s aria-label="%s">'
            '<svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></a>'
            % (href, blank, label, ICONS[key])
        )
    out.append("</div>")
    return "\n".join(out)


def footer(extra_class=""):
    return """<footer class="sf-footer%s">
%s
  <div class="sf-footer__legal">© %d %s</div>
</footer>""" % (extra_class, indent(social_row("sf-footer__social"), "  "), SITE["year"], SITE["wordmark"])


def lead_block():
    """Финальная строка перед футером: запись не отделяется от страницы
    самостоятельной секцией, а завершает просмотр вместе с соцсетями."""
    ch = C.CONTACT["channels"]
    links = "\n".join(
        '      <a class="sf-reach__link" href="%s" target="_blank" rel="noopener">%s</a>'
        % (href, t(label))
        for href, label in (
            (SITE["telegram"]["href"], ch["telegram"]),
            (SITE["whatsapp"]["href"], ch["whatsapp"]),
            (SITE["instagram"]["href"], ch["instagram"]),
        )
    )
    return """<section class="sf-lead-in sf-lead-in--footer">
  <div class="sf-reach">
    <button class="sf-reach__open" type="button" aria-expanded="false">%s<span class="sf-lead-in__arrow" aria-hidden="true">→</span></button>
    <div class="sf-reach__list" hidden>
%s
    </div>
  </div>
</section>""" % (t(C.LEAD["title"]), links)
# ------------------------------------------------------------ home parts
def home_strapline():
    """Три строки капслоком над сеткой: чем занимается, как зовут, где снимает.
    На телефоне это единственный текст на первом экране, поэтому он и держит
    страницу; на компьютере всё то же сообщение уже несёт шапка."""
    return """<section class="sf-strapline">
  <p class="sf-strapline__line">CINEMATIC &amp; VINTAGE PHOTOGRAPHER</p>
  <p class="sf-strapline__name">SOFIA FILATOVA</p>
  %s
</section>""" % tb(C.HOME["places"], "p", "sf-strapline__line")


def home_grid():
    """Сетка избранных кадров — только на компьютере.

    Собирается тем же mosaic(), что и галереи: пропорции берутся из общего
    списка, поэтому при замене снимка ряды пересчитаются сами."""
    ratios = {n: a for n, a, _ in P.PORTRAITS + P.STREET + P.LOVE}
    items = [(n, ratios[n]) for n in P.BEST]
    return '<div class="sf-homegrid">\n%s\n</div>' % indent(
        mosaic(items, "Sofia Filatova", eager=8), "  ")


def home_tagline():
    """Строка под сеткой: зачем смотреть дальше. Только на компьютере —
    на телефоне под ней сразу идут три раздела, и звать никуда не нужно."""
    return '<section class="sf-tagline">\n  %s\n</section>' % tb(
        C.HOME["tagline"], "p", "sf-tagline__text")
# --------------------------------------------------------- other blocks

def about_block():
    prose = lambda lang: "\n        ".join("<p>%s</p>" % p for p in C.ABOUT["body"][lang])

    return """<section class="sf-sect sf-wrap">
  <div class="sf-split sf-split--narrow">
    <div class="sf-split__media">
      <img src="%s" alt="Sofia Filatova" width="1200" height="1200" loading="eager" decoding="async">
    </div>
    <div class="sf-split__body">
      <h1 class="sf-abouttitle">
        %s
        <span class="sf-abouttitle__role">%s</span>
      </h1>
      <div class="sf-lead" style="margin-top:1.5em">
        <div data-l="en">
        %s
        </div>
        <div data-l="ru">
        %s
        </div>
      </div>
    </div>
  </div>
</section>""" % (
        P.SELF_PORTRAIT,
        t(C.ABOUT["title"]), t(C.ABOUT["role"]),
        prose("en"), prose("ru"),
    )


def gallery_block(key):
    """Название раздела строкой над сеткой, по центру страницы."""
    g = C.GALLERIES[key]
    return """<section class="sf-pagehead">
  %s
</section>

%s""" % (
        tb(g["title"], "h1", "sf-pagehead__title"),
        mosaic(P.GALLERIES[key], "%s — Sofia Filatova" % a(g["title"]), eager=6),
    )


def process_block():
    """Четыре шага съёмки. Стоит перед пакетами: человек сначала понимает,
    как это будет происходить, и только потом смотрит на цены."""
    steps = "\n".join(
        '    <li class="sf-step">\n'
        '      <span class="sf-step__n">%s</span>\n'
        '      <div>\n'
        '        <h3 class="sf-step__name">%s</h3>\n'
        '        %s\n'
        '      </div>\n'
        '    </li>' % (st["n"], t(st["name"]), tb(st["text"], "p", "sf-step__text"))
        for st in C.PROCESS["steps"]
    )
    return """<section class="sf-sect sf-wrap sf-process">
  %s
  <ol class="sf-steps">
%s
  </ol>
</section>""" % (tb(C.PROCESS["title"], "h2", "sf-sectitle"), steps)


def price_block():
    tabs = "\n".join(
        '    <button class="sf-tab%s" type="button" role="tab" aria-selected="%s" data-city="%s">%s</button>'
        % (" is-active" if i == 0 else "", "true" if i == 0 else "false", c["id"], t(c["label"]))
        for i, c in enumerate(C.PRICE["cities"])
    )

    def pack(p):
        items = "\n".join("        <li>%s</li>" % t(it) for it in p["items"])
        return """    <article class="sf-pack">
      <div class="sf-pack__media">
        <img src="%s" alt="%s" width="1000" height="1250" loading="lazy" decoding="async">
      </div>
      <div class="sf-pack__body">
        <h2 class="sf-pack__name">%s</h2>
        <p class="sf-pack__price">%s</p>
        <ul class="sf-pack__list">
%s
        </ul>
        <div class="sf-pack__extras">
          <strong>%s</strong>
          %s
        </div>
      </div>
    </article>""" % (
            sm(P.PRICE_SHOTS[p["shot"]]), a(p["name"]),
            t(p["name"]), t(p["cost"]), items,
            t(UI["extras"]), tb(p["extras"], "span"),
        )

    def city_list(city_id, hidden):
        return '  <div class="sf-pricelist" data-city="%s"%s>\n%s\n  </div>' % (
            city_id,
            " hidden" if hidden else "",
            "\n".join(pack(p) for p in C.PRICE["packages"][city_id]),
        )

    return """<section class="sf-pagehead sf-pricehead">
  %s
</section>

<section class="sf-wrap" style="padding-bottom:var(--sf-sect-y)">
  <div class="sf-tabs" role="tablist">
%s
  </div>

%s
%s
</section>""" % (
        tb(PAGES["price"]["nav"], "h1", "sf-pagehead__title"),
        tabs, city_list("lisbon", False), city_list("moscow", True),
    )


def contact_details():
    """Версия для Tilda: тот же список каналов, без фото — снимок там ставится
    родным блоком, поэтому в коде не остаётся ни одной ссылки на файл."""
    return '<section class="sf-sect sf-wrap">\n  <div class="sf-reach">\n%s\n  </div>\n</section>' % reach_list("    ")


def reach(indent_by="    ", label=None):
    """Одна кнопка по центру. По нажатию раскрываются три канала — только
    названия, без ников и номеров: ссылка и так ведёт в нужный аккаунт.

    label позволяет подставить свою подпись: под галереей кнопкой служит сама
    фраза «Расскажите, что снимаем», на «Контактах» — короткое «связаться»."""
    ch = C.CONTACT["channels"]
    rows = [
        ("telegram",  SITE["telegram"]["href"],  ch["telegram"]),
        ("whatsapp",  SITE["whatsapp"]["href"],  ch["whatsapp"]),
        ("instagram", SITE["instagram"]["href"], ch["instagram"]),
    ]
    links = "\n".join(
        '%s    <a class="sf-reach__link" href="%s" target="_blank" rel="noopener">%s</a>'
        % (indent_by, href, t(label)) for _key, href, label in rows
    )
    return """%s<div class="sf-reach">
%s  <button class="sf-reach__open" type="button" aria-expanded="false">%s</button>
%s  <div class="sf-reach__list" hidden>
%s
%s  </div>
%s</div>""" % (indent_by, indent_by, t(label or C.CONTACT["open"]), indent_by, links, indent_by, indent_by)


def contact_details():
    """Версия для Tilda — та же кнопка, без фотографии."""
    return '<section class="sf-sect sf-wrap sf-contactpage">\n  %s\n</section>' % tb(
        PAGES["contact"]["nav"], "h1", "sf-vh") + "\n" + reach("  ")


def contact_block():
    """Контакты поверх одного кадра.

    «Телефон» стоит последним и показывается только в русской версии: ссылка
    ведёт на звонок, англоязычному посетителю российский номер бесполезен.
    Прячет её CSS по data-lang, поэтому переключение языка работает без
    перезагрузки страницы."""
    return """<section class="sf-contactpage">
  %s
  <img class="sf-contactpage__photo" src="assets/img/home/launch-01.jpg" alt="" width="1200" height="1800" loading="eager" decoding="async">
  <div class="sf-contactpage__shade" aria-hidden="true"></div>
  <nav class="sf-contactpage__channels" aria-label="Contacts">
    <a href="%s" target="_blank" rel="noopener">Telegram</a>
    <a href="%s" target="_blank" rel="noopener">WhatsApp</a>
    <a href="%s" target="_blank" rel="noopener">Instagram</a>
    <a class="sf-contactpage__phone" href="%s">Телефон</a>
  </nav>
</section>""" % (
        tb(PAGES["contact"]["nav"], "h1", "sf-vh"),
        SITE["telegram"]["href"], SITE["whatsapp"]["href"], SITE["instagram"]["href"],
        SITE["phone_ru"]["href"],
    )


# ------------------------------------------------------------ page shell

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400'
    '&amp;family=Cormorant+SC:wght@400'
    '&amp;family=Jost:wght@300;400;500&amp;display=swap">'
)


def page(key, body, has_gallery, body_class=""):
    m = C.META[key]
    return """<!doctype html>
<html lang="en" class="sf-html">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%s</title>
  <meta name="description" content="%s">
  <meta property="og:title" content="%s">
  <meta property="og:description" content="%s">
  <meta property="og:type" content="website">
  <meta property="og:image" content="%s">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  %s
  <link rel="stylesheet" href="%s">
</head>
<body class="sf-body%s">
<div class="sf-root" data-lang="en">

%s

<main class="sf-main">

%s

</main>

%s
%s
</div>
<script src="%s"></script>
</body>
</html>
""" % (
        m["title"]["en"], m["description"]["en"],
        m["title"]["en"], m["description"]["en"],
        P.BASE + P.PORTRAITS[0][0],
        FONTS,
        asset_version("assets/css/style.css"),
        (" " + body_class) if body_class else "",
        header(key), body, footer(" sf-footer--contact" if key == "contact" else ""),
        "\n" + lightbox() if has_gallery else "",
        asset_version("assets/js/main.js"),
    )


# ------------------------------------------------------------------ emit

def write(rel, text):
    full = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("  ✓", rel)


def main():
    print("Building site…")

    write(PAGES["home"]["file"], page(
        "home",
        "\n\n".join([home_strapline(), home_grid(), home_tagline()]),
        body_class="sf-body--home",
        has_gallery=True,
    ))

    for key in ("portraits", "street", "love"):
        write(PAGES[key]["file"], page(
            key, "\n\n".join([gallery_block(key), lead_block()]), has_gallery=True,
        ))

    write(PAGES["about"]["file"], page("about", about_block(), has_gallery=False,
                                      body_class="sf-body--fit"))
    write(PAGES["price"]["file"], page(
        "price", "\n\n".join([process_block(), lead_block(), price_block()]),
        has_gallery=False))
    write(PAGES["contact"]["file"], page("contact", contact_block(), has_gallery=False))

    # ------------------------------------------------------ Tilda paste-kit
    print("Building Tilda blocks…")

    tilda_dir = os.path.join(ROOT, "tilda")
    if os.path.isdir(tilda_dir):
        for name in os.listdir(tilda_dir):
            if name.endswith(".html"):
                os.remove(os.path.join(tilda_dir, name))

    def banner(num, what, where):
        return (
            "<!-- ==========================================================\n"
            "     %s — %s\n"
            "     Куда: %s\n"
            "     ========================================================== -->\n"
            % (num, what, where)
        )

    def tilda_links(html):
        """index.html → /, portraits.html → /portraits, and so on. Tilda pages
        live at clean paths, not at .html files."""
        html = html.replace('href="%s"' % PAGES["home"]["file"], 'href="/"')
        for key, p in PAGES.items():
            if key == "home":
                continue
            html = html.replace('href="%s"' % p["file"], 'href="/%s"' % p["file"][:-5])
        return html

    # Each block gets its own .sf-root so the design tokens and the scoped
    # reset reach it. Several .sf-root elements on one page is fine.
    def block(num, what, where, html):
        return banner(num, what, where) + '<div class="sf-root">\n%s\n</div>\n' % indent(
            tilda_links(html), "  "
        )

    # Everything after the @tilda-cut sentinel is standalone-only html/body
    # styling that would fight Tilda's own page chrome.
    css = open(os.path.join(ROOT, "assets/css/style.css"), encoding="utf-8").read()
    tilda_css = css.split("/* @tilda-cut")[0]

    write("tilda/01-head-code.html",
          banner("01", "Шрифты + стили",
                 "Настройки сайта → Ещё → HTML-код для вставки внутрь HEAD")
          + FONTS + "\n<style>\n" + tilda_css.rstrip() + "\n</style>\n")

    write("tilda/02-header.html", block(
        "02", "Хедер + мобильное меню",
        "Блок T123 в самом верху страницы. Нужен закреплённый хедер — "
        "добавьте класс sf-header--fixed к <header>.",
        header("home")))

    write("tilda/03-home-strapline.html", block(
        "03", "Главная — скрытый заголовок для поиска",
        "Блок T123 на главной, в самом верху",
        '<section class="sf-hero">\n  %s\n  %s\n</section>' % (
            tb(C.HOME["hero_title"], "h1", "sf-vh"),
            tb(C.HOME["hero_sub"], "p", "sf-hero__sub"))))

    write("tilda/06b-lead-in.html", block(
        "06b", "Строка «съёмка по записи»",
        "Блок T123 в самом низу /portraits, /street, /love — под кнопкой «ещё». "
        "Сама строка и есть кнопка: по нажатию раскрываются три мессенджера.",
        lead_block()))

    write("tilda/07-page-title.html", block(
        "07", "Тихий заголовок страницы",
        "Блок T123 над родной галереей на /portraits, /street, /love. "
        "Замените текст на нужный раздел.",
        '<section class="sf-pagehead">\n  %s\n</section>' % tb(
            C.GALLERIES["portraits"]["title"], "h1", "sf-pagehead__title")))

    write("tilda/08-process.html", block(
        "08", "Как проходит съёмка — четыре шага",
        "Блок T123 на странице /price, НАД пакетами", process_block()))

    write("tilda/09-contact-details.html", block(
        "09", "Контакты — кадр во весь экран и три мессенджера",
        "Блок T123 на /contact, единственный на странице", contact_details()))

    write("tilda/10-footer.html", block(
        "10", "Футер", "Блок T123 внизу каждой страницы", footer()))

    js = open(os.path.join(ROOT, "assets/js/main.js"), encoding="utf-8").read()
    write("tilda/11-foot-code.html",
          banner("11", "Скрипт поведения",
                 "Настройки сайта → Ещё → HTML-код для вставки внутрь BODY (в самый низ)")
          + "<script>\n" + js.rstrip() + "\n</script>\n")

    # -------------------------------------------- проверка: картинок нет
    leftover = []
    for name in sorted(os.listdir(tilda_dir)):
        if not name.endswith(".html"):
            continue
        text = open(os.path.join(tilda_dir, name), encoding="utf-8").read()
        for chunk in text.split('"'):
            if chunk.startswith(P.BASE):
                leftover.append("%s -> %s" % (name, chunk))

    if leftover:
        print("\n  ВНИМАНИЕ: в блоках остались картинки:")
        for x in leftover:
            print("   ", x)
    else:
        print("\n  Картинок в блоках нет — вручную грузить нечего.")

    print("Done.")


if __name__ == "__main__":
    main()
