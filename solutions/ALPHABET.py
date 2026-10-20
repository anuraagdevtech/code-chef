import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    # No test-case count: known letters, then the word count, then the words.
    known = set(data[0])
    n = int(data[1])
    # Repetition and order are irrelevant, so compare as sets.
    out = ["Yes" if set(data[2 + i]) <= known else "No" for i in range(n)]
    sys.stdout.write("\n".join(out) + "\n")


main()
