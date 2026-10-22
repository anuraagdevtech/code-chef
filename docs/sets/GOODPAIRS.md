[&larr; 337. Version Control System](VCS.md) &middot; [Index](../../README.md) &middot; [417. Fencing &rarr;](FENCE.md)

# 386. Good Pairs

> CodeChef problem code [`GOODPAIRS`](https://www.codechef.com/problems/GOODPAIRS) &middot; difficulty **1469** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | One-pass tally of mirrored keys |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

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

## Edge cases

- **A self-mirrored index** ($A_i = B_i$) pairs with every other such index, so three identical pairs give $\binom{3}{2} = 3$ — the third row. The tally handles it because the counter already holds the earlier matches when the current index is examined.
- **The count must happen before the insert**, which is what enforces $i < j$ and stops an index pairing with itself. Inserting first would add a spurious self-pair for every self-mirrored index and inflate the third row to $6$.
- **No matches at all** (the second row) → $0$, even though the values repeat across the arrays.
- **Order within the pair is fixed** by $i < j$, so each good pair is counted exactly once.
- **$A_i, B_i$ up to $10^9$**: the dictionary is keyed on tuples of raw byte tokens, with no integer conversion — safe because the input has no leading zeros.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass with a `Counter`.

## Dry run

Fourth sample: $A = 4, 8, 1, 1$ and $B = 8, 4, 1, 1$.

| $j$ | key $(A_j, B_j)$ | mirror sought | times seen before | running total |
|---:|---|---|---:|---:|
| 1 | $(4, 8)$ | $(8, 4)$ | 0 | 0 |
| 2 | $(8, 4)$ | $(4, 8)$ | **1** | 1 |
| 3 | $(1, 1)$ | $(1, 1)$ | 0 | 1 |
| 4 | $(1, 1)$ | $(1, 1)$ | **1** | 2 |

Output `2`.

---

Same problem in rating order (#266 of 486): [../../by-rating/266-GOODPAIRS.md](../../by-rating/266-GOODPAIRS.md)
