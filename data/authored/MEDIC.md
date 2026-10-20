---
topic: Simulation
subtopic: Where a parity rule breaks at month boundaries
time: $O(1)$ per test case
space: $O(1)$
---
The doctor wants a pill every **two days**; the patient instead takes one on every date whose day-of-month has the same parity as the start. Inside a month those agree perfectly — $d, d+2, d+4, \ldots$ are both alternate days and same-parity dates. The rules can only diverge at a **month boundary**.

So the question is when the crossing preserves the two-day spacing. Let $\ell$ be the length of the month just ending.

- **Odd start parity.** The last qualifying date is $\ell$ if $\ell$ is odd, else $\ell - 1$. The next is day $1$ of the following month. The gap is $1$ when $\ell$ is odd and $2$ when $\ell$ is even.
- **Even start parity.** The last qualifying date is $\ell$ if $\ell$ is even, else $\ell - 1$, and the next is day $2$. The gap is $2$ when $\ell$ is even and $3$ when $\ell$ is odd.

Both cases give the same rule: **the sequence survives a month boundary exactly when that month has an even number of days.** Parity of the start date does not matter at all.

Even-length months are April, June, September, November (all $30$) and February in a common year ($28$); every $31$-day month and a leap February break the chain. Since no two even-length months are adjacent, the run spans at most two months — but the code loops anyway rather than relying on that.

Counting within a month from day $d$ is $\lfloor (\ell - d)/2 \rfloor + 1$, and the next month restarts at day $1$ or $2$ according to the parity.

The sample, `2019:03:31`, starts on an odd date in a $31$-day month: one pill on March 31, then the chain breaks, since the patient would take the next on April 1 — a single day later. The answer is $1$.

Leap years follow the usual rule, so February can be either parity depending on the year.
