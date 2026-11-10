"""CodeChef LUNCHTIM — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        answer = [0]*n
        for indices in (range(n), range(n-1,-1,-1)):
            stack = []
            for i in indices:
                h = a[i]
                while stack and stack[-1][0] < h:
                    stack.pop()
                if stack and stack[-1][0] == h:
                    answer[i] += stack[-1][1]
                    stack[-1] = (h, stack[-1][1]+1)
                else:
                    stack.append((h, 1))
        out.append(' '.join(map(str, answer)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
