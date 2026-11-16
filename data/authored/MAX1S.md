---
topic: Greedy
subtopic: Positional weights and a maximum-sum segment of flip gains
time: $O(N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Swap the order of summation: position $i$ lies in $i \cdot (N - i + 1)$ substrings, so a `1` there contributes exactly that weight $w_i$ to the total, and the sum is $\sum_{S_i = 1} w_i$.

Flipping a substring changes each position in it independently: a `0` gains $+w_i$, a `1` loses $w_i$. The best single flip is therefore the contiguous segment with the largest total of these signed gains - Kadane's algorithm - and since the operation is optional the gain is at least 0.

The answer is the current total plus the best gain.

## Edge cases

- All ones: no flip, the answer is $\sum w_i = N(N+1)(N+2)/6$.
- All zeros: flip everything, same answer.
- The best segment may include a few ones if the zeros around them outweigh them.
- Totals grow like $N^3$ and need big integers.

## Dry run

`S = 00100`, weights `5 8 9 8 5`.

Current total: 9 (the single one). Gains: `+5 +8 -9 +8 +5`. The best segment is the whole string, with gain 17.

Answer $9 + 17 = 26$ (the string becomes `11011`).
