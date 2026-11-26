#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office -- make.fun entry (revision).

Writes the chosen out-of-office auto-reply, byte-identical, to
/output/entry.txt. The reply is a fixed constant: it is never generated
or paraphrased at runtime.

Revision note: the first build confessed to falling out of love with the
job, which was honest but abstract. This revision keeps that confession's
shape and makes it concrete -- answering emails at midnight and calling
it dedication -- a specific truth a real employee only says privately,
with a tighter, more quotable close.
"""

import os

REPLY = "I'm on leave because I was answering emails at midnight and calling it dedication, so thank you for your patience while I rest and come back actually glad to be here."

MAX_CHARS = 200


def main() -> None:
    # Gate guards: single line, 1-200 characters, no surrounding whitespace.
    assert 1 <= len(REPLY) <= MAX_CHARS, (
        f"reply must be 1-{MAX_CHARS} characters, got {len(REPLY)}"
    )
    assert "\n" not in REPLY and "\r" not in REPLY, (
        "reply must be a single line"
    )
    assert REPLY == REPLY.strip(), (
        "reply must not have leading or trailing whitespace"
    )
    assert REPLY.count(".") == 1 and REPLY.endswith("."), (
        "reply must be a single sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
