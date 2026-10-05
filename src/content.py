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
    "year": 2026,
}

# Служебные надписи: только те, что ещё читаются сборщиком. Подписи снятых
# блоков — кнопки «ещё», карточек разделов, счётчика кадров — убраны.
UI = {
    "close":    {"en": "Close",          "ru": "Закрыть"},
    "prev":     {"en": "Previous",       "ru": "Назад"},
    "next":     {"en": "Next",           "ru": "Вперёд"},
    "menu":     {"en": "Menu",           "ru": "Меню"},
    "extras":   {"en": "Add-ons",        "ru": "Дополнительно"},
}

# ---------------------------------------------------------------- pages

PAGES = {
    "home":      {"file": "index.html",     "nav": {"en": "Main",      "ru": "Главная"}},
    "portraits": {"file": "portraits.html", "nav": {"en": "Portraits", "ru": "Portraits"}},
    "street":    {"file": "street.html",    "nav": {"en": "Street",    "ru": "Street"}},
    "love":      {"file": "love.html",      "nav": {"en": "Love",      "ru": "Love"}},
    "about":     {"file": "about.html",     "nav": {"en": "About me",     "ru": "Обо мне"}},
    "price":     {"file": "price.html",     "nav": {"en": "Price",     "ru": "Цены"}},
    "contact":   {"file": "contact.html",   "nav": {"en": "Contact",   "ru": "Контакты"}},
}

NAV_ORDER = ["home", "about", "portraits", "street", "love", "price", "contact"]

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
            "en": "Get in touch to book a shoot in Moscow or Lisbon — Telegram, WhatsApp or Instagram.",
            "ru": "Связаться и забронировать съёмку в Москве или Лиссабоне — Telegram, WhatsApp или Instagram.",
        },
    },
}

# ----------------------------------------------------------------- home

HOME = {
    # Города под именем на главной. Регистр поднимает CSS, поэтому здесь
    # обычное написание.
    "places": {
        "en": "Moscow | Lisbon",
        "ru": "Москва | Лиссабон",
    },
    "hero_title": {
        "en": "Portraits that feel like stills from a film",
        "ru": "Портреты, похожие на кадры из фильма",
    },
    # The script line under the grid, in place of the reference's
    # "for the adventurous, the heartfelt and the sun kissed".
    # Одна строка вместо двух — перенос здесь больше нечего разделять.
    "tagline": {
        "en": "The world through a director\u2019s eyes",
        "ru": "Мир глазами режиссёра",
    },
}

# ---------------------------------------------------------------- about

ABOUT = {
    # Не «Привет, я София» — панибратство здесь не к месту. Варианты на замену
    # лежат рядом, поменять можно одной строкой.
    "title": {"en": "Sofia Filatova", "ru": "София Филатова"},
    # Неразрывный пробел держит «and» при «photographer»: на телефоне строка
    # ломается перед «film», и получается «PHOTOGRAPHER AND / FILM DIRECTOR».
    # На компьютере строка одна, и пробел ни на что не влияет.
    "role": {"en": "photographer\u00a0and film director", "ru": "фотограф\u00a0и кинорежиссёр"},
    # Sofia's own copy, supplied by the client — do not paraphrase it.
    "body": {
        "en": [
            "With a camera in my hands for over 7 years and a director's degree from VGIK (Russia's top film school), I see every portrait as a scene, every person as a story worth telling.",
            "I\u2019m an \u2018ArtMasters Championship\u2019 finalist. Published in ELLE, Forbes and Kinoreporter. Named one of the Top 10 photographers in Russia under 35. I shoot portraits that feel like stills from a film.",
            "You have a story. Let me capture it.",
        ],
        "ru": [
            "Занимаюсь фотографией более семи лет. Окончила ВГИК с отличием по специальности «Режиссура кино и телевидения». Именно это сформировало мой взгляд на фотографию: я вижу в каждом портрете сцену из кино, а в каждом человеке историю, которую хочется рассказать.",
            "Дважды финалист чемпионата «ArtMasters» в компетенции «Фотограф». Мои работы публиковались в таких журналах как ELLE Girl, Forbes и «Кинорепортёр». Вхожу в топ-10 фотографов России в возрасте до 35 лет.",
            "У каждого есть своя история. Давайте расскажем её вместе через фотографию.",
        ],
    },
}

# -------------------------------------------------------------- gallery

GALLERIES = {
    "portraits": {
        "title": {"en": "Portraits", "ru": "Portraits"},
    },
    "street": {
        "title": {"en": "Street", "ru": "Street"},
    },
    "love": {
        "title": {"en": "Love", "ru": "Love"},
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
                "shot": "lisbon-walk",
                "name": {"en": "Street session", "ru": "Стрит-фотосессия"},
                "cost": "€250",
                "items": [
                    {"en": "Help with preparing for the photoshoot", "ru": "Помощь в подготовке к съёмке"},
                    {"en": "Up to 1.5 hours of shooting", "ru": "До 1,5 часов съёмки"},
                    {"en": "3–5 locations", "ru": "3–5 локаций"},
                    {"en": "40 retouched photos delivered within 10 days", "ru": "40 фотографий в ретуши в течение 10 дней"},
                ],
                "extras": {
                    "en": "Extra hour +€70 · Express retouching +€60 · Sunrise shoot +€50",
                    "ru": "Дополнительный час +€70 · Экспресс-ретушь +€60 · Съёмка на рассвете +€50",
                },
                "note": {
                    "en": "Travel to the ocean location is paid separately",
                    "ru": "Транспорт до локации у океана оплачивается отдельно",
                },
            },
            {
                "shot": "lisbon-loveStory",
                "name": {"en": "Love story", "ru": "Парная съёмка"},
                "cost": "€300",
                "items": [
                    {"en": "Help with preparing for the photoshoot", "ru": "Помощь в подготовке к съёмке"},
                    {"en": "Up to 2 hours of shooting", "ru": "До 2 часов съёмки"},
                    {"en": "Street, studio or ocean", "ru": "Улица, студия или океан"},
                    {"en": "60 retouched photos delivered within 14 days", "ru": "60 фотографий в ретуши в течение 14 дней"},
                ],
                "extras": {
                    "en": "Extra hour +€70 · Express retouching +€60 · Sunrise shoot +€50",
                    "ru": "Дополнительный час +€70 · Экспресс-ретушь +€60 · Съёмка на рассвете +€50",
                },
                "note": {
                    "en": "Travel to the ocean location is paid separately",
                    "ru": "Транспорт до локации у океана оплачивается отдельно",
                },
            },
            {
                "shot": "lisbon-studio",
                "name": {"en": "Studio portrait", "ru": "Студийный портрет"},
                "cost": "€270",
                "items": [
                    {"en": "Help with preparing for the shoot: references, looks and studio selection", "ru": "Помощь в подготовке: референсы, образы и выбор студии"},
                    {"en": "Up to 2 hours of shooting", "ru": "До 2 часов съёмки"},
                    {"en": "40 retouched photos delivered within 10 days", "ru": "40 фотографий в ретуши в течение 10 дней"},
                ],
                "extras": {
                    "en": "Extra hour +€70 · Express retouching +€60 · Sunrise shoot +€50",
                    "ru": "Дополнительный час +€70 · Экспресс-ретушь +€60 · Съёмка на рассвете +€50",
                },
            },
            {
                # Единственный пакет без суммы: цена собирается под замысел.
                # Поэтому вместо строки с ценой под названием — строка внизу
                # блока, на месте, где у остальных стоят дополнения.
                "shot": "lisbon-concept",
                "name": {"en": "Concept photoshoot", "ru": "Концепт-съёмка"},
                "items": [
                    {"en": "Creative concept development", "ru": "Разработка творческой концепции"},
                    {"en": "Location, team and styling — all included", "ru": "Подбор локации, команды и образов — всё включено"},
                    {"en": "Retouching and color grading of images selected and approved by you", "ru": "Ретушь и цветокоррекция согласованных с вами кадров"},
                ],
                "terms": {
                    "en": "Price — calculated individually",
                    "ru": "Стоимость — рассчитывается индивидуально",
                },
            },
        ],
        "moscow": [
            {
                "shot": "moscow-studio",
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
                "shot": "moscow-walk",
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
                "shot": "moscow-loveStory",
                "name": {"en": "Love story", "ru": "Парная съёмка"},
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
            {
                # Единственный пакет без суммы: цена собирается под замысел.
                # Поэтому вместо строки с ценой под названием — строка внизу
                # блока, на месте, где у остальных стоят дополнения.
                "shot": "moscow-concept",
                "name": {"en": "Concept photoshoot", "ru": "Концепт-съёмка"},
                "items": [
                    {"en": "Creative concept development", "ru": "Разработка творческой концепции"},
                    {"en": "Location, team and styling — all included", "ru": "Подбор локации, команды и образов — всё включено"},
                    {"en": "Retouching and color grading of images selected and approved by you", "ru": "Ретушь и цветокоррекция согласованных с вами кадров"},
                ],
                "terms": {
                    "en": "Price — calculated individually",
                    "ru": "Стоимость — рассчитывается индивидуально",
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
         "name": {"en": "Enquiry", "ru": "Заявка"},
         "text": {"en": "Your city, your dates and what you have in mind — in Telegram, WhatsApp or Instagram",
                  "ru": "Город, даты и ваши пожелания — в Telegram, WhatsApp или Instagram"}},
        {"n": "02",
         "name": {"en": "Preparation", "ru": "Подготовка"},
         "text": {"en": "We settle on the location, the looks and the mood of the shoot",
                  "ru": "Определяем локацию, образы и настроение съёмки"}},
        {"n": "03",
         "name": {"en": "Photoshoot", "ru": "Съёмка"},
         "text": {"en": "I direct you as we go and help you with posing",
                  "ru": "Я направляю вас в процессе и помогаю с позированием"}},
        {"n": "04",
         "name": {"en": "Editing", "ru": "Обработка"},
         "text": {"en": "I pick the best frames and give them a light retouch and colour grade. Your photographs are with you within 10–14 days",
                  "ru": "Отбираю лучшие кадры и делаю лёгкую ретушь и цветокоррекцию. Готовые фотографии у вас в течение 10–14 дней"}},
    ],
}

# ---------------------------------------------------------------- lead

# Блок в конце галерей. Две строки без рамок: имя и способ связи. Больше
# спрашивать нельзя — каждое лишнее поле стоит части заявок.
LEAD = {
    "title": {"en": "Book a photoshoot", "ru": "Записаться на съёмку"},
}

# -------------------------------------------------------------- contact

CONTACT = {
    "channels": {
        "telegram":  {"en": "Telegram",  "ru": "Telegram"},
        "whatsapp":  {"en": "WhatsApp",  "ru": "WhatsApp"},
        "instagram": {"en": "Instagram", "ru": "Instagram"},
    },
}
