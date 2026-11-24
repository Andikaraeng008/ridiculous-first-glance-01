"""Ridiculous at First Glance, Real by the Second.

Writes one sentence pitching a bizarre startup idea that sounds
ridiculous at first glance but makes sense as a real business.
"""

import os

TEXT = (
    "We train pigeons to deliver your passwords on paper, because "
    "people who distrust the cloud will pay for a bird that cannot "
    "be hacked."
)


def main():
    # One sentence, 1-200 UTF-8 characters, no trailing newline.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
