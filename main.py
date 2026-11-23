#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes one original roast line to /output/entry.txt: the smart fridge
that texts its owner about being out of milk while the owner stands
in front of it holding the milk. Deterministic, stdlib only: the same
bytes on every run, no network, no randomness, no time, no input.
"""

import os

ROAST = (
    "My smart fridge texts me we're out of milk while I'm "
    "standing right in front of it, holding the milk."
)


def main() -> None:
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
