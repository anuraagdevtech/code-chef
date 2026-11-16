import sys
from functools import lru_cache


def main() -> None:
    MOD = 1000000007

    @lru_cache(None)
    def distribution(n, count_a):
        if count_a < 0 or count_a > n:
            return ()
        if n <= 1:
            return (1,) if count_a == 0 else (0, 1)
        left = n // 2
        right = n - left
        result = [0] * (count_a * (n.bit_length() + 1) + 1)
        for x in range(max(0, count_a - right), min(count_a, left) + 1):
            f = distribution(left, x)
            g = distribution(right, count_a - x)
            sf = sg = 0
            for v in range(max(len(f), len(g))):
                fv = f[v] if v < len(f) else 0
                gv = g[v] if v < len(g) else 0
                sg = (sg + gv) % MOD
                result[count_a + v] = (result[count_a + v] + fv * sg + gv * sf) % MOD
                sf = (sf + fv) % MOD
        while result and result[-1] == 0:
            result.pop()
        return tuple(result)
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        count_a, count_e, v = (next(tokens), next(tokens), next(tokens))
        table = distribution(count_a + count_e, count_a)
        out.append(str(table[v] if v < len(table) else 0))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
