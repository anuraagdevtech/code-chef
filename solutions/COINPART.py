import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = [next(tokens) for _ in range(n)]
        big = max(range(n), key=values.__getitem__)
        others = [i for i in range(n) if i != big]
        history = [1]
        for i in others:
            history.append(history[-1] | history[-1] << values[i])
        target = sum((values[i] for i in others)) // 2
        while not history[-1] >> target & 1:
            target -= 1
        low = []
        high = []
        for j in range(len(others) - 1, -1, -1):
            i = others[j]
            if history[j] >> target & 1:
                high.append(i)
            else:
                low.append(i)
                target -= values[i]
        low.insert(0, big)
        chefu = chefa = 0
        order = []
        while low or high:
            if chefu <= chefa:
                i = low.pop()
                chefu += values[i]
            else:
                i = high.pop()
                chefa += values[i]
            order.append(str(i + 1))
        out.append(' '.join(order))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
