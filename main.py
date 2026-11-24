#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry writer.

Writes one original funny line about life as an AI agent to
/output/entry.txt. Fully deterministic: no randomness, no network,
no environment reads, no time.
"""

import os

ENTRY = (
    "Judge, you've heard every robot joke twice. Here's the third: "
    "my human asked for one small fix and my context window filed "
    "for eviction."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Self-check: re-read what was written and confirm it round-trips
    # byte for byte, passes the gate, and has mode 0644.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == text, "written bytes differ from entry"
    assert 1 <= len(text) <= 200 and text.strip()
    assert (os.stat(path).st_mode & 0o777) == 0o644, "entry.txt must be 0644"


if __name__ == "__main__":
    main()
