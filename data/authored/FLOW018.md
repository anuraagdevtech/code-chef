---
topic: Basic Math
subtopic: Factorials within fixed-width limits
time: $O(N)$ per test case
space: $O(1)$
---
Print $N!$ for $0 \leq N \leq 20$. In Python the whole solution is `math.factorial(n)`.

The bound of $20$ is chosen deliberately. $20! = 2{,}432{,}902{,}008{,}176{,}640{,}000 \approx 2.4 \times 10^{18}$, which still fits in a signed 64-bit integer (whose ceiling is about $9.22 \times 10^{18}$) — but $21!$ is roughly $5.1 \times 10^{19}$ and overflows it. So this problem is the largest factorial a C `long long` can hold, and it is the counterpart to Small Factorials, where $N$ reaches $100$ and genuine big-number arithmetic is unavoidable.

In Python the distinction is invisible, since `int` grows as needed. The lesson is to recognise *why* a problem setter picks $20$ rather than $25$: the bound is telling you which integer type the intended solution uses.

The edge case is $N = 0$. By definition $0! = 1$, not $0$, and `math.factorial(0)` returns $1$ correctly. A hand-written loop seeded with `result = 1` also gets this right, whereas one seeded with `result = n` does not.

With $T$ up to $1000$ and $N$ capped at $20$, the inputs repeat heavily, so a precomputed table of the $21$ possible answers would avoid recomputation entirely — an easy win in a hotter loop, though unnecessary at this scale.

## Edge cases

- **$N = 0$**: $0! = 1$. The lower bound here is $0$, unlike the sibling problem where it is $1$, and `math.factorial(0)` returns $1$ without a special case — a hand-rolled `for i in range(1, n+1)` loop also gets this right only because the empty product is $1$.
- **$N = 20$**, the upper bound: $20! = 2{,}432{,}902{,}008{,}176{,}640{,}000$, which just fits in a signed 64-bit integer (limit about $9.22 \times 10^{18}$). **$21!$ would not**, and that is precisely why the bound is $20$ — the problem is calibrated so a `long long` suffices.
- **$N = 1$**: $1$.
- In Python the bound is irrelevant, since integers are arbitrary precision.

## Dry run

| $N$ | product | output |
|---:|---|---:|
| 3 | $1 \times 2 \times 3$ | `6` |
| 4 | $6 \times 4$ | `24` |
| 5 | $24 \times 5$ | `120` |
