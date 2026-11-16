import sys


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    rows,cols,n = next(tokens),next(tokens),next(tokens)
    cells = {(next(tokens),next(tokens)) for _ in range(n)}
    visited = set()
    answer = 0
    for start in cells:
        if start in visited:
            continue
        visited.add(start)
        stack = [start]
        perimeter = 0
        while stack:
            r,c = stack.pop()
            for v in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if v not in cells:
                    perimeter += 1
                elif v not in visited:
                    visited.add(v)
                    stack.append(v)
        answer = max(answer,perimeter)
    print(answer)

if __name__ == '__main__':
    main()
