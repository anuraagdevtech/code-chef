[&larr; 329. Chef and Sign Sequences](329-CHEFSIGN.md) &middot; [Index](README.md) &middot; [331. Boring String &rarr;](331-BORSTR.md)

# 330. Nice Pairs 

> [`NPAIRS`](https://www.codechef.com/problems/NPAIRS) &middot; difficulty **1564** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Counting pairs that share an invariant key |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Given a string $S$ of length $N$ containing only numeric characters, find the number of **Nice Pairs**.

A **Nice Pair** is a pair of indices - $(i, j)$ such that $1 \leq i \lt j \leq N$ and $j - i = |S_j - S_i|$.

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each testcase contains a single integer, $N$, the length of the string
- The second line of each testcase contains a string $S$ of length $N$. The string contains only numeric characters $[0-9]$

**Output**

For each testcase, output a single integer - the number of nice pairs in the given string.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- String $S$ contains only numeric characters
- The sum of $N$ over all test cases does not exceed $2\cdot10^5$

## Sample

**Sample input**

```
3
3
123
5
13492
8
94241234
```

**Sample output**

```
3
2
9
```

<details><summary>Explanation</summary>

**Test Case $1$:** There are $3$ nice pairs in the given string - $(1,2) , (1,3) , (2,3)$

**Test Case $2$:** There are $2$ nice pairs in the given string - $(2,3) , (3,5)$

</details>

## Approach

Removing the absolute value splits the condition $j - i = |S_j - S_i|$ (with $i < j$) into two linear cases:

$$S_j - S_i = j - i \iff S_j - j = S_i - i$$
$$S_i - S_j = j - i \iff S_i + i = S_j + j$$

So a nice pair is exactly a pair of indices agreeing on the key $S_i - i$, **or** a pair agreeing on the key $S_i + i$. Each case automatically carries its own sign condition — if $S_j - j = S_i - i$ then $S_j - S_i = j - i > 0$, so the absolute value is indeed $j - i$ — and no pair can satisfy both, since that would force $j - i = 0$.

The answer is therefore a sum of two independent tallies, with no double counting to correct:

$$\sum_{v} \binom{\mathrm{cnt}^-_v}{2} \;+\; \sum_{v} \binom{\mathrm{cnt}^+_v}{2}$$

Two `Counter` passes and a sum, giving $O(N)$ with no dependence on the alphabet.

There is also a cheaper-looking shortcut: digits bound $|S_j - S_i| \leq 9$, so only gaps $j - i \leq 9$ can ever qualify, and brute force over those nine offsets is $O(9N)$. That works here, but the key-counting formulation is both faster and indifferent to the alphabet.

The third sample shows the two tallies carrying different weight. For `94241234`, the key $S_i - i$ takes the value $-4$ at four positions, contributing $\binom{4}{2} = 6$, while $S_i + i$ has three colliding pairs, for a total of $9$.

## Solution

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for case in range(t):
        s = data[2 + 2 * case]
        # j - i = |S_j - S_i| holds iff S-i matches, or S+i matches.
        down = Counter(d - i for i, d in enumerate(s))
        up = Counter(d + i for i, d in enumerate(s))
        total = sum(c * (c - 1) // 2 for c in down.values())
        total += sum(c * (c - 1) // 2 for c in up.values())
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The condition splits into two linear cases.** $j - i = |S_j - S_i|$ holds either when $S_j - S_i = j - i$, so $S - \text{index}$ is constant, or when $S_i - S_j = j - i$, so $S + \text{index}$ is constant. Counting equal keys in each map is the whole algorithm.
- **No pair is counted twice.** Both cases together would force $S_i = S_j$ and $j - i = 0$, which $i < j$ rules out — so the two tallies are disjoint and simply add.
- **Digit characters work as raw byte codes**, since only differences matter and the $+48$ offset cancels on both sides of every comparison.
- **Adjacent equal digits are not a pair**: the gap is $1$ but the digit difference is $0$.
- **Digits ascending by exactly one put every index in the same `down` bucket**, since $S - \text{index}$ never changes — which is why `123` gives all three pairs rather than only the adjacent two.
- **The keys can be negative** (for `down`) and are unbounded above (for `up`), so a dictionary rather than an array is the right structure.
- **Sum of $N \leq 2 \cdot 10^5$**: two `Counter`s per case.

## Dry run

First sample: `123`.

| index $i$ | digit | $S - i$ | $S + i$ |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 2 | 1 | 3 |
| 2 | 3 | 1 | 5 |

The `down` key $1$ holds all three indices, giving $\binom{3}{2} = 3$ pairs; the `up` keys are all distinct and contribute nothing. Output `3` — the pairs are $(1,2)$, $(2,3)$ and $(1,3)$, each with $j - i = S_j - S_i$.

---

Same problem grouped by topic: [../docs/combinatorics/NPAIRS.md](../docs/combinatorics/NPAIRS.md)
