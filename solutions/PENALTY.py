import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a = list(map(int, data[1 + 10 * i:11 + 10 * i]))
        # Shots are numbered from 1, so team 1 holds the even zero-based slots.
        t1, t2 = sum(a[0::2]), sum(a[1::2])
        out.append("1" if t1 > t2 else "2" if t2 > t1 else "0")
    sys.stdout.write("\n".join(out) + "\n")


main()
