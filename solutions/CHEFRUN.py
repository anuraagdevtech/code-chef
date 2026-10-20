import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x1, x2, x3, v1, v2 = map(int, data[1 + 5 * i:6 + 5 * i])
        # x1 < x3 < x2 is guaranteed, so both distances are positive.
        chef, kefa = (x3 - x1) * v2, (x2 - x3) * v1
        out.append("Chef" if chef < kefa else "Kefa" if kefa < chef else "Draw")
    sys.stdout.write("\n".join(out) + "\n")


main()
