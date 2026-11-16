import sys

MOD = 1000000007

def transfer():
    matrix = [[0]*4 for _ in range(4)]
    shapes = ((3,1),(3,2),(1,3),(2,3))
    def fill(start, current, following):
        if current == 3:
            matrix[start][following] += 1
            return
        cell = 1 if not current&1 else 2
        fill(start, current|cell, following)
        for here, there in shapes:
            if here&cell and not here&current and not there&following:
                fill(start,current|here,following|there)
    for mask in range(4):
        fill(mask,mask,0)
    return matrix

def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(4))%MOD for j in range(4)] for i in range(4)]

POWERS = [transfer()]
for _ in range(29):
    POWERS.append(multiply(POWERS[-1],POWERS[-1]))


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        vector = [1,0,0,0]
        bit = 0
        while n:
            if n&1:
                matrix = POWERS[bit]
                vector = [sum(vector[i]*matrix[i][j] for i in range(4)) % MOD for j in range(4)]
            n >>= 1
            bit += 1
        out.append(str(vector[0]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
