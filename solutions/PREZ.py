import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, budget = int(next(tokens)), int(next(tokens))
        s = next(tokens)
        cost = previous = answer = 0
        for i, digit in enumerate(s):
            required = (48-digit)%10
            if i == 0:
                cost = required
            else:
                cost += required-previous+(previous-required)%10
            previous = required
            if cost <= budget:
                answer = i+1
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
