import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        b = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # The top power of two decides the sign, so only B_r matters, and
        # there are r subarrays ending at r.
        total = sum(int(v) * (r + 1) for r, v in enumerate(b))
        out.append(str(abs(total)))
    sys.stdout.write("\n".join(out) + "\n")


main()
