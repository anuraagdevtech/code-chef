---
topic: Number Theory
subtopic: Only 1 and the primes above N/2 can be separated from the rest
time: $O(N \log \log N)$ sieve, then $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Build a graph on $1 \dots N$ joining two numbers when their gcd exceeds 1. Two numbers in the same connected component must go to the same side, so a valid split is a union of components.

Which components are there? The number 1 is alone. A prime $p > N/2$ has no other multiple up to $N$, so it is alone too. Everything else hangs together: a prime $p \le N/2$ is joined to $2p$ and hence to 2, and every composite is joined to its prime factors, all of which are at most $N/2$. So there is one big component and a set of isolated vertices.

One side of the split must therefore consist only of isolated vertices. If $K$ is at most the number of isolated vertices, give $K$ of them to the friend. Otherwise the friend must take the big component, and Chef's $N - K$ numbers must all be isolated; if that fits, give the friend everything except $N - K$ isolated numbers. If neither fits the answer is NO.

## Edge cases

- $N = 2$ or $3$: every number is isolated and any split works.
- Any valid set may be printed; the judge checks the gcd condition.
- The "complement" case is needed when $K$ is large.
- The sieve is built once up to the maximum $N$.

## Dry run

`N = 6`: isolated numbers are 1 and 5 (the only prime above 3).

- $K = 3$: more than 2 isolated numbers would be needed on one side, and $N - K = 3$ is also more than 2. NO.
- $K = 2$: `1 5`.
- $K = 4$: Chef keeps the two isolated numbers and the friend gets `2 3 4 6`.
