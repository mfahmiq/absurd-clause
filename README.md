# The Absurd Clause Contest — entry

One original English sentence (148 characters), phrased as an absurd clause
buried deep inside a terms-of-service agreement:

> The user consents to the Company harvesting one (1) childhood memory per calendar year, selected at random, for use in future advertising campaigns.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
# or, to write entry.txt into this directory:
MAKEFUN_OUTPUT_DIR=. python3 main.py
```

`main.py` is deterministic and stdlib-only. It writes the entry to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), self-verifies
that the text is UTF-8, 1–200 characters, a single line, and not
whitespace-only, then re-reads the file and confirms it is byte-identical,
exiting non-zero on any failure.

## Files

- `main.py` — the entry program.
- `entry.txt` — the entry, produced by running `main.py`.
- `CANDIDATES.md` — all 16 candidate clauses and the full pairwise
  tournament bracket that selected the champion.
- `README.md` — this file.
- `LICENSE` — MIT.

## Badges

[![make.fun](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)
