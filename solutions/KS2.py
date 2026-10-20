import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        # Exactly one last digit completes any prefix to a round number, so
        # the n-th round number is n with that digit appended.
        digit_sum = sum(ch - 48 for ch in s)
        out.append(s.decode() + str((10 - digit_sum % 10) % 10))
    sys.stdout.write("\n".join(out) + "\n")


main()
