[&larr; 210. Cooking Machine](210-COOKMACH.md) &middot; [Index](README.md) &middot; [212. Count Substrings &rarr;](212-CSUB.md)

# 211. Indivisible Permutation

> [`INDIPERM`](https://www.codechef.com/problems/INDIPERM) &middot; difficulty **1329** &middot; time limit **0.5s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | A single cyclic shift |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given an integer $N$. Construct an array $P$ of size $N$ such that:

- $P$ is a permutation of the first $N$ natural numbers, i.e, each integer $1, 2, 3, \ldots N$ occurs exactly once in $P$. For example, $[1, 3, 2]$ is a permutation of size $3$, but $[1, 3, 4]$ and $[2, 1, 2]$ are not.
- $P$ is **indivisible**. $P$ is said to be **indivisible** if $i$ does not divide $P_i$ for every index $2 \leq i \leq N$.

It can be proven that under the given constraints, there always exists an **indivisible** permutation. If there are multiple, you may print any of them.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$, denoting the size of the indivisible permutation you must construct.

**Output**

- For every test case, print a single line containing $N$ space-separated integers. These integers must form an **indivisible**  permutation.

## Constraints

- $1 \leq T \leq 600$
- $2 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

## Sample

**Sample input**

```
4
2
3
4
5
```

**Sample output**

```
2 1 
1 3 2 
1 3 4 2 
4 5 2 3 1
```

<details><summary>Explanation</summary>

- For the last test case:
    - $P_2 = 5$ is not divisible by $2$
    - $P_3 = 2$ is not divisible by $3$
    - $P_4 = 3$ is not divisible by $4$
    - $P_5 = 1$ is not divisible by $5$
- Since $i$ does not divide $P_i$ for every index $2\leq i\leq N$, the permutation is **indivisible**.

</details>

## Approach

The requirement is that $i \nmid P_i$ for every $i \geq 2$. Index $1$ is deliberately excluded, because $1$ divides everything and no permutation could satisfy it there.

The simplest construction is a **cyclic shift by one**:

$$P = [N, 1, 2, 3, \ldots, N-1]$$

so that $P_i = i - 1$ for every $i \geq 2$.

Why it works: for $i \geq 2$ we have $0 < i - 1 < i$, and a positive integer strictly smaller than $i$ can never be a multiple of $i$. So $i \nmid P_i$ holds for every index at once, with no case analysis.

The wrapped value $N$ lands at index $1$, which is exactly the index with no constraint — the shift puts the one problematic value in the one position where nothing is required.

Contrast this with the identity permutation, which fails at **every** index since $i \mid i$ always. Shifting by one is the minimal perturbation that fixes all of them simultaneously.

For $N = 2$ this gives `2 1`, matching the sample exactly. For $N = 3$ it gives `3 1 2` where the sample prints `1 3 2` — both satisfy the condition ($2 \nmid 3$ and $3 \nmid 2$), so **any indivisible permutation is accepted** and this is judged by a checker.

The guarantee $N \geq 2$ means the shift always has somewhere to wrap to.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # P_i = i - 1 for i >= 2, and 0 < i - 1 < i can never be a multiple
        # of i. The wrapped N lands at index 1, which is unconstrained.
        out.append(" ".join(map(str, [n] + list(range(1, n)))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Index $1$ is exempt by the statement** ($i \nmid P_i$ is required only for $2 \leq i \leq N$), which is what makes the problem solvable at all — every integer is divisible by $1$.
- **The wrapped $N$ lands at index $1$**, precisely the unconstrained slot, so the single cyclic shift is enough.
- **Every other index is safe for the same reason**: $P_i = i - 1$ satisfies $0 < i - 1 < i$, and no multiple of $i$ lies strictly between $0$ and $i$.
- **$N = 2$** (the smallest case): $[2, 1]$, where $P_2 = 1$ is not divisible by $2$.
- **This answer differs from the sample's** at $N \geq 3$ — it prints `3 1 2` where the sample shows `1 3 2`. The statement allows any valid permutation, so a special judge checks the divisibility rather than the exact output.
- **Sum of $N \leq 2 \cdot 10^5$**, so each line is built once and all output is joined at the end.

## Dry run

$N = 5$ gives $P = 5, 1, 2, 3, 4$.

| $i$ | $P_i$ | $P_i \bmod i$ | required? |
|---:|---:|---:|---|
| 1 | 5 | 0 | exempt |
| 2 | 1 | 1 | ✓ |
| 3 | 2 | 2 | ✓ |
| 4 | 3 | 3 | ✓ |
| 5 | 4 | 4 | ✓ |

For $i \geq 2$ the remainder is always $i - 1$, never zero.

---

Same problem grouped by topic: [../docs/constructive/INDIPERM.md](../docs/constructive/INDIPERM.md)
