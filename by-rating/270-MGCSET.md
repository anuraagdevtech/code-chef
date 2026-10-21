# 270. Magic Set

> [`MGCSET`](https://www.codechef.com/problems/MGCSET) &middot; difficulty **1472** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | A condition that reduces to its singletons |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Combinatorics`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(n)$ per test case |
| **Space** | $O(1)$ |

## Question

Katya has a sequence of integers $a_1, a_2, \dots, a_n$ and an integer $m$.

She defines a *good* sequence of integers as a non-empty sequence such that the sum of the elements in each of its non-empty subsequences is divisible by $m$.

Katya wants to know the number of good subsequences of the sequence $a$. Can you help her?

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $n$ and $m$.
- The second line contains $n$ space-separated integers $a_1, a_2, \dots, a_n$.

**Output**
For each test case, print a single line containing one integer — the number of good subsequences.

**Constraints**
- $1 \le T \le 1,000$
- $1 \le n \le 30$
- $1 \le m \le 1,000$
- $1 \le a_i \le 1,000$ for each valid $i$

**Subtasks**
**Subtask #1 (30 points):** $1 \le n \le 5$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 1,000$
- $1 \le n \le 30$
- $1 \le m \le 1,000$
- $1 \le a_i \le 1,000$ for each valid $i$

## Sample

**Sample input**

```
2
2 3
1 2
2 3
1 3
```

**Sample output**

```
0
1
```

<details><summary>Explanation</summary>

**Example case 1:** There are no good subsequences.

**Example case 2:** There is exactly one good subsequence of $a$: $[3]$.

</details>

## Approach

A subsequence is *good* when **every** non-empty subsequence of it has sum divisible by $m$. The condition looks expensive — exponentially many sub-subsequences — but it collapses.

The singletons are themselves non-empty subsequences, so every chosen element must individually be divisible by $m$. Conversely, if all chosen elements are multiples of $m$, then any sum of them is a multiple of $m$ too, so every sub-subsequence qualifies automatically.

So a subsequence is good **exactly when all of its elements are divisible by $m$**, and the count is the number of non-empty subsets of those elements:

$$2^{c} - 1, \qquad c = \#\{i : m \mid a_i\}$$

The $-1$ excludes the empty subsequence, which the problem rules out.

Spotting that the strongest constraints are the smallest ones — the singletons — is the move here. Without it, one might reach for a subset-sum DP over residues, which at $n = 30$ would be $2^{30}$ by brute force or $O(n \cdot m)$ by DP, both unnecessary.

Sample case 1 has $a = [1, 2]$ with $m = 3$: neither element is a multiple of $3$, so $c = 0$ and the answer is $2^0 - 1 = 0$. Sample case 2 has $a = [1, 3]$: only the $3$ qualifies, giving $2^1 - 1 = 1$ — the subsequence $[3]$ alone.

With $n \leq 30$ the count fits comfortably in $2^{30}$, so no modular arithmetic is needed.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        # Singletons force every chosen element to be divisible by m, and that
        # is also sufficient, so just count those and take all subsets.
        c = sum(1 for v in data[pos + 2:pos + 2 + n] if int(v) % m == 0)
        pos += 2 + n
        out.append(str((1 << c) - 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The singletons carry the whole condition.** Every non-empty subsequence must have a sum divisible by $m$, and the one-element subsequences force each chosen $a_i \equiv 0 \pmod m$ — after which every larger sum is a sum of multiples and is automatically divisible. So the condition collapses to a per-element test.
- **No divisible element** (the first row, $m = 3$ with values $1, 2$) → $0$ good subsequences, since even a single element fails.
- **The subsequence must be non-empty**, hence the $-1$: with $c$ divisible elements there are $2^c$ subsets but the empty one does not count.
- **Duplicates count as distinct positions**, so two copies of a divisible value give $3$ good subsequences, not $1$.
- **$m = 1$** would make every element divisible and the answer $2^n - 1$.
- **$n \leq 30$** keeps $2^c$ inside 32 bits, and the shift is exact in Python regardless.

## Dry run

| $n$ | $m$ | values | divisible by $m$ | $c$ | $2^c - 1$ |
|---:|---:|---|---|---:|---:|
| 2 | 3 | $1, 2$ | none | 0 | `0` |
| 2 | 3 | $1, 3$ | $3$ | 1 | `1` |

The only good subsequence in the second row is $[3]$ itself.

---

Same problem grouped by topic: [../docs/combinatorics/MGCSET.md](../docs/combinatorics/MGCSET.md)
