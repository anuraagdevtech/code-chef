---
topic: Combinatorics
subtopic: Choosing among the tied boundary value
time: $O(N \log N)$ per test case
space: $O(N)$
---
The minimum sum is obtained by taking the $K$ smallest elements, so sort and look at where the cut falls. Let $v = A_{(K)}$ be the $K$-th smallest value. Everything strictly below $v$ is **forced** into the subsequence, and everything strictly above is forced out — swapping either way would change the sum.

The only freedom is among the copies of $v$ itself. If $v$ occurs $c$ times in the whole array and $u$ of them lie in the first $K$ sorted positions, then any $u$ of the $c$ copies may be chosen, and the sum is the same:

$$\text{answer} = \binom{c}{u}$$

Subsequences are indexed by position, so two choices of copies are different subsequences even though they produce the same multiset of values — which is exactly what the problem counts.

The sample has $A = [1,2,3,4]$ with $K = 2$. The cut value is $2$, which occurs once and is used once, giving $\binom{1}{1} = 1$: the subsequence $\{1,2\}$ is the unique minimiser.

The count only becomes interesting with ties. For $A = [1,2,2,2]$ with $K = 2$ the cut value $2$ occurs three times and one is used, giving $\binom{3}{1} = 3$. And for $A = [5,5,5]$ with $K = 2$ it is $\binom{3}{2} = 3$.

With $N \leq 50$ the binomial fits easily in Python's unbounded integers; $\binom{50}{25} \approx 1.3 \times 10^{14}$ needs 64-bit arithmetic in C++.

## Edge cases

- **The minimum sum is forced** — it takes the $K$ smallest values — so the only freedom is *which* copies of the boundary value are chosen.
- **Only the tied boundary value is interchangeable.** Values strictly below the cut must all be taken, and values strictly above can never be, so the count is $\binom{\text{total copies of the cut}}{\text{copies used}}$.
- **All values distinct** (the sample) → exactly one interesting subsequence, since $\binom{1}{1} = 1$.
- **All values equal** → the answer is $\binom{N}{K}$, with the cut value being the only value there is.
- **$K = N$** → one subsequence, the whole array, which the formula gives as $\binom{c}{c} = 1$.
- **Subsequences are counted by index set, not by value**, which is exactly why identical values at different positions count separately.
- **$N \leq 50$**, so the binomial fits comfortably and `math.comb` needs no modular arithmetic.

## Dry run

Take $A = 1, 2, 2, 2, 5$ with $K = 3$, sorted as shown.

| step | value |
|---|---|
| the $K$ smallest | $1, 2, 2$ |
| boundary value (the $K$-th) | 2 |
| copies of $2$ in the whole array | 3 |
| copies of $2$ among the first $K$ | 2 |
| count | $\binom{3}{2} = 3$ |

The sample's own case, $1,2,3,4$ with $K = 2$, has a unique boundary copy and so answers `1`.
