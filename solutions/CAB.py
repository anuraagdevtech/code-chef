import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, k = int(next(tokens)), int(next(tokens))
        counts = [0] * 26
        counts[25], rest = divmod(k, 1 << 25)
        for b in range(25):
            counts[b] = (rest >> b) & 1
        size = sum(counts)
        if size > n or n > k:
            out.append('-1')
            continue
        for b in range(25, 0, -1):
            split = min(counts[b], n-size)
            counts[b] -= split
            counts[b-1] += 2*split
            size += split
        out.append(''.join(chr(97+b)*counts[b] for b in range(25,-1,-1)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
