"""CodeChef PREFIXFLIP — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, k = int(next(it)), int(next(it))
        s = next(it)
        changes = sum(s[i] != s[i-1] for i in range(1, k))
        answer = changes + (s[k-1] == 48)
        for r in range(k, n):
            changes += (s[r] != s[r-1]) - (s[r-k+1] != s[r-k])
            answer = min(answer, changes + (s[r] == 48))
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
