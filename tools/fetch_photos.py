#!/usr/bin/env python3
"""
FETCH PHOTOS
============
    python3 tools/fetch_photos.py [--force]

Downloads every photo listed in src/photos.py from its recorded source URL,
resizes it to MAX_EDGE on the longest side and saves it under assets/img/.
Already-present files are skipped unless --force is passed.

Resizing uses `sips`, which ships with macOS. On a machine without it the
originals are saved unchanged — larger, but the site still works.
"""

import os
import shutil
import subprocess
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))

import photos as P  # noqa: E402

MAX_EDGE = 1800          # plenty for a full-screen lightbox on a retina laptop
THUMB_EDGE = 800         # what the justified grid actually displays, at 2x
OUT = os.path.join(ROOT, "assets", "img")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"


def thumb_path(path):
    """assets/img/love/03.jpg → assets/img/love/03@sm.jpg"""
    stem, ext = os.path.splitext(path)
    return stem + "@sm" + ext


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp, open(dest, "wb") as fh:
        shutil.copyfileobj(resp, fh)


def resize(path, edge):
    if not shutil.which("sips"):
        return
    subprocess.run(
        ["sips", "-Z", str(edge), path],
        check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def derive_thumb(full):
    """Grid-sized copy beside the full one. The grid loads these; only the
    lightbox reaches for the big file."""
    small = thumb_path(full)
    shutil.copyfile(full, small)
    resize(small, THUMB_EDGE)


def main():
    force = "--force" in sys.argv
    os.makedirs(OUT, exist_ok=True)

    manifest = list(P.ALL_PHOTOS)
    done = skipped = failed = 0

    for i, (name, _ar, source) in enumerate(manifest, 1):
        dest = os.path.join(OUT, name)
        os.makedirs(os.path.dirname(dest), exist_ok=True)

        if os.path.exists(dest) and not force:
            if not os.path.exists(thumb_path(dest)):
                derive_thumb(dest)
            skipped += 1
            continue

        try:
            download(source, dest)
            resize(dest, MAX_EDGE)
            derive_thumb(dest)
            done += 1
            size = os.path.getsize(dest) // 1024
            print("  [%d/%d] %s  %d KB" % (i, len(manifest), name, size))
        except Exception as exc:                      # noqa: BLE001
            failed += 1
            print("  [%d/%d] %s  FAILED — %s" % (i, len(manifest), name, exc))
            if os.path.exists(dest):
                os.remove(dest)

    print("\ndownloaded %d · skipped %d · failed %d" % (done, skipped, failed))
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
