import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    buckets = [[] for _ in range(65)]
    for tok in data[2:2 + n]:
        v = int(tok)
        buckets[v.bit_length()].append(v)
    for bucket in buckets:
        bucket.sort()
    queries = [int(x) for x in data[2 + n:2 + n + m]]

    out = []
    level = []        # ascending values of the current bit length
    done = 0          # moves consumed by longer bit lengths
    qi = 0
    for bits in range(64, 0, -1):
        # Halving preserves order, so this is a merge of two sorted runs.
        level = sorted([v >> 1 for v in level] + buckets[bits])
        size = len(level)
        if not size:
            continue
        while qi < m and queries[qi] <= done + size:
            # Within a level the divisions run descending, so count from the end.
            out.append(str(level[size - (queries[qi] - done)]))
            qi += 1
        done += size
        if qi == m:
            break
    sys.stdout.write("\n".join(out) + "\n")


main()
