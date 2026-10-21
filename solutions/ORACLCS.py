import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        words = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # An all-a or all-b omen caps the LCS at the scarcest letter count.
        fewest_a = min(w.count(b"a") for w in words)
        fewest_b = min(w.count(b"b") for w in words)
        out.append(str(min(fewest_a, fewest_b)))
    sys.stdout.write("\n".join(out) + "\n")


main()
