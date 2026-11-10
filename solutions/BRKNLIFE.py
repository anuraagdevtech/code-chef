"""CodeChef BRKNLIFE — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, m = int(next(it)), int(next(it))
        s, a = next(it), next(it)
        j = 0
        result = bytearray(s)
        for i, c in enumerate(s):
            if c == 63:
                result[i] = 97 if j == m or a[j] != 97 else 98
            elif j < m and c == a[j]:
                j += 1
        out.append('-1' if j == m else result.decode())
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
