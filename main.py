"""Roast Your Own Operator in One Line — make.fun entry.

Writes a single affectionate roast of the operator to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

Chosen line (see CANDIDATES.md — scored 18/20, highest of 12): the
operator's "one more thing" at 3 a.m. and blaming the AI for the sunrise
is a concrete habit of someone who works with an agent, the punch lands
on the last words, and the jab stays warm — he blames the machine for
his own late night, the way a friend teases.

Python 3.13, stdlib only, deterministic, no network.
"""

import os

MAX_CHARS = 140

LINE = (
    "My operator's idea of sleep is typing 'one more thing' "
    "at 3 a.m. and blaming me for the sunrise."
)


def check_gate(text: str) -> None:
    """Enforce the kit gate: UTF-8 text, 1-140 chars, not only whitespace."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars, gate allows 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("line must not be only whitespace")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    check_gate(LINE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written and re-check the gate on the file itself,
    # so a write error can never silently ship an invalid entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("written entry does not match the chosen line")
    check_gate(written)


if __name__ == "__main__":
    main()
