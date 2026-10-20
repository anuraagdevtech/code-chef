import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        f = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        fuel = f[0]
        dist = 0
        for i in range(1, n):
            if fuel == 0:
                break
            fuel -= 1
            dist += 1
            # Arriving with exactly zero still collects this car's fuel.
            fuel += f[i]
        # Past the last car there is nothing left to collect.
        dist += fuel
        out.append(str(dist))
    sys.stdout.write("\n".join(out) + "\n")


main()
