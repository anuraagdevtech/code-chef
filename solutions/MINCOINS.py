import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        if x % 5:
            out.append("-1")          # only multiples of 5 are payable
        else:
            # 10s are nested multiples of 5, so greedy is safe here.
            out.append(str(x // 10 + (1 if x % 10 else 0)))
    sys.stdout.write("\n".join(out) + "\n")


main()
