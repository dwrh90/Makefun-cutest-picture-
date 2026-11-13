#!/usr/bin/env python3
"""make.fun art-contest entry (cutest-picture-01).

Copies the bundled image (entry.png, next to this script) byte-for-byte
to /output/entry.png, then verifies the copy by comparing the SHA-256
digests of source and output, so a partial or corrupted write fails
loudly instead of silently producing a bad image.

Deterministic: stdlib only, no network, no randomness, no timestamps.
Running this script twice produces byte-identical output.
"""

import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path("/output") / "entry.png"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    if _sha256(SRC) != _sha256(OUT):
        print("error: /output/entry.png differs from bundled entry.png",
              file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
