#!/usr/bin/env python3
"""Aged Like Wine — entry for The Painfully Honest Out-of-Office on make.fun.

Prints exactly one out-of-office auto-reply (at most 200 characters):
painfully honest about the absence, still polite.
"""

LINE = "I am out of office until Monday. My inbox is not monitored, my enthusiasm is on leave too, and your 'urgent' email will be aged like a fine wine."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
