import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    pos = 1
    shelf = []
    out = []
    for _ in range(q):
        # Type 1 takes two tokens, type -1 only one.
        if data[pos] == b"1":
            shelf.append(data[pos + 1])
            pos += 2
        else:
            pos += 1
            out.append(shelf.pop().decode() if shelf else "kuchbhi?")
    sys.stdout.write("\n".join(out) + "\n")


main()
