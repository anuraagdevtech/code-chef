import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1]
        pos += 2
        # Keep the two longest runs per letter; nothing else can matter.
        best1 = [0] * 26
        best2 = [0] * 26
        run_ch, run_len = -1, 0
        for ch in s + b"\x00":
            if ch == run_ch:
                run_len += 1
                continue
            if run_ch != -1:
                c = run_ch - 97
                if run_len > best1[c]:
                    best1[c], best2[c] = run_len, best1[c]
                elif run_len > best2[c]:
                    best2[c] = run_len
            run_ch, run_len = ch, 1
        # Twice inside the longest run, or once in each of the top two.
        out.append(str(max(max(b1 - 1, b2) for b1, b2 in zip(best1, best2))))
    sys.stdout.write("\n".join(out) + "\n")


main()
