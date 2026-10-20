import sys


def main() -> None:
    # Two values on separate lines, no test-case count.
    length, breadth = map(int, sys.stdin.buffer.read().split()[:2])
    area = length * breadth
    peri = 2 * (length + breadth)
    if area > peri:
        print("Area"); print(area)
    elif peri > area:
        print("Peri"); print(peri)
    else:
        print("Eq"); print(area)


main()
