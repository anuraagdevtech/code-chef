import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    r = int(data[0])
    pos = 1
    out = []
    for _ in range(r):
        # data[pos] is L, which Python does not need.
        s = data[pos + 1]
        pos += 2
        inside = False
        valid = True
        for ch in s:
            if ch == 72:          # 'H'
                if inside:
                    valid = False
                    break
                inside = True
            elif ch == 84:        # 'T'
                if not inside:
                    valid = False
                    break
                inside = False
        # A snake left open at the end is also invalid.
        out.append("Valid" if valid and not inside else "Invalid")
    sys.stdout.write("\n".join(out) + "\n")


main()
