import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + 2 * i].decode()
        g = data[2 + 2 * i].decode()
        # Each index is judged on its own; there is no "right letter, wrong
        # place" state in this variant.
        out.append("".join("G" if a == b else "B" for a, b in zip(s, g)))
    sys.stdout.write("\n".join(out) + "\n")


main()
