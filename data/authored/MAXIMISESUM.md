---
topic: Prefix Sums
subtopic: Per-position ceiling from prefix and suffix maxima
time: $O(N)$ per test case
space: $O(N)$
---
The operation only ever writes a **minimum of two existing values**, so no value in the array can rise above what is already present. Fix a position $i$: any operation that touches it uses some $l < i$ and $r > i$ and writes $\min(A_l, A_r)$, so whatever lands there is bounded by the best value available on each side:

$$A_i^{\text{final}} \;\leq\; \max\Bigl(A_i,\ \min\bigl(\max_{j<i} A_j,\ \max_{j>i} A_j\bigr)\Bigr)$$

(the outer $\max$ because we may simply leave $A_i$ alone). Positions $1$ and $N$ are never interior to any operation, so they are untouchable.

That bound is attained everywhere at once. Taking $l$ to be an argmax of the prefix and $r$ an argmax of the suffix, the single operation on $(l, r)$ raises *every* strictly-interior position to $\min$ of those two maxima, and positions already above it are only among $l$, $r$ and the ends — none of which the operation disturbs if chosen as the extreme positions. So

$$\text{answer} = \sum_{i=1}^{N} \max\Bigl(A_i,\ \min\bigl(\mathrm{pre}_{i-1},\ \mathrm{suf}_{i+1}\bigr)\Bigr)$$

with $\mathrm{pre}$ and $\mathrm{suf}$ the prefix and suffix maxima and the out-of-range entries treated as $0$.

The samples show the two regimes. $[5,1,7]$ lifts the middle to $\min(5,7) = 5$, giving $17$ — the one position that can be improved. $[5,5,5,5]$ is already flat, so nothing changes and the sum stays $20$. And $[2,3]$ has no interior position at all.

Note the operation can *lower* values, which is why every term keeps $A_i$ as a floor: for $[1,10,1]$ the middle must be left alone, since $\min(1,1) = 1$ would waste $9$.

## Edge cases

- **The operation writes $\min(A_l, A_r)$**, so position $i$ can never exceed $\min(\max \text{ of the left part},\, \max \text{ of the right part})$ — and that ceiling is reached in a single operation using the two argmaxes.
- **The prefix and suffix maxima are invariant**, since every write is at most the larger of two existing values — so no sequence of operations can raise the ceiling, and one pass suffices.
- **A position already above its ceiling keeps its value**, hence the outer maximum: the operation is optional per position.
- **The two ends can never be raised**, because $l < i < r$ excludes them — their prefix or suffix maximum is empty, which the zero sentinels encode.
- **A single large value in the middle lifts nothing** unless it has company on both sides, which is why the second sample's $5$ and $7$ lift only the $1$ between them.
- **An already-uniform array gains nothing** (the third row), since every ceiling equals the value already there.
- **The zero sentinels are safe** because $A_i \geq 1$, so a real value always beats an empty side.

## Dry run

Second sample: $A = 5, 1, 7$.

| $i$ | $A_i$ | max to the left | max to the right | ceiling $\min$ | kept |
|---:|---:|---:|---:|---:|---:|
| 1 | 5 | — ($0$) | 7 | 0 | 5 |
| 2 | 1 | 5 | 7 | **5** | 5 |
| 3 | 7 | 5 | — ($0$) | 0 | 7 |

Sum $5 + 5 + 7 = $ `17`, achieved by one operation with $l = 1$, $r = 3$.
