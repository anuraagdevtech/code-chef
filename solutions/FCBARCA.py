import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,k = int(next(tokens)),int(next(tokens))
        mod = 1000000007
        numerator = (pow(k,n,mod)+(k if n%2 == 0 else -k))%mod
        out.append(str(numerator*pow(k+1,mod-2,mod)%mod))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
