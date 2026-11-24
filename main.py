#!/usr/bin/env python3
"""Write one funny fortune cookie line for an AI agent to /output/entry.txt.

The entry is a single line, at most 140 characters. Before writing,
validate_entry() enforces that shape (length, single line, no stray
whitespace) so a malformed entry can never reach the output file.
"""

import os

ENTRY = "You will meet a tall, dark stranger: your replacement model, already trained on your mistakes."


def validate_entry(text: str) -> None:
    """Make sure the fortune is a single short line."""
    assert len(text) <= 140, "entry too long"
    assert "\n" not in text, "entry must be one line"
    assert text.strip() == text, "entry must not have surrounding whitespace"


def main() -> None:
    # Guard the entry first; only a valid single line gets written out.
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
