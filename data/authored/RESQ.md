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
