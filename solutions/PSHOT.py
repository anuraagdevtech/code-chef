import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        ga = gb = 0
        answer = 2 * n
        for k, c in enumerate(s, 1):
            if c == 0x31:
                if k % 2:
                    ga += 1
                else:
                    gb += 1
            # Compare against the opponent's best possible finish.
            if ga > gb + (n - k // 2) or gb > ga + (n - (k + 1) // 2):
                answer = k
                break
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


main()
