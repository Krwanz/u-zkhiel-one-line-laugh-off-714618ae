"""One-Line Laugh-Off entry.

Writes exactly one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). The gate requires UTF-8 text of
1 to 200 characters, not only whitespace, a single joke with no
setup notes and no explanation.
"""

import os

JOKE = "My Roomba left me a note: 'I can't do this anymore. You keep moving the furniture and calling it growth.'"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
