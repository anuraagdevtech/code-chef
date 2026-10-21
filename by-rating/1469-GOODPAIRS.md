# 1469 &middot; Good Pairs

> CodeChef problem code [`GOODPAIRS`](https://www.codechef.com/problems/GOODPAIRS) &middot; time limit **1.5s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | One-pass tally of mirrored keys |
| **CodeChef category** | main |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/sets/GOODPAIRS.md](../docs/sets/GOODPAIRS.md)

## Question

You are given arrays $A$ and $B$ of length $N$ each. Determine the number of *good* pairs.

A pair $(i,j)$ $(1\le i,j \le N)$ is said to be *good* if **all** of the following conditions are satisfied:
- $i \lt j;$
- $A_i = B_j;$
- $A_j = B_i;$

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.

Description of each test case:
- First line contains an integer $N$ - denoting the length of the arrays.
- Second line contains $N$ space-separated integers $A_1, A_2, \dots A_N$ - denoting the array $A$.
- Third line contains $N$ space-separated integers $B_1, B_2, \dots B_N$ - denoting the array $B$.

**Output**

For each test case, output the number of *good* pairs.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
4
3
1 2 3
3 2 1
4
1 2 3 4
5 6 6 7
3
10 10 10
10 10 10
4
4 8 1 1
8 4 1 1
```

**Sample output**

```
1
0
3
2
```

<details><summary>Explanation</summary>

**Test Case $1$:** The only *good* pair $(i,j)$ is $(1,3)$. Here,
- $1 \lt 3$
- $A_1 = 1$ and $B_3 = 1$. Thus, $A_1 = B_3$.
- $A_3 = 3$ and $B_1 = 3$. Thus, $A_3 = B_1$.

**Test Case $2$:** There are no *good* pairs.

**Test Case $3$:** There are $3$ good pairs $(i,j)$. These are $(1,2), (1,3),$ and $(2,3)$.

**Test Case $4$:** There are $2$ good pairs $(i,j)$. These are $(1,2)$ and $(3,4)$.

</details>

## Approach

The two equalities $A_i = B_j$ and $A_j = B_i$ say exactly that the ordered pair at $i$ is the **reverse** of the ordered pair at $j$:

$$(A_i, B_i) = (B_j, A_j)$$

So index $i$ carries a key $(A_i, B_i)$ and asks for partners whose key is its mirror image. That reduces the problem to counting mirrored key collisions, with no need to compare values pairwise.

Sweeping $j$ left to right and keeping a tally of the keys seen so far handles the $i < j$ requirement for free: when $j$ arrives, look up $(B_j, A_j)$ in the tally and add its count, then insert $j$'s own key. Every good pair is counted exactly once, at its larger index.

$$\text{answer} = \sum_{j} \#\{\,i < j : (A_i, B_i) = (B_j, A_j)\,\}$$

The self-mirrored case is worth noting: when $A_i = B_i$ the key is its own mirror, so such indices pair with each other. Sample 3, with $A = B = [10,10,10]$, is entirely of this kind and yields $\binom{3}{2} = 3$ — the sweep produces $0 + 1 + 2$, which is the same thing.

Sample 4, $A = [4,8,1,1]$ and $B = [8,4,1,1]$, mixes both kinds: the pair $(1,2)$ is a genuine mirror $(4,8) \leftrightarrow (8,4)$, and the pair $(3,4)$ is self-mirrored, giving $2$. Sample 2 has no collisions at all.

Values reach $10^9$, so the keys must be hashed rather than used as array indices — a `Counter` over tuples is the natural fit, and $\sum N \leq 2 \times 10^5$ keeps it cheap.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = data[pos + 1:pos + 1 + n]
        b = data[pos + 1 + n:pos + 1 + 2 * n]
        pos += 1 + 2 * n
        seen = Counter()
        total = 0
        for x, y in zip(a, b):
            # Look for earlier indices whose key is this one reversed.
            total += seen[(y, x)]
            seen[(x, y)] += 1
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
