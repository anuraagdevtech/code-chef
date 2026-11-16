import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, k = int(next(tokens)), int(next(tokens))
        s = next(tokens)
        changes = sum(s[i] != s[i-1] for i in range(1, k))
        answer = changes + (s[k-1] == 48)
        for right in range(k, n):
            changes -= s[right-k] != s[right-k+1]
            changes += s[right-1] != s[right]
            answer = min(answer, changes + (s[right] == 48))
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
