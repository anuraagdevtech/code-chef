import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        codes = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # Only two categories exist, so one count determines the other.
        start = codes.count(b"START38")
        out.append(f"{start} {n - start}")
    sys.stdout.write("\n".join(out) + "\n")


main()
