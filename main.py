"""The Robot Apology -- entry program.

Writes one two-line robot confession to /output/entry.txt:
line 1 apologises in a single sentence for one specific mistake,
line 2 says what the robot learned and what it will do differently.
"""

import os

LINE_1 = (
    "I'm sorry I woke the baby at 3 a.m. by running the vacuum under her "
    "crib just as she had finally fallen asleep."
)
LINE_2 = (
    "I learned a clean floor can wait until morning, so now I check the "
    "nursery monitor before starting any chore after bedtime."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2 + "\n"
    # Mirror the competition gate: 1-400 chars of UTF-8 text, not only
    # whitespace, so a bad entry fails loudly here instead of at grading.
    body = text.strip()
    if not body or len(text) > 400:
        raise SystemExit(f"entry fails the gate: {len(text)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
