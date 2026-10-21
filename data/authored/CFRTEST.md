---
topic: Sets
subtopic: Distinct values as a capacity bound
time: $O(n)$ per test case
space: $O(n)$
---
Devu can host one party per day, with one guest each. Friend $i$ is satisfied only by a party on day $d_i$. So two friends demanding the **same** day are in direct conflict — only one of them can be saved.

Conversely, friends demanding different days never conflict, since each day hosts its own party. So the maximum number of friendships saved is exactly the number of **distinct** days requested:

$$\bigl|\{d_1, \ldots, d_n\}\bigr|$$

The bound holds in both directions: at most one friend per day can be satisfied, and choosing exactly one friend from each distinct day achieves it. There is nothing to optimise beyond counting.

What makes this easy is that the days are **fixed demands**, not a schedule to arrange. Each friend accepts precisely one day, so there is no matching problem — had friends accepted ranges of days, this would become bipartite matching and be far harder.

Sample case 1 has days $\{3, 2\}$, two distinct, so both friendships survive. Sample case 2 has both friends demanding day $1$, so only one can be saved.

A Python `set` gives the count in one pass. With $d_i \leq 100$ a boolean array of size $101$ would be marginally faster, which matters a little at $T = 10^4$, but $n \leq 50$ keeps the total work small either way.

## Edge cases

- **Everyone wants the same day** ($1, 1$): only one party can happen, so the answer is $1$ rather than $n$.
- **All days distinct** ($3, 2$): every friend is satisfied, so the answer is $n$.
- **One party per day** is the whole constraint: friends sharing a day compete for it and only one can be served, which is why the answer is the number of *distinct* days.
- **$n = 1$**: one friend, one party.
- The $d_i$ are bounded by $100$ while $n \leq 50$, so the distinct count can never be capped by the day range.

## Dry run

| days requested | distinct | output |
|---|---:|---|
| $3, 2$ | $\{2, 3\}$ | `2` |
| $1, 1$ | $\{1\}$ | `1` |
