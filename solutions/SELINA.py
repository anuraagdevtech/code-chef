import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for word in data[1:1 + t]:
        mask = 0
        for c in word:
            # A letter seen twice toggles its bit back off.
            mask ^= 1 << (c - 0x61)
        if mask == 0:
            out.append("-1")
        else:
            out.append(chr(0x61 + (mask & -mask).bit_length() - 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
