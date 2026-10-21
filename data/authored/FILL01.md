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
