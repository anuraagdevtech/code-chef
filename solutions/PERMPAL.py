import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for word in data[1:1 + t]:
        n = len(word)
        spots = defaultdict(list)
        for i, c in enumerate(word):
            spots[c].append(i)
        if sum(len(v) % 2 for v in spots.values()) > 1:
            out.append("-1")
            continue
        perm = [0] * n
        left, right = 0, n - 1
        middle = -1
        for idxs in spots.values():
            for k in range(0, len(idxs) - 1, 2):
                # The two slots receive the same letter, keeping it a palindrome.
                perm[left] = idxs[k] + 1
                perm[right] = idxs[k + 1] + 1
                left += 1
                right -= 1
            if len(idxs) % 2:
                middle = idxs[-1]
        if middle >= 0:
            perm[left] = middle + 1
        out.append(" ".join(map(str, perm)))
    sys.stdout.write("\n".join(out) + "\n")


main()
