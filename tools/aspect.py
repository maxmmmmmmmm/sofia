#!/usr/bin/env python3
"""
ASPECT RATIO
============
    python3 tools/aspect.py assets/img/portraits/07.jpg [more files…]

Prints the width ÷ height of each image — the number that goes in the middle
column of src/photos.py. Pass a whole folder to check everything at once:

    python3 tools/aspect.py assets/img/love/*.jpg

Reads JPEG and PNG headers directly, so there is nothing to install.
"""

import os
import struct
import sys


def jpeg_size(fh):
    fh.seek(2)
    while True:
        marker = fh.read(2)
        if len(marker) < 2 or marker[0] != 0xFF:
            return None
        code = marker[1]
        (length,) = struct.unpack(">H", fh.read(2))
        # SOF0..SOF15, skipping the four that are not frame headers
        if 0xC0 <= code <= 0xCF and code not in (0xC4, 0xC8, 0xCC):
            fh.read(1)
            height, width = struct.unpack(">HH", fh.read(4))
            return width, height
        fh.seek(length - 2, os.SEEK_CUR)


def png_size(fh):
    fh.seek(16)
    width, height = struct.unpack(">II", fh.read(8))
    return width, height


def size_of(path):
    with open(path, "rb") as fh:
        head = fh.read(8)
        fh.seek(0)
        if head[:2] == b"\xff\xd8":
            return jpeg_size(fh)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            return png_size(fh)
    return None


def main():
    paths = sys.argv[1:]
    if not paths:
        sys.exit(__doc__.strip())

    for path in paths:
        if not os.path.isfile(path):
            print("%-44s  not a file" % path)
            continue
        try:
            dims = size_of(path)
        except Exception as exc:                      # noqa: BLE001
            print("%-44s  unreadable — %s" % (path, exc))
            continue
        if not dims:
            print("%-44s  unsupported format" % path)
            continue
        w, h = dims
        print("%-44s  %5d × %-5d   ratio %.3f" % (path, w, h, w / h))


if __name__ == "__main__":
    main()
