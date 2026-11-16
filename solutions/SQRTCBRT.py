import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []

    def cube_root(n):
        estimate = int(n ** (1 / 3))
        while (estimate + 1) ** 3 <= n:
            estimate += 1
        while estimate ** 3 > n:
            estimate -= 1
        return estimate
    for _ in range(next(tokens)):
        need = next(tokens)
        root = need
        while True:
            candidate = need + cube_root(root * root)
            if candidate == root:
                break
            root = candidate
        out.append(str(root * root))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
