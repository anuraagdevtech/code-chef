[&larr; 219. Reversal Sorting](REVSORT.md) &middot; [Index](../../README.md) &middot; [229. Fit to Play &rarr;](PLAYFIT.md)

# 223. Array Halves

> CodeChef problem code [`ARRHALVES`](https://www.codechef.com/problems/ARRHALVES) &middot; difficulty **1407** &middot; time limit **3s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Minimum adjacent swaps to gather a set |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Chef has a permutation $P$ of length $2 \cdot N$. He can perform the following operation on $P$:
- Select an index $i$ $(1 \le i \lt 2 \cdot N)$ and swap $P_i$ and $P_{i + 1}$.

Chef would call the permutation $P$ *good*, if the **maximum** element of the first half of $P$ is **less** than the **minimum** element of the second half of $P$.
Formally $\displaystyle \max_{(1 \le i \le N)} P_i \lt \min_{(N \lt i \le 2 \cdot N)} P_i$.

Find the **minimum** number of operations Chef needs to apply to make $P$ *good*.

**Note:** A permutation of length $N$ is an array where every integer from $1$ to $N$ occurs exactly once.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — half the size of the permutation $P$.
- The second line of each test case contains $2 \cdot N$ space-separated integers $P_1, P_2, \dots, P_{2 \cdot N}$ denoting the permutation $P$.

**Output**

For each test case, output the minimum number of operations required to make $P$ *good*.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $P$ is a permutation of length $2 \cdot N$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
2
3 2 1 4
3
1 2 3 4 5 6
3
6 5 4 3 2 1
```

**Sample output**

```
2
0
9
```

<details><summary>Explanation</summary>

**Test case $1$:** We can perform the following operations:
- Apply operation at $i = 1$: $[3, 2, 1, 4] \rightarrow [2, 3, 1, 4]$
- Apply operation at $i = 2$: $[2, 3, 1, 4] \rightarrow [2, 1, 3, 4]$

**Test case $2$:** $P$ is already good.

</details>

## Approach

Since $P$ is a permutation of $1 \ldots 2N$, "max of the first half below min of the second half" can only mean the first half holds exactly $\{1, \ldots, N\}$ and the second holds $\{N+1, \ldots, 2N\}$. **Their order within each half is irrelevant.**

So the task is: move the $N$ small values into the first $N$ positions, using adjacent swaps, as cheaply as possible.

The classic result applies. If the small values currently sit at positions $p_1 < p_2 < \cdots < p_N$ (zero-indexed), the minimum number of adjacent swaps to gather them into the first $N$ slots is

$$\sum_{i=0}^{N-1} (p_i - i)$$

The reasoning: the relative order of the small values never needs to change — swapping two of them is wasted work — so the $i$-th small value from the left is destined for slot $i$, and each must step past exactly the large values standing before it. The sum counts precisely those crossings.

That subtraction of $i$ is what prevents double-counting. Summing the raw positions would also charge each small value for the small values ahead of it, which it never has to cross.

Sample case 3 is the worst case: $[6,5,4,3,2,1]$ has its small values at positions $3,4,5$, giving $(3-0)+(4-1)+(5-2) = 9$. Sample case 2 is already good at $0$ cost. Sample case 1, $[3,2,1,4]$ with $N=2$, has small values at $1$ and $2$, giving $1 + 1 = 2$ — note the result is already good without sorting either half.

The answer can reach about $N^2 \approx 10^{10}$, which **overflows 32 bits** — Python is fine, but a C solution needs a 64-bit accumulator.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        p = data[pos + 1:pos + 1 + 2 * n]
        pos += 1 + 2 * n
        # Only which half each value lands in matters, not the order within.
        swaps = 0
        target = 0
        for idx, v in enumerate(p):
            if int(v) <= n:
                swaps += idx - target
                target += 1
        out.append(str(swaps))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **The first half must hold exactly $1 \dots N$** — not merely be separated from the second. The third row, $6,5,4,3,2,1$, already has the small values grouped in the *second* half, yet the answer is $9$, because they must be moved to the front.
- **Only which half a value lands in matters**, not its order within that half, so the cost is the number of cross-class inversions rather than a full sort.
- **Already good** (the second row) → $0$.
- **Fully reversed** (the third row) → the maximum, $N^2 = 9$.
- **The target pointer advances only when a small value is placed**, so each small value is charged exactly the number of large values preceding it — which is the minimum, since adjacent swaps can fix one such inversion at a time.
- **$P$ is a permutation of $1 \dots 2N$**, so exactly $N$ values are at most $N$ and the pointer ends at $N$.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass, with the threshold test done on converted integers since byte comparison would order `10` before `9`.

## Dry run

First sample: $N = 2$, $P = 3, 2, 1, 4$. Small values are $1$ and $2$.

| index | value | small? | target slot | cost added |
|---:|---:|:---:|---:|---:|
| 0 | 3 | no | 0 | — |
| 1 | 2 | yes | 0 | $1 - 0 = 1$ |
| 2 | 1 | yes | 1 | $2 - 1 = 1$ |
| 3 | 4 | no | 2 | — |

Total `2`: swap $3$ with $2$, then $3$ with $1$, giving $2,1,3,4$.

> CodeChef tags: `Algorithms`, `Constructive`

---

Same problem in rating order (#229 of 486): [../../by-rating/229-ARRHALVES.md](../../by-rating/229-ARRHALVES.md)
