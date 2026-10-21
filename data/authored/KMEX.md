---
topic: Conditionals & Case Work
subtopic: Feasibility as a counting interval
time: $O(N)$ per test case
space: $O(N)$
---
"MEX exactly $K$" is two requirements pulling in opposite directions, and separating them makes the problem a plain interval test.

**Must include** every one of $0, 1, \ldots, K-1$ at least once — so each must be present in $A$ at all, and the chosen set needs at least $K$ elements. **Must exclude** $K$ entirely, so every occurrence of $K$ in $A$ is off limits, leaving $N - \mathrm{cnt}(K)$ usable elements.

Nothing else constrains the choice: values above $K$, and extra copies of values below $K$, are all **free padding** that cannot change the MEX. So any count between the floor and the ceiling is achievable, and the answer is `YES` exactly when

$$\{0, \ldots, K-1\} \subseteq A \quad\text{and}\quad K \leq M \leq N - \mathrm{cnt}(K)$$

The sample is built to fail each clause in turn. Case 2 ($M = 1 < K = 2$) has both $0$ and $1$ available but too few picks to include them. Case 4 needs $0, 1, 2$ but the array has no $1$ at all. Case 5 has $M = 4$ while only $5 - 2 = 3$ elements avoid $K = 2$ — the exclusion is what runs out. Case 6 is the same shape but with one fewer $2$, so $5 \leq 5$ just fits.

Case 3 is the tight corner: $K = M = N = 3$ with $A = [0,1,2]$, so every element is needed and the MEX is $3$ exactly. That is also why the ceiling is $N - \mathrm{cnt}(K)$ rather than $N$: here $\mathrm{cnt}(3) = 0$, so nothing is lost.

The case $K = 0$ falls out of the same formula — no values are required, only that enough elements avoid $0$.

## Edge cases

- **Everything below $K$ is mandatory.** The fourth row lacks any $1$, so no subsequence can have MEX $3$ and the answer is `NO` regardless of the length.
- **Every copy of $K$ is unusable**, so the pool shrinks by $\mathrm{count}(K)$. The fifth row needs length $4$ but has two $2$s among its five elements, leaving only $3$ usable — `NO`.
- **The subsequence must be at least $K$ long** just to hold $0, \dots, K-1$. The second row needs length $2$ and $M$ is $1$ — `NO`.
- **$K = 0$ makes nothing mandatory**, and the test collapses to $M \leq N - \mathrm{count}(0)$.
- **Duplicates and values above $K$ are free padding**, which is how the sixth row pads out to length $5$ using its extra zeros.
- **Both bounds are inclusive**: $K \leq M \leq N - \mathrm{count}(K)$, and the third row sits on both ends at once ($K = M = N = 3$).

## Dry run

Fifth sample: $N = 5$, $M = 4$, $K = 2$, $A = 0, 2, 1, 2, 5$.

| check | value | verdict |
|---|---|---|
| are $0$ and $1$ present? | yes, one each | ✓ |
| $K \leq M$ | $2 \leq 4$ | ✓ |
| usable elements $N - \mathrm{count}(2)$ | $5 - 2 = 3$ | — |
| $M \leq$ usable | $4 \leq 3$ | **✗** |

Output `NO`: the two $2$s must be excluded, and the remaining $0, 1, 5$ cannot reach length $4$.
