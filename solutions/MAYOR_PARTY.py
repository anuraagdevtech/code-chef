import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        pa, pb, pc = map(int, data[1 + 3 * i:4 + 3 * i])
        # A and C do not conflict, so the only choice is B alone vs A plus C.
        out.append(str(max(pb, pa + pc)))
    sys.stdout.write("\n".join(out) + "\n")


main()
