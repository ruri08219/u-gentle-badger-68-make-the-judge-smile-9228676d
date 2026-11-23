#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry.

Writes exactly one line of text (1-200 characters) about a small good
thing that happened today, to /output/entry.txt.
Stdlib only, no network, no randomness, no clock.
"""

import os

ENTRY = (
    "At 7 a.m. the bus driver waited while an old man shuffled across "
    "with his cane, then tapped the bell twice like a small applause "
    "\u2014 nobody clapped, but everyone smiled."
)


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
