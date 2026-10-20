---
topic: Number Theory
subtopic: Trial division to the square root
time: $O(\sqrt{N})$ per test case
space: $O(1)$
---
Test whether $N$ is prime. The standard method is trial division, and the key optimisation is that divisors need only be checked up to $\sqrt{N}$.

The reason: if $N = a \cdot b$ with $a \leq b$, then $a \leq \sqrt{N}$. So any composite number must have a factor at or below its square root, and finding none there proves primality. This cuts the work from $N$ divisions to about $\sqrt{N}$ — for $N = 10^5$ that is roughly $316$ instead of $100{,}000$.

Two refinements halve it again: handle $2$ separately, then test only odd divisors $3, 5, 7, \ldots$, since no even number above $2$ can be prime.

The edge cases are where this problem is actually decided.

- **$N = 1$ is not prime**, as the statement says explicitly. It has only one divisor, and trial division finds no factor $\leq 1$, so a naive loop would wrongly report `yes`. This needs an explicit guard.
- **$N = 2$ is prime** and is the only even prime, so it must be excluded from the "reject all evens" rule.

The bound should be computed as `math.isqrt(n)` rather than `int(n ** 0.5)`, for the same reason as in the square-root problem: the float version can land just under a perfect square and drop a divisor. For $N = p^2$ with $p$ prime, that would skip the only factor and declare a composite prime.

With $T \leq 20$ and $N \leq 10^5$ this is instant. For many queries over a fixed range, a Sieve of Eratosthenes precomputing all primes up to $10^5$ once would be the better structure — which is what the problem's own tags point at.

The expected output is lowercase `yes` / `no`.
