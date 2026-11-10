"""CodeChef F3 — standalone Python 3 solution."""
import sys



def solve():
    it = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(it))):
        n = int(next(it))
        grid = [next(it) for _ in range(8)]
        seen = set()
        answer = 0
        for r in range(8):
            for c in range(8):
                if grid[r][c] != 49 or (r,c) in seen:
                    continue
                seen.add((r,c))
                stack = [(r,c)]
                top = bottom = left = right = False
                while stack:
                    rr,cc = stack.pop()
                    top |= rr == 0
                    bottom |= rr == 7
                    left |= cc == 0
                    right |= cc == 7
                    for u,v in ((rr-1,cc),(rr+1,cc),(rr,cc-1),(rr,cc+1)):
                        if 0 <= u < 8 and 0 <= v < 8 and grid[u][v] == 49 and (u,v) not in seen:
                            seen.add((u,v))
                            stack.append((u,v))
                if n == 3:
                    answer += 1
                else:
                    half = pow(2,n-4,21945)
                    def factor(first,last):
                        if first and last:
                            return 1
                        if not first and not last:
                            return 2*half
                        return half+int(first)
                    answer += factor(top,bottom)*factor(left,right)
        out.append(str(answer % 21945))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
