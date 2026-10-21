---
topic: Constructive
subtopic: Forcing every good subsegment to be a prefix
time: $O(N)$ per test case
space: $O(N)$
---
The construction becomes easy after one normalising decision: **put $1$ first**. Every good subsegment must contain the value $1$, so with $1$ at position $1$ every good subsegment is a *prefix*. And a prefix of length $L$ holds $L$ distinct values from $1 \ldots N$, so it is good exactly when

$$\max(P_1, \ldots, P_L) = L$$

That turns "exactly $K$ good subsegments" into "exactly $K$ prefix maxima that equal their own length". Prefixes $1$ and $N$ always qualify, which settles the impossible case: for $N \geq 2$, $K = 1$ is unachievable, so print $-1$. ($N = 1$ has only $K = 1$.)

Otherwise pick the good lengths to be $1, 2, \ldots, K-1$ and $N$. To realise a jump from length $\ell$ to length $\ell'$, fill positions $\ell+1 \ldots \ell'$ with the values $\ell+1 \ldots \ell'$ **in decreasing order**. Then every intermediate prefix already contains the block's largest value $\ell'$ while being shorter than $\ell'$, so it is not good, and the prefix of length $\ell'$ is. Concretely:

$$P = [\,1,\, 2,\, \ldots,\, K-1,\ N,\, N-1,\, \ldots,\, K\,]$$

The leading run gives the jumps of size one, and the descending tail gives the single big jump to $N$. When $K = N$ the tail is a single element and this is the identity permutation, whose every prefix is good.

For $N = 3, K = 2$ this is `1 3 2`, matching the sample. For $N = 5, K = 3$ it gives `1 2 5 4 3`, whose good prefixes are lengths $1, 2, 5$; the sample's `5 3 1 4 2` has good segments at lengths $1, 4, 5$ instead — different positions, same count, and both accepted.
