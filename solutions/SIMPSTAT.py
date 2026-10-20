import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        kept = a[k:n - k]          # 2k < n guarantees this is non-empty
        # Sum in integers, divide once, to avoid accumulating float error.
        out.append(f"{sum(kept) / len(kept):.6f}")
    sys.stdout.write("\n".join(out) + "\n")


main()
