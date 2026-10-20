import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = map(int, data[1 + 3 * i:4 + 3 * i])
        # Each inequality is decided at the top bit where its pair differs.
        p = (a ^ b).bit_length() - 1
        q = (b ^ c).bit_length() - 1
        if p == q:
            # One bit, two incompatible demands.
            out.append("-1")
        else:
            x = (a & (1 << p)) | (b & (1 << q))
            out.append(str(x))
    sys.stdout.write("\n".join(out) + "\n")


main()
