import sys

SPECIAL = set("@#%&?")


def secure(s: str) -> bool:
    if len(s) < 10:
        return False
    inside = s[1:-1]        # the first and last characters do not count
    return (any(c.islower() for c in s)
            and any(c.isupper() for c in inside)
            and any(c.isdigit() for c in inside)
            and any(c in SPECIAL for c in inside))


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = ["YES" if secure(data[1 + i].decode()) else "NO" for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
