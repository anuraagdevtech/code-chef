import sys

TRANSITION = []
for u in range(10):
    if u < 5:
        neighbours = ((u-1)%5,(u+1)%5,u+5)
    else:
        i = u-5
        neighbours = ((i-2)%5+5,(i+2)%5+5,i)
    TRANSITION.append({v%5:v for v in neighbours})


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        s = next(tokens)
        first = s[0]-65
        answer = '-1'
        for start in (first,first+5):
            walk = [start]
            u = start
            for c in s[1:]:
                v = TRANSITION[u].get(c-65)
                if v is None:
                    break
                walk.append(v)
                u = v
            else:
                answer = ''.join(map(str,walk))
                break
        out.append(answer)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
