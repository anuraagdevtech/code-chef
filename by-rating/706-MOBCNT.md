[&larr; 705. E - Make it Zero](705-INFDIV.md) &middot; [Index](README.md) &middot; [707. Gifts at Olympics &rarr;](707-OLYMPIC.md)

# 706. Counting Mobiles

> [`MOBCNT`](https://www.codechef.com/problems/MOBCNT) &middot; difficulty **2690** &middot; time limit **2s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Leaves forced by depth, choosing which slots of each level are leaves |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + \log \sum a_i)$ per test case |
| **Space** | $O(N)$ |

## Question

A **mobile** is a rooted tree with weighted leaves that satisfies the following property: each non-leaf vertex $v$ has exactly two children $L(v)$ and $R(v)$, and the total weight of leaves in the subtree of $L(v)$ is equal to the total weight of leaves in the subtree of $R(v)$.

We have $n$ positive integer weights $a_1, \ldots, a_n$. You have to count the number of **suitable** mobiles. A mobile is **suitable** if the multiset of weights in its leaves is equal to the multiset $\{a_1, \ldots, a_n\}$. Two mobiles are considered different if they are not **equal**. Two mobiles $T_1$ and $T_2$ are **equal** in one of two cases:

- $T_1$ and $T_2$ each consist of a single leaf vertex, and the leaves' weights are equal;
- Respective roots $r_1$ and $r_2$ of $T_1$ and $T_2$ are both not leaves, and subtrees of $L(r_1)$ and $L(r_2)$ are equal mobiles, as well as subtrees of $R(r_1)$ and $R(r_2)$.
Since the answer can be large, print it modulo $10^9 + 7$.

**Input**

- The first line contains a single integer $T$, the number of test cases. $T$ test case descriptions follow.
- Each test case description starts with a line containing a single integer $n$, the number of weights. The next line contains $n$ integers $a_1, \ldots, a_n$ .

**Output**

Print answers for each test case in a new line, in the order of appearance in the input. For each test case print a single integer, the number of different suitable mobiles modulo $10^9 + 7$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq n \leq 10^5$
- $1 \leq a_i \leq 10^9$
- The sum of all $n$ does not exceed $5 \cdot 10^5$.

## Sample

**Sample input**

```
5
1
7
3
1 1 2
4
3 3 3 3
4
5 5 10 20
3
1 2 3
```

**Sample output**

```
1
2
1
4
0
```

## Approach

Every internal vertex splits its weight into two equal halves, so a vertex at depth $d$ carries exactly $S / 2^d$, where $S$ is the total weight. In particular a leaf of weight $w$ can only sit at the depth where $S / 2^d = w$: the multiset of weights fixes how many leaves each level has.

Walk down level by level. Start with one slot (the root) carrying weight $S$. If the current level has `slots` positions and `leaves` of the given weights are equal to the current weight, choose which positions become leaves in $\binom{\text{slots}}{\text{leaves}}$ ways; the left and right child are distinguishable, so different choices give different mobiles. The remaining positions are internal and produce $2 (\text{slots} - \text{leaves})$ slots of half the weight.

The count is the product of these binomials. It is 0 if there are more leaves than slots at some level, if a weight that still has to be split is odd, if slots remain when the weights are used up, or if weights remain when no slot is left. Since every open slot needs at least one leaf below it, having more slots than remaining weights is also an immediate 0, which bounds the loop.

## Solution

```python
import sys
from collections import Counter


MOD = 1000000007


def solve():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = []
    for _ in range(next(tokens)):
        n = next(tokens)
        cases.append([next(tokens) for _ in range(n)])
    limit = max(map(len, cases))
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    inverse = [1] * (limit + 1)
    inverse[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inverse[i - 1] = inverse[i] * i % MOD
    out = []
    for a in cases:
        counts = Counter(a)
        weight = sum(a)
        slots = 1
        remaining = len(a)
        answer = 1
        while remaining and slots:
            leaves = counts.get(weight, 0)
            if leaves > slots or slots > remaining:
                answer = 0
                break
            answer = answer * fact[slots] * inverse[leaves] * inverse[slots - leaves] % MOD
            remaining -= leaves
            slots = 2 * (slots - leaves)
            if slots and weight % 2:
                answer = 0
                break
            weight //= 2
        if remaining or slots:
            answer = 0
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
```

## Edge cases

- A single weight is one leaf: answer 1.
- Weights that are not $S / 2^d$ for any $d$ can never be placed and leave unused leaves: answer 0.
- An odd weight cannot be halved while internal slots remain.
- Equal weights are interchangeable; only positions are chosen, which is exactly what the binomial counts.

## Dry run

Weights `5 5 10 20`, total 40.

| depth | weight | slots | leaves | ways | next slots |
|---:|---:|---:|---:|---:|---:|
| 0 | 40 | 1 | 0 | 1 | 2 |
| 1 | 20 | 2 | 1 | 2 | 2 |
| 2 | 10 | 2 | 1 | 2 | 2 |
| 3 | 5 | 2 | 2 | 1 | 0 |

Answer $1 \cdot 2 \cdot 2 \cdot 1 = 4$.

---

Same problem grouped by topic: [../docs/combinatorics/MOBCNT.md](../docs/combinatorics/MOBCNT.md)
