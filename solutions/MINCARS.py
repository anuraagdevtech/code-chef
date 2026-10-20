import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Everyone must travel, so a partial carload still needs a whole car.
        out.append(str((n + 3) // 4))
    sys.stdout.write("\n".join(out) + "\n")


main()
