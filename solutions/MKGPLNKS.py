import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        # data[pos] is N, which Python does not need.
        s = data[pos + 1]
        pos += 2
        # Painting a plank repaints its whole run, merging it with both
        # neighbours, so each operation removes two runs.
        runs = 1 + sum(1 for i in range(1, len(s)) if s[i] != s[i - 1])
        out.append(str(runs // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
