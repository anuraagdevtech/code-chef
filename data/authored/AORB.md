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
