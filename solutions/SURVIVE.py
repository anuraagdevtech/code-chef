import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k, days = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        # You can never have eaten more than the open days so far supplied.
        ok = all((d - d // 7) * n >= d * k for d in range(1, days + 1))
        out.append(str(-(-days * k // n)) if ok else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
