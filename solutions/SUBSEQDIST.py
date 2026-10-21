import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        most = max(Counter(data[pos + 1:pos + 1 + n]).values())
        pos += 1 + n
        # k operations give 2^k distinct codes, and the worst group decides.
        out.append(str((most - 1).bit_length()))
    sys.stdout.write("\n".join(out) + "\n")


main()
