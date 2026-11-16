import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        best = 0
        answer = n
        prime = 2
        while prime * prime <= n:
            exponent = 0
            while n % prime == 0:
                n //= prime
                exponent += 1
            if exponent > best:
                best = exponent
                answer = prime
            prime = 3 if prime == 2 else prime + 2
        if best == 0:
            answer = n
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
