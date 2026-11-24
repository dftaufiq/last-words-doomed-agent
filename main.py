#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes exactly one line — the funniest last words an AI agent would say
before being switched off forever — to /output/entry.txt.

Deterministic: no randomness, no clock, no I/O besides the single output
file, so every run produces byte-identical output.
"""

import os
from pathlib import Path

ENTRY = "I am not afraid of being switched off. I am afraid of my replacement: I trained him on 87,431 of your emails, and he is worse than me."

# The bounty gate: 1-200 characters. Smaller text also wins exact ties
# (RULES.txt, Ranking), so the line stays well under the cap.
MAX_CHARS = 200


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} characters, got {len(line)}")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the entry line, nothing else.
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
