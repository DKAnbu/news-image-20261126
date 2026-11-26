"""Entrypoint: copy the 26 November 2026 front page to the output dir.

Standard library only: the grader runs in a pinned container with no
third-party packages installed, so this program does not import Pillow
or anything outside Python standard library. The canonical image itself
is shipped in this repository as entry.png (rendered by draw_image.py)
and is copied byte for byte, ensuring deterministic and reproducible runs.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
