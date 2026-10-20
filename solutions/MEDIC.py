import sys


def is_leap(y: int) -> bool:
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def month_len(y: int, m: int) -> int:
    if m == 2:
        return 29 if is_leap(y) else 28
    return 30 if m in (4, 6, 9, 11) else 31


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        y, m, d = (int(p) for p in data[1 + i].decode().split(":"))
        parity = d % 2
        total = 0
        while True:
            ell = month_len(y, m)
            total += (ell - d) // 2 + 1
            # The chain survives the boundary only from an even-length month.
            if ell % 2:
                break
            m += 1
            if m == 13:
                m, y = 1, y + 1
            d = 1 if parity else 2
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
