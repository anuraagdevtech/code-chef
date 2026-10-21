---
topic: Number Theory
subtopic: Segmented sieve plus prime-power exponents
time: $O(\sqrt{R} \log\log \sqrt{R} + (R-L))$ per test case
space: $O(\sqrt{R} + (R-L))$
---
Start by characterising the special numbers. If $n = p_1^{e_1} \cdots p_r^{e_r}$ then

$$d(n) = \prod_{i=1}^{r} (e_i + 1)$$

For that product to be **prime** it must have exactly one factor above $1$, so $r = 1$: the special numbers are precisely the prime powers $p^e$ with $e + 1$ prime. ($n = 1$ has $d = 1$, which is not prime.)

That splits the count into cases by exponent, and the cases are wildly uneven:

- **$e = 1$** — the primes themselves, $d = 2$. These are dense in $[L, R]$ and need a **segmented sieve**: sieve base primes up to $\sqrt{R} = 10^6$, then mark their multiples inside the window of size at most $10^6$. Starting each prime's marking at $\max(p^2, \text{first multiple} \geq L)$ keeps a base prime that lies in the window from crossing itself off.
- **$e = 2$** — squares of primes, $d = 3$. Count primes in $[\lceil\sqrt{L}\rceil, \lfloor\sqrt{R}\rfloor]$ by binary-searching the base prime list; no second sieve needed.
- **$e \geq 4$** — handfuls. Since $2^{40} > 10^{12}$, only $e \in \{4, 6, 10, 12, 16, 18, 22, 28, 30, 36\}$ can occur (each $e+1$ prime), and for $e = 4$ already $p \leq 1000$. Enumerate directly and test the window.

Note the exponents are not $1, 2, 3, \ldots$: $e = 3$ is excluded because $d = 4$ is composite, so cubes of primes are *not* special — an easy case to include by mistake.

Use `isqrt` for the $e = 2$ bounds; floating-point square roots are off by one near perfect squares at $10^{12}$ and would miscount the endpoints.

For $[1, 10]$ the primes $2, 3, 5, 7$ give four, and the prime squares $4$ and $9$ give two more, totalling $6$. Note $8 = 2^3$ has four divisors and is correctly skipped.
