import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    subtask = int(data[0])            # not the test count
    t = int(data[1])
    out = []
    for i in range(t):
        x1, y1, x2, y2, x3, y3 = map(int, data[2 + 6 * i:8 + 6 * i])
        # Squared lengths stay exact integers, so no sqrt and no floats.
        d = sorted((
            (x1 - x2) ** 2 + (y1 - y2) ** 2,
            (x2 - x3) ** 2 + (y2 - y3) ** 2,
            (x1 - x3) ** 2 + (y1 - y3) ** 2,
        ))
        by_side = "Isosceles" if d[0] == d[1] or d[1] == d[2] else "Scalene"
        if subtask == 1:
            out.append(f"{by_side} triangle")
        else:
            # The largest side faces the largest angle.
            total = d[0] + d[1]
            by_angle = "right" if total == d[2] else "acute" if total > d[2] else "obtuse"
            out.append(f"{by_side} {by_angle} triangle")
    sys.stdout.write("\n".join(out) + "\n")


main()
