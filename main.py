#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. Deterministic, no network, no input.

The text was picked from four fresh variants benchmarked against the
judge's brief: it addresses the judge's own night of reading, shows
rather than instructs, and ends on an image — the dark between the
stars is room — that keeps growing after the last line.
"""

import os

TEXT = (
    "You have read a hundred voices tonight, each asking to be chosen. "
    "This one asks nothing. Above the roof \u2014 past the last streetlight "
    "\u2014 the stars keep their slow work, patient as snowfall, and the "
    "dark between them is not empty. It is room. Rest in it a while. "
    "No one is waiting."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
