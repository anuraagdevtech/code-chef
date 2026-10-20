import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Two odd counts admit no palindrome; fewer than two of either letter
        # admits only one.
        if (x % 2 and y % 2) or x < 2 or y < 2:
            out.append("-1")
            continue
        ha, hb = x // 2, y // 2
        middle = "a" if x % 2 else ("b" if y % 2 else "")
        h1 = "a" * ha + "b" * hb
        h2 = "b" + "a" * ha + "b" * (hb - 1)
        out.append(h1 + middle + h1[::-1])
        out.append(h2 + middle + h2[::-1])
    sys.stdout.write("\n".join(out) + "\n")


main()
