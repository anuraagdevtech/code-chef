---
topic: Prefix Sums
subtopic: Minimising the heavier side of a split
time: $O(N)$ per test case
space: $O(1)$
---
The split point is the only decision: the first processor takes a prefix, the second takes the rest. Both run **simultaneously**, so the finishing time is the larger of the two workloads, not their sum:

$$\min_{0 \leq c \leq N} \max\bigl(\text{prefix}(c),\ \text{total} - \text{prefix}(c)\bigr)$$

Computing the total once, then sweeping $c$ from $0$ to $N$ with a running prefix sum, evaluates every split in $O(N)$ with no stored array.

Taking the **maximum** rather than the sum is the crux. Sample case 1, $[4,2,3]$, totals $9$ but finishes in $5$ — one processor runs $4$ while the other runs $2+3 = 5$, and they overlap.

The split must be a **contiguous prefix**, which is what keeps this simple. Were any subset allowed, this would be the partition problem and NP-hard; the prefix restriction reduces it to a linear scan.

Note the two extreme splits are legal — all tasks to one processor — so $c = 0$ and $c = N$ must both be considered. Sample case 3, a single task, relies on that: whichever processor takes it, the answer is $5$.

Sample case 2 splits six unit tasks evenly into $3$ and $3$. The best split is not always perfectly even, though: with $[4,2,3]$ the halves are $4$ and $5$, since the boundary can only fall between tasks.

Values reach $10^5$ with $N$ up to $10^5$, so totals reach $10^{10}$ — beyond 32 bits, though Python is unaffected.

## Edge cases

- **The split must be a prefix/suffix cut**, not an arbitrary partition — the jobs keep their order, which is what makes a single scan enough instead of a subset-sum search.
- **Giving everything to one processor is legal**, which is why `best` starts at the full total and the final iteration (an empty suffix) is included. The third row, with $N = 1$, has no other option.
- **The two processors run in parallel**, so the cost is the *heavier* side — summing them would just reproduce the total.
- **$\max(\text{prefix}, \text{total} - \text{prefix})$ is V-shaped** in the cut point, since $A_i \geq 1$ makes prefixes strictly increase; so the single pass finds the true minimum and no binary search is needed.
- **A balanced split may be impossible.** The first row's best is $5$ against $4$, not an even $4.5$ — the answer is the achievable maximum, not half the total.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass per case with a running prefix rather than a stored prefix array.

## Dry run

Second sample: six jobs of cost $1$, total $6$.

| cut after | prefix | suffix | heavier side |
|---:|---:|---:|---:|
| 1 | 1 | 5 | 5 |
| 2 | 2 | 4 | 4 |
| 3 | 3 | 3 | **3** |
| 4 | 4 | 2 | 4 |
| 5 | 5 | 1 | 5 |
| 6 | 6 | 0 | 6 |

Output `3`, at the balanced cut.
