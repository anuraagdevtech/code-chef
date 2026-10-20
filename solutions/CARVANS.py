import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        speeds = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        free = 0
        running_min = float("inf")
        for v in speeds:
            s = int(v)
            # Capped by every car ahead, not merely the one in front.
            if s <= running_min:
                free += 1
                running_min = s
        out.append(str(free))
    sys.stdout.write("\n".join(out) + "\n")


main()
