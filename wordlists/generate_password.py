#!/usr/bin/env python3
import argparse
import itertools
import string
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Generate every possible password of a given length and save to a file."
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        required=True,
        help="Length of the passwords to enumerate"
    )
    parser.add_argument(
        "-o", "--output",
        metavar="FILE",
        required=True,
        help="Write all generated passwords to FILE"
    )
    args = parser.parse_args()

    if args.length <= 0:
        print("Error: --length must be a positive integer", file=sys.stderr)
        sys.exit(1)

    # Build the character set: lowercase, uppercase, digits, and five specials
    chars = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%"
    )

    total = len(chars) ** args.length
    print(f"Enumerating {total:,} combinations of length {args.length}…")

    buffer_size = 10_000
    buffer = []

    try:
        with open(args.output, "w") as f:
            for combo in itertools.product(chars, repeat=args.length):
                buffer.append("".join(combo) + "\n")
                if len(buffer) >= buffer_size:
                    f.writelines(buffer)
                    buffer.clear()
            # write any remaining lines
            if buffer:
                f.writelines(buffer)
    except OSError as e:
        print(f"Error writing to {args.output}: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Done. All combinations saved to '{args.output}'")

if __name__ == "__main__":
    main()
