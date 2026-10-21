import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        total = 0
        run = 0
        prev = None
        for v in a:
            # run = subarrays ending here, which is the stretch length itself.
            run = run + 1 if prev is not None and v >= prev else 1
            total += run
            prev = v
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
