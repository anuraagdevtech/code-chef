import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        grid = [next(tokens) for _ in range(8)]
        seen = set()
        components = []
        for r in range(8):
            for c in range(8):
                if grid[r][c] != 49 or (r,c) in seen:
                    continue
                flags = [False]*4
                seen.add((r,c))
                stack = [(r,c)]
                while stack:
                    rr,cc = stack.pop()
                    flags[0] |= cc == 0
                    flags[1] |= cc == 7
                    flags[2] |= rr == 0
                    flags[3] |= rr == 7
                    for x,y in ((rr-1,cc),(rr+1,cc),(rr,cc-1),(rr,cc+1)):
                        if 0 <= x < 8 and 0 <= y < 8 and grid[x][y] == 49 and (x,y) not in seen:
                            seen.add((x,y))
                            stack.append((x,y))
                components.append(flags)
        if n == 3:
            answer = len(components)
        else:
            half = pow(2,n-4,21945)
            m = 2*half
            answer = sum((m-half*right-(half-1)*left)*(m-half*bottom-(half-1)*top)
                         for left,right,top,bottom in components)%21945
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
