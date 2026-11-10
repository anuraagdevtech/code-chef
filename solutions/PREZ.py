"""CodeChef PREZ — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, k = int(next(it)), int(next(it))
        s = next(it)
        answer = 0
        cost = (48-s[0]) % 10
        for i in range(n):
            if i:
                cost += (s[i]-s[i-1]) % 10 + (48-s[i]) % 10 - (48-s[i-1]) % 10
            if cost <= k:
                answer = i+1
            else:
                break
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
