---
topic: Constructive
subtopic: Pairing symmetrically around the mean
time: $O(N)$ per test case
space: $O(N)$
---
A mean of $X$ over $N$ elements means the total must be exactly $NX$. The clean construction builds that total out of **symmetric pairs around $X$**: the pair $(X - d,\ X + d)$ sums to $2X$ and contributes a mean of $X$ by itself.

- **$N$ even:** emit $N/2$ pairs with offsets $d = 1, 2, \ldots, N/2$.
- **$N$ odd:** emit $X$ itself, then $(N-1)/2$ such pairs.

Every value is distinct, because the offsets are distinct and positive and $X$ appears at most once.

The construction also has to respect $|A_i| \leq 1000$, which is worth checking rather than assuming. The largest offset is $\lfloor N/2 \rfloor \leq 500$, and $0 \leq X \leq 100$, so values stay within $[-500,\ 600]$ — comfortably inside the bound.

The alternative of "write $X$ many times" fails the distinctness requirement, and "fill with $0 \ldots N-1$ and patch the last element" tends to collide with an existing value or overflow the range. Pairing sidesteps both.

**Multiple answers are accepted**, so this is judged by a special checker and the output will generally differ from the sample text — the sample's `5 10 6` for $N=3, X=7$ sums to $21$, as does the `7 6 8` produced here. A verbatim diff would report a mismatch where none exists, so the repository checks this one by validating the three properties instead: correct length, all distinct, in range, and the mean exactly $X$.

$N = 1$ is the degenerate case, emitting the single value $X$.
