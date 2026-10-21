import sys

ONE = 0x31


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        rows = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        row_has = [ONE in r for r in rows]
        col_has = [False] * m
        for r in rows:
            for j in range(m):
                if r[j] == ONE:
                    col_has[j] = True
        if not any(row_has):
            line = " ".join(["-1"] * m)
            out.extend([line] * n)
            continue
        for i in range(n):
            r = rows[i]
            # 0 if already one, 1 if the row or column has one, else 2.
            out.append(" ".join(
                "0" if r[j] == ONE else ("1" if row_has[i] or col_has[j] else "2")
                for j in range(m)))
    sys.stdout.write("\n".join(out) + "\n")


main()
