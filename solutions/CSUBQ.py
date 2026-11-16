import sys
from array import array


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, q, low, high = (next(tokens) for _ in range(4))
    size = 1
    while size < n:
        size *= 2
    length = array('I', [0]) * (2 * size)
    for i in range(size, size + n):
        length[i] = 1
    for i in range(size - 1, 0, -1):
        length[i] = length[i * 2] + length[i * 2 + 1]
    prefix_good = [array('I', length), array('I', length)]
    suffix_good = [array('I', length), array('I', length)]
    count = [array('Q', [0]) * (2 * size), array('Q', [0]) * (2 * size)]
    for z in range(2):
        for i in range(1, 2 * size):
            count[z][i] = length[i] * (length[i] + 1) // 2
    out = []
    for _ in range(q):
        kind, x, y = (next(tokens), next(tokens), next(tokens))
        if kind == 1:
            leaf = size + x - 1
            for z, bound in enumerate((high, low - 1)):
                good = int(y <= bound)
                prefix_good[z][leaf] = suffix_good[z][leaf] = count[z][leaf] = good
                i = leaf // 2
                pre_z, suf_z, cnt_z = (prefix_good[z], suffix_good[z], count[z])
                while i:
                    a, b = (i * 2, i * 2 + 1)
                    pre_z[i] = pre_z[a] + (pre_z[b] if pre_z[a] == length[a] else 0)
                    suf_z[i] = suf_z[b] + (suf_z[a] if suf_z[b] == length[b] else 0)
                    cnt_z[i] = cnt_z[a] + cnt_z[b] + suf_z[a] * pre_z[b]
                    i //= 2
        else:
            results = []
            for z in range(2):
                l, r = (size + x - 1, size + y)
                ll = lp = ls = lc = 0
                rl = rp = rs = rc = 0
                pre_z, suf_z, cnt_z = (prefix_good[z], suffix_good[z], count[z])
                while l < r:
                    if l & 1:
                        lc += cnt_z[l] + ls * pre_z[l]
                        lp += pre_z[l] if lp == ll else 0
                        ls = suf_z[l] + (ls if suf_z[l] == length[l] else 0)
                        ll += length[l]
                        l += 1
                    if r & 1:
                        r -= 1
                        rc = cnt_z[r] + rc + suf_z[r] * rp
                        rs += suf_z[r] if rs == rl else 0
                        rp = pre_z[r] + (rp if pre_z[r] == length[r] else 0)
                        rl += length[r]
                    l //= 2
                    r //= 2
                results.append(lc + rc + ls * rp)
            out.append(str(results[0] - results[1]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
