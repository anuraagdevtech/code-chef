---
topic: Conditionals & Case Work
subtopic: Signed difference against one-sided supplies
time: $O(1)$ per test case
space: $O(1)$
---
Each litre of hot water raises the temperature by one degree and each litre of cold lowers it by one, so the reachable temperatures form the interval

$$[A - Y,\; A + X]$$

and the question is whether $B$ lies inside it.

The cleaner way to think about it is through the signed difference $d = B - A$, because its **sign** selects which supply is relevant:

- $d > 0$: the bath must warm up, needing $d$ litres of hot water, so the test is $d \leq X$. The cold supply is irrelevant.
- $d < 0$: it must cool, needing $|d|$ litres of cold, so the test is $|d| \leq Y$.
- $d = 0$: nothing to do, always `YES`.

The trap is treating the two supplies as interchangeable. They are not — hot water cannot cool a bath. Sample case 3 is exactly this: it needs to drop $10$ degrees and there are $10$ litres of *hot* water available but only $9$ of cold, so the answer is `NO` despite the totals looking sufficient. Sample case 4 is the mirror image, needing one degree of warming with no hot water at all.

The interval form `a - y <= b <= a + x` expresses the same rule in a single line without branching, and is the version used below.

Sample case 2 covers $d = 0$, where both supplies go unused.

## Edge cases

- **Already at the target** ($A = B = 37$): no mixing needed, so `YES`. The sample's second row.
- **No warming available** ($X = 0$ with a target above $A$): the reachable range collapses on that side, so `NO`. The sample's fourth row is exactly this.
- **Short by one** ($A = 30$, $B = 20$, cold supply $Y = 9$ but $10$ is needed): `NO`. The sample's third row, which a solution ignoring the supply sizes would pass wrongly.
- **Exactly on a boundary** ($B = A + X$ or $B = A - Y$): reachable, so the comparisons are non-strict.
- **The supplies are one-sided**: hot water only raises the temperature and cold only lowers it, so the reachable set is the asymmetric interval $[A - Y,\ A + X]$ rather than a symmetric window.

## Dry run

| $A$ | $B$ | $X$ (hot) | $Y$ (cold) | reachable $[A-Y,\ A+X]$ | $B$ inside? | output |
|---:|---:|---:|---:|---|:---:|---|
| 24 | 25 | 2 | 0 | $[24, 26]$ | yes | `YES` |
| 37 | 37 | 2 | 9 | $[28, 39]$ | yes | `YES` |
| 30 | 20 | 10 | 9 | $[21, 40]$ | no, by one | `NO` |
| 30 | 31 | 0 | 20 | $[10, 30]$ | no | `NO` |

Row 3 misses by a single degree; row 4 has no warming at all.
