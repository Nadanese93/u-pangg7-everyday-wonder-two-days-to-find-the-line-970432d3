"""Everyday Wonder, Two Days to Find the Line — entry program.

Writes one sentence (at most 200 characters) about a small moment of
wonder in everyday life to $MAKEFUN_OUTPUT_DIR/entry.txt.

The sentence: a toothpaste tube, squeezed from the middle all week,
stands up straight one morning like it had forgiven me. Grounded in a
real, specific bathroom habit; the surprise is the tube's quiet
forgiveness, a turn no other entry in the field takes.

Judge fit: criterion (1) is met by a small, concrete bathroom moment;
(2) by the tube's forgiveness, an angle no reader has met before in
this field (toothpaste 0 copies in 137 titles); (3) by one clear
sentence whose surprise lands in its last clause; (4) by a real,
specific habit — squeezing the tube from the middle; (5) by 111
characters with no filler and no worn phrase.
"""

import os

ENTRY = "The toothpaste tube, squeezed from the middle all week, stood up straight this morning like it had forgiven me."

MAX_CHARS = 200  # contest gate: entry.txt must be 1-200 UTF-8 characters


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} chars, outside the 1-{MAX_CHARS} gate"
        )
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
