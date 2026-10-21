---
topic: Number Theory
subtopic: Divisor nearest the square root
time: $O(\sqrt{N})$ per test case
space: $O(1)$
---
A rectangular arrangement of $N$ cupcakes is a factorisation $N = \ell \times w$, and the difference $|\ell - w|$ shrinks as the factors move toward each other. Writing $\ell = N/d$ and $w = d$ with $d \leq \sqrt{N}$, the gap

$$\frac{N}{d} - d$$

is **strictly decreasing in $d$** on $(0, \sqrt{N}]$, since both terms move the right way. So the best arrangement comes from the **largest divisor of $N$ that is at most $\sqrt{N}$** — no comparison of candidates is needed, just the last one found.

Scanning $d$ from $1$ to $\lfloor \sqrt{N} \rfloor$ and keeping the largest divisor costs $O(\sqrt{N}) = 10^4$ steps, which with $T \leq 100$ is trivial. The divisor $1$ always qualifies, so the scan never comes up empty.

The samples cover the extremes. $N = 4$ is a perfect square, so $d = 2$ gives $0$ — the only way to hit zero. $N = 13$ is prime, so the only option is $1 \times 13$, giving $12$; primes are always the worst case. $N = 20$ gives $d = 4$ and $5 - 4 = 1$, and $N = 8$ gives $d = 2$ and $4 - 2 = 2$ — note $8$'s divisors skip over $\sqrt 8 \approx 2.83$, which is why the answer is not smaller.

Use integer arithmetic for the loop bound: `isqrt(n)` rather than `int(n ** 0.5)`, which can be off by one near a perfect square and would silently miss the $0$ answer.

## Edge cases

- **A perfect square** ($N = 4$) gives $0$, and that is the only way to reach $0$ — rows and columns are equal.
- **A prime** ($N = 13$) forces the $1 \times N$ arrangement and the worst possible answer, $N - 1$.
- **$N = 1$**: $\mathrm{isqrt}(1) = 1$, the divisor $1$ is found, and the answer is $1 - 1 = 0$.
- **$N/d - d$ decreases as $d$ rises** over $(0, \sqrt{N}]$, so the *largest* divisor not exceeding $\sqrt{N}$ is optimal; searching from the other side gives the same pair, since each divisor below the root has exactly one partner above it.
- **`isqrt` must be exact.** `int(math.sqrt(n))` can come out one too small on a large perfect square, and at $N = 10^8$ that would miss the divisor $10^4$ and report $10^4 - 1$ instead of $0$.
- **$N$ up to $10^8$** means $10^4$ trial divisions per case and $10^6$ across the file — fine, but a full factorisation would not be.

## Dry run

| $N$ | $\mathrm{isqrt}(N)$ | divisors $\leq$ root | best $d$ | $N/d$ | output |
|---:|---:|---|---:|---:|---:|
| 20 | 4 | $1, 2, 4$ | 4 | 5 | `1` |
| 13 | 3 | $1$ | 1 | 13 | `12` |
| 8 | 2 | $1, 2$ | 2 | 4 | `2` |
| 4 | 2 | $1, 2$ | 2 | 2 | `0` |
