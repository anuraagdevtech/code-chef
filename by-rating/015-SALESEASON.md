# 015. Sale Season

> [`SALESEASON`](https://www.codechef.com/problems/SALESEASON) &middot; difficulty **541** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Ordered threshold ladder |
| **CodeChef tags** | `Basic Programming Concepts` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

It's the sale season again and Chef bought items worth a total of $X$ rupees. The sale season offer is as follows:
- if $X \le 100$, no discount.
- if $100 \lt X \le 1000$, discount is $25$ rupees.
- if $1000 \lt X \le 5000$, discount is $100$ rupees.
- if $X \gt 5000$, discount is $500$ rupees.

Find the final amount Chef needs to pay for his shopping.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line of input containing an integer $X$.

**Output**

For each test case, output on a new line the final amount Chef needs to pay for his shopping.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 10000$

## Sample

**Sample input**

```
4
15
70
250
1000
```

**Sample output**

```
15
70
225
975
```

<details><summary>Explanation</summary>

**Test case $1$:** Since $X \le 100 $, there is no discount.

**Test case $3$:** Here, $X = 250$. Since $100 \lt 250 \le 1000$, discount is of $25$ rupees. Therefore, Chef needs to pay $250-25 = 225$ rupees.

</details>

## Approach

The discount is a step function of the bill $X$: nothing up to $100$, then $25$, then $100$, then $500$ above $5000$. The answer is $X$ minus whichever step applies.

The one thing to get right is that the bands are **half-open and ordered**, so an `if / elif` ladder tested from the smallest band upward is enough — once a branch matches, the later ones are skipped and the lower bound of each band is implied by the branch above it. Writing independent `if` statements instead would apply several discounts to the same bill.

Watch the boundaries, which are deliberately awkward: the first band is $X \le 100$, so $X = 100$ gets **no** discount, while $X = 101$ gets $25$. The third band is $1000 < X \le 5000$, so $X = 1000$ still sits in the $25$ band — sample case 4 pins this down, paying $1000 - 25 = 975$ rather than $900$.

A table-driven alternative is to store `(limit, discount)` pairs and walk them, which generalises better if the bands ever grow; for four fixed bands the explicit ladder is clearer.

## Solution

```python
import sys


def discount(x: int) -> int:
    # Bands are half-open and ordered, so the first match wins.
    if x <= 100:
        return 0
    if x <= 1000:
        return 25
    if x <= 5000:
        return 100
    return 500


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        out.append(str(x - discount(x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Exactly on each boundary.** $X = 100$ sits in the first band, so no discount; $X = 1000$ is still in the second band, so $25$ off, giving $975$ (the sample checks this); $X = 5000$ takes $100$ off.
- **One past a boundary.** $X = 101$ drops into the second band for $76$ — a single rupee more than $100$ costs $25$ less.
- **Smallest input** ($X = 1$): no discount, so $1$.
- **Largest input** ($X = 10000$): $500$ off, so $9500$.
- **Band order matters.** The tests are written ascending with `<=` so the first match wins; reordering them, or using open intervals, silently applies the wrong discount.
- The discount never exceeds the price in any band, so the answer cannot go negative.

## Dry run

| $X$ | band | discount | output |
|---:|---|---:|---|
| 15 | $X \leq 100$ | 0 | `15` |
| 70 | $X \leq 100$ | 0 | `70` |
| 250 | $100 < X \leq 1000$ | 25 | `225` |
| 1000 | $100 < X \leq 1000$ | 25 | `975` |

The last row is the boundary: $1000$ belongs to the second band, not the third.

---

Same problem grouped by topic: [../docs/conditionals-case-work/SALESEASON.md](../docs/conditionals-case-work/SALESEASON.md)
