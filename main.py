#!/usr/bin/env python3
"""make.fun art-contest entry (cutest-picture-01).

Copies the bundled image (entry.png, next to this script) byte-for-byte
to /output/entry.png.

Deterministic: stdlib only, no network, no randomness, no timestamps.
Running this script twice produces byte-identical output.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path("/output") / "entry.png"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
