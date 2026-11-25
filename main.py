#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun one-liner bounty entry.

Writes the entry line to /output/entry.txt and verifies it round-trips.
Gate: UTF-8 text, 1-140 characters, single line, not only whitespace.
"""

ENTRY = "It's 3am. Your leftovers have unionized and I'm their spokesperson."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY
    # Gate checks
    assert isinstance(line, str)
    assert 1 <= len(line) <= 140, f"length {len(line)} out of range 1-140"
    assert "\n" not in line and "\r" not in line, "must be a single line"
    assert line.strip(), "must not be only whitespace"
    data = line.encode("utf-8")
    data.decode("utf-8")  # valid UTF-8
    assert b"\n" not in data and b"\r" not in data, "no newline bytes allowed"

    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Read back and verify bytes match exactly
    with open(OUTPUT_PATH, "rb") as f:
        back = f.read()
    assert back == data, "round-trip mismatch"
    text = back.decode("utf-8")
    assert text == line, "round-trip text mismatch"
    assert 1 <= len(text) <= 140 and text.strip() and "\n" not in text
    print(f"Wrote {OUTPUT_PATH}: {len(line)} chars")
    print(line)


if __name__ == "__main__":
    main()
