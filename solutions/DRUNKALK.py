import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        k = int(data[1 + i])
        # +3 then -1 nets +2 per 2 seconds; an odd second ends mid-stagger.
        out.append(str(k if k % 2 == 0 else k + 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
