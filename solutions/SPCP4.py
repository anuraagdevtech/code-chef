import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, k = map(int, data[1 + 3 * i:4 + 3 * i])
        boys_left, girls_left = x % k, (n - x) % k
        # Dancing pairs cancel leftovers off; only the imbalance reads.
        out.append(str(abs(boys_left - girls_left)))
    sys.stdout.write("\n".join(out) + "\n")


main()
