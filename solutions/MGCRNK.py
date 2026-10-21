import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        row = [0] * n
        for i in range(n):
            vals = [int(x) for x in data[pos:pos + n]]
            pos += n
            for j in range(n):
                if i == 0:
                    row[j] = vals[j] + (row[j - 1] if j else 0)
                elif j == 0:
                    row[j] += vals[j]
                else:
                    row[j] = vals[j] + (row[j] if row[j] > row[j - 1] else row[j - 1])
        best = row[n - 1]
        # Every monotone path passes the same 2N - 3 judges, so the average is
        # just the best sum over a constant.
        out.append("Bad Judges" if best < 0 else f"{best / (2 * n - 3):.6f}")
    sys.stdout.write("\n".join(out) + "\n")


main()
