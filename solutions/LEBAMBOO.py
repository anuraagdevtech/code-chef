"""CodeChef LEBAMBOO — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        h = [int(next(it)) for _ in range(n)]
        d = [int(next(it))-x for x in h]
        if n == 1:
            answer = -d[0] if d[0] <= 0 else -1
        elif n == 2:
            answer = abs(d[0]) if sum(d) == 0 else -1
        else:
            total = sum(d)
            if total < 0 or total % (n-2):
                answer = -1
            else:
                answer = total // (n-2)
                if any(x > answer or (answer-x) % 2 for x in d):
                    answer = -1
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
