import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])       # no test-case count
    special = set(data[2:2 + n])
    pos = 2 + n
    posts = []
    for _ in range(m):
        friend, popularity, text = data[pos], int(data[pos + 1]), data[pos + 2]
        pos += 3
        # Special first, then popularity descending.
        posts.append((friend not in special, -popularity, text))
    posts.sort()
    sys.stdout.write("\n".join(p[2].decode() for p in posts) + "\n")


main()
