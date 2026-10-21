---
topic: Bit Manipulation
subtopic: AND is monotone, so only adjacent pairs matter
time: $O(N)$ per test case
space: $O(N)$
---
The search space looks large — every subarray of size $\geq 2$ through each index — but **bitwise AND only ever loses bits**. Extending a subarray can clear bits and never set them, so for any subarray $S$ and any $S' \subseteq S$,

$$\mathrm{AND}(S) \leq \mathrm{AND}(S')$$

Every subarray of size $\geq 2$ containing index $i$ contains one of the two adjacent pairs $(i-1, i)$ or $(i, i+1)$, and by monotonicity its AND is no larger than that pair's. So the maximum is attained at size exactly $2$:

$$d_i = \max\bigl(A_{i-1} \,\&\, A_i,\; A_i \,\&\, A_{i+1}\bigr)$$

with the missing term dropped at the two ends — and since $N \geq 2$, each index always has at least one neighbour, so $d_i$ is always defined.

The implementation is then one pass computing the $N - 1$ adjacent ANDs and a second taking the max of each index's one or two incident pairs. There is no need for a sparse table or a two-pointer sweep over bit counts; the monotonicity collapses the whole problem.

Sample 1, $[29, 412, 671, 255, 912]$, has adjacent ANDs $28, 156, 159, 144$, so the answers are $28$, $\max(28,156)$, $\max(156,159)$, $\max(159,144)$, $144$ — i.e. `28 156 159 159 144`. Note $d_4 = 159$ comes from the pair to its *left*, which is the point of taking the max over both neighbours rather than always looking one way.

## Edge cases

- **AND never gains bits**, so extending a subarray can only lower its value — meaning the best subarray containing shop $i$ is as small as the rules allow.
- **The size must be strictly larger than $1$**, so the smallest candidate is a pair — and the best pair containing $i$ is either $\{i-1, i\}$ or $\{i, i+1\}$. That reduces the whole problem to $N-1$ pairwise ANDs.
- **The ends have only one neighbour**, so shop $1$ takes the first pair and shop $N$ the last, with no maximum to compute.
- **A single shop is never a valid answer** even when its own value is large — the sample's first shop holds $29$ but its damage is $28$, the AND with its neighbour.
- **$A_i$ may be $0$**, which zeroes both pairs it belongs to.
- **$N \geq 2$ is guaranteed**, so at least one pair exists and `pairs` is never empty.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass for the pairs and one for the maxima.

## Dry run

First sample: $A = 29, 412, 671, 255, 912$.

| pair | AND |
|---|---:|
| $29 \,\&\, 412$ | 28 |
| $412 \,\&\, 671$ | 156 |
| $671 \,\&\, 255$ | 159 |
| $255 \,\&\, 912$ | 144 |

| shop | pairs available | damage |
|---:|---|---:|
| 1 | 28 | 28 |
| 2 | 28, 156 | 156 |
| 3 | 156, 159 | 159 |
| 4 | 159, 144 | 159 |
| 5 | 144 | 144 |
