"""CodeChef TINOI17A — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    rows, cols, n = int(next(it)), int(next(it)), int(next(it))
    cells = {(int(next(it)),int(next(it))) for _ in range(n)}
    unseen = cells.copy()
    answer = 0
    while unseen:
        stack = [unseen.pop()]
        perimeter = 0
        while stack:
            r,c = stack.pop()
            for u in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if u not in cells:
                    perimeter += 1
                elif u in unseen:
                    unseen.remove(u)
                    stack.append(u)
        answer = max(answer,perimeter)
    out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
