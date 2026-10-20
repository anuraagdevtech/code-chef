import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        evens = sum(1 for v in data[pos + 2:pos + 2 + n] if int(v) % 2 == 0)
        pos += 2 + n
        if evens == 0:
            out.append("0")
        elif x % 2:
            # The OR forces the low bit, so one move fixes two elements.
            out.append(str((evens + 1) // 2))
        elif evens == n:
            # No odd partner exists and none can be created.
            out.append("-1")
        else:
            # Each move needs one odd partner and converts one even.
            out.append(str(evens))
    sys.stdout.write("\n".join(out) + "\n")


main()
