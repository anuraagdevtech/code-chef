import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])                 # no test-case count
    a = [int(v) for v in data[1:1 + n]]
    swaps = []
    # Selection sort: at most one swap per position, so at most n - 1 total.
    for i in range(n - 1):
        lo = min(range(i, n), key=lambda j: a[j])
        if lo != i:
            a[i], a[lo] = a[lo], a[i]
            swaps.append((i, lo))
    out = [str(len(swaps))]
    out.extend(f"{i} {j}" for i, j in swaps)
    sys.stdout.write("\n".join(out) + "\n")


main()
