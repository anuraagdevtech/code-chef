"""CodeChef BINTREE — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        u,v = int(next(it)),int(next(it))
        answer = 0
        while u != v:
            if u > v:
                u //= 2
            else:
                v //= 2
            answer += 1
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
