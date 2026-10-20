import sys

# Applied in one pass, so A->T does not get undone by a later T->A.
COMPLEMENT = str.maketrans("ATCG", "TAGC")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        # data[pos] is N, which Python does not need, but must be skipped.
        s = data[pos + 1].decode()
        pos += 2
        out.append(s.translate(COMPLEMENT))
    sys.stdout.write("\n".join(out) + "\n")


main()
