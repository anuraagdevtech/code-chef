# 1702 &middot; Mystical Numbers

> CodeChef problem code [`XORGAND`](https://www.codechef.com/problems/XORGAND) &middot; time limit **1.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | The comparison reduces to equal bit lengths |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Simple Algos`, `Bitwise Operation`, `Prefix Sum` |
| **CodeChef category** | easy |
| **Time** | $O(N + Q)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/prefix-sums/XORGAND.md](../docs/prefix-sums/XORGAND.md)

## Question

A number $M$ is said to be a *Mystical Number* with respect to a number $X$ if $(M \oplus X) \gt (M \& X)$.

You are given an array $A$ of size $N$. You are also given $Q$ queries. Each query consists of three integers $L$, $R$, and $X$.

For each query, find the count of *Mystical Numbers* in the subarray $A[L:R]$ with respect to the number $X$.

**Notes:**
- $\oplus$ represents the [Bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation and $\&$ represents the [Bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operation.
- $A[L:R]$ denotes the subarray $A[L], A[L+1], \ldots, A[R]$.

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.
- The third line of each test case contains an integer $Q$ - denoting the number of queries.
- The $i^{th}$ of the next $Q$ lines contains three space-separated integers $L$ , $R$ and $X$.

**Output**

For each testcase,
- For each query, print in a new line, the count of *Mystical Numbers* among $A[L], A[L+1], \ldots, A[R]$ with respect to the number $X$.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 2 \cdot 10^5$
- $0 \leq A_i \lt 2^{31}$
- $1 \leq Q \leq 2 \cdot 10^5$
- $1 \leq L \leq R \leq N$
- $0 \leq X \lt 2^{31}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.
- Sum of $Q$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
1
5
1 2 3 4 5
2
1 5 4
2 5 2
```

**Sample output**

```
3
2
```

<details><summary>Explanation</summary>

**Test case $1$**:
- Query $1$: $L = 1 , R = 5 , X = 4$.
    - $A_1 \oplus X = 5, A_1 \& X = 0$.
    - $A_2 \oplus X = 6, A_2 \& X = 0$.
    - $A_3 \oplus X = 7, A_3 \& X = 0$.
    - $A_4 \oplus X = 0, A_4 \& X = 4$.
    - $A_5 \oplus X = 1, A_5 \& X = 4$.

Mystical numbers are $A_1 , A_2,$ and $A_3$ with respect to $4$. Therefore, the answer to this query is $3$.
- Query $2$: $L = 2 , R = 5 , X = 2$.
    - $A_2 \oplus X = 0, A_2 \& X = 2$.
    - $A_3 \oplus X = 1, A_3 \& X = 2$.
    - $A_4 \oplus X = 6, A_4 \& X = 0$.
    - $A_5 \oplus X = 7, A_5 \& X = 0$.

Mystical numbers are $A_4$ and $A_5$ with respect to $2$. Therefore , the answer to this query is $2$.

</details>

## Approach

Compare $M \oplus X$ with $M \mathbin{\&} X$ at the **highest bit either number has**, position $h = \mathrm{bitlen}(M \mathbin{|} X) - 1$. At any bit, the two results differ only in two situations: when exactly one of $M, X$ has the bit (XOR gets $1$, AND gets $0$) and when both have it (XOR gets $0$, AND gets $1$). Above $h$ both are zero, so bit $h$ decides everything:

- both $M$ and $X$ carry bit $h$: the AND wins, so $M$ is **not** mystical;
- exactly one carries it: the XOR wins, so $M$ **is** mystical.

Both carry the top bit of $M \mathbin{|} X$ exactly when $M$ and $X$ have the **same bit length** (and are non-zero). So the whole condition is

$$M \text{ is mystical} \iff \mathrm{bitlen}(M) \neq \mathrm{bitlen}(X)$$

with $M = X = 0$ correctly excluded, since then both sides are $0$ and the inequality is strict.

So each query is a counting problem over at most $32$ classes: precompute, for each bit length, a prefix count over the array, and answer with

$$(R - L + 1) \;-\; \#\{\,i \in [L,R] : \mathrm{bitlen}(A_i) = \mathrm{bitlen}(X)\,\}$$

in $O(1)$. That turns what looks like a per-element bitwise test into one subtraction — essential with $\sum N$ and $\sum Q$ both at $2 \times 10^5$.

With $A = [1,2,3,4,5]$ the bit lengths are $1,2,2,3,3$. The query $(1,5,4)$ has $\mathrm{bitlen}(4) = 3$, so the two matching elements are excluded and the answer is $5 - 2 = 3$. The query $(2,5,2)$ has $\mathrm{bitlen}(2) = 2$, excluding $2$ and $3$, giving $4 - 2 = 2$.

## Solution (Python)

```python
import sys

WIDTH = 32


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # Prefix counts per bit length: that is all the comparison depends on.
        pre = [[0] * (n + 1) for _ in range(WIDTH + 1)]
        for i in range(n):
            width = int(data[pos + 1 + i]).bit_length()
            for k in range(WIDTH + 1):
                pre[k][i + 1] = pre[k][i] + (k == width)
        pos += 1 + n
        q = int(data[pos])
        pos += 1
        for _ in range(q):
            l, r, x = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
            pos += 3
            same = pre[int(x).bit_length()]
            out.append(str((r - l + 1) - (same[r] - same[l - 1])))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N + Q)$ per test case
- **Space:** $O(N)$
