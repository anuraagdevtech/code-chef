import sys

ZERO = 0x30


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        if s.count(ZERO) == n:
            out.append(str(n))          # nothing ever spreads
            continue
        neutral = 0
        run = 0
        left = None                     # charge bounding the run on the left
        for c in s:
            if c == ZERO:
                run += 1
                continue
            # Only a run squeezed between opposite charges can survive, and
            # then only its centre cell, when the run has odd length.
            if run and left is not None and left != c:
                neutral += run % 2
            run = 0
            left = c
        out.append(str(neutral))
    sys.stdout.write("\n".join(out) + "\n")


main()
