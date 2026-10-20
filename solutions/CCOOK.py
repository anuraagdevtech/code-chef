import sys

LEVELS = ("Beginner", "Junior Developer", "Middle Developer",
          "Senior Developer", "Hacker", "Jeff Dean")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])          # no test-case count: this is the contestant count
    out = []
    for i in range(n):
        solved = sum(map(int, data[1 + 5 * i:6 + 5 * i]))
        out.append(LEVELS[solved])
    sys.stdout.write("\n".join(out) + "\n")


main()
