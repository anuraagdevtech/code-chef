---
topic: Greedy
subtopic: Exchange the largest for the smallest
time: $O(N \log N)$ per test case
space: $O(N)$
---
Play proceeds strictly left to right, so Motu takes the even-indexed elements and Tomu the odd ones — the positions are fixed, and only *which values sit in them* can change.

A swap moves one value out of Motu's set and one into it. The useful kind trades one of **Motu's largest** for one of **Tomu's smallest**: if Motu holds $m$ and Tomu holds $u$ with $m > u$, swapping shifts the score gap by $2(m - u)$ in Tomu's favour — he gains $m - u$ and Motu loses the same.

So sort Motu's values descending and Tomu's ascending, then pair them off: the first swap trades Motu's biggest for Tomu's smallest, the second his next biggest for her next smallest, and so on for up to $K$ swaps. Stop early once $m \leq u$, because from there every remaining trade would shrink the gap rather than widen it.

The greedy is optimal because the swaps are independent — each takes one element from each side — and the gains $2(m_i - u_i)$ are sorted descending by construction, so taking the $K$ largest gains is best possible.

Swapping within one player's own set is pointless, since it changes neither total.

Sample case 1 has $K = 0$ and equal totals of $3$; Tomu needs **strictly** greater, so a tie is a loss — `NO`. Sample case 2 trades Motu's $6$ for Tomu's $3$, turning $12$–$7$ into $9$–$10$.

## Edge cases

- **Motu plays the odd-numbered rounds**, which is `a[0::2]` in 0-based indexing; getting the parity backwards exchanges the two sums and flips both sample answers.
- **$K = 0$** (the first row): no trades, so the raw sums decide — and they tie, which answers `NO`.
- **A strict win is required.** The first row's $3$ against $3$ is not enough for Tomu.
- **A useless trade must be refused.** The loop breaks once Motu's $i$-th largest is no greater than Tomu's $i$-th smallest, since swapping equal or already-favourable values cannot raise Tomu's total — forcing all $K$ trades can actively hurt.
- **Odd $N$ gives Motu one extra round**, so the trade count is bounded by `min(k, len(motu), len(tomu))`; the second row has three against two.
- **Each trade moves twice the difference between the totals**, which is why both sums are updated rather than just one.

## Dry run

Second sample: $A = 2, 4, 6, 3, 4$ with $K = 1$.

| | values | sorted for trading | sum |
|---|---|---|---:|
| Motu (rounds 1,3,5) | $2, 6, 4$ | $6, 4, 2$ descending | 12 |
| Tomu (rounds 2,4) | $4, 3$ | $3, 4$ ascending | 7 |

One trade swaps Motu's $6$ for Tomu's $3$:

| | before | after |
|---|---:|---:|
| Motu | 12 | 9 |
| Tomu | 7 | **10** |

$10 > 9$, so `YES`.
