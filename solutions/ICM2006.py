"""CodeChef ICM2006 — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        s = next(it)
        state = 0
        for c in s:
            state = ((state+1)%5 if state else 0) if c == 48 else 1
        out.append('YES' if state == 4 else 'NO')
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
