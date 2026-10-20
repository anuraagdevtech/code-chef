import sys


def floor_of(room: int) -> int:
    # Rooms are numbered from 1, so shift to zero-based before dividing.
    return (room - 1) // 10 + 1


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        out.append(str(abs(floor_of(x) - floor_of(y))))
    sys.stdout.write("\n".join(out) + "\n")


main()
