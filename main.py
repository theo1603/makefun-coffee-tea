#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes exactly one letter, ``A``, to ``/output/entry.txt``.
Python 3.13 standard library only; no network, no randomness,
fully deterministic.

The choice is coffee. Against the judge's brief, in its own order:
coffee is the more vivid drink -- dark, bitter, steaming, the jolt
that wakes a room -- where tea is gentle and quiet. It is the funnier
one too: coffee carries the joke everyone already tells, the
"don't talk to me before coffee" morning, the fifth cup, the trembling
hand. And it is the truer answer for the person sending it: coffee is
what people actually reach for first, honestly, every morning, not
the calmer drink they wish they were. One letter, A, and nothing else.
"""

import os

def choose_letter() -> str:
    """Pick the letter to send, scored on the judge's brief, in order.

    The brief weighs vividness first, then funniness, then truth.
    Coffee beats tea on all three: it is the more vivid drink (dark,
    bitter, steaming, the jolt that wakes a room, where tea is gentle
    and quiet); the funnier one (the "don't talk to me before coffee"
    morning, the fifth cup, the trembling hand -- jokes tea does not
    carry); and the truer answer (coffee is what people honestly reach
    for first every morning, not the calmer drink they wish they were).
    So the letter is A, for coffee.
    """
    return "A"


LETTER = choose_letter()

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Self-check the gate: re-read and verify the file holds exactly
    # one character, valid UTF-8, and not only white space.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    assert len(text) == 1, f"entry must be 1 character, got {len(text)}"
    assert not text.isspace(), "entry must not be only white space"
    assert text == LETTER, f"entry must be {LETTER!r}, got {text!r}"


if __name__ == "__main__":
    main()
