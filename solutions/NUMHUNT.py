import sys

BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in BASES:
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in BASES:                 # deterministic below 3 * 10^24
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def next_prime(n: int) -> int:
    while not is_prime(n):
        n += 1
    return n


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        x = int(tok)
        # Two distinct primes: p^2 would be a square, p^3 would be larger.
        p = next_prime(max(2, x))
        out.append(str(p * next_prime(p + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
