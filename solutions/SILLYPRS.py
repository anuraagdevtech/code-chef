import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        b = [int(v) for v in data[pos + 1 + n:pos + 1 + 2 * n]]
        pos += 1 + 2 * n
        odd_a = sum(1 for v in a if v % 2)
        odd_b = sum(1 for v in b if v % 2)
        # Only parity matters: each mismatched pair costs half a unit.
        matched = min(odd_a, odd_b) + min(n - odd_a, n - odd_b)
        out.append(str((sum(a) + sum(b) - (n - matched)) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
