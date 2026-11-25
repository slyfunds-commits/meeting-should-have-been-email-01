"""Meeting That Should Have Been an Email — make.fun entry.

Writes the keeper line to /output/entry.txt, exactly, with no trailing newline.
Pure stdlib; the grader runs python:3.13-slim with no site-packages.
"""

import os

# The turn: the follow-up email (3 minutes) does the meeting's whole job (47 minutes).
# The number 47 vs 3 is the mechanism — the meeting decided nothing, the follow-up everything.
ENTRY = "The meeting took 47 minutes and decided nothing, but the follow-up took 3 and decided everything."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
