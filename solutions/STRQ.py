import sys
from array import array


def main() -> None:
    read = sys.stdin.buffer.readline
    text = read().strip()
    q = int(read())
    by_pair = {}
    for i in range(q):
        a, b, l, r = read().split()
        by_pair.setdefault((a[0], b[0]), array('I')).extend((i, int(l) - 1, int(r)))
    chars = sorted(set(text))
    counts = {c: array('I', [0]) for c in chars}
    for ch in text:
        for c in chars:
            counts[c].append(counts[c][-1] + (c == ch))
    answers = array('Q', [0]) * q
    for (a, b), group in by_pair.items():
        if a not in counts or b not in counts:
            continue
        prefix = array('Q', [0])
        count_a = counts[a]
        count_b = counts[b]
        total = 0
        for i, ch in enumerate(text):
            if ch == b:
                total += count_a[i]
            prefix.append(total)
        for j in range(0, len(group), 3):
            i, l, r = group[j:j + 3]
            answers[i] = prefix[r] - prefix[l] - count_a[l] * (count_b[r] - count_b[l])
    for start in range(0, q, 8192):
        sys.stdout.write('\n'.join(map(str, answers[start:start + 8192])) + '\n')


if __name__ == "__main__":
    main()
