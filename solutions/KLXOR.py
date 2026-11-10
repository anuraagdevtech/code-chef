"""CodeChef KLXOR — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n, k = int(next(it)), int(next(it))
        s = next(it)
        width = n-k+1
        parity = sum(s[:width]) % 2
        answer = parity
        for i in range(1,k):
            parity ^= (s[i-1]-48) ^ (s[i+width-1]-48)
            answer += parity
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
