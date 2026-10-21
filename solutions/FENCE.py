import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        k = int(data[pos + 2])
        pos += 3
        plants = set()
        for _ in range(k):
            plants.add((int(data[pos]), int(data[pos + 1])))
            pos += 2
        # Look only right and down so each adjacent pair is counted once.
        shared = sum(((r, c + 1) in plants) + ((r + 1, c) in plants)
                     for r, c in plants)
        out.append(str(4 * k - 2 * shared))
    sys.stdout.write("\n".join(out) + "\n")


main()
