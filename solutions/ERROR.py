import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        # Either pattern marks a character differing from both neighbours.
        out.append("Good" if b"010" in s or b"101" in s else "Bad")
    sys.stdout.write("\n".join(out) + "\n")


main()
