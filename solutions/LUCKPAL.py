import sys

LUCKY = b"lucky"
YKCUL = b"ykcul"


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for s in data[1:1 + t]:
        n = len(s)
        half = n // 2
        # Cost of keeping each mirror pair as it is.
        mism = [0] * (half + 1)
        for i in range(half):
            mism[i + 1] = mism[i] + (s[i] != s[n - 1 - i])
        total_pairs = mism[half]

        best_cost = None
        winners = []
        for p in range(n - 4):
            q = n - 5 - p
            if abs(p - q) < 4:        # the two forced blocks would clash
                continue
            cost = sum(s[p + k] != LUCKY[k] for k in range(5))
            cost += sum(s[q + k] != YKCUL[k] for k in range(5))
            if abs(p - q) == 4:       # one position is forced by both blocks
                shared = max(p, q)
                cost -= s[shared] != LUCKY[shared - p]
            lo = min(p, q)
            top = min(lo + 4, half - 1)
            cost += total_pairs - (mism[top + 1] - mism[lo] if top >= lo else 0)
            if best_cost is None or cost < best_cost:
                best_cost, winners = cost, [p]
            elif cost == best_cost:
                winners.append(p)

        if best_cost is None:
            out.append("unlucky")
            continue
        answer = None
        for p in winners:
            q = n - 5 - p
            r = [None] * n
            for k in range(5):
                r[p + k] = LUCKY[k]
                r[q + k] = YKCUL[k]
            for i in range(half):
                if r[i] is None:
                    # Equal pair costs nothing; otherwise take the smaller letter.
                    r[i] = r[n - 1 - i] = min(s[i], s[n - 1 - i])
            if n % 2 and r[half] is None:
                r[half] = s[half]
            word = bytes(r).decode()
            if answer is None or word < answer:
                answer = word
        out.append(f"{answer} {best_cost}")
    sys.stdout.write("\n".join(out) + "\n")


main()
