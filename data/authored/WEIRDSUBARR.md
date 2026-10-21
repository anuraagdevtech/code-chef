---
topic: Arrays
subtopic: Counting valley subarrays from run lengths
time: $O(N)$ per test case
space: $O(N)$
---
Negating an element makes it negative, and every value here is a positive distinct integer, so in a sorted result all the negated elements come first. Their negatives must be non-decreasing, i.e. their **magnitudes decreasing**, and the untouched suffix must be increasing. So a subarray is weird exactly when it is a **valley**: strictly decreasing, then strictly increasing.

Count valleys by right endpoint. Let $\mathrm{inc}[R]$ be the length of the maximal strictly increasing run ending at $R$, and $m = R - \mathrm{inc}[R] + 1$ its start — the valley's turning point is forced to be $m$, since the increasing arm cannot reach further left. The decreasing arm then extends from $m$ back as far as $\mathrm{dec}[m]$, the maximal strictly decreasing run ending at $m$. So the valid left endpoints are $[\,m - \mathrm{dec}[m] + 1,\ R\,]$ and

$$\#\{\text{valleys ending at } R\} = R - m + \mathrm{dec}[m]$$

Both run-length arrays build in one pass each, so the whole count is linear — no $O(N^2)$ scan over pairs.

Note the turning point is shared by both arms, which is why a single element counts (both arms have length $1$) and why the formula needs no special case for a purely increasing or purely decreasing subarray.

The samples: $[2,3,1]$ gives $1 + 2 + 2 = 5$, excluding only the whole array — $2, 3, 1$ rises then falls, the one shape that cannot be fixed. $[2,1,3]$ is itself a valley, so all $6$ subarrays qualify. And $[1,2,3,4]$ is wholly increasing, giving all $10$.
