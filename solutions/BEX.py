import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    pos = 1
    vals = [0] * (n + 1)
    names = [b""] * (n + 1)
    best = [0] * (n + 1)      # best[i] = position of the pick among the bottom i
    sz = 0
    out = []
    for _ in range(n):
        tok = data[pos]
        pos += 1
        if tok == b"-1":
            j = best[sz]
            out.append(f"{sz - j} {names[j].decode()}")
            sz = j - 1        # the pick and everything above it leave the pile
        else:
            v = int(tok)
            name = data[pos]
            pos += 1
            if v == 0:        # no exercises left, so it never joins the pile
                continue
            sz += 1
            vals[sz] = v
            names[sz] = name
            # <= rather than < so a tie prefers the higher (newer) book.
            best[sz] = sz if sz == 1 or v <= vals[best[sz - 1]] else best[sz - 1]
    sys.stdout.write("\n".join(out) + "\n")


main()
