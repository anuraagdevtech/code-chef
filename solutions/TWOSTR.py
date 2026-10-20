import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = data[1 + 2 * i].decode()
        y = data[2 + 2 * i].decode()
        # '?' matches exactly one character, and may appear in either string.
        ok = all(a == "?" or b == "?" or a == b for a, b in zip(x, y))
        out.append("Yes" if ok else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
