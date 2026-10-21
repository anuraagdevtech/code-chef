import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # Only zeros inside N's own width count, so measure against bit_length.
        out.append(str(n.bit_length() - n.bit_count()))
    sys.stdout.write("\n".join(out) + "\n")


main()
