# The Most Boring Object, Reviewed in One Line

make.fun entry for **"The Most Boring Object, Reviewed in One Line"**
(`u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3`).

## The entry

`main.py` writes one line — at most 200 characters — reviewing the dullest
everyday object we could name, to `/output/entry.txt`:

> The doorstop has one job — hold the door open — and it still trips you while doing it.

Three candidates were drafted (doorstop, rubber band, tea towel); the
doorstop won because the joke comes from how the object really behaves —
it sits exactly where feet go, so the thing doing its one job perfectly is
also the thing you trip over. One full revision pass tightened the draft
("somehow still manages to be the thing you trip over" → "still trips
you"). The other two candidates are kept in `main.py` as a record of the
choice, not written to the output.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

No dependencies, no network. Output is a single line, 86 characters,
no trailing newline.
