import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        heights = [int(next(tokens)) for _ in range(n)]
        answer = [0]*n
        stack = []
        for i, h in enumerate(heights):
            while stack and stack[-1][0] < h:
                _, group = stack.pop()
                count = len(group)-1
                for index in group:
                    answer[index] = count
            if stack and stack[-1][0] == h:
                stack[-1][1].append(i)
            else:
                stack.append((h, [i]))
        for _, group in stack:
            count = len(group)-1
            for i in group:
                answer[i] = count
        out.append(' '.join(map(str, answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
