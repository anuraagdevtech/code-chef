import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        total = sum(a)
        ways = 0
        left = 0
        for v in a:
            if v == 0:
                right = total - left
                # Strikes alternate, so the two sides must differ by 0 or 1.
                if left == right:
                    ways += 2
                elif abs(left - right) == 1:
                    ways += 1
            left += v
        out.append(str(ways))
    sys.stdout.write("\n".join(out) + "\n")


main()
