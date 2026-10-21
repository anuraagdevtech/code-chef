import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        best = second = 0
        run = 0
        for i in range(n):
            if data[pos + 1 + i] == b"0":
                run += 1
                continue
            if run > best:
                best, second = run, best
            elif run > second:
                second = run
            run = 0
        if run > best:
            best, second = run, best
        elif run > second:
            second = run
        pos += 1 + n
        # Odd longest run, and its half must outgrow the runner-up.
        out.append("Yes" if best % 2 and (best + 1) // 2 > second else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
