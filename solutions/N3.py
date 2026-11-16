import sys
from array import array


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, length, k = (int(next(tokens)) for _ in range(3))
        strings = [next(tokens).decode() for _ in range(n)]
        overlap = [[0] * n for _ in range(n)]
        for j in range(n):
            pattern = strings[j]
            failure = [0] * length
            for p in range(1, length):
                v = failure[p - 1]
                while v and pattern[p] != pattern[v]:
                    v = failure[v - 1]
                failure[p] = v + (pattern[p] == pattern[v])
            for i in range(n):
                matched = 0
                for ch in strings[i][1:]:
                    while matched and ch != pattern[matched]:
                        matched = failure[matched - 1]
                    if ch == pattern[matched]:
                        matched += 1
                overlap[i][j] = matched
        cost = [length] * n
        parents = []
        for _ in range(k - 1):
            next_cost = [10 ** 9] * n
            prev = array('h', [-1]) * n
            for i in range(n):
                base = cost[i] + length
                for j in range(n):
                    v = base - overlap[i][j]
                    if v < next_cost[j]:
                        next_cost[j] = v
                        prev[j] = i
            parents.append(prev)
            cost = next_cost
        last = min(range(n), key=cost.__getitem__)
        path = [last]
        for prev in reversed(parents):
            last = prev[last]
            path.append(last)
        path.reverse()
        answer = strings[path[0]]
        positions = [0]
        for i, j in zip(path, path[1:]):
            positions.append(len(answer) - overlap[i][j])
            answer += strings[j][overlap[i][j]:]
        out.extend((str(len(answer)), answer))
        out.extend((f'{i} {p}' for i, p in zip(path, positions)))
        out.append('')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
