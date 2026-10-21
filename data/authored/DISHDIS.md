---
topic: Dynamic Programming
subtopic: Bounded compositions via a prefix-sum convolution
time: $O(nm)$ per test case
space: $O(n)$
---
The dishes are indistinguishable, so a distribution is a tuple $(d_1, \ldots, d_m)$ with $x_i \leq d_i \leq y_i$ and $\sum d_i = n$ — a **bounded composition** of $n$. Processing cooks one at a time gives

$$\mathrm{dp}_i[j] = \sum_{d = x_i}^{\min(y_i,\, j)} \mathrm{dp}_{i-1}[j - d]$$

with $\mathrm{dp}_0[0] = 1$. Done literally this is $O(nm \cdot 101)$ per test, and with $T = 50$ that is tens of millions of operations for no reason.

The inner sum is a **contiguous window** of the previous row, so one prefix-sum array $P[j] = \sum_{u \leq j} \mathrm{dp}_{i-1}[u]$ collapses it to a subtraction:

$$\mathrm{dp}_i[j] = P[j - x_i] - P[j - y_i - 1]$$

treating out-of-range indices as $0$. Each cook is then $O(n)$ and the whole test $O(nm)$. Doing the subtraction under the modulus can go negative, so add $\mathrm{MOD}$ before reducing.

One edge case the bounds permit: $x_i$ and $y_i$ are independent, so a cook may have $x_i > y_i$ — an empty range, making the answer $0$ outright. Also $x_i$ may be $0$, so a cook can be given nothing.

The sample has $n = 3$ with ranges $[0,3]$ and $[1,3]$. The three distributions are $(0,3)$, $(1,2)$ and $(2,1)$; $(3,0)$ is excluded because the second cook must receive at least one dish. Note that *every* dish must be handed out — the count is of distributions summing to exactly $n$, not at most $n$.
