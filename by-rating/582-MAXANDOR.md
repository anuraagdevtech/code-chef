[&larr; 581. Queries About Numbers](581-QNUMBER.md) &middot; [Index](README.md) &middot; [583. No sequence &rarr;](583-NOSEQ.md)

# 582. Maximum And Or

> [`MAXANDOR`](https://www.codechef.com/problems/MAXANDOR) &middot; difficulty **2028** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Independent bits - free exactly where A and B differ |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Bitwise Operation` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has been recently introduced to bitwise operations.

Chefina defines a function $F(P,Q,R) = (R$ $|$ $P) - (Q$ $\&$ $P)$
where $|$ represents the [bitwise or](https://en.wikipedia.org/wiki/Bitwise_operation#OR) and $\&$ represents the [bitwise and](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operator.

Chef has three non-negative integers $A,B,$ and $C$.
Chef has to count the number of integers $X$, such that:
- $0 \leq X \lt 2^C;$
- $F(X,A,B)$ has the **maximum** possible value among all values of $X$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing three space-separated integers $A,B,C-$ as defined in the statement.

**Output**

For each test case, output on a new line, the count of $X$ such that $F(X,A,B)$ is maximum possible.

## Constraints

- $1 \leq T \leq 2 \cdot 10^5$
- $0 \leq C \leq 30$
- $0 \leq A,B < 2^{C}$

## Sample

**Sample input**

```
3
1 2 3
0 0 2
87 986 15
```

**Sample output**

```
4
1
64
```

<details><summary>Explanation</summary>

**Test case $1$:** There are $4$ possible values of $X$ which give maximum value for $F(X, A, B)$. These values are $4,5,6,7$.
For all these values, $F(X,A,B)$ is $5$.

**Test case $2$:** The only possible value of $X$ which gives maximum value for $F(X, A, B)$ is $3$.
For $X = 3$:
- $0\le X \lt 2^2$
- $F(3, 0, 0) = (0$ $|$ $3) - (0$ $\&$ $3) = 3$

It can be shown that $F(X, 0, 0)$ cannot have a value greater than $3$ for $0\le X \lt 2^2$.

</details>

## Approach

$F(X) = (B \mid X) - (A \mathbin{\&} X)$. Since $A \mathbin{\&} X$ is a submask of $X$, which is a submask of $B \mid X$, the subtraction never borrows and each bit position contributes independently: bit of $(B \mid X)$ minus bit of $(A \mathbin{\&} X)$.

| $a$ | $b$ | $x = 0$ | $x = 1$ |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |

Where the bits of $A$ and $B$ are equal exactly one choice of $x$ is optimal; where they differ both choices give the same contribution. The number of maximising $X$ is therefore $2^{\text{popcount}(A \oplus B)}$.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        a = next(tokens)
        b = next(tokens)
        c = next(tokens)
        out.append(str(1 << (a ^ b).bit_count()))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $C = 0$: only $X = 0$ exists and the answer is 1.
- Bits of $X$ above those of $A$ and $B$ are positions where both are 0, so $x = 1$ is forced there.
- $A = B$ gives exactly one optimal $X$, the complement of $A$ within $C$ bits.
- $C$ itself does not appear in the formula because $A, B < 2^C$.

## Dry run

`A = 1, B = 2, C = 3`: $A \oplus B = 3$ has two set bits, so the answer is $2^2 = 4$.

Bit 2 is 0 in both numbers, forcing $x = 1$; bits 0 and 1 are free. The optimal values are $X = 4, 5, 6, 7$.

---

Same problem grouped by topic: [../docs/bit-manipulation/MAXANDOR.md](../docs/bit-manipulation/MAXANDOR.md)
