import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, hours = int(next(tokens)), int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        lo, hi = 1, max(a)
        while lo < hi:
            mid = (lo+hi)//2
            if sum((v+mid-1)//mid for v in a) <= hours:
                hi = mid
            else:
                lo = mid+1
        out.append(str(lo))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
