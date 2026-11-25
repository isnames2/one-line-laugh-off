"""One-Line Laugh-Off entry: a single funny line, written to entry.txt.

Pure standard library. Deterministic: same bytes on every run.
"""

import os
from pathlib import Path

LINE = "My fitness tracker congratulated me on 10,000 steps. 9,000 of them were to the fridge."

# Gate: entry.txt must be 1-200 characters of UTF-8 text (RULES.txt).
assert 1 <= len(LINE) <= 200, "line must fit the 1-200 character gate"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
