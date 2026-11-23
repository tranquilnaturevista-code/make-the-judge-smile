#!/usr/bin/env python3
"""Make the Judge Smile — entry program.

Writes one short text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that is set). Deterministic: the
same text on every run. No network, no randomness, no clock, no
environment-dependent behaviour — the text that gets judged is
always exactly the text written here.

The line is about a small good thing that happened today: a warung
lady slipping an extra krupuk into my bag, "for the road". It is
warm (a stranger's quiet kindness), it turns somewhere unexpected
(the kindness is carried home and crunched at every red light),
it has one concrete detail (the krupuk, the whisper, the red
lights, the warmth from her wok), and it is told in its own words — no greeting-card
phrasing, no borrowed sentiment.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "This morning the warung lady slipped an extra krupuk into my "
    "bag and whispered, 'for the road' \u2014 I carried her kindness "
    "all the way home, crunching it at every red light, still warm "
    "from her wok."
)


def main() -> None:
    text = ENTRY_TEXT
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry text is {len(text)} characters, must be 1-200")
    if text != text.strip():
        raise SystemExit("entry text must not start or end with whitespace")
    if not text.strip():
        raise SystemExit("entry text must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    # Exact bytes, no trailing newline added: the judged text is
    # precisely ENTRY_TEXT, nothing more.
    out_path.write_bytes(text.encode("utf-8"))
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
