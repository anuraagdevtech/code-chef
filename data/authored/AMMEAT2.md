---
topic: Number Theory
subtopic: A shared prime factor guarantees non-coprimality
time: $O(K)$ per test case
space: $O(K)$
---
The requirement is that **every pair** of chosen plates share a common factor above $1$. The simplest way to guarantee that is to give them all the same prime factor — and $2$ is the best choice, because the multiples of $2$ are the most numerous in $1 \ldots N$.

So take $2, 4, 6, \ldots, 2K$, which works whenever $2K \leq N$, i.e.

$$K \leq \left\lfloor \frac{N}{2} \right\rfloor$$

That bound is also the limit. The even numbers form a **maximal** set: no odd number can join, since it would have to share a factor with every even number present, including the largest power of two — and only an even number does that. And no larger pairwise-non-coprime set exists in $1 \ldots N$.

$K = 1$ is a genuine exception and needs its own branch. With a single plate there are no pairs at all, so the condition holds vacuously and any plate works — even when $\lfloor N/2 \rfloor = 0$, as happens for $N = 1$. Falling through to the general rule would wrongly print $-1$ there.

Sample case 2 asks for all $100$ plates from $1 \ldots 100$, far beyond the $50$ evens, so $-1$. Sample case 1 asks for $3$ and publishes `45 63 35` — an odd triple whose pairwise gcds are $9$, $5$ and $7$, with **no common factor at all**. That is a perfectly valid alternative, which is why this is judged by a checker rather than by text comparison; the construction here simply prints `2 4 6`.

## Edge cases

- **All-even indices always work**, since any two share the factor $2$ and are therefore never coprime — so the construction needs no search.
- **$2K \leq N$ is exactly the feasibility bound.** The even numbers form the largest pairwise non-coprime set in $[1, N]$, of size $\lfloor N/2 \rfloor$, so $K$ beyond that is impossible.
- **$K = 1$ needs its own branch.** There are no pairs to check, so any single plate works — including plate $1$, which the even construction would never reach and which $2K \leq N$ might reject for small $N$.
- **Plate $1$ is unusable for $K \geq 2$**, because $\gcd(1, j) = 1$ for every $j$.
- **$K = N$** (the second row, $N = K = 100$) is impossible for $N \geq 2$, since half the plates are odd.
- **This answer differs from the sample's** (`2 4 6` against `45 63 35`); the statement asks for one of the possible choices, so a special judge verifies the pairwise gcds.
- **$N \leq 777$** keeps the output small, and the plates may be printed in any order.

## Dry run

First sample: $N = 100$, $K = 3$, and $2K = 6 \leq 100$.

| chosen plates | pairwise gcds |
|---|---|
| $2, 4, 6$ | $\gcd(2,4) = 2$, $\gcd(2,6) = 2$, $\gcd(4,6) = 2$ |

None is $1$, so the choice is valid. Output `2 4 6`.
