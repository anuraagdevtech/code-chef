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

## Edge cases

- **The chain survives a month boundary only from an even-length month.** From an odd-length month, stepping by two off the last correct day lands on the wrong parity: a $31$-day month's odd chain ends at $31$, and $+2$ gives day $2$ of the next month, which is even. That single observation is the whole problem.
- **An even-length month preserves parity either way**: the odd chain ends at $\ell-1$ and continues at day $1$; the even chain ends at $\ell$ and continues at day $2$.
- **February is the interesting month**: $28$ days is even and the chain continues, while a leap year's $29$ is odd and it breaks.
- **Leap years need the full rule** — divisible by $4$, except centuries unless divisible by $400$ — since the range $1900$–$2038$ includes $1900$ (not a leap year) and $2000$ (one).
- **Starting on the last day of an odd month** gives exactly one pill, which is the sample: $31$ March yields $1$.
- **The count within a month is $(\ell - d)/2 + 1$**, which handles both parities with the same expression.
- **The year may roll over**, so December is followed by January of the next year — and December has $31$ days, so the chain always breaks there anyway.

## Dry run

Starting $2019{:}03{:}31$ — day $31$, odd parity, in a $31$-day month.

| month | length | days taken | count | boundary survives? |
|---|---:|---|---:|---|
| March 2019 | 31 | $31$ | 1 | **no** ($31$ is odd) |

Output `1`. Had the start been $2019{:}04{:}2$, April's $30$ days would give $15$ pills and the chain would carry into May.
