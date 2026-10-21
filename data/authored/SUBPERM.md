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

## Edge cases

- **$K = 1$ is impossible for $N > 1$.** The singleton holding the value $1$ is always good, and so is the whole array — two distinct subsegments — so at least $2$ good subsegments exist. Only $N = 1$ can have exactly one.
- **Every good subsegment must contain the value $1$**, since a permutation of any length includes $1$. Placing $1$ at the front therefore makes every good subsegment a *prefix*, which is what reduces the construction to choosing which prefixes are good.
- **The leading run $1, 2, \dots, K-1$ gives $K-1$ good prefixes**, each being a permutation of $1 \dots j$.
- **The descending tail blocks every prefix in between.** Position $K$ holds $N$, so any prefix of length $j \geq K$ contains $N$ and can only be a permutation when $j = N$ — supplying exactly one more good prefix, for $K$ in total.
- **$N = 1$, $K = 1$** falls out of the same code: an empty head and a one-element tail.
- **This answer differs from the sample's** at $N = 5$, $K = 3$ (`1 2 5 4 3` against `5 3 1 4 2`); the statement asks for any such permutation, so a special judge counts the good subsegments.

## Dry run

$N = 5$, $K = 3$ gives $P = 1, 2, 5, 4, 3$.

| prefix | values | permutation of its length? |
|---|---|:---:|
| $[1]$ | $\{1\}$ | **yes** |
| $[1,2]$ | $\{1,2\}$ | **yes** |
| $[1,2,5]$ | $\{1,2,5\}$ | no |
| $[1,2,5,4]$ | $\{1,2,4,5\}$ | no |
| $[1,2,5,4,3]$ | $\{1,\dots,5\}$ | **yes** |

No non-prefix subsegment is good, since none of them contains the $1$. Total: `3`.
