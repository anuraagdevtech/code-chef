import sys

MAX_QUESTIONS = 10          # a constant from the statement, not an input


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    pos = 3
    eligible = 0
    for _ in range(n):
        row = data[pos:pos + k + 1]       # k watch times, then the question count
        pos += k + 1
        watched = sum(int(v) for v in row[:k])
        questions = int(row[k])
        if watched >= m and questions <= MAX_QUESTIONS:
            eligible += 1
    print(eligible)


main()
