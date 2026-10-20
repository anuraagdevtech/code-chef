import sys

LIMIT = 10 ** 6 + 1


def build_omega():
    """omega[k] = number of distinct prime factors of k."""
    omega = [0] * LIMIT
    for p in range(2, LIMIT):
        if omega[p] == 0:                 # p is prime
            for multiple in range(p, LIMIT, p):
                omega[multiple] += 1
    return omega


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    omega = build_omega()
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # The step out of level m is never taken, so stop at m - 1.
        out.append(str(sum(omega[n:m])))
    sys.stdout.write("\n".join(out) + "\n")


main()
