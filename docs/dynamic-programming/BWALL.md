[&larr; 503. K-Concatenation](KCON.md) &middot; [Index](../../README.md) &middot; [526. Subtree Removal &rarr;](SUBREM.md)

# 515. The Great Wall of Byteland

> CodeChef problem code [`BWALL`](https://www.codechef.com/problems/BWALL) &middot; difficulty **1796** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Profile tiling with exponentiated transfer matrices |
| **Time** | $O(\log N)$ per test case after $O(\log N_{max})$ fixed-size matrix preprocessing |
| **Space** | $O(\log N_{max})$ for fixed-size matrix powers |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

In order to protect the southern border of Bytelandian Empire against intrusions by various nomadic groups, the Emperor of Byteland has decided to build a wall along the southern border. The best architect Johny is recruited for the task.

In order to minimise the cost of raw material, Johny is restricted to use only following two kinds of building blocks:
X      #

XX

The height of the wall is fixed and is 2 units, but the length of the wall varies. As a part of his job Johny needs to find out the number of ways he can construct the wall using above two types of building blocks where the length of the wall is specified. Write a program to help Johny.

**Input Format:**

The first line contains the number of test cases T followed by T lines. Each of the next lines contains an integer N representing the length of the wall.

**Output Format:**

Print T lines one for each test case, containing an integer that represents the number of ways of constructing the wall, modulo 1000000007.

**Constraints:**
1<=T<=1000
1<=N<=10^9

## Constraints

1<=T<=1000
1<=N<=10^9

## Sample

**Sample input**

```
3
7
2
13
```

**Sample output**

```
655
5
272767
```

<details><summary>Explanation</summary>

**Explanation of 2nd Test Case**
**Given:**
`N = 2`

We want to count all possible ways to build the wall using the allowed tiles. Each configuration below represents one valid way.

---

**All 5 Possible Ways**
```
1) ####
```

```
2) X#XX
```

```
3) #XXX
```

```
4) XXX#
```

```
5) XX#X
```

</details>

## Approach

A column has two cells. Represent cells already covered from the previous column by a two-bit mask. Fill the first uncovered cell with either a one-cell block or one of the four orientations of an L-shaped three-cell block. The L block occupies cells in the current and next column. Reject overlaps and accumulate a transition to the resulting next-column mask.

This produces a $4	imes4$ transfer matrix. Starting from empty mask zero, after $N$ transitions the coefficient of empty mask zero counts exactly complete walls. Precompute binary powers of the matrix once, then multiply the initial row vector by powers selected by the bits of $N$. All arithmetic is modulo $10^9+7$.

## Solution (Python)

```python
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
```

## Complexity

- **Time:** $O(\log N)$ per test case after $O(\log N_{max})$ fixed-size matrix preprocessing
- **Space:** $O(\log N_{max})$ for fixed-size matrix powers
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Only final mask zero is a completed wall.
- All four L rotations are allowed.
- A single-column wall has just the two single-cell blocks.
- Precompute powers once across the test cases.

## Dry run

For width two, there is one arrangement using only single cells and four arrangements containing one L block with one single cell. Thus the answer is 5.

> CodeChef tags: `Mathematics`, `Matrices`, `Matrix Multiplication`, `Algorithms`, `Recursion`

---

Same problem in rating order (#516 of 735): [../../by-rating/516-BWALL.md](../../by-rating/516-BWALL.md)
