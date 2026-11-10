"""CodeChef BWALL — standalone Python 3 solution."""
import sys


MOD = 1000000007


def transitions(mask):
    result = [0]*4

    def fill(cur, nxt):
        if cur == 3:
            result[nxt] += 1
            return
        row = 0 if not cur & 1 else 1
        fill(cur | (1 << row), nxt)
        for missing in range(4):
            cells = [i for i in range(4) if i != missing]
            if row not in cells:
                continue
            left = sum(1 << i for i in cells if i < 2)
            right = sum(1 << (i-2) for i in cells if i >= 2)
            if not cur & left and not nxt & right:
                fill(cur | left, nxt | right)

    fill(mask, 0)
    return result


powers = [[transitions(mask) for mask in range(4)]]
for _ in range(30):
    a = powers[-1]
    powers.append([[sum(a[i][k]*a[k][j] for k in range(4)) % MOD for j in range(4)] for i in range(4)])


def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        v = [1,0,0,0]
        bit = 0
        while n:
            if n & 1:
                v = [sum(v[i]*powers[bit][i][j] for i in range(4)) % MOD for j in range(4)]
            n >>= 1
            bit += 1
        out.append(str(v[0]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
