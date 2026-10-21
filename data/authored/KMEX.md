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
