[&larr; 139. Make all equal using Pairs](139-PAIREQ.md) &middot; [Index](README.md) &middot; [141. Hoop Jump &rarr;](141-HOOPS.md)

# 140. Chef and Pairing Slippers

> [`CHEFSLP`](https://www.codechef.com/problems/CHEFSLP) &middot; difficulty **930** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Pairing limited by the scarcer side |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Constructive`, `Basic Math`, `ad-hoc`, `Observation` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has $N$ slippers, $L$ of which are left slippers and the rest are right slippers. Slippers must always be sold in pairs, where each pair contains one left and one right slipper. If each pair of slippers cost $X$ rupees, what is the maximum amount of rupees that Chef can get for these slippers?

**Input**

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains three space-separated integers $N$, $L$, and $X$ - the total number of slippers, the number of left slippers, and the price of a pair of slippers in rupees.

**Output**

For each test case, output on one line the maximum amount of rupees that Chef can get by selling the slippers that are available.

## Constraints

- $1 \leq T \leq 10^3$
- $0 \leq L \leq N \leq 10^3$
- $0 \leq X \leq 10^3$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
4
0 0 100
10 1 0
1000 10 1000
10 7 1
```

**Sample output**

```
0
0
10000
3
```

<details><summary>Explanation</summary>

- **Test case $1$:** Chef has no pairs to sell, so the amount obtained is $0$.
- **Test case $2$:** The amount earned by selling a pair is $0$, so the total amount obtained is $0$.
- **Test case $3$:** Chef can sell $10$ pairs of slippers, each giving $1000$ rupees, so the total amount earned is $1000 \cdot 10 = 10000$.
- **Test case $4$:** Chef has $10$ slippers of which $7$ are left and $3$ are right. Therefore Chef can sell a maximum of $3$ pairs and in total can get at most $3 \cdot 1 = 3$.

</details>

## Approach

Of the $N$ slippers, $L$ are left and the remaining $N - L$ are right. A sellable pair needs one of each, so the number of pairs is limited by whichever side is scarcer:

$$\text{pairs} = \min(L,\; N - L)$$

and the revenue is that count times $X$.

Taking the minimum is the whole idea — surplus slippers on the abundant side are unsellable, exactly as the spare left shoes were useless in the shoes problem. Sample case 4 shows it: $7$ left and $3$ right out of $10$ yields only $3$ pairs, stranding four left slippers.

Sample case 3 is the opposite imbalance, with $10$ left against $990$ right giving $10$ pairs — the small side binds, whichever side it happens to be, which is why `min` is used rather than assuming lefts are scarce.

Two degenerate inputs are inside the constraints and both work without special handling. $N = 0$ gives zero pairs, and $X = 0$ makes the revenue zero regardless of how many pairs exist — sample cases 1 and 2 respectively. Neither needs a guard, but it is worth noticing that a zero answer can arise for two quite different reasons.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, l, x = map(int, data[1 + 3 * i:4 + 3 * i])
        # The scarcer side caps the pairs; the surplus is unsellable.
        out.append(str(min(l, n - l) * x))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **No slippers at all** ($N = 0$): zero revenue.
- **A price of zero** ($X = 0$): zero revenue even though pairs exist. The sample's second row.
- **The scarcer side caps the pairs.** The fourth row has $7$ left and $3$ right, so only $3$ pairs sell and the four surplus left shoes are worthless — using $L$ alone would report $7$.
- **All of one kind** ($L = 0$ or $L = N$): no pairs at all.
- **Largest input** ($N = X = 1000$): $500 \times 1000 = 5 \times 10^5$.

## Dry run

| $N$ | $L$ (left) | right $N-L$ | pairs $\min$ | $X$ | output |
|---:|---:|---:|---:|---:|---|
| 0 | 0 | 0 | 0 | 100 | `0` |
| 10 | 1 | 9 | 1 | 0 | `0` |
| 1000 | 10 | 990 | 10 | 1000 | `10000` |
| 10 | 7 | 3 | 3 | 1 | `3` |

Row 4 is limited by the right shoes; row 2 by the price.

---

Same problem grouped by topic: [../docs/basic-math/CHEFSLP.md](../docs/basic-math/CHEFSLP.md)
