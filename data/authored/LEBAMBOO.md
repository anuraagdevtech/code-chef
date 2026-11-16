---
topic: Basic Math
subtopic: Solve the linear equations for operation counts
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $d_i=D_i-H_i$, let $m$ be the total number of bottles, and let $x_i$ bottles be applied to stem $i$. Each bottle raises all stems by one except its selected stem, which instead decreases by one, so $d_i=m-2x_i$.

For $N>2$, summing gives $m=\sum d_i/(N-2)$. This uniquely determines the answer: require a nonnegative integer $m$ and nonnegative integer $x_i=(m-d_i)/2$ for every stem. For $N=2$, the sum must stay unchanged and the minimum is $|d_0|$. For $N=1$, only decreases are possible.

## Edge cases

- Treat $N=1$ and $N=2$ separately.
- A nonnegative total alone does not ensure parity or individual feasibility.
- Intermediate negative heights are explicitly allowed.

## Dry run

For `[3,2,2]` to `[4,5,3]`, differences are `[1,3,1]`. The total is `m=5`; operation counts are `[2,1,2]`, summing to five.
