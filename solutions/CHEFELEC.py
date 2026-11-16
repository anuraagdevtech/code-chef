import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        s = next(tokens)
        x = [int(next(tokens)) for _ in range(n)]
        answer = x[-1]-x[0]
        seen = s[0] == 49
        largest = 0
        for i in range(1,n):
            if seen:
                largest = max(largest, x[i]-x[i-1])
            if s[i] == 49:
                if seen:
                    answer -= largest
                seen = True
                largest = 0
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
