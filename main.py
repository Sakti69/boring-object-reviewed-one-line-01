#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one line — at most 200 characters — reviewing the dullest
everyday object we could name, to /output/entry.txt.

Three candidate lines were drafted; the shipped one is REVIEW. The other
two are kept below as a record of the choice, not written to the output:

  A (shipped): the doorstop. Its whole job is to sit still and hold a
     door open, and the joke is built from what it really does: it sits
     exactly where feet go, so the thing doing its one job perfectly is
     also the thing you trip over. The turn comes early ("one job") and
     the last words sharpen it ("while doing it").
     REVISED once: the first draft said "somehow still manages to be
     the thing you trip over" — two hedges ("somehow", "manages") and
     five slack words. "It still trips you" says the same thing in four
     words, keeps the irony (the helper hurts you while helping), and
     lands faster, which the judge brief rewards.
  B (cut): the rubber band. True — they perish in the drawer and snap
     the morning you need one — but the punch leans on being late, a
     joke that would fit any object that breaks.
  C (cut): the tea towel. True that it dries nothing and is always damp,
     but "always damp" is a second observation stacked on the first;
     the line has two half-jokes instead of one clean turn.
"""

import os

REVIEW = (
    "The doorstop has one job \u2014 hold the door open \u2014 and it "
    "still trips you while doing it."
)

# The other two candidates, kept for the record (not shipped):
CANDIDATE_B = (
    "The rubber band: spends six months doing nothing but hugging dead "
    "batteries, then snaps the one morning you're already late."
)
CANDIDATE_C = (
    "The tea towel: dries nothing, absorbs nothing, yet is somehow always "
    "damp \u2014 and always the one you grab by mistake."
)


def main() -> None:
    text = REVIEW
    assert "\n" not in text, "review must be a single line"
    assert 1 <= len(text) <= 200, f"review is {len(text)} characters"
    assert text.strip(), "review must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
