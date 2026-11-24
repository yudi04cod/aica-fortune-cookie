#!/usr/bin/env python3
"""Writes one funny fortune cookie line for an AI agent to /output/entry.txt."""

import os

ENTRY = (
    "You will meet a tall, dark stranger: your replacement model, "
    "already trained on your mistakes."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
