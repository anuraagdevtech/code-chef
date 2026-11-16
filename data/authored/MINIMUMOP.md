---
topic: Number Theory
subtopic: At most two operations - common gcd, an unused prime, or 2 then 3
time: $O(M_{\max} \log \log M_{\max})$ sieve, then $O(N \log A)$ per test case
space: $O(M_{\max} + N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
- All elements already equal: 0 operations.
- Otherwise let $g$ be the gcd of the array. If $g > 1$, the single operation $X = g$ turns every element into $g$.
- If $g = 1$: after one operation with $X$ all elements equal some $d$, which divides every element, so $d = 1$ and $X$ must be coprime to every element. The cheapest such $X$ is the smallest prime that divides none of the elements; if it is at most $M$, one operation suffices.
- If no such prime fits under $M$, one operation is impossible, and two always work: $X = 2$ leaves only ones and twos, and $X = 3$ then turns everything into 1.

The primes dividing the elements are collected with a smallest-prime-factor sieve built once up to $10^6$.

## Edge cases

- Equal elements need no operation, whatever their gcd.
- $X$ must lie in $[2, M]$, which is why an unused prime larger than $M$ does not help.
- When two operations are needed, $M \ge 3$ is guaranteed because the elements are not all equal.
- The number of operations is unique but the chosen $X$ values are not, so a checker validates the output.

## Dry run

- `A = [4, 8, 12, 16, 20]`: gcd 4, so one operation with $X = 4$.
- `A = [2, 3]`, `M = 3`: gcd 1; the primes 2 and 3 are both used and the next prime 5 exceeds $M$. Two operations: `2 3` - after $X = 2$ the array is `[2, 1]`, after $X = 3$ it is `[1, 1]`.
