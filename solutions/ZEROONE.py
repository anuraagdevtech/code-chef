import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        c = [int(next(tokens)) for _ in range(n)]
        c[::2] = sorted(c[::2], reverse=True)
        c[1::2] = sorted(c[1::2])
        zeros = answer = 0
        for i, value in enumerate(c):
            if i%2 == 0:
                zeros += value
            else:
                answer += zeros*value
        out.append(' '.join(map(str,c)))
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
