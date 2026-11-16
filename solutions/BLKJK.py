import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,x,y = (int(next(tokens)) for _ in range(3))
        a = [int(next(tokens)) for _ in range(n)]
        total = 0
        already = False
        for value in a:
            total += value
            if x <= total <= y:
                already = True
        if already:
            out.append('0')
            continue
        mask = (1 << (y+1))-1
        history = [1]
        for value in a:
            history.append(history[-1]|((history[-1] << value)&mask))
        valid = history[-1]&(((1 << (y+1))-1)^((1 << x)-1))
        if not valid:
            out.append('-1')
            continue
        target = (valid&-valid).bit_length()-1
        selected = []
        for i in range(n-1,-1,-1):
            if not (history[i] >> target)&1:
                selected.append(i)
                target -= a[i]
        best = sum(i >= len(selected) for i in selected)
        if best <= 1:
            out.append(str(best))
            continue
        qmax = best-1
        count_limit = min(n,y)
        prefix = [[0]*(qmax+1) for _ in range(n+1)]
        prefix[0] = [1]*(qmax+1)
        reachable = [0]*(count_limit+1)
        reachable[0] = 1
        for length,value in enumerate(a,1):
            row = prefix[length]
            if value <= y:
                for count in range(min(length,count_limit),0,-1):
                    shifted = (reachable[count-1] << value)&mask
                    added = shifted&~reachable[count]
                    reachable[count] |= shifted
                    exclusions = length-count
                    if exclusions <= qmax:
                        row[exclusions] |= added
            previous = prefix[length-1]
            cumulative = 0
            for q in range(qmax+1):
                cumulative |= row[q]|previous[q]
                row[q] = cumulative
        suffix = [0]*(qmax+1)
        suffix[0] = 1
        for i in range(n-1,-1,-1):
            value = a[i]
            if value > y:
                continue
            for count in range(min(qmax,n-i,best-1),0,-1):
                shifted = (suffix[count-1] << value)&mask
                added = shifted&~suffix[count]
                suffix[count] |= shifted
                options = prefix[i][count]
                if not options:
                    continue
                while added:
                    bit = added&-added
                    s = bit.bit_length()-1
                    low,high = max(0,x-s),y-s
                    if high >= low and options&(((1 << (high+1))-1)^((1 << low)-1)):
                        best = count
                        break
                    added -= bit
            if best == 1:
                break
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
