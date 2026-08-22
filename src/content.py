"""
CONTENT
=======
All copy lives here, in both languages: {"en": "...", "ru": "..."}.
Edit this file, run `python3 src/build.py`, and every page plus every Tilda
block is regenerated. Nothing else needs touching.

Values are inserted into HTML as-is, so if you write an ampersand, write it
as &amp;.
"""

SITE = {
    "wordmark": "Sofia Filatova",
    "email": "sofia.filat280303@gmail.com",
    "phone_ru": {"display": "+7 926 375 97 95", "href": "tel:+79263759795"},
    "phone_pt": {"display": "+351 910 207 480", "href": "tel:+351910207480"},
    "instagram": {"handle": "@sfx.ph", "href": "https://instagram.com/sfx.ph"},
    "telegram": {"handle": "@sfxx1", "href": "https://t.me/sfxx1"},
    "whatsapp": {"handle": "+7 926 375 97 95", "href": "https://wa.me/79263759795"},
    "booking_href": "https://t.me/sfxx1",
    "year": 2026,
}

UI = {
    "book":     {"en": "Book a date",    "ru": "Забронировать"},
    "read_more": {"en": "More about me", "ru": "Обо мне"},
    "see_more": {"en": "more",           "ru": "ещё"},
    "photos":   {"en": "photographs",    "ru": "фотографий"},
    "close":    {"en": "Close",          "ru": "Закрыть"},
    "prev":     {"en": "Previous",       "ru": "Назад"},
    "next":     {"en": "Next",           "ru": "Вперёд"},
    "menu":     {"en": "Menu",           "ru": "Меню"},
    "extras":   {"en": "Add-ons",        "ru": "Дополнительно"},
}

# ---------------------------------------------------------------- pages

PAGES = {
    "home":      {"file": "index.html",     "nav": {"en": "Main",      "ru": "Главная"}},
    "portraits": {"file": "portraits.html", "nav": {"en": "Portraits", "ru": "Портреты"}},
    "street":    {"file": "street.html",    "nav": {"en": "Street",    "ru": "Улица"}},
    "love":      {"file": "love.html",      "nav": {"en": "Love",      "ru": "Пары"}},
    "about":     {"file": "about.html",     "nav": {"en": "About",     "ru": "Обо мне"}},
    "price":     {"file": "price.html",     "nav": {"en": "Price",     "ru": "Прайс"}},
    "contact":   {"file": "contact.html",   "nav": {"en": "Contact",   "ru": "Контакты"}},
}

NAV_ORDER = ["home", "portraits", "street", "love", "about", "price", "contact"]

# ------------------------------------------------------------------ SEO

META = {
    "home": {
        "title": {
            "en": "Sofia Filatova — cinematic portrait photographer, Moscow &amp; Lisbon",
            "ru": "София Филатова — кинематографичный фотограф, Москва и Лиссабон",
        },
        "description": {
            "en": "Cinematic and vintage portrait photography by Sofia Filatova. Studio portraits, street sessions and couple shoots in Moscow and Lisbon.",
            "ru": "Кинематографичная портретная съёмка. София Филатова: студийные портреты, стрит-фотосессии и парные съёмки в Москве и Лиссабоне.",
        },
    },
    "portraits": {
        "title": {"en": "Portraits — Sofia Filatova", "ru": "Портреты — София Филатова"},
        "description": {
            "en": "Studio portrait photography with a cinematic, vintage feel. Selected work by Sofia Filatova.",
            "ru": "Студийная портретная съёмка в кинематографичной винтажной эстетике. Избранные работы Софии Филатовой.",
        },
    },
    "street": {
        "title": {"en": "Street sessions — Sofia Filatova", "ru": "Стрит-фотосессии — София Филатова"},
        "description": {
            "en": "Street photo sessions in Moscow and Lisbon — three to five locations, natural light, film stills.",
            "ru": "Стрит-фотосессии в Москве и Лиссабоне: 3–5 локаций, естественный свет, кадры как из фильма.",
        },
    },
    "love": {
        "title": {"en": "Love stories — Sofia Filatova", "ru": "Парные съёмки — София Филатова"},
        "description": {
            "en": "Couple and love story photography — street, studio and ocean, shot like scenes from a film.",
            "ru": "Парные съёмки и love story: улица, студия и океан — как сцены из фильма.",
        },
    },
    "about": {
        "title": {"en": "About — Sofia Filatova", "ru": "Обо мне — София Филатова"},
        "description": {
            "en": "Photographer and film director based in Moscow and Lisbon. VGIK-trained, ArtMasters finalist, published in ELLE, Forbes and Kinoreporter.",
            "ru": "Фотограф и режиссёр. Москва и Лиссабон. Выпускница ВГИКа, финалистка ArtMasters, публикации в ELLE и Forbes.",
        },
    },
    "price": {
        "title": {"en": "Price — Sofia Filatova", "ru": "Цены — София Филатова"},
        "description": {
            "en": "Photo session packages and prices in Lisbon and Moscow — studio portraits, street sessions, love stories.",
            "ru": "Пакеты и цены на съёмку в Лиссабоне и Москве: студийный портрет, стрит-фотосессия, парная съёмка.",
        },
    },
    "contact": {
        "title": {"en": "Contact — Sofia Filatova", "ru": "Контакты — София Филатова"},
        "description": {
            "en": "Get in touch to book a shoot in Moscow or Lisbon — Telegram, WhatsApp, Instagram or email.",
            "ru": "Связаться и забронировать съёмку в Москве или Лиссабоне — Telegram, WhatsApp, Instagram или почта.",
        },
    },
}

# ----------------------------------------------------------------- home

HOME = {
    "hero_title": {
        "en": "Portraits that feel like stills from a film",
        "ru": "Портреты, похожие на кадры из фильма",
    },
    "hero_sub": {
        "en": "Cinematic &amp; vintage photographer from Moscow &amp; Lisbon",
        "ru": "Кинематографичный фотограф, Москва и Лиссабон",
    },
    # The script line under the grid, in place of the reference's
    # "for the adventurous, the heartfelt and the sun kissed".
    "tagline": {
        "en": "every portrait a scene,<br>every person a story",
        "ru": "каждый портрет — сцена,<br>каждый человек — история",
    },
    "cta_title": {
        "en": "You have a story. Let me capture it.",
        "ru": "У вас есть история. Позвольте мне её снять.",
    },
}

# ---------------------------------------------------------------- about

ABOUT = {
    # Не «Привет, я София» — панибратство здесь не к месту. Варианты на замену
    # лежат рядом, поменять можно одной строкой.
    # Имя и род занятий вынесены в заголовок. Первая фраза текста повторяла
    # их слово в слово, поэтому из тела она убрана — осталась только география.
    "title": {"en": "Sofia Filatova", "ru": "София Филатова"},
    "role": {"en": "photographer and film director", "ru": "фотограф и кинорежиссёр"},
    # Sofia's own copy, supplied by the client — do not paraphrase it.
    "body": {
        "en": [
            "Based in Moscow &amp; Lisbon.",
            "With a camera in my hands for over 7 years and a director's degree from VGIK (Russia's top film school), I see every portrait as a scene, every person as a story worth telling.",
            "I\u2019m an \u2018ArtMasters Championship\u2019 finalist. Published in ELLE, Forbes and Kinoreporter. Named one of the Top 10 photographers in Russia under 35.",
            "I shoot portraits that feel like stills from a film.",
            "You have a story. Let me capture it.",
        ],
        "ru": [
            "Снимаю в Москве и Лиссабоне.",
            "Я фотографирую более семи лет. Окончила ВГИК с отличием по специальности «Режиссер». Именно режиссура сформировала мой взгляд на фотографию: я вижу в каждом портрете сцену из кино, а в каждом человеке историю, которую хочется рассказать.",
            "Я дважды финалист чемпионата «ArtMasters» в компетенции «фотограф». Мои работы публиковались в таких журналах как ELLE, Forbes и «Кинорепортёр». Вхожу в топ-10 фотографов России в возрасте до 35 лет.",
            "У каждого есть своя история. Давайте расскажем её вместе через фотографию.",
        ],
    },
}

# -------------------------------------------------------------- gallery

GALLERIES = {
    "portraits": {
        "title": {"en": "Portraits", "ru": "Портреты"},
    },
    "street": {
        "title": {"en": "Street", "ru": "Улица"},
    },
    "love": {
        "title": {"en": "Love", "ru": "Пары"},
    },
}

# ---------------------------------------------------------------- price

PRICE = {
    "cities": [
        {"id": "lisbon", "label": {"en": "Lisbon", "ru": "Лиссабон"}},
        {"id": "moscow", "label": {"en": "Moscow", "ru": "Москва"}},
    ],
    "packages": {
        "lisbon": [
            {
                "shot": "studio",
                "name": {"en": "Studio portraits", "ru": "Студийный портрет"},
                "cost": "€300",
                "items": [
                    {"en": "Up to 2 hours of shooting", "ru": "До 2 часов съёмки"},
                    {"en": "50 retouched photographs within 10 days", "ru": "50 отретушированных фотографий в течение 10 дней"},
                    {"en": "Help with preparation — references, wardrobe, studio", "ru": "Помощь в подготовке — референсы, образы, студия"},
                ],
                "extras": {
                    "en": "Extra hour +€70 · Express retouching in 3 days +€60 · Studio rental paid separately",
                    "ru": "Дополнительный час +€70 · Экспресс-ретушь за 3 дня +€60 · Аренда студии оплачивается отдельно",
                },
            },
            {
                "shot": "walk",
                "name": {"en": "Photo walk", "ru": "Фотопрогулка"},
                "cost": "€250",
                "items": [
                    {"en": "1.5 hours of shooting", "ru": "1,5 часа съёмки"},
                    {"en": "60 retouched photographs within 10 days", "ru": "60 отретушированных фотографий в течение 10 дней"},
                    {"en": "3–5 locations — street or ocean", "ru": "3–5 локаций — улица или океан"},
                    {"en": "Help with preparation", "ru": "Помощь в подготовке"},
                ],
                "extras": {
                    "en": "Extra hour +€70 · Express retouching +€60 · Ocean location +€50 (taxi covered by the client)",
                    "ru": "Дополнительный час +€70 · Экспресс-ретушь +€60 · Локация у океана +€50 (такси за счёт клиента)",
                },
            },
            {
                "shot": "loveStory",
                "name": {"en": "Love story", "ru": "Парная съёмка"},
                "cost": "€350",
                "items": [
                    {"en": "Up to 2 hours of shooting", "ru": "До 2 часов съёмки"},
                    {"en": "60 retouched photographs within 14 days", "ru": "60 отретушированных фотографий в течение 14 дней"},
                    {"en": "Street, studio or ocean", "ru": "Улица, студия или океан"},
                    {"en": "Help with preparation", "ru": "Помощь в подготовке"},
                ],
                "extras": {
                    "en": "Extra hour +€70 · Express retouching +€60 · Ocean location +€50 · Studio rental paid separately",
                    "ru": "Дополнительный час +€70 · Экспресс-ретушь +€60 · Локация у океана +€50 · Аренда студии отдельно",
                },
            },
        ],
        "moscow": [
            {
                "shot": "studio",
                "name": {"en": "Studio portrait", "ru": "Студийный портрет"},
                "cost": "20 000 ₽",
                "items": [
                    {"en": "2 hours of shooting", "ru": "2 часа съёмки"},
                    {"en": "40 retouched photographs within 10 days", "ru": "40 отретушированных фотографий в течение 10 дней"},
                    {"en": "Consultation, mood board, choosing the studio", "ru": "Консультация, мудборд, подбор студии"},
                ],
                "extras": {
                    "en": "Extra hour +6 000 ₽ · Express retouching +4 000 ₽ · Make-up and styling on request · Studio paid separately",
                    "ru": "Дополнительный час +6 000 ₽ · Экспресс-ретушь +4 000 ₽ · Макияж и стайлинг по запросу · Студия оплачивается отдельно",
                },
            },
            {
                "shot": "walk",
                "name": {"en": "Street session", "ru": "Стрит-фотосессия"},
                "cost": "15 000 ₽",
                "items": [
                    {"en": "1.5 hours of shooting", "ru": "1,5 часа съёмки"},
                    {"en": "50 retouched photographs within 10 days", "ru": "50 отретушированных фотографий в течение 10 дней"},
                    {"en": "3–5 locations", "ru": "3–5 локаций"},
                    {"en": "Consultation and mood board", "ru": "Консультация и мудборд"},
                ],
                "extras": {
                    "en": "Extra hour +6 000 ₽ · Express retouching +4 000 ₽",
                    "ru": "Дополнительный час +6 000 ₽ · Экспресс-ретушь +4 000 ₽",
                },
            },
            {
                "shot": "loveStory",
                "name": {"en": "Couple shoot", "ru": "Парная съёмка"},
                "cost": "25 000 ₽",
                "items": [
                    {"en": "2 hours of shooting", "ru": "2 часа съёмки"},
                    {"en": "50 retouched photographs within 14 days", "ru": "50 отретушированных фотографий в течение 14 дней"},
                    {"en": "Studio or street", "ru": "Студия или улица"},
                    {"en": "Consultation and mood board", "ru": "Консультация и мудборд"},
                ],
                "extras": {
                    "en": "Extra hour +6 000 ₽ · Express retouching +4 000 ₽ · Studio paid separately",
                    "ru": "Дополнительный час +6 000 ₽ · Экспресс-ретушь +4 000 ₽ · Студия оплачивается отдельно",
                },
            },
        ],
    },
}

# -------------------------------------------------------------- process

# Четыре шага съёмки. Снимают тревогу у тех, кто идёт впервые, и убирают
# половину повторяющихся вопросов из личных сообщений.
PROCESS = {
    "title": {"en": "How a shoot goes", "ru": "Как проходит съёмка"},
    "steps": [
        {"n": "01",
         "name": {"en": "You write", "ru": "Заявка"},
         "text": {"en": "Telegram or WhatsApp: city, rough dates, what you have in mind.",
                  "ru": "Telegram или WhatsApp: город, примерные даты, что хочется снять."}},
        {"n": "02",
         "name": {"en": "We prepare", "ru": "Подготовка"},
         "text": {"en": "Mood board, studio or locations, the looks. I will tell you what to wear.",
                  "ru": "Мудборд, студия или локации, образы. Подскажу, что надеть."}},
        {"n": "03",
         "name": {"en": "The shoot", "ru": "Съёмка"},
         "text": {"en": "An hour and a half to two. I direct as we go — posing is my job, not yours.",
                  "ru": "Полтора-два часа. Направляю по ходу — позировать не нужно."}},
        {"n": "04",
         "name": {"en": "Selection and retouch", "ru": "Отбор и ретушь"},
         "text": {"en": "Full gallery to choose from, retouched frames in 10 to 14 days.",
                  "ru": "Галерея на выбор, отретушированные кадры за 10–14 дней."}},
    ],
}

# ---------------------------------------------------------------- lead

# Блок в конце галерей. Две строки без рамок: имя и способ связи. Больше
# спрашивать нельзя — каждое лишнее поле стоит части заявок.
LEAD = {
    "title": {"en": "sessions by appointment", "ru": "съёмка по записи"},
}

# -------------------------------------------------------------- contact

CONTACT = {
    "open": {"en": "get in touch", "ru": "связаться"},
    "channels": {
        "telegram":  {"en": "Telegram",  "ru": "Telegram"},
        "whatsapp":  {"en": "WhatsApp",  "ru": "WhatsApp"},
        "instagram": {"en": "Instagram", "ru": "Instagram"},
    },
    "form": {
        "name":    {"en": "Your name", "ru": "Ваше имя"},
        "contact": {"en": "Telegram, WhatsApp or email", "ru": "Telegram, WhatsApp или почта"},
        "message": {"en": "What are we shooting?", "ru": "Что снимаем?"},
        "submit":  {"en": "Send", "ru": "Отправить"},
    },
}
