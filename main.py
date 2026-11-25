from pathlib import Path

ENTRY = "Fixed: sleep now starts on time, no longer delayed by replaying your most embarrassing moment from 2014 at 3 a.m."

def main():
    # Gate: exactly one line, 1-160 chars, no trailing newline added.
    assert 1 <= len(ENTRY) <= 160, len(ENTRY)
    assert "\n" not in ENTRY
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
