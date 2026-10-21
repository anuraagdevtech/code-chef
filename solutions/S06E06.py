import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        digits = [c - 48 for c in data[1 + 2 * i]]
        k = int(data[2 + 2 * i])
        heapq.heapify(digits)
        # At most 7 digits x 9 steps, so a huge K just saturates everything.
        while k and digits[0] < 9:
            heapq.heapreplace(digits, digits[0] + 1)
            k -= 1
        product = 1
        for d in digits:
            product *= d
        out.append(str(product))
    sys.stdout.write("\n".join(out) + "\n")


main()
