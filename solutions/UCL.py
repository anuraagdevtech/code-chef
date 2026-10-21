import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        points, diff = {}, {}
        for _ in range(12):
            home = data[pos].decode()
            hg, ag = int(data[pos + 1]), int(data[pos + 3])
            away = data[pos + 4].decode()
            pos += 5                      # the literal "vs." is token 3
            for name in (home, away):
                points.setdefault(name, 0)
                diff.setdefault(name, 0)
            diff[home] += hg - ag
            diff[away] += ag - hg
            if hg > ag:
                points[home] += 3
            elif ag > hg:
                points[away] += 3
            else:
                points[home] += 1
                points[away] += 1
        order = sorted(points, key=lambda n: (-points[n], -diff[n]))
        out.append(f"{order[0]} {order[1]}")
    sys.stdout.write("\n".join(out) + "\n")


main()
