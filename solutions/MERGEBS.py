import sys


def solve(tokens):
    n = int(next(tokens))
    first = next(tokens)
    second = next(tokens)
    second_ones = [0]
    for char in second:
        second_ones.append(second_ones[-1] + (char == 49))
    cost = [0] * (n + 1)
    for j in range(1, n + 1):
        cost[j] = cost[j - 1] + (second_ones[j - 1] if second[j - 1] == 48 else 0)
    first_ones = 0
    for char_a in first:
        first_ones += char_a == 49
        cost[0] += first_ones if char_a == 48 else 0
        for j, char_b in enumerate(second, 1):
            cost[j] = min(cost[j] + (first_ones + second_ones[j] if char_a == 48 else 0), cost[j - 1] + (first_ones + second_ones[j - 1] if char_b == 48 else 0))
    return str(cost[n])


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
