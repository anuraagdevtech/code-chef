---
topic: Prefix Sums
subtopic: Net gain of removing an interval as a range sum of +1 and -1 scores
time: $O(N + C)$ per test case, $C = 10^5$
space: $O(N + C)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
First apply all $N$ operations with a difference array to get every cake's height, and count the cakes of height exactly $K$.

Removing one operation lowers the heights on its interval by 1 and changes nothing else. Inside the interval a cake of height $K + 1$ becomes a cake of height $K$ (gain 1) and a cake of height $K$ stops being one (loss 1). So give every cake the score $+1$ if its height is $K + 1$, $-1$ if it is $K$, and 0 otherwise; the net change for an operation is the sum of scores over $[L, R]$, an $O(1)$ prefix-sum query.

The answer is the base count plus the best net change over the $N$ operations.

## Edge cases

- Exactly one operation must be removed, even if every removal makes things worse.
- Several identical intervals are all candidates but give the same result.
- The cake indices go up to 100000 regardless of $N$.
- The best net change can be negative.

## Dry run

`K = 2`, operations `[2,6] [4,9] [1,4]`.

Heights of cakes 1-9: `1 2 2 3 2 2 1 1 1`; four cakes have height 2. Scores: `0 -1 -1 +1 -1 -1 0 0 0`.

- remove `[2,6]`: $-1 - 1 + 1 - 1 - 1 = -3$, leaving 1
- remove `[4,9]`: $+1 - 1 - 1 = -1$, leaving 3
- remove `[1,4]`: $-1 - 1 + 1 = -1$, leaving 3

Answer 3.
