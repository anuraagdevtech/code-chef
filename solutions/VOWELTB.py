import sys

VOWELS = {"A", "E", "I", "O", "U"}


def main() -> None:
    # Single character, no test-case count.
    c = sys.stdin.buffer.read().split()[0].decode()
    print("Vowel" if c in VOWELS else "Consonant")


main()
