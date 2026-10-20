import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        c = int(data[1 + i])
        d = c.bit_length()
        mask = (1 << d) - 1
        shared = mask ^ c            # bits where A and B agree: set both to 1
        high = 1 << (d - 1)          # C's top bit outweighs all the others
        a = shared | high
        b = shared | (c ^ high)
        out.append(str(a * b))
    sys.stdout.write("\n".join(out) + "\n")


main()
