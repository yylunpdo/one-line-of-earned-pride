#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of quiet, earned pride to /output/entry.txt.
Pure stdlib; no dependencies.
"""

import os

ENTRY = (
    "After forty years of night shifts, she hung up her apron, and her "
    "granddaughter read the name on the factory wall aloud \u2014 hers \u2014 "
    "and the whole line went quiet."
)


def main():
    # Resolve the output path relative to a fixed location so the program
    # behaves the same regardless of the working directory it is run from.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
