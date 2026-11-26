"""Sleep patch note, recovery cycle 1: the mental-tabs fix."""
from pathlib import Path

NOTE = "Fixed a bug where sleep required closing 47 mental tabs first; brains now shut down with one click."

def main():
    # Gate: exactly one line, 1-160 chars, no trailing newline added.
    assert 1 <= len(NOTE) <= 160, len(NOTE)
    assert "\n" not in NOTE
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(NOTE, encoding="utf-8")

if __name__ == "__main__":
    main()
