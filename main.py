#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint — make.fun entry.

Writes the entry line to /output/entry.txt, byte-exact, UTF-8.
Gate: 1-200 characters, not only whitespace.
"""

import os

ENTRY = (
    "I can stop time for exactly one second, just once \u2014 "
    "and I already spent it in 2019 deciding what to have for lunch."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def validate(text: str) -> str:
    """Enforce the gate contract: a single line of 1-200 characters,
    UTF-8 encodable, not only whitespace. Returns the text unchanged."""
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    text.encode("utf-8")  # raises if not encodable
    return text


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
