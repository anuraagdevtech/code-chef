import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])                 # no test-case count
    # Pairs are compared on the first component only.
    keys = [data[1 + 2 * i] for i in range(n)]
    seen = set()
    valid = []
    for i, key in enumerate(keys):
        # Only the earliest occurrence of a key can be pivoted on without
        # pulling it ahead of equal elements that came before it.
        if key not in seen:
            seen.add(key)
            valid.append(i)
    sys.stdout.write(f"{len(valid)}\n" + " ".join(map(str, valid)) + "\n")


main()
