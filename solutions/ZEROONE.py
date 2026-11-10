"""CodeChef ZEROONE — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        c = [int(next(it)) for _ in range(n)]
        c[::2] = sorted(c[::2], reverse=True)
        c[1::2] = sorted(c[1::2])
        zeros = answer = 0
        for i, x in enumerate(c):
            if i % 2 == 0:
                zeros += x
            else:
                answer += zeros*x
        out.append(' '.join(map(str, c)))
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
