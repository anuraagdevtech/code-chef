---
topic: Greedy
subtopic: Opposite pairing of the top halves
time: $O(N \log N)$ per test case
space: $O(N)$
---
With $N$ odd, the median is the $m$-th largest for $m = \frac{N+1}{2}$. So the median is at least $v$ exactly when $m$ pairs have sum at least $v$, and the task becomes: choose $m$ pairs to **maximise their minimum sum**.

Those $m$ pairs should use the $m$ largest values from each side — a smaller value brings nothing — and within that selection they should be paired in **opposite order**: the largest $A$ with the smallest chosen $B$, and so on. That is the standard max-min pairing: if two pairs were matched in the same order, swapping their partners raises the smaller sum without lowering the larger one above it.

$$\text{answer} = \min_{0 \leq i < m}\ \bigl(A_{N-m+i} + B_{N-1-i}\bigr)$$

with both arrays sorted ascending. The leftover $\frac{N-1}{2}$ values on each side pair arbitrarily; their sums can only be smaller, so they sit below the median and never affect it.

Why opposite rather than same order: pairing the two largest together wastes one of them, since a pair contributes only one sum. Spreading the big values across different pairs is what lifts the minimum.

The third sample shows this clearly. With $A = [4,5,10,16,93]$ and $B = [4,6,26,34,62]$ and $m = 3$, the chosen pairs are $10{+}62 = 72$, $16{+}34 = 50$ and $93{+}26 = 119$, so the median is $50$. Pairing in the same order would give $10{+}26 = 36$ as the minimum instead.

The second sample, $A = [1,6,6]$ and $B = [2,2,7]$, gives $6{+}7$ and $6{+}2$, so the median is $8$ — the leftover $1{+}2 = 3$ sits below it as expected.
