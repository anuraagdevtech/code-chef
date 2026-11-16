---
topic: Basic Math
subtopic: Recover the common difference from the angle sum
time: $O(\log V)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The angle sum is $180(N-2)$. For an arithmetic progression starting at $A$, this equals $NA+N(N-1)d/2$. Therefore the $K$-th angle is $A+2(K-1)(180(N-2)-NA)/(N(N-1))$.

Form one integer numerator over denominator $N(N-1)$, then divide both by their GCD. Keeping integer arithmetic avoids rounding rational angles.

## Edge cases

- $K=1$ returns exactly $A/1$.
- Equal angles have common difference zero.
- Reduce the fraction even when the angle is an integer.

## Dry run

For `N=3, A=30, K=2`, the total is 180, so the progression difference is 30 and the second angle is `60 1`.
