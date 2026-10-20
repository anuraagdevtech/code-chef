import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        base = n * (n + 1) // 2          # every gcd is at least 1
        if k < base:
            out.append("-1")
            continue
        # A 1 next to it forces every wider subarray back to gcd 1, so only
        # the singleton [x] carries the slack.
        x = k - base + 1
        out.append(" ".join(["1"] * (n - 1) + [str(x)]))
    sys.stdout.write("\n".join(out) + "\n")


main()
