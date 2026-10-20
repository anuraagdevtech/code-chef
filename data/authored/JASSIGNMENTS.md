---
topic: Basic Math
subtopic: Conditional arithmetic
time: $O(1)$ per test case
space: $O(1)$
---
Janmansh starts at $X$ pm and each of the $3$ assignments costs exactly one hour, so he finishes at hour $X + 3$. He is on time when that finishing moment is no later than the $10$ pm deadline:

$$X + 3 \leq 10 \quad\Longleftrightarrow\quad X \leq 7$$

So the whole problem collapses to a single comparison. The constraint $1 \le X \le 9$ keeps everything inside one afternoon, so there is no wrap-around past midnight to worry about and no need to convert to a 24-hour clock.

The boundary is the only place to slip. At $X = 7$ he finishes exactly at $10$ pm, and "before 10 pm" in the sense used here is satisfied — the sample confirms it, since $X = 7$ answers `Yes` while $X = 9$ (finishing at midnight) answers `No`. That makes the comparison `<=`, not `<`.
