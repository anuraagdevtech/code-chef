import sys
import heapq


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        required = [next(tokens) for _ in range(n)]
        last = {want: i for i, want in enumerate(required) if want >= 0}
        available = [want for want in range(n + 1) if want not in last]
        heapq.heapify(available)
        seen = bytearray(n + 2)
        mex = 0
        result = []
        ok = True
        for i, want in enumerate(required):
            value = heapq.heappop(available)
            result.append(value)
            seen[value] = 1
            while seen[mex]:
                mex += 1
            if want >= 0 and want != mex:
                ok = False
            if want >= 0 and last[want] == i:
                heapq.heappush(available, want)
        out.append(' '.join(map(str, result)) if ok else '-1')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
