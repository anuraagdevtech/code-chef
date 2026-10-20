import sys

LIMIT = 10 ** 6 + 1


def build_sieve():
    is_prime = bytearray([1]) * LIMIT
    is_prime[0] = is_prime[1] = 0
    for p in range(2, int(LIMIT ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p::p] = bytearray(len(is_prime[p * p::p]))
    return is_prime


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    is_prime = build_sieve()
    out = []
    for i in range(t):
        h = int(data[1 + i])
        best = -1
        k = 0
        # k regular attacks always deal exactly 2^k - 1.
        while (1 << k) - 1 <= h:
            dealt = (1 << k) - 1
            if dealt == h:
                best = k
                break
            rest = h - dealt
            if rest < LIMIT and is_prime[rest]:
                best = k + 1
                break
            k += 1
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
