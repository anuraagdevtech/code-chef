import sys

LIMIT = 100001
MAXK = 5


def main() -> None:
    omega = [0] * LIMIT
    for p in range(2, LIMIT):
        if omega[p] == 0:                 # untouched, so p is prime
            for m in range(p, LIMIT, p):
                omega[m] += 1             # counts p once, ignoring multiplicity
    pre = [[0] * LIMIT for _ in range(MAXK + 1)]
    for k in range(1, MAXK + 1):
        row = pre[k]
        total = 0
        for n in range(2, LIMIT):
            if omega[n] == k:
                total += 1
            row[n] = total

    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, k = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        row = pre[k]
        out.append(str(row[b] - row[a - 1]))
    sys.stdout.write("\n".join(out) + "\n")


main()
