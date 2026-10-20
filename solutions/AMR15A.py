import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    # "Lucky" means an even weapon count; a strict majority wins.
    evens = sum(1 for v in data[1:1 + n] if int(v) % 2 == 0)
    print("READY FOR BATTLE" if 2 * evens > n else "NOT READY")


main()
