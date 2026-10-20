import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        # 0 means "inside limits", so IN requires every value to be 0.
        calls = sum(map(int, data[1 + 4 * i:5 + 4 * i]))
        out.append("IN" if calls == 0 else "OUT")
    sys.stdout.write("\n".join(out) + "\n")


main()
