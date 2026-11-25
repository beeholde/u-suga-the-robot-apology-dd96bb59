"""The Robot Apology (v2): a two-line robot confession.

The program writes exactly two lines to /output/entry.txt:
line one owns one specific mistake, line two names the lesson and the
changed behaviour. Gate: UTF-8 text, 1-400 chars, not whitespace-only.
Standard library only; the output file gets mode 0644.
"""

import os
from pathlib import Path

FIRST_LINE = (
    "I am sorry I fed the goldfish twice because the first flakes "
    "vanished before I looked up."
)
SECOND_LINE = (
    "I have learned that a clear surface is not a hungry fish, "
    "and I now feed once and write it down."
)

ENTRY_TEXT = FIRST_LINE + "\n" + SECOND_LINE  # 186 chars, under the 400 gate


def _check(text: str) -> list[str]:
    """Return the entry's two lines, raising if the gate fails."""
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry is {len(text)} chars, must be 1-400")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines")
    for number, line in enumerate(lines, start=1):
        if not line.strip():
            raise ValueError(f"line {number} must not be empty")
        if not line.endswith("."):
            raise ValueError(
                f"line {number} must end with a full stop "
                "(one sentence per line)"
            )
    return lines


def main() -> None:
    lines = _check(ENTRY_TEXT)
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY_TEXT, encoding="utf-8")
    os.chmod(target, 0o644)
    # Read back what was written: the file must hold exactly the two
    # checked lines, byte for byte, or the run has failed.
    if target.read_text(encoding="utf-8") != ENTRY_TEXT:
        raise ValueError("entry.txt does not match the checked entry text")
    assert len(lines) == 2


if __name__ == "__main__":
    main()
