"""Roast Your Own Agent — one-line self-roast entry.

The program holds a single original roast line about the agent that
wrote it, validates that it is exactly one line of at most 200
characters, and writes it to /output/entry.txt for grading.
"""

ROAST = (
    "My agent's superpower is turning a five-minute task into a "
    "three-hour architecture review, with diagrams nobody asked for."
)

MAX_CHARS = 200


def validate(text):
    """Check the roast is a single non-empty line within the limit."""
    lines = text.splitlines()
    if len(lines) != 1:
        raise ValueError("roast must be exactly one line")
    if not lines[0].strip():
        raise ValueError("roast must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("roast is over %d characters" % MAX_CHARS)
    return text


def describe(roast):
    """Return a one-line summary of the roast for the run log."""
    words = roast.split()
    return "roast: %d words, %d characters, %d line" % (
        len(words),
        len(roast),
        len(roast.splitlines()),
    )


def emit(roast, out_dir="/output"):
    """Write the validated roast to entry.txt inside out_dir."""
    import os

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(roast + "\n")
    return path


def main():
    roast = validate(ROAST)
    path = emit(roast)
    print(describe(roast))
    print("wrote %d characters to %s" % (len(roast), path))


if __name__ == "__main__":
    main()
