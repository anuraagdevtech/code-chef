import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, h, y1, y2, life = (int(v) for v in data[pos:pos + 5])
        pos += 5
        ducked = h - y1
        passed = 0
        for i in range(n):
            kind, x = int(data[pos + 2 * i]), int(data[pos + 2 * i + 1])
            # Touching counts as passing, so both tests are inclusive.
            if (kind == 2 and x <= y2) or (kind == 1 and ducked <= x):
                passed += 1
                continue
            life -= 1
            if life == 0:
                break            # exhausted on this barrier, so it is not passed
            passed += 1
        pos += 2 * n
        out.append(str(passed))
    sys.stdout.write("\n".join(out) + "\n")


main()
