---
topic: Greedy
subtopic: Scheduling order and the exchange argument
time: $O(1)$ per test case
space: $O(1)$
---
Chef solves both problems, so the only decision is the **order**. Points decay with wall-clock time from the start of the contest, and whichever problem is attempted second absorbs the first one's solving time as extra delay.

Solving `A` first, `A` is submitted at minute $X$ and `B` at minute $X + Y$:

$$(500 - 2X) + \bigl(1000 - 4(X+Y)\bigr) = 1500 - 6X - 4Y$$

Solving `B` first, `B` lands at $Y$ and `A` at $X + Y$:

$$(1000 - 4Y) + \bigl(500 - 2(X+Y)\bigr) = 1500 - 2X - 6Y$$

The answer is the larger of the two.

Comparing them shows the structure. `A` first wins when $-6X - 4Y > -2X - 6Y$, that is when $2Y > 4X$, or $Y > 2X$. So Chef should start with `A` exactly when `B` takes more than twice as long — the quick problem goes first, but weighted by decay rate, not by raw time.

This is the classic **exchange argument**: with two jobs, swapping adjacent ones and comparing totals reveals the ordering rule, which here is to sort by $\frac{\text{solve time}}{\text{decay rate}}$. The same reasoning generalises to $n$ jobs and underlies scheduling results such as Smith's rule.

Sample case 3 makes the point concretely: with $X = Y = 15$ the times are identical, yet order still matters — doing `B` first scores $1380$ against $1350$, because delaying the faster-decaying problem is the costlier mistake. With only two orderings available, evaluating both is simplest and avoids re-deriving the inequality.

## Edge cases

- **The two orders tie** ($X = 10$, $Y = 20$: both give $1360$). The sample's first row, so taking either is fine but the maximum must still be computed.
- **Equal solving times, unequal decay** ($X = Y = 15$): B-first scores $1380$ against A-first's $1350$. Which order wins is decided by the *decay rates*, not by which problem is quicker — B loses $4$ points a minute and so should be submitted early. A rule like "solve the faster one first" gets this row wrong.
- **Scores never go negative** at these bounds: with $X + Y \leq 200$ the worst cases are $1000 - 4 \times 200 = 200$ and $500 - 2 \times 200 = 100$, both positive, so no clamping is needed.
- Only two orders exist, so evaluating both and taking the larger is exact — there is no greedy rule to justify.

## Dry run

| $X$ | $Y$ | A first | B first | output |
|---:|---:|---:|---:|---|
| 10 | 20 | $480 + 880 = 1360$ | $920 + 440 = 1360$ | `1360` |
| 8 | 40 | $484 + 808 = 1292$ | $840 + 404 = 1244$ | `1292` |
| 15 | 15 | $470 + 880 = 1350$ | $940 + 440 = 1380$ | `1380` |
| 20 | 10 | $460 + 880 = 1340$ | $960 + 440 = 1400$ | `1400` |

In each pair the problem solved second pays for the first one's time; rows 3 and 4 both favour B first.
