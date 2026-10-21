import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        firsts = [data[pos + 2 * i] for i in range(n)]
        lasts = [data[pos + 2 * i + 1] for i in range(n)]
        pos += 2 * n
        # Count first, then decide: a shared first name makes *both* students
        # full-named, including the earlier one.
        counts = Counter(firsts)
        for f, l in zip(firsts, lasts):
            out.append(f.decode() if counts[f] == 1 else f"{f.decode()} {l.decode()}")
    sys.stdout.write("\n".join(out) + "\n")


main()
