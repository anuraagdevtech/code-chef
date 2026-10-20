import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        b = [int(v) for v in data[pos + 1 + n:pos + 1 + 2 * n]]
        pos += 1 + 2 * n
        done = 0
        prev = 0                      # the first student starts at time 0
        for i in range(n):
            # Slots are fixed, so an overrun does not eat into the next one.
            if b[i] <= a[i] - prev:
                done += 1
            prev = a[i]
        out.append(str(done))
    sys.stdout.write("\n".join(out) + "\n")


main()
