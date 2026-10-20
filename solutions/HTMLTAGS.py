import sys


def valid(s: str) -> bool:
    # "</" + at least one body character + ">" needs four characters.
    if len(s) < 4 or not s.startswith("</") or not s.endswith(">"):
        return False
    body = s[2:-1]
    # isalnum() would also accept uppercase and non-ASCII letters.
    return all(c.islower() or c.isdigit() for c in body)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = ["Success" if valid(data[1 + i].decode()) else "Error" for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
