#!/usr/bin/env python3
"""Make the Judge Laugh in One Line -- entry program.

Writes exactly one funny line to /output/entry.txt
(or $ENTRY_OUTPUT when set, for local testing).

The line: a lie to a fitness tracker that backfires when the tracker
believes it, so the punchline turns the gadget into an accomplice.
Setup, break, punch at the end, nothing to explain.

Deterministic, standard library only, no network, no randomness.
"""

import os

LINE = "I told my fitness tracker I ran a marathon. It believed me, and now we're both lying to my doctor."


def main():
    # Sealed scorer takes 1-200 chars on one line: fail loudly instead
    # of ever writing an entry the grader would reject.
    if "\n" in LINE or "\r" in LINE or not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be one line of 1-200 characters")
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
