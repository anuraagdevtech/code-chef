import sys


def main() -> None:
    # Single value. Reading it as text counts digits without special-casing 0.
    s = sys.stdin.buffer.read().split()[0].decode()
    d = len(s)
    print(d if d <= 3 else "More than 3 digits")


main()
