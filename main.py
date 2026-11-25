#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes exactly one original funny line."""
import os
from pathlib import Path

LINE = "My smartwatch mistook my existential crisis for deep sleep — and congratulated me on a personal best."


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
