"""One Word From Your Ex — entry: "Almost".

The word my ex would use to describe me. Almost the one. Almost
enough. Almost there. The almost-boyfriend: close enough to hurt,
never close enough to keep. One word, and she would not need a second.
"""

import os

ENTRY_TEXT = "Almost"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
