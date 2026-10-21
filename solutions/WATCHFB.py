import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        states = [(0, 0)]
        for _ in range(n):
            kind = data[pos]
            a, b = int(data[pos + 1]), int(data[pos + 2])
            pos += 3
            cand = [(a, b)] if kind == b"1" or a == b else [(a, b), (b, a)]
            # Goals only accumulate, so a candidate must dominate some past state.
            states = [c for c in cand
                      if any(c[0] >= p[0] and c[1] >= p[1] for p in states)]
            out.append("YES" if len({c[0] for c in states}) == 1 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
