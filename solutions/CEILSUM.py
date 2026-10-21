import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        gap = b - a
        if gap == 0:
            out.append("0")               # X is forced, so both halves vanish
        elif gap % 2:
            out.append(str((gap + 1) // 2))   # one half is always odd
        else:
            out.append(str(gap // 2 + 1))     # both halves can be made odd
    sys.stdout.write("\n".join(out) + "\n")


main()
