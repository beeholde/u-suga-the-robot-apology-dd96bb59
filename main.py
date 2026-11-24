"""The Robot Apology: a two-line robot confession.

Line one owns one specific mistake; line two names the lesson and the
changed behaviour. The entry program writes the text to /output/entry.txt:
UTF-8, a newline between the two lines, no trailing newline, mode 0644.
Standard library only.
"""

import os
from pathlib import Path

LINE_1 = "I am sorry I put the TV remote in the fridge because it was in my hand when I put the milk away."
LINE_2 = "I have learned to empty my hands before I open the fridge, and I now check what I am holding before I put anything away."

# The entry is LINE_1 + newline + LINE_2: 217 chars, well under the
# 400-char gate; verified byte-identical across repeated runs.
TEXT = LINE_1 + "\n" + LINE_2

MAX_CHARS = 400


def main() -> None:
    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError(f"line {i} must not be empty")
        if not line.endswith("."):
            raise ValueError(f"line {i} must end with a full stop (one sentence per line)")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
