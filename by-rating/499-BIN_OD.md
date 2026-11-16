[&larr; 498. Chef and Polygon Cakes](498-PCJ18C.md) &middot; [Index](README.md) &middot; [500. Chef Restaurant  &rarr;](500-CHEFRES.md)

# 499. Binod

> [`BIN_OD`](https://www.codechef.com/problems/BIN_OD) &middot; difficulty **1776** &middot; time limit **2.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Offline queries grouped by bit with prefix counts |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Simple Algos`, `Bitwise Operation`, `Prefix Sum` |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(NB+Q)$ per test case for $B$ queried bits |
| **Space** | $O(N+Q)$ |

## Question

*A Binod is a person who is very good with bitwise operations. Help Alice solve the following problem and become a Binod.*

You are given an array $A$ of $N$ elements. Process $Q$ queries on this array, of the following form:
- Each query contains $5$ integers $k, L_1, R_1, L_2, R_2$. It is guaranteed that $L_1 \leq R_1 \lt L_2 \leq R_2$.
- The answer to a query is the number of pairs $(i, j)$ such that:
    - $L_1 \leq i \leq R_1$ and $L_2 \leq j \leq R_2$
    - $A_i \oplus A_j$ has its $k$-th bit set. Here $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

**Note:** An integer $x$ is said to have its $k$-th bit set if the (unique) binary representation of $x$ contains $2^k$. For example, $5 = 101_2 = 2^0 + 2^2$ has its zeroth and second bits set but not the first, while $16 = 10000_2 = 2^4$ has only its fourth bit set.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $Q$ — the number of elements in array and number of queries, respectively.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
    - The next $Q$ lines describe queries. The $i$-th of these $Q$ lines contains $5$ space-separated integers $k, L_1, R_1, L_2, R_2$ — the parameters described in the statement.

**Output**

For each test case, output $Q$ lines.The $i$-th of these lines should be the answer to the $i$-th query.

## Constraints

- $1 \leq T \leq 5 \cdot 10^4$
- $2 \leq N \leq 10^5$
- $1 \leq Q \leq 5\cdot 10^5$
- $0 \leq A_i \lt 2^{60}$
- $1 \leq L_1 \leq R_1 \lt L_2 \leq R_2 \leq N$.
- $0 \leq k \lt 60$
- The sum of $N$ and $Q$ over all test cases won't exceed $10^5$ and $5\cdot 10^5$ respectively.

## Sample

**Sample input**

```
2
5 2
1 2 4 3 2
1 1 3 5 5
2 1 2 3 5
6 2
3 5 6 13 12 20
1 1 4 5 6
3 2 3 4 6
```

**Sample output**

```
2
2
4
4
```

<details><summary>Explanation</summary>

**Test case $1$:** The array is $A = [1, 2, 4, 3, 2]$.
- Query $1$: the ranges are $[1, 3]$ and $[5, 5]$, and $k = 1$. There are three pairs of $(i, j)$: $(1, 5), (2, 5), (3, 5)$.
    - $A_1 \oplus A_5 = 1 \oplus 2 = 3 = 11_2$ has its first bit set
    - $A_2 \oplus A_5 = 2 \oplus 2 = 0 = 0_2$ doesn't have its first bit set
    - $A_3 \oplus A_5 = 4 \oplus 2 = 6 = 110_2$ has its first bit set
    - So, the answer is $2$.
- Query $2$: the ranges are $[1, 2]$ and $[3, 5]$, and now $k = 2$. This time, there are $6$ pairs of indices. Of them, it can be verified that $(1, 3)$ and $(2, 3)$ are the ones that satisfy the given condition.

</details>

## Approach

An XOR bit is one exactly when its two input bits differ. For a query, if the two ranges have $a,b$ set bits and lengths $u,v$, the answer is $a(v-b)+(u-a)b$.

Group queries by their requested bit. Build one prefix-count array for that bit, answer all its queries, then discard it before processing the next bit. This uses linear memory instead of retaining a prefix array for every bit.

## Solution

```python
import sys
from collections import defaultdict


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, q = int(next(tokens)), int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        groups = defaultdict(list)
        for index in range(q):
            bit, l1, r1, l2, r2 = (int(next(tokens)) for _ in range(5))
            groups[bit].append((index,l1,r1,l2,r2))
        answer = [0]*q
        for bit, queries in groups.items():
            prefix = [0]*(n+1)
            for i, value in enumerate(a):
                prefix[i+1] = prefix[i]+((value >> bit)&1)
            for index,l1,r1,l2,r2 in queries:
                ones1 = prefix[r1]-prefix[l1-1]
                ones2 = prefix[r2]-prefix[l2-1]
                answer[index] = ones1*(r2-l2+1-ones2)+(r1-l1+1-ones1)*ones2
        out.extend(map(str, answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Bits are zero-based.
- Count pairs of indices, including repeated values separately.
- Preserve original query order after grouping.

## Dry run

In the first sample query, bit 1 has one set bit among `[1,2,4]` and one among `[2]`. The count is `1*0+2*1=2`.

---

Same problem grouped by topic: [../docs/bit-manipulation/BIN_OD.md](../docs/bit-manipulation/BIN_OD.md)
