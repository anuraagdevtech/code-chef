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
