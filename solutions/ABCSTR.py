import sys


def main():
    text = sys.stdin.buffer.read().strip()
    x = y = total = 0
    seen = {(0, 0): 1}
    for char in text:
        if char == 65:
            x += 1
            y += 1
        elif char == 66:
            x -= 1
        else:
            y -= 1
        key = (x, y)
        total += seen.get(key, 0)
        seen[key] = seen.get(key, 0) + 1
    print(total)


if __name__ == "__main__":
    main()
