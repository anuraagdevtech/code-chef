import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        h = data[1 + i]
        # All the 'a's form one palindrome and all the 'b's another, so two
        # troops always suffice; one is enough only for a palindrome.
        out.append("1" if h == h[::-1] else "2")
    sys.stdout.write("\n".join(out) + "\n")


main()
