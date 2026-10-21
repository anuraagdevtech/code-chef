import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    sizes = [int(data[1 + i]) for i in range(t)]
    limit = max(sizes) + 1
    # Smallest prime factor, then Omega(i) = Omega(i / spf) + 1.
    spf = list(range(limit))
    i = 2
    while i * i < limit:
        if spf[i] == i:
            for j in range(i * i, limit, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    omega = [0] * limit
    for v in range(2, limit):
        omega[v] = omega[v // spf[v]] + 1
    out = []
    for n in sizes:
        # x | y with x != y forces Omega(y) > Omega(x), so colours differ.
        out.append(str(omega[n and 1 << (n.bit_length() - 1)] + 1))
        out.append(" ".join(str(omega[v] + 1) for v in range(1, n + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
