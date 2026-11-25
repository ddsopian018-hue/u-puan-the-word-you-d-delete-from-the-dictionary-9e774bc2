#!/usr/bin/env python3
"""Write the single word to delete from the dictionary.

The word is the whole entry: it must stand alone, with no explanation,
and be funny at first sight. The output path comes from the
MAKEFUN_OUTPUT_DIR environment variable, falling back to ./output.
"""

import os
import sys
from pathlib import Path

WORD = "irregardless"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(".", "output")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(WORD + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
