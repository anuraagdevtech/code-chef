import sys

MOD = 1_000_000_007
VOWELS = frozenset(b"aeiou")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        k = int(data[2 + 3 * i])
        s = data[3 + 3 * i]
        spots = [j for j, c in enumerate(s) if c in VOWELS]
        ways = 1
        # One cut per vowel block boundary; it may sit anywhere between them.
        for j in range(k, len(spots), k):
            ways = ways * (spots[j] - spots[j - 1]) % MOD
        out.append(str(ways))
    sys.stdout.write("\n".join(out) + "\n")


main()
