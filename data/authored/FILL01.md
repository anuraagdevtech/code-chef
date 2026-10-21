---
topic: Greedy
subtopic: Independent runs, each packed by division
time: $O(N)$ per test case
space: $O(1)$
---
A nap needs $K$ **consecutive** free hours, so it must lie inside a single maximal run of zeros — no nap can span a working hour. The runs are therefore independent, and the answer is the sum of what each run can hold.

Within a run of length $\ell$, naps are disjoint blocks of exactly $K$ hours, and consecutive naps are explicitly allowed to touch. So a run holds at most $\lfloor \ell / K \rfloor$ naps, and packing them back to back from the left attains that bound. Hence

$$\text{answer} = \sum_{\text{runs}} \left\lfloor \frac{\ell}{K} \right\rfloor$$

The leftover $\ell \bmod K$ hours are simply wasted — they cannot be combined with another run's remainder, which is the trap in treating the problem as "total free hours divided by $K$". Sample 3 shows the difference plainly: `00100000001` with $K = 3$ has $10$ free hours, so the naive division would say $3$, but the runs are $2$ and $8$, giving $0 + 2 = 2$.

Sample 2 is the same trap in miniature: `0100` with $K = 2$ has three free hours but runs of $1$ and $2$, so only one nap. And sample 1 with $K = 1$ shows the other extreme — every free hour is its own nap, so the answer is the count of zeros, $2$.

A single pass with a running counter suffices: on a `0` extend the run, on a `1` flush it. Remember to flush the final run after the loop, which is the usual off-by-one here.

## Edge cases

- **Leftovers cannot be pooled across runs.** The first row's two isolated zeros give $2$ naps at $K = 1$ but $0$ at $K = 2$, whereas treating the total zero count as one block would wrongly report $1$. Each maximal run of free hours must be divided on its own.
- **Splitting on `1` yields empty pieces** at the ends and between adjacent `1`s; they contribute $0$ and need no filtering.
- **$K$ larger than every run** → $0$ naps, even when there are plenty of free hours in total.
- **$K = 1$** → the answer is simply the number of zeros.
- **An all-zero string** is a single run, giving $\lfloor N/K \rfloor$.
- **Sum of $N \leq 2 \cdot 10^5$**: the split happens at C speed on the byte string, with no per-character Python loop.

## Dry run

| $S$ | $K$ | runs of free hours | naps per run | total |
|---|---:|---|---|---:|
| `1010` | 1 | `""`, `0`, `0` | $0, 1, 1$ | `2` |
| `0100` | 2 | `0`, `00` | $0, 1$ | `1` |
| `00100000001` | 3 | `00`, `00000000`, `""` | $0, 2, 0$ | `2` |

Row 1 at $K = 2$ would give $0$, which is why the runs cannot be merged.
