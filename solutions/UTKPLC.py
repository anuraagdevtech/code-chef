import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        first, second, third, x, y = (c.decode() for c in data[1 + 5 * i:6 + 5 * i])
        # Preference order comes from the input, so build the ranking per case.
        rank = {first: 0, second: 1, third: 2}
        out.append(min(x, y, key=rank.get))
    sys.stdout.write("\n".join(out) + "\n")


main()
