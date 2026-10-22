---
topic: Greedy
subtopic: Earliest cut maximises the number of GCD-$G$ pieces
time: $O(N \log A)$ per test case
space: $O(1)$
---
$G$ divides every element, so the GCD of **any** subarray is a multiple of $G$ and hence at least $G$. An average of values each $\geq G$ equals $G$ only if they are *all* exactly $G$. So the arithmetic-mean condition is not an averaging problem at all — it demands

$$g_1 = g_2 = \cdots = g_K = G$$

and the question becomes: can we find $K$ disjoint subarrays each with GCD exactly $G$? Equivalently, is the maximum number of such disjoint subarrays at least $K$?

That maximum comes from a greedy sweep: run a running GCD from left to right and **cut as soon as it reaches $G$**, then reset. Cutting at the earliest possible point is optimal because a GCD only shrinks as a subarray grows, so any solution's first piece can be shortened to the greedy's first piece without affecting the rest — the classic exchange argument for interval packing.

Leftover elements at the end are simply discarded; the subarrays need not cover the array.

The samples separate the two outcomes. $[1,2,3,4,5]$ has $G = 1$ and the greedy cuts at $[1]$, $[2,3]$, $[4,5]$ — three pieces, enough for $K = 3$. But $[2,2,3,3,2,2]$ also has $G = 1$ and yields only two pieces, $[2,2,3]$ and $[3,2]$, falling short of $K = 4$: the twos cannot reach GCD $1$ on their own.

The last sample shows the same with a larger $G$: $[6,12,18,24]$ has $G = 6$, and only $[6]$ and $[12,18]$ qualify before the trailing $24$ is stranded, so $K = 3$ is impossible.

## Edge cases

- **Every subarray's gcd is a multiple of $G$**, so each $g_i \geq G$ — and an average of exactly $G$ therefore forces *every* chosen subarray to have gcd exactly $G$. The averaging condition is a disguise for a counting one.
- **So the question is "are there $K$ disjoint subarrays with gcd $G$"**, answered by cutting as early as possible: the moment the running gcd reaches $G$, close the piece and reset.
- **The earliest cut is optimal**, since a longer piece can only use up elements that a later piece might have needed — the standard exchange argument.
- **A single element equal to $G$ closes a piece immediately** (the third row's leading $1$, where $G = 1$).
- **Resetting to $0$ rather than to the next element** is what makes `gcd(0, v) == v` start the next run correctly.
- **A trailing partial run is discarded**: in the last row the final $24$ stands alone with gcd $24 \neq 6$, so those elements contribute nothing and are simply left out of the $K$ pieces.
- **$K$ may exceed what is achievable** even when $G$ divides everything; the fourth row manages only $2$ pieces against $K = 3$.

## Dry run

Fourth sample: $A = 6, 12, 18, 24$, so $G = \gcd = 6$ and $K = 3$.

| element | running gcd | equals $G$? | pieces |
|---:|---:|:---:|---:|
| 6 | 6 | **yes** → cut | 1 |
| 12 | 12 | no | 1 |
| 18 | 6 | **yes** → cut | 2 |
| 24 | 24 | no | 2 |

Only $2$ disjoint pieces have gcd $6$, short of $K = 3$, so `NO`.
