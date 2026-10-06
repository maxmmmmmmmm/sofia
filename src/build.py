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
import re
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

    # На телефоне в середине шапки вместо имени стоит название раздела. Это
    # копия заголовка, а не сам заголовок: настоящий h1 остаётся на странице,
    # спрятанный от глаз, — иначе читалка объявляла бы название дважды.
    if current in C.GALLERIES:
        label = C.GALLERIES[current]["title"]
    elif current == "price":
        label = PAGES[current]["nav"]
    else:
        label = None
    pagename = ('\n    <span class="sf-pagename" aria-hidden="true">%s</span>'
                % t(label)) if label else ""

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
    <a class="sf-logo" href="%s">%s</a>%s
  </div>
</header>

<div class="sf-drawer">
%s
</div>""" % (
        a(UI["menu"]), nav_links, a(UI["menu"]),
        PAGES["home"]["file"], SITE["wordmark"], pagename, drawer_links,
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


def footer(extra_class="", social=True):
    """Футер. На контактах иконки соцсетей не нужны: прямо над ними уже стоят
    те же каналы, крупно. На сайте их прячет правило по соседству с кадром,
    но в Tilda футер — отдельный блок, и дотянуться до него селектором
    неоткуда. Поэтому для той страницы собирается отдельный файл."""
    icons = (indent(social_row("sf-footer__social"), "  ") + "\n") if social else ""
    return """<footer class="sf-footer%s">
%s  <div class="sf-footer__legal">© %d %s</div>
</footer>""" % (extra_class, icons, SITE["year"], SITE["wordmark"])


ARROW = (
    '<svg class="sf-lead-in__arrow" viewBox="0 0 100 39" aria-hidden="true" '
    'focusable="false">'
    # древко: прямая постоянной толщины, 4.8 единицы из ста — та же доля,
    # что на присланном рисунке
    '<rect x="0" y="17.1" width="86" height="4.8"/>'
    # остриё: две дуги наружу от кончика к концам усов и две внутрь, к древку
    '<path d="M100 19.5C88 12 78 5 70 0c6 8 10 14 14 19.5'
    'C80 25 76 31 70 39c8-5 18-12 30-19.5Z"/>'
    "</svg>"
)


def lead_block():
    """Финальная строка страницы: она завершает просмотр и раскрывает каналы
    связи окном по центру экрана.

    «Телефон» стоит последним и показывается только в русской версии — тем же
    правилом, что и на странице контактов: российский номер англоязычному
    посетителю бесполезен. Прячет его CSS по data-lang, поэтому переключение
    языка работает без перезагрузки."""
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
    links += ('\n      <a class="sf-reach__link sf-reach__link--phone" href="%s">'
              'Телефон</a>' % SITE["phone_ru"]["href"])
    return """<section class="sf-lead-in sf-lead-in--footer">
  <div class="sf-reach">
    <button class="sf-reach__open" type="button" aria-expanded="false">%s%s</button>
    <div class="sf-reach__list" role="dialog" aria-modal="true" aria-label="%s" tabindex="-1" hidden>
      <button class="sf-reach__close" type="button" aria-label="%s">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>
      </button>
%s
    </div>
  </div>
</section>""" % (t(C.LEAD["title"]), ARROW, a(C.LEAD["title"]), a(UI["close"]), links)
# ------------------------------------------------------------ home parts
def home_strapline():
    """Три строки капслоком над сеткой: чем занимается, как зовут, где снимает.
    На телефоне это единственный текст на первом экране, поэтому он и держит
    страницу; на компьютере всё то же сообщение уже несёт шапка."""
    # Имя набрано абзацем, а не заголовком: это подпись, а не название
    # страницы. Настоящий h1 стоит рядом, спрятанный от глаз, — без него
    # главная была единственной страницей сайта вообще без заголовка.
    return """<section class="sf-strapline">
  %s
  <p class="sf-strapline__line">CINEMATIC &amp; VINTAGE PHOTOGRAPHER</p>
  <p class="sf-strapline__name">SOFIA FILATOVA</p>
  %s
</section>""" % (tb(C.HOME["hero_title"], "h1", "sf-vh"),
                 tb(C.HOME["places"], "p", "sf-strapline__line"))


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
      <div class="sf-lead" style="margin-top:40px">
        <div data-l="en" lang="en">
        %s
        </div>
        <div data-l="ru" lang="ru">
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
    как это будет происходить, и только потом смотрит на цены. Позвать на
    съёмку посреди страницы нечем — строка записи ждёт внизу, как в галереях."""
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

    def extras(v):
        """Дополнения — список, а не сплошная строка. Каждый пункт обёрнут
        отдельно и не переносится внутри себя: не влез — уходит на новую
        строку целиком. Точку-разделитель ставит CSS, поэтому в тексте её
        нет и она не отрывается от своего пункта."""
        def one(lang):
            return "".join('<span class="sf-pack__extra">%s</span>\n          ' % part.strip()
                           for part in v[lang].split("·"))
        return ('<span data-l="en">%s</span><span data-l="ru">%s</span>'
                % (one("en"), one("ru")))

    def pack(p):
        """Пакет. Три части необязательны, и каждая отсутствует осмысленно.

        Сумма: у концепт-съёмки её нет — цена собирается под замысел, и на
        месте цифры стоит условие. Пустой строки в этом месте не остаётся ни
        в одном из двух случаев.

        Дополнения: тоже только у пакетов с фиксированной суммой.

        Сноска: про дорогу к океану — в студию ехать никуда не нужно."""
        body = [tb(p["name"], "h2", "sf-pack__name")]

        # Строка вместо суммы — тот же элемент на том же месте, что цена:
        # под названием. Отличается только кеглем, его задаёт модификатор.
        if p.get("cost"):
            body.append('<p class="sf-pack__price">%s</p>' % t(p["cost"]))
        elif p.get("terms"):
            body.append('<p class="sf-pack__price sf-pack__price--request">%s<br>%s</p>'
                        % (t(p["terms"]["lead"]), t(p["terms"]["rest"])))

        body.append('<ul class="sf-pack__list">\n%s\n        </ul>'
                    % "\n".join("          <li>%s</li>" % t(it) for it in p["items"]))

        if p.get("extras"):
            note = ("\n          %s" % tb(p["note"], "span", "sf-pack__note")
                    if p.get("note") else "")
            body.append('<div class="sf-pack__extras">\n          <strong>%s</strong>\n          %s%s\n        </div>'
                        % (t(UI["extras"]), extras(p["extras"]), note))

        return """    <article class="sf-pack">
      <div class="sf-pack__media">
        <img src="%s" alt="%s" width="1000" height="1250" loading="lazy" decoding="async">
      </div>
      <div class="sf-pack__body">
        %s
      </div>
    </article>""" % (
            P.PRICE_SHOTS[p["shot"]], a(p["name"]),
            "\n        ".join(body),
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

<section class="sf-wrap sf-pricebody">
  <div class="sf-tabs" role="tablist">
%s
  </div>

%s
%s
</section>""" % (
        tb(PAGES["price"]["nav"], "h1", "sf-pagehead__title"),
        tabs, city_list("lisbon", False), city_list("moscow", True),
    )


# Единственное место во всём наборе, куда нужно подставить адрес фотографии.
PHOTO_SLOT = "ВСТАВЬТЕ-СЮДА-АДРЕС-ФОТО"
PORTRAIT_SLOT = "ВСТАВЬТЕ-СЮДА-АДРЕС-ПОРТРЕТА"


def page_class(name):
    """Строка, которой блок помечает страницу своим классом.

    На сайте класс стоит в разметке, на теге body. В Tilda разметку страницы
    отдаёт она сама, и поставить его некому — а от него зависит и шапка
    (на галереях и цене вместо имени стоит название раздела), и отступы.
    Поэтому класс ставит сам блок, одной строкой при загрузке."""
    return ('\n<script>document.body.classList.add("%s");</script>' % name)


def tilda_price():
    """Пакеты цен для Tilda — нашей разметкой, а не родными блоками.

    Так сохраняются две вещи, которых родным блоком не получить:
    переключатель «Лиссабон / Москва» (он прячет и показывает наши списки,
    а родные блоки лежат вне них) и телефонная раскладка пакета — кадр в
    край экрана, условия колонкой рядом, блоки в шахматку.

    Платим за это тем, что шесть обложек меняются не перетаскиванием, а
    вставкой адреса: загрузили кадр в библиотеку Tilda, скопировали адрес,
    подставили вместо метки. Метки названы по городу и пакету.

    Собираем подменой самого справочника кадров, а не поиском путей в
    готовой разметке: пока два города показывают один и тот же снимок,
    поиск по пути легко ошибся бы местом."""
    names = {p["shot"]: p["name"]["ru"] for packs in C.PRICE["packages"].values()
             for p in packs}
    city_of = {"lisbon": "ЛИССАБОН", "moscow": "МОСКВА"}
    slots = {}
    for city, packs in C.PRICE["packages"].items():
        for pack in packs:
            slots[pack["shot"]] = "ФОТО-%s-%s" % (
                city_of[city], names[pack["shot"]].upper().replace(" ", "-"))
    assert len(slots) == len(set(slots.values())), "метки обложек повторяются"

    real, P.PRICE_SHOTS = P.PRICE_SHOTS, slots
    try:
        html = price_block()
    finally:
        P.PRICE_SHOTS = real
    assert P.BASE not in html, "в блоке остались наши пути к файлам"
    need = sum(len(v) for v in C.PRICE["packages"].values())
    assert html.count('src="ФОТО-') == need, "обложек должно быть %d" % need
    return html


def tilda_about():
    """«Обо мне» для Tilda: та же страница, что на сайте, но вместо портрета —
    место под адрес.

    Блок едет кодом, а не родным «изображение + текст», потому что на телефоне
    у этой страницы своя раскладка: имя с новой строки, род занятий под ним,
    черточки между абзацами, текст прижат к правому краю. Родным блоком этого
    не собрать.

    Чего в Tilda не будет: на компьютере страница перестанет укладываться
    ровно в один экран. Правило, которое тянет разворот по высоте окна, стоит
    ниже отсечки @tilda-cut и в набор не попадает — оно опирается на нашу
    обвязку страницы, а её в Tilda отдаёт сама Tilda. Страница просто
    прокручивается, как остальные."""
    html = about_block()
    old = 'src="%s"' % P.SELF_PORTRAIT
    assert html.count(old) == 1, "разметка портрета изменилась"
    return html.replace(old, 'src="%s"' % PORTRAIT_SLOT)


def tilda_contact():
    """Контакты для Tilda: та же страница, что на сайте, но вместо нашего
    кадра — одно место под адрес. Снимок грузится в библиотеку Tilda, и её
    адрес подставляется прямо в блоке; подбора размеров под экран здесь нет,
    Tilda отдаёт один файл."""
    html = contact_block()
    old = ('src="assets/img/contact/bg.jpg"\n'
           '       srcset="assets/img/contact/bg@sm.jpg 1400w, '
           'assets/img/contact/bg.jpg 2400w"\n'
           '       sizes="100vw" alt=""')
    assert old in html, "разметка кадра на контактах изменилась"
    return html.replace(old, 'src="%s" alt=""' % PHOTO_SLOT)


def contact_block():
    """Контакты поверх одного кадра.

    «Телефон» стоит последним и показывается только в русской версии: ссылка
    ведёт на звонок, англоязычному посетителю российский номер бесполезен.
    Прячет её CSS по data-lang, поэтому переключение языка работает без
    перезагрузки страницы."""
    return """<section class="sf-contactpage">
  %s
  <img class="sf-contactpage__photo" src="assets/img/contact/bg.jpg"
       srcset="assets/img/contact/bg@sm.jpg 1400w, assets/img/contact/bg.jpg 2400w"
       sizes="100vw" alt="" width="2400" height="1801" loading="eager" decoding="async" fetchpriority="high">
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
    # Только те начертания, что действительно рисуются на страницах.
    # Проверено обходом всех элементов на семи страницах, двух языках и двух
    # ширинах: Cormorant Garamond идёт весом 400 и 500, курсив и вес 300 не
    # встречаются ни разу. Каждое лишнее начертание — отдельный файл в загрузке.
    'family=Cormorant+Garamond:wght@400;500'
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


def tilda_native_css():
    """Стили для родных блоков Tilda.

    Родные блоки лежат снаружи нашего .sf-root, и переменные палитры там не
    разрешаются — поэтому дублируем их на :root. Берём прямо из style.css,
    вместе с тёмной стороной: пока это делалось руками, файл успел отстать
    от сайта на один снятый шрифт и одну целую тему.
    """
    css = open(os.path.join(ROOT, "assets/css/style.css"), encoding="utf-8").read()

    def palette(block):
        """Объявления `--sf-…` из переданного куска, по одному на строку.

        Режем по точке с запятой, а не по строкам: часть переменных записана
        в две строки, у части в хвосте комментарий — построчный разбор их
        молча терял, и в наборе для Tilda не оказывалось самого ходового
        шрифта."""
        body = re.sub(r"/\*.*?\*/", "", block, flags=re.S)
        return "\n".join(
            "  %s: %s;" % (m.group(1), " ".join(m.group(2).split()))
            for m in re.finditer(r"(--sf-[a-z0-9-]+)\s*:\s*([^;]+);", body)
        )

    light = palette(css[css.index(".sf-root {"):css.index("\n}", css.index(".sf-root {"))])
    dark_src = css[css.index("@media (prefers-color-scheme: dark)"):]
    dark = palette(dark_src[:dark_src.index("\n  }")])
    assert light and dark, "палитра не вычиталась из style.css"
    # Самая ходовая переменная: без неё у родных блоков не будет фона вовсе.
    assert "--sf-bg:" in light and "--sf-bg:" in dark, "в палитре потерялся фон"

    return """/* ==========================================================================
   10 — РОДНЫЕ БЛОКИ TILDA ПОД ОБЩИЙ СТИЛЬ

   Куда: Настройки сайта → Вставка кода → Пользовательские CSS-стили.
   Это отдельное поле, не то, куда идёт 01-head-code.html. Тег <style>
   писать не нужно, только содержимое этого файла.

   Зачем: галереи, «Обо мне» и пакеты цен собираются родными блоками Tilda,
   чтобы фотографии менялись мышкой. По умолчанию они выглядят
   «по-тильдовски»: скруглённые углы, свои поля и шрифты. Этот файл приводит
   их к нашему виду.

   ЭТОТ ФАЙЛ СОБИРАЕТСЯ. Палитра и тёмная тема берутся из assets/css/style.css
   при каждой сборке — править их здесь бесполезно, правьте в style.css.

   ВАЖНО ПРО СЕЛЕКТОРЫ. У Tilda классы отличаются от блока к блоку, и точный
   набор зависит от того, какие блоки вы выберете. Считайте это заготовкой:
   если что-то не подхватилось — правый клик по элементу → «Просмотреть код»,
   посмотрите настоящий класс и допишите его сюда рядом через запятую.

   Чтобы правило подействовало только на один блок, поставьте перед ним его
   номер: #rec123456789 .t-title { … }. Номер виден в редакторе слева.
   ========================================================================== */

/* --------------------------------------------------------------------------
   1. ПАЛИТРА НА :root
   Наши переменные объявлены на .sf-root, а родные блоки лежат снаружи него.
   -------------------------------------------------------------------------- */

:root {
%s
}

/* Тёмная сторона — те же переменные в других тонах. Включается от настройки
   телефона или компьютера, как и на остальном сайте. */
@media (prefers-color-scheme: dark) {
  :root {
%s
  }
}

/* --------------------------------------------------------------------------
   2. ФОН И НАБОР
   -------------------------------------------------------------------------- */

body,
.t-body,
.t-records { background-color: var(--sf-bg); }

.t-title {
  font-family: var(--sf-serif) !important;
  font-weight: 400 !important;
  color: var(--sf-ink);
  letter-spacing: 0.04em;
}

.t-descr,
.t-text,
.t-name {
  font-family: var(--sf-sans) !important;
  color: var(--sf-ink-text);
  line-height: 1.8;
}

/* --------------------------------------------------------------------------
   3. ГАЛЕРЕИ
   Убираем скругления и тени, сводим зазор к нашему просвету и выводим сетку
   на те же поля, что и остальной сайт.
   -------------------------------------------------------------------------- */

.t-gallery__item,
.t-slds__item,
.t-slds__bgimg,
.t-gallery__img,
.t-img { border-radius: 0 !important; box-shadow: none !important; }

.t-gallery .t-container,
.t-gallery .t-container_100,
.t-slds .t-container_100 {
  max-width: 100%% !important;
  padding-left: var(--sf-pad-x) !important;
  padding-right: var(--sf-pad-x) !important;
}

/* Приближение по наведению — как в наших галереях. На телефоне наведения
   нет, поэтому и правила нет: иначе кадр «залипал» бы увеличенным. */
@media (hover: hover) {
  .t-gallery__item img,
  .t-slds__item img { transition: transform 1.1s var(--sf-ease); }
  .t-gallery__item:hover img,
  .t-slds__item:hover img { transform: scale(1.035); }
}

/* --------------------------------------------------------------------------
   4. КНОПКИ
   Своих кнопок у нас нет: всё, что нажимается, — это набранная разрядкой
   строка. Если родной блок принесёт кнопку, пусть выглядит так же.
   -------------------------------------------------------------------------- */

.t-btn,
.t-btntext {
  border: 0 !important;
  border-radius: 0 !important;
  background-color: transparent !important;
  color: var(--sf-ink) !important;
  font-family: var(--sf-sans) !important;
  font-weight: 300 !important;
  font-size: 16px !important;
  letter-spacing: 0.08em !important;
  text-transform: lowercase !important;
  padding: 0 !important;
  transition: letter-spacing .6s var(--sf-ease);
}
@media (hover: hover) {
  .t-btn:hover { letter-spacing: 0.12em !important; }
}

/* --------------------------------------------------------------------------
   5. ОТКРЫВАЛКА КАДРА
   С родными галереями работает своя, наш лайтбокс не нужен — приводим только
   подложку к нашей. В тёмной теме она темнеет сама: это та же переменная.
   -------------------------------------------------------------------------- */

.t-popup__container,
.t-slds__wrapper { background-color: var(--sf-overlay) !important; }
""" % (light, "  " + dark.replace("\n", "\n  "))


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
            body_class="sf-body--gallery",
        ))

    write(PAGES["about"]["file"], page("about", about_block(), has_gallery=False,
                                      body_class="sf-body--fit"))
    write(PAGES["price"]["file"], page(
        # Сначала цены, потом порядок работы: человек приходит сюда за суммой,
        # а как всё будет происходить читает уже после. Порядок один на все
        # ширины — раньше его переставляла раскладка, и только на телефоне.
        "price", "\n\n".join([price_block(), process_block(), lead_block()]),
        has_gallery=False, body_class="sf-body--price"))
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
        # data-lang="en" — то же, что в разметке сайта: до загрузки скрипта
        # должен быть виден один язык, а не оба сразу.
        return banner(num, what, where) + '<div class="sf-root" data-lang="en">\n%s\n</div>\n' % indent(
            tilda_links(html), "  "
        )

    # Everything after the @tilda-cut sentinel is standalone-only html/body
    # styling that would fight Tilda's own page chrome.
    css = open(os.path.join(ROOT, "assets/css/style.css"), encoding="utf-8").read()
    tilda_css = css.split("/* @tilda-cut")[0]

    write("tilda/01-head-code.html",
          banner("01", "Шрифты + стили",
                 "Настройки сайта → Вставка кода → HTML-код для вставки внутрь HEAD")
          + FONTS + "\n<style>\n" + tilda_css.rstrip() + "\n</style>\n")

    write("tilda/02-header.html", block(
        "02", "Хедер + мобильное меню",
        "Блок T123 в самом верху страницы. Нужен закреплённый хедер — "
        "добавьте класс sf-header--fixed к <header>.",
        header("home")))

    write("tilda/03-home-strapline.html", block(
        "03", "Главная — три строки над сеткой",
        "Блок T123 на главной, в самом верху, НАД родной галереей. "
        "Внутри спрятан заголовок страницы — он нужен поиску, видно его не будет.",
        home_strapline()) + page_class("sf-body--home"))

    write("tilda/04-home-tagline.html", block(
        "04", "Главная — строка под сеткой",
        "Блок T123 на главной, ПОД родной галереей",
        home_tagline()))

    write("tilda/05-about.html", block(
        "05", "Обо мне — портрет и текст",
        "Блок T123 на /about, единственный на странице. Нужен портрет: "
        "загрузите его в Tilda и подставьте адрес вместо " + PORTRAIT_SLOT
        + ". На компьютере страница здесь не укладывается в один экран, как "
        "на сайте, — она прокручивается.",
        tilda_about()))

    write("tilda/06b-lead-in.html", block(
        "06b", "Строка «записаться на съёмку»",
        "Блок T123 в самом низу /portraits, /street, /love и /price. "
        "Сама строка и есть кнопка: по нажатию каналы связи открываются окном "
        "по центру экрана.",
        lead_block()))

    write("tilda/07-page-title.html", block(
        "07", "Тихий заголовок страницы",
        "Блок T123 над родной галереей на /portraits, /street, /love. "
        "Замените текст на нужный раздел.",
        '<section class="sf-pagehead">\n  %s\n</section>' % tb(
            C.GALLERIES["portraits"]["title"], "h1", "sf-pagehead__title"))
        + page_class("sf-body--gallery"))

    write("tilda/07b-price-packages.html", block(
        "07b", "Цены — заголовок, пакеты и переключатель городов",
        "Блок T123 на /price, ПЕРВЫЙ на странице: заголовок «Цены» уже внутри, "
        "отдельный блок 07 сюда не нужен. Восемь обложек: загрузите кадры в "
        "Tilda и подставьте их адреса вместо меток ФОТО-ГОРОД-НАЗВАНИЕ.",
        tilda_price()) + page_class("sf-body--price"))

    write("tilda/08-process.html", block(
        "08", "Как проходит съёмка — четыре шага",
        "Блок T123 на /price, ПОД пакетами. Порядок страницы: 07b, 08, 06b — "
        "сначала суммы, потом как всё устроено, в самом низу строка записи.",
        process_block()))

    write("tilda/09-contact-details.html", block(
        "09", "Контакты — кадр во весь экран и каналы связи",
        "Блок T123 на /contact, единственный на странице. Нужна фотография: "
        "загрузите кадр в Tilda и подставьте его адрес вместо "
        + PHOTO_SLOT + ".",
        tilda_contact()))

    write("tilda/10-footer.html", block(
        "10", "Футер",
        "Блок T123 внизу каждой страницы. На /contact он встаёт обычным "
        "блоком под кадром: на сайте футер лежит поверх фотографии, но там "
        "он держится обвязкой страницы, а её в Tilda отдаёт сама Tilda.",
        footer()))

    write("tilda/10b-footer-contact.html", block(
        "10b", "Футер для страницы контактов",
        "Блок T123 внизу /contact — вместо обычного футера 10. Отличается "
        "одним: в нём нет иконок соцсетей. Прямо над ними стоят те же каналы, "
        "крупно, и на сайте иконки там спрятаны.",
        footer(social=False)))

    write("tilda/10-native-blocks.css", tilda_native_css())

    js = open(os.path.join(ROOT, "assets/js/main.js"), encoding="utf-8").read()
    write("tilda/11-foot-code.html",
          banner("11", "Скрипт поведения",
                 "Настройки сайта → Вставка кода → HTML-код для вставки внутрь HEAD, "
                 "следом за кодом из 01-head-code.html. Поля для конца BODY у Tilda "
                 "больше нет; скрипт ждёт, пока страница построится, поэтому из HEAD "
                 "работает так же.")
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

    # Считаем только настоящие места в разметке, не упоминания в пояснениях.
    slots = sum(
        len(re.findall(r'src="(?:%s|ФОТО-[А-ЯЁ-]+)"' % PHOTO_SLOT,
                       open(os.path.join(tilda_dir, n), encoding="utf-8").read()))
        for n in os.listdir(tilda_dir) if n.endswith(".html")
    )
    if leftover:
        print("\n  ВНИМАНИЕ: в блоках остались наши пути к файлам:")
        for x in leftover:
            print("   ", x)
    else:
        print("\n  Путей к нашим файлам в блоках нет.")
    print("  Мест под фотографию: %d — портрет в «Обо мне», кадр на контактах "
          "и %d обложек пакетов. Галереи и сетка на главной ставятся родными "
          "блоками Tilda." % (slots, sum(len(v) for v in C.PRICE["packages"].values())))

    print("Done.")


if __name__ == "__main__":
    main()
