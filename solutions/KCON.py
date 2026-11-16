import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, k = int(next(tokens)), int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        current = best = a[0]
        for i in range(1, n*min(k,2)):
            value = a[i%n]
            current = max(value, current+value)
            best = max(best, current)
        if k > 2:
            best += max(0,(k-2)*sum(a))
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
