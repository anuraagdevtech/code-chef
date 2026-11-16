import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        residue = n % k
        candidates = [residue // 2]
        if n >= k:
            candidates.append((residue + k) // 2)
        out.append(str(max(candidates, key=lambda x: x % k * ((n - x) % k))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
