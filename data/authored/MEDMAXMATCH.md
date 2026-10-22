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

## Edge cases

- **$N$ is odd**, so the median is the $m$-th largest with $m = (N+1)/2$ — meaning $m$ pairs must clear the target and the rest are free.
- **Only the top $m$ of each side are used**, paired against each other in *opposite* order: the $m$-th largest boy with the largest girl, and so on. That maximises the minimum of those $m$ sums.
- **The remaining pairs are irrelevant.** Their sums fall below the median by construction, so how the leftover boys and girls are matched never matters.
- **Pairing in the same order would be wrong.** On the second sample that gives sums $6+2$ and $6+7$, whose minimum is $8$ — the same here by coincidence — but opposite pairing is what guarantees the optimum in general, by the standard exchange argument.
- **$N = 1$** makes $m = 1$: the single pair, and the median is its sum.
- **Duplicates need no special handling**, as the second sample's two $6$s show.
- **$A_i, B_i$ up to $10^9$** put a sum at $2 \times 10^9$ — past 32-bit signed.

## Dry run

Third sample: $A$ sorted $= 4, 5, 10, 16, 93$ and $B$ sorted $= 4, 6, 26, 34, 62$, so $m = 3$.

| pair | boy | girl | sum |
|---:|---:|---:|---:|
| 1 | 10 (3rd largest) | 62 (largest) | 72 |
| 2 | 16 | 34 | **50** |
| 3 | 93 | 26 | 119 |

The median is the smallest of these three, `50`.
