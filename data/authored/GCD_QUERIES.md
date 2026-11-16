---
topic: Number Theory
subtopic: One min-heap of sorted indices per prime, with lazy deletion
time: $O(V \log \log V + (N + Q) \log V \log N)$
space: $O(V + N \log V)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
$\gcd(X, k) > 1$ exactly when $X$ and $k$ share a prime factor. Sort the array; then "the minimum element" means "the smallest sorted index", and ties between equal values do not matter.

For every prime $p$ keep a list of the sorted indices of the elements divisible by $p$. Indices are appended in increasing order, so each list is already a valid min-heap. A smallest-prime-factor sieve up to $10^6$ factorises any number into its distinct primes in $O(\log V)$.

For a query $X$, look at the heap of each prime factor of $X$: discard removed indices from its top, and take the smallest live top over all those heaps. If none of the heaps has a live element, fall back to the globally smallest live index, found with a pointer that only moves forward. Mark the chosen index as removed and print its value.

An element sits in several heaps; it is removed physically from each only when it reaches the top, so every heap entry is popped at most once.

## Edge cases

- $X = 1$ has no prime factors and always takes the global minimum.
- Elements equal to 1 are in no heap and can only be removed by the fallback.
- $Q \le N$, so the array never runs out.
- The sieve is shared by all test cases.

## Dry run

`A = [2, 9, 3, 15, 10]`, sorted `2 3 9 10 15`. Heaps: prime 2 -> `{2, 10}`, prime 3 -> `{3, 9, 15}`, prime 5 -> `{10, 15}`.

- `X = 2`: heap of 2 gives 2. Remove it.
- `X = 2`: heap of 2 now gives 10. Remove it.
- `X = 3`: heap of 3 gives 3.
- `X = 7`: no heap for 7, so the global minimum 9.

Output `2 10 3 9`.
