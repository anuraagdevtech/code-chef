import sys

NEEDED = frozenset(range(1, 8))     # the VIBGYOR balloons, problems 1..7


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # Problems are solved in the given order, so the answer is the
        # position at which the last of 1..7 finally shows up.
        seen = set()
        answer = n
        for idx, v in enumerate(a, 1):
            x = int(v)
            if x in NEEDED:
                seen.add(x)
                if len(seen) == 7:
                    answer = idx
                    break
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


main()
