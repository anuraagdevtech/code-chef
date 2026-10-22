---
topic: Number Theory
subtopic: Stripping shared factors with repeated GCDs
time: $O(\log^2 \max(A,B))$ per test case
space: $O(1)$
---
At $10^{18}$ there is no factorising $B$ outright, so work with GCDs instead. The idea: repeatedly divide out of $B$ everything it shares with $A$, and see whether anything survives.

$$g \leftarrow \gcd(A, B), \qquad \text{then divide } B \text{ by } g \text{ while it divides}$$

Each round removes from $B$ all the prime powers whose primes also divide $A$, at least partly; repeating until $B$ stops shrinking removes them completely, because every prime of $g$ divides $A$ and is stripped from $B$ to its full multiplicity.

Two terminating conditions:

- $B$ reaches $1$ — every prime of the original $B$ divided $A$, so print `Yes`.
- $g$ becomes $1$ while $B > 1$ — the remaining $B$ is coprime to $A$, so its primes are **not** in $A$, and the answer is `No`.

Note that multiplicity does not matter: the question is about *which* primes divide $B$, not how often. That is why $A = 128 = 2^7$ passes for $B = 16 = 2^4$ and would equally pass for $B = 2^{60}$.

The loop runs $O(\log B)$ times, since each outer round at least halves $B$ when it shrinks at all.

The samples cover the three behaviours. $A = 120, B = 75$: $\gcd = 15$ strips the $3$ and one $5$, leaving $B = 5$; a second round strips that too, so `Yes`. $A = 128, B = 16$: one round clears $B$ entirely. And $A = 7, B = 8$: the first GCD is already $1$ with $B > 1$, so `No`.

## Edge cases

- **Repeated gcd stripping avoids factorising at all.** Each round removes from $B$ every prime it shares with $A$, to full multiplicity — and with $A, B$ up to $10^{18}$, trial division would be hopeless.
- **The inner loop must divide to exhaustion**, not once: $B = 128$ against $A = 16$ has $\gcd = 16$, and $128$ needs dividing twice before that prime is gone.
- **A gcd of $1$ means the remainder is coprime to $A$**, so whatever is left carries a prime that $A$ lacks — the loop breaks and the answer is `No`.
- **$B$ reaching $1$ means every prime was shared** → `Yes`.
- **$B = 1$ initially** has no prime divisors, so the condition holds vacuously and the loop never runs.
- **$A = 1$** shares no prime with anything, so the answer is `No` for every $B > 1$.
- **Termination is guaranteed**, since each outer round divides $B$ by a gcd of at least $2$ — giving $O(\log^2)$ overall.

## Dry run

Second sample: $A = 128$, $B = 16$.

| round | $B$ | $\gcd(128, B)$ | after stripping |
|---:|---:|---:|---:|
| 1 | 16 | 16 | $16 / 16 = 1$ |

$B$ reaches $1$, so `Yes`. The third sample, $A = 7$ with $B = 8$, has $\gcd(7, 8) = 1$ immediately, leaving $B = 8 > 1$ → `No`.
