import sys
from itertools import groupby


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        a = bytes(c for c,_ in groupby(next(tokens)))
        b = bytes(c for c,_ in groupby(next(tokens)))
        if len(a) < len(b):
            a,b = b,a
        positions = {}
        for i,c in enumerate(b):
            positions[c] = positions.get(c,0)|(1 << i)
        row = 0
        for c in a:
            x = row|positions.get(c,0)
            row = x&~(x-((row << 1)|1))
        out.append(str(len(a)+len(b)-row.bit_count()))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
