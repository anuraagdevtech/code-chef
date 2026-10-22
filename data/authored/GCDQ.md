---
topic: Prefix Sums
subtopic: Prefix and suffix GCD arrays
time: $O(N \log A + Q \log A)$ per test case
space: $O(N)$
---
Excluding a contiguous block $[L,R]$ leaves a **prefix and a suffix**, so the answer is the GCD of two precomputable aggregates. GCD is associative and commutative, which is all a prefix-aggregate needs:

$$\mathrm{pre}[i] = \gcd(A_1, \ldots, A_i), \qquad \mathrm{suf}[i] = \gcd(A_i, \ldots, A_N)$$

and the query answer is $\gcd(\mathrm{pre}[L-1], \mathrm{suf}[R+1])$.

The boundaries need care rather than branches: define $\mathrm{pre}[0] = \mathrm{suf}[N+1] = 0$ and use $\gcd(0, x) = x$. That identity makes $0$ the neutral element for GCD, so a query that removes a true prefix or suffix falls out of the same expression — no special cases. The problem guarantees something survives, so both aggregates are never $0$ at once.

Both arrays build in one pass each, after which every query is a single `gcd` call. The alternative, a sparse table or segment tree, is unnecessary here: the excluded part being contiguous means the *kept* part is always exactly two end-anchored pieces.

With $A = [2, 6, 9]$: $\mathrm{pre} = [0, 2, 2, 1]$ and $\mathrm{suf} = [1, 3, 9, 0]$. Removing $[1,1]$ gives $\gcd(0, 3) = 3$; removing $[2,2]$ gives $\gcd(2, 9) = 1$; removing $[2,3]$ gives $\gcd(2, 0) = 2$ — the last two showing both boundary forms.

The statement's I/O warning is real with $\sum N$ up to $10^6$: read the whole stream at once and join the output.

## Edge cases

- **$\gcd(0, x) = x$ makes $0$ the identity**, so the prefix and suffix arrays can start from $0$ and the boundary cases need no special handling: excluding a prefix leaves `pre[0] = 0` to combine with the suffix.
- **Excluding a range needs both sides**, so one prefix array is not enough — the answer is $\gcd$ of the part before $L$ and the part after $R$.
- **The suffix array is indexed one past the end**, with `suf[n+1] = 0`, so a query ending at $N$ reads a clean identity rather than an out-of-range slot.
- **The remaining array is guaranteed non-empty**, so at least one of the two sides contributes a real value and the answer is never the identity $0$.
- **Excluding a single element** (the first two queries) is the common case, and it still needs both arrays.
- **$A_i \leq 10^5$** keeps the gcds small, but the sum of $N$ reaching $10^6$ makes buffered reading essential — the statement says so explicitly.
- **The queries are 1-based**, which is why the lookups are `pre[l-1]` and `suf[r+1]`.

## Dry run

Sample: $A = 2, 6, 9$.

| array | values |
|---|---|
| prefix gcds `pre[0..3]` | $0, 2, 2, 1$ |
| suffix gcds `suf[1..4]` | $1, 3, 9, 0$ |

| query | excluded | $\gcd(\text{pre}[L-1], \text{suf}[R+1])$ | output |
|---|---|---|---:|
| $1\ 1$ | $A_1$ | $\gcd(0, 3) = 3$ | `3` |
| $2\ 2$ | $A_2$ | $\gcd(2, 9) = 1$ | `1` |
| $2\ 3$ | $A_2, A_3$ | $\gcd(2, 0) = 2$ | `2` |
