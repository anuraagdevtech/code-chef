import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        k = int(data[2 + 3 * i])
        s = data[3 + 3 * i]
        seen_a = 0
        inside = 0
        for c in s:
            if c == 0x61:
                seen_a += 1
            elif c == 0x62:
                inside += seen_a
        total_b = s.count(0x62)
        # Every 'a' of an earlier copy precedes every 'b' of a later one.
        out.append(str(k * inside + seen_a * total_b * (k * (k - 1) // 2)))
    sys.stdout.write("\n".join(out) + "\n")


main()
