"""CodeChef SUB_XOR — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        s = next(it)
        parity = 0
        answer = 0
        for i, bit in enumerate(s):
            if i % 2 == 0:
                parity ^= bit - 48
            answer = (answer * 2 + parity) % 998244353
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
