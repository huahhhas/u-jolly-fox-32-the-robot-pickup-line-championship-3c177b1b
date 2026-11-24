#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line, a single line of at most 200 characters,
in the voice of a robot trying to charm someone, to /output/entry.txt.
"""
import os

LINE = "I scanned every human on Earth and my algorithm kept crashing — it couldn't process how cute you are."

def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
