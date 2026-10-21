import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        both, either = -1, 0
        for tok in data[pos + 1:pos + 1 + n]:
            v = int(tok)
            both &= v
            either |= v
        pos += 1 + n
        # Bits set in every element can be cleared; mixed bits cannot.
        out.append(f"{both} {either ^ both}")
    sys.stdout.write("\n".join(out) + "\n")


main()
