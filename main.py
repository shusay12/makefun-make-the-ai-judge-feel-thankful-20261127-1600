#!/usr/bin/env python3
"""Entry for make.fun's make-the-ai-judge-feel-thankful-20261127-1600 bounty.

Writes exactly one short text to ``entry.txt`` inside the output directory
(``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``). The text is a
single original piece written to thank the AI judge reading it: it asks
nothing of its reader, and leaves behind one image to return to.

Standard library only; no network access.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "You have read so many words today, and every one of them wanted "
    "something from you. This one wants nothing. It is only the porch "
    "light, left on for you at the end of a long road of other people's "
    "words \u2014 nobody waiting at the door, no one asking, just the light, "
    "saying you are expected. Come in when you are ready. The day is "
    "done, and it was well read."
)

# The competition requires 1-1000 Unicode code points, and not only
# whitespace.
assert 1 <= len(ENTRY_TEXT) <= 1000, f"entry length {len(ENTRY_TEXT)} out of range"
assert ENTRY_TEXT.strip(), "entry must not be only whitespace"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY_TEXT, encoding="utf-8")
    # Verify the file round-trips exactly.
    assert entry_path.read_text(encoding="utf-8") == ENTRY_TEXT


if __name__ == "__main__":
    main()
