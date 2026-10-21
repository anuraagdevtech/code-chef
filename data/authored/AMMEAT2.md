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
