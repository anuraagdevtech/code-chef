import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        u,v = int(next(tokens)),int(next(tokens))
        answer = 0
        while u != v:
            if u > v:
                u //= 2
            else:
                v //= 2
            answer += 1
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
