---
topic: Basic Math
subtopic: Exact integer square root
time: $O(1)$ per test case in practice
space: $O(1)$
---
The task is $\lfloor \sqrt{N} \rfloor$. The obvious `int(math.sqrt(n))` passes here, but it is the wrong habit and the reason is worth understanding.

`math.sqrt` returns a 64-bit float. For a perfect square the true root is representable exactly, but the computed result can land a hair below it — so `math.sqrt(x*x)` may evaluate to something like $k - 10^{-9}$, and truncating yields $k - 1$. The failure only appears for large $N$, which makes it a nasty bug: it passes every small test and breaks in the one case the problem cares about.

`math.isqrt`, added in Python 3.8, is the correct tool. It works entirely in integers and is *defined* to return the exact floor of the square root for any non-negative `int`, with no floating point anywhere. It is also the only version that stays correct once $N$ exceeds $2^{53}$, where floats can no longer represent consecutive integers.

With $N \leq 10^4$ here neither approach can actually fail, so this problem is really a vocabulary lesson: reach for `isqrt` whenever an integer square root is wanted.

Sample case 3 is the perfect square $10000 \to 100$, exactly the shape that would expose a float rounding error at larger magnitudes.

## Edge cases

- **$N = 1$** (the smallest input): $\lfloor\sqrt1\rfloor = 1$.
- **$N$ a perfect square**, as in the sample's $10000$. This is the case that breaks `int(math.sqrt(n))`: the float root may land a hair below the exact integer and truncate to $99$ instead of $100$. `isqrt` is defined to be exact, so it cannot.
- **$N$ one below a perfect square** ($9999 \to 99$) and one above ($10001$, outside these bounds but $\to 100$) — the answer must not jump early.
- **$N = 2, 3$**: the root lies strictly between $1$ and $2$, so the answer floors to $1$ rather than rounding to $2$.

## Dry run

Sample input: three values, each handled independently.

| $N$ | largest $k$ with $k^2 \leq N$ | why | output |
|---:|---:|---|---:|
| $10$ | $3$ | $3^2 = 9 \leq 10 < 16 = 4^2$ | `3` |
| $5$ | $2$ | $2^2 = 4 \leq 5 < 9 = 3^2$ | `2` |
| $10000$ | $100$ | $100^2 = 10000$ exactly | `100` |

Printed as `3`, `2`, `100`.
