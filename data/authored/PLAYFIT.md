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
