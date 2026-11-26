"""Absurd Clause Contest entry — make.fun.

Entry (148 characters, one sentence, one line):
    The user consents to the Company harvesting one (1) childhood memory
    per calendar year, selected at random, for use in future advertising
    campaigns.

Why it won the internal tournament (see CANDIDATES.md): of 16 candidates,
this clause hides deepest in a real terms-of-service agreement — it is a
data-consent clause, the single most common real ToS clause type, written in
verbatim data-harvesting boilerplate ("consents to the Company harvesting ...
for use in future advertising campaigns") until the harvested object turns
out to be a childhood memory. The joke is one clean absurd image, lands on a
single reading with no outside setup, and the register does the work: the
sentence sounds like genuine legal boilerplate until the absurdity hits.
It beat the runner-up (the interpretive-dance duel before three impartial
pigeons) in the final because it is tighter — a single absurd noun swap
inside an otherwise real clause, rather than two stacked absurdities — and
because a data-consent clause is the clause a reader would least expect to
be a joke, so the ambush is strongest. Tournament path: beat C9 in round 1,
C14 (three raccoons in a trench coat) in the quarterfinal, C5 (goose Gerald,
senior management) in the semifinal, and C2 in the final.

The program also enforces the brief's "one clean sentence" rule: the entry
must end with a full stop and contain no internal sentence terminator that
would split it into two sentences.
"""

import os
import sys

ENTRY = (
    "The user consents to the Company harvesting one (1) childhood memory "
    "per calendar year, selected at random, for use in future advertising "
    "campaigns."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory (repo dir) or a full file path.
    if out_dir.endswith(".txt"):
        out_path = out_dir
    else:
        out_path = os.path.join(out_dir, "entry.txt")

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    data = ENTRY.encode("utf-8")

    # Self-verification before writing.
    if not (1 <= len(ENTRY) <= 200):
        print(f"FAIL: entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1
    if ENTRY.strip() == "":
        print("FAIL: entry is whitespace-only", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("FAIL: entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.endswith("."):
        print("FAIL: entry must be one sentence ending with a full stop", file=sys.stderr)
        return 1
    if ENTRY[:-1].count(".") > 0:
        print("FAIL: entry must be a single sentence", file=sys.stderr)
        return 1

    with open(out_path, "wb") as f:
        f.write(data)

    # Re-read the written file and confirm it is byte-identical.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != data:
        print("FAIL: written file differs from ENTRY", file=sys.stderr)
        return 1
    text = written.decode("utf-8")  # raises on invalid UTF-8
    if not (1 <= len(text) <= 200) or text.strip() == "" or "\n" in text:
        print("FAIL: written file fails gate re-check", file=sys.stderr)
        return 1

    print(f"OK: wrote {out_path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
