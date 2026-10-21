import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k, l = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        speeds = [int(x) for x in data[pos + 3:pos + 3 + n]]
        pos += 3 + n
        rival = max(speeds[:-1]) if n > 1 else float("-inf")
        # The dose is capped at L - 1, and a non-positive K is never worth using.
        boost = (l - 1) * k if k > 0 else 0
        out.append("Yes" if speeds[-1] + boost > rival else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
