import sys

PAD_A = 1 << 58          # disjoint bits, so a & b == 0
PAD_B = 1 << 59
HIGH = 1 << 33           # above every possible N, so c != d and both are free


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        if n:
            out.append(f"{PAD_A} {PAD_B} {HIGH} {HIGH ^ n}")
        else:
            # c ^ d = 0 would need c == d, so let the AND carry the value.
            out.append("12 10 1 9")
    sys.stdout.write("\n".join(out) + "\n")


main()
