---
topic: Probability
subtopic: Expectation recurrence over remainders, summed by quotient blocks
time: $O(N \sqrt{N})$
space: $O(N \log N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $E(x)$ be the expected number of operations from value $x$. For $x < n$, a divisor $r > x$ leaves $x$ unchanged, so

$$E(x) = 1 + \frac{1}{n}\Bigl(\sum_{r \le x} E(x \bmod r) + (n - x) E(x)\Bigr) \;\Longrightarrow\; x \cdot E(x) = n + \sum_{r \le x} E(x \bmod r).$$

With $D(x) = E(x) / n$ this becomes $D(x) = \bigl(1 + \sum_{r \le x} D(x \bmod r)\bigr) / x$, which no longer depends on $n$. If $m < n$ the answer is $n \cdot D(m)$. If $m \ge n$ every divisor is at most $m$, so the answer is $1 + \sum_{r=1}^{n} D(m \bmod r)$, and only values below $n$ are ever needed.

Computing the inner sum naively is quadratic. Split the divisors at $\sqrt{x}$: small ones are added directly; large ones are grouped by the quotient $q = \lfloor x / r \rfloor$, and within a group the remainders $x - q r$ form an arithmetic progression with step $q$. Keeping, for each small $q$, prefix sums of $D$ along step $q$ turns every group into one or two lookups. A progression for quotient $q$ only ever needs indices up to $\text{limit} / (q + 1)$, which keeps the tables at $O(N \log N)$ cells.

## Edge cases

- $r = 1$ always ends the process; $D(0) = 0$.
- $m$ can be as large as $10^{18}$, but only $m \bmod r$ for $r \le n$ is used.
- When $m < n$ only values up to $m$ are computed.
- Results are fractions modulo $10^9 + 7$; inverses of $1 \dots$ limit are precomputed linearly.

## Dry run

`n = 3, m = 2`. Since $m < n$ the answer is $3 \cdot D(2)$.

$D(1) = (1 + D(0)) / 1 = 1$. $D(2) = (1 + D(2 \bmod 1) + D(2 \bmod 2)) / 2 = 1/2$.

Answer $3/2$, printed as $3 \cdot 2^{-1} \bmod (10^9 + 7) = 500000005$. Check: each operation stops with probability $2/3$, so the expectation is $3/2$.
