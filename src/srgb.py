#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Перевод фотографии в sRGB — обязательный шаг перед выкладкой.

Зачем. Телефон снимает в Display P3, это шире sRGB. Если просто открыть такой
файл и сохранить, числа пикселей останутся прежними, а профиль потеряется —
и браузер прочтёт широкие координаты как узкие. Картинка выйдет бледнее и
холоднее задуманного: на кадре концепт-съёмки средний тон уезжал со 102,73,51
на 98,74,55, то есть из тёплого в сторону серого. На глаз это читается как
«не та цветокоррекция».

Поэтому профиль не выбрасываем, а именно переводим: цвет пересчитывается в
sRGB, и дальше файл можно хранить без профиля — sRGB браузер и так подразумевает.

Чего эта мера не ловит. Если профиль уже потерян кем-то до нас, определить по
файлу, широкий в нём цвет или узкий, нельзя — числа одинаковые. Поэтому любой
новый кадр прогоняем через этот модуль, а не на глаз.

Использование:
    python3 src/srgb.py вход.jpg выход.jpg [--ratio 4:5] [--max 1680] [-q 88]
"""

import argparse
import io
import os
import sys

from PIL import Image, ImageCms

Image.MAX_IMAGE_PIXELS = None


def описание(путь):
    """Имя цветового профиля файла или None, если профиля нет."""
    icc = Image.open(путь).info.get("icc_profile")
    if not icc:
        return None
    return ImageCms.getProfileDescription(ImageCms.ImageCmsProfile(io.BytesIO(icc))).strip()


def в_srgb(im):
    """Картинка в sRGB. Профиль переводится, а не отбрасывается."""
    icc = im.info.get("icc_profile")
    im = im.convert("RGB")
    if not icc:
        # Профиля нет — считаем, что это уже sRGB. Другого выбора файл не даёт.
        return im
    исходный = ImageCms.ImageCmsProfile(io.BytesIO(icc))
    if "srgb" in (ImageCms.getProfileDescription(исходный) or "").strip().lower():
        return im
    return ImageCms.profileToProfile(
        im, исходный, ImageCms.createProfile("sRGB"), outputMode="RGB"
    )


def обрезать(im, ratio):
    """Центральная обрезка под заданное отношение сторон, без растяжения."""
    if not ratio:
        return im
    rw, rh = (int(x) for x in ratio.split(":"))
    w, h = im.size
    th = h - (h % rh)
    tw = int(round(th * rw / rh))
    if tw > w:
        tw = w - (w % rw)
        th = int(round(tw * rh / rw))
    left = (w - tw) // 2
    top = (h - th) // 2
    return im.crop((left, top, left + tw, top + th))


def уместить(im, предел):
    """Уменьшить до предела по длинной стороне. Вверх никогда не тянем:
    деталей от этого не прибавится, только вес файла."""
    if not предел or max(im.size) <= предел:
        return im
    k = предел / float(max(im.size))
    return im.resize((max(1, round(im.size[0] * k)), max(1, round(im.size[1] * k))), Image.LANCZOS)


def подготовить(вход, выход, ratio=None, предел=None, качество=88):
    im = Image.open(вход)
    был = описание(вход)
    im = обрезать(в_srgb(im), ratio)
    im = уместить(im, предел)
    im.save(выход, "JPEG", quality=качество, subsampling=0, optimize=True, progressive=True)
    return был, im.size


def main():
    p = argparse.ArgumentParser(description="Перевод фотографии в sRGB с обрезкой под формат")
    p.add_argument("вход")
    p.add_argument("выход")
    p.add_argument("--ratio", help="отношение сторон, например 4:5")
    p.add_argument("--max", type=int, help="предел по длинной стороне, пикселей")
    p.add_argument("-q", "--quality", type=int, default=88)
    a = p.parse_args()
    был, размер = подготовить(a.вход, a.выход, a.ratio, a.max, a.quality)
    print("  профиль исходника: %s" % (был or "нет, считаем sRGB"))
    print("  записан %s — %dx%d, %d байт" % (a.выход, размер[0], размер[1], os.path.getsize(a.выход)))


if __name__ == "__main__":
    sys.exit(main())
