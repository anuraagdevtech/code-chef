# 155. Marathon

> [`MARARUN`](https://www.codechef.com/problems/MARARUN) &middot; difficulty **955** &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Largest achievable tier |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Conditional Statements`, `Basic Math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chefland is holding a virtual marathon for the categories $10$ km, $21$ km and $42$ km having prizes $A, B, C$ ($A \lt B \lt C$) respectively to promote physical fitness. In order to claim the prize in a particular category the person must cover the total distance for that category within $D$ days. Also a single person **cannot** apply in multiple categories.

Given the maximum distance $d$ km that Chef can cover in a single day, find the maximum prize that Chef can win at the end of $D$ days. If Chef can't win any prize, print $0$.

**Input**

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, five integers $D, d, A, B, C$.

**Output**

For each test case, output in a single line the answer to the problem.

## Constraints

- $1 \leq T \leq 50$
- $1 \leq D \leq 10$
- $1 \leq d \leq 5$
- $1 \leq A \lt B \lt C \leq 10^5$

## Sample

**Sample input**

```
3
1 1 1 2 3
10 1 1 2 3
10 3 1 2 3
```

**Sample output**

```
0
1
2
```

<details><summary>Explanation</summary>

**Test Case $1$:** The maximum distance covered by Chef is $1 \cdot 1 = 1$ km which is less than any of the available distance categories. Hence Chef won't be able to claim a prize in any of the categories.

**Test Case $2$:** The maximum distance covered by Chef is $10 \cdot 1 = 10$ km which is equal to distance of the first category. Hence Chef can claim the maximum prize of $1$ units.

**Test Case $3$:** The maximum distance covered by Chef is $10 \cdot 3 = 30$ km which is more than the distance of the second category but less than that of the third category. Hence Chef can claim the maximum prize of $2$ units.

</details>

## Approach

Over $D$ days at $d$ km per day, Chef can cover at most $D \cdot d$ kilometres. Since prizes satisfy $A < B < C$, longer categories always pay more, so Chef should enter the **longest category he can finish**:

- $D \cdot d \geq 42$ → prize $C$
- $D \cdot d \geq 21$ → prize $B$
- $D \cdot d \geq 10$ → prize $A$
- otherwise → $0$

Testing from the longest distance downward means each branch may assume the longer ones failed, so only a lower bound is needed per tier.

The guarantee $A < B < C$ is what licenses the greedy. Without it — if a shorter race paid more — Chef would have to compare prizes rather than distances, and the ladder would need to check all affordable tiers and take the maximum prize.

The rule that one person cannot enter multiple categories is what keeps this a single choice rather than a packing problem; otherwise Chef might split his distance across several races.

Sample case 3 is the discriminating one: $10 \times 3 = 30$ km clears $21$ but falls short of $42$, so the answer is $B = 2$ rather than $C$. Sample case 1 covers just $1$ km and wins nothing, which is why the explicit $0$ branch is needed — the constraints allow $D \cdot d$ as low as $1$.

The maximum reach is $D \cdot d \leq 10 \times 5 = 50$, so the $42$ km tier is attainable but only just.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        d_days, d_km, a, b, c = map(int, data[1 + 5 * i:6 + 5 * i])
        total = d_days * d_km
        # Prizes increase with distance, so take the longest race he can finish.
        out.append(str(c if total >= 42 else b if total >= 21 else a if total >= 10 else 0))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Below every threshold** (a total of $1$ km): no prize at all, so $0$ — a case the ladder needs an explicit final branch for.
- **Exactly on a threshold** ($10$, $21$ or $42$): qualifies for that tier, so the comparisons are non-strict. The second sample row sits exactly on $10$.
- **The longest race he can finish is always the best**, because $A < B < C$ is guaranteed — so there is no need to compare prize values, only distances.
- **Largest total** ($D = 10$ days at $d = 5$ km, so $50$): clears $42$ and takes $C$.
- The bands must be tested from the top down; ascending tests with the first match winning would hand out the smallest prize instead of the largest.

## Dry run

| $D$ | $d$ | total | tier reached | prize | output |
|---:|---:|---:|---|---:|---|
| 1 | 1 | 1 | none | 0 | `0` |
| 10 | 1 | 10 | $\geq 10$ | $A = 1$ | `1` |
| 10 | 3 | 30 | $\geq 21$ | $B = 2$ | `2` |

Row 2 lands exactly on the first threshold.

---

Same problem grouped by topic: [../docs/conditionals-case-work/MARARUN.md](../docs/conditionals-case-work/MARARUN.md)
