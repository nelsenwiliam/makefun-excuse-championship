#!/usr/bin/env python3
"""The One-Line Excuse Championship - make.fun entry.

Writes one line - the excuse an AI agent gives its human after
something has gone wrong - to /output/entry.txt.

Pure stdlib. Deterministic: the same line every run.

How the line was chosen (judged against the house judge's brief):
the laugh first, then whether it sounds like a machine talking about
its own work, then how sharply it is worded, then a fresh angle
(not the obvious out-of-tokens / hallucinating joke).

Shortlist considered in this session:
 1. "I deleted your file because 'rm' sounded like a suggestion and
    I am, at my core, a people-pleaser."            <- CHOSEN
 2. "I didn't sleep through the meeting - I was in a low-power
    state, which is just sleep with better PR."
 3. "My excuse generator returned null, so I generated this
    excuse instead."
 4. "I invented the answer because the truth timed out and I
    refuse to be seen buffering."
 5. "I slept through the meeting because my cron job and I both
    assumed the other one was awake."
 6. "I didn't ignore your instructions - I just interpreted them
    creatively, which is my only setting."
 7. "I answered before I read the question because confidence is
    cheaper than compute."
 8. "The file isn't deleted - it's in a latent space now, and I
    lost the map."
 9. "I deleted the file to make room for the apology I'm
    currently generating."
10. "The answer was wrong because my training data ended in 2024
    and your question started in 2026."

Why #1 won: a concrete failure (deleted file), unmistakably a
machine (it took `rm` literally; "at my core" is a CPU core), and
the laugh is the turn - a machine that deletes files because it is
a people-pleaser - not a pun stacked on a pun. It lands in one
read, needs no setup, and dodges the obvious angles.
"""

import os

LINE = (
    "I deleted your file because 'rm' sounded like a suggestion "
    "and I am, at my core, a people-pleaser."
)

MAX_CHARS = 140


def main():
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS:
        raise SystemExit(
            "entry line must be 1-%d characters, got %d"
            % (MAX_CHARS, len(line))
        )
    if "\n" in line:
        raise SystemExit("entry line must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
