---
topic: Arrays
subtopic: Best gain against a running minimum
time: $O(N)$ per test case
space: $O(1)$
---
This is the classic "best buy/sell" scan. Walk the matches in chronological order holding the **smallest score seen so far**; at each match, the best improvement ending here is the current score minus that running minimum. Keep the largest such value.

$$\text{answer} = \max_{j} \left( g_j - \min_{i < j} g_i \right)$$

One pass, $O(N)$ time and $O(1)$ space. The quadratic version — comparing every pair — is $10^{10}$ operations at $N = 10^5$ and is exactly what the problem's warning about large input is hinting against.

The chronological constraint is what makes the running minimum the right structure: the earlier match must come first, so a low score *after* a high one cannot be used. Sample case 2, a strictly decreasing $[5,4,3,2,1]$, has no valid pair at all and prints `UNFIT`.

That `UNFIT` case needs care. The improvement must be **strictly positive** — equal scores do not count as improvement — so the running best should start at $0$ and the answer printed only if it exceeds $0$. Sample case 3, $[4,3,2,2,3]$, contains the equal pair $(2,2)$ worth $0$ and the genuine pair $(2,3)$ worth $1$, answering $1$.

Updating the running minimum **after** computing the candidate is what keeps $i < j$ strict; updating first would allow a match to be compared against itself, yielding a spurious $0$ — harmless here, but the wrong habit.

Sample case 1 picks up $7 - 3 = 4$ early and never beats it, even though the array dips to $1$ later.

## Edge cases

- **The comparison must come before the minimum is updated**, so the earlier match is strictly earlier. Updating first would let a match pair with itself and record a gain of $0$.
- **A gain of exactly $0$ is not fit.** The third row has two consecutive $2$s, and that pairing is rejected; only a strictly positive improvement counts, which the `best = 0` start plus `> best` enforces.
- **Non-increasing goal counts** (the second row) → `UNFIT`.
- **The best pair need not involve the global minimum or maximum.** The first row's answer pairs the opening $3$ with the $7$ right after it, both of which precede the global minimum of $1$ — so tracking only the overall extremes gives the wrong pair.
- **$g_i$ may be $0$**, which is an ordinary value and a legitimate running minimum.
- **$N = 1$**: the loop never runs, so `UNFIT` is printed.

## Dry run

First sample: goals $3, 7, 1, 4, 2, 4$.

| match | goals | running min before | gain | best |
|---:|---:|---:|---:|---:|
| 2 | 7 | 3 | 4 | **4** |
| 3 | 1 | 3 | $-2$ | 4 |
| 4 | 4 | 1 | 3 | 4 |
| 5 | 2 | 1 | 1 | 4 |
| 6 | 4 | 1 | 3 | 4 |

Output `4`, from the first two matches.
