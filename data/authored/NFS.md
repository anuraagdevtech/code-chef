---
topic: Basic Math
subtopic: Rearranging a kinematic inequality
time: $O(1)$ per test case
space: $O(1)$
---
The statement supplies $v^2 = U^2 + 2aS$. Chef brakes as hard as he can, so $a = -A$ and the speed at the turn satisfies

$$v^2 = U^2 - 2AS$$

He crosses safely when $v \leq V$, which — since both are non-negative — is equivalent to comparing the squares:

$$U^2 - 2AS \leq V^2$$

Working with $v^2$ rather than $v$ is the whole trick. It keeps everything in integers and avoids a square root, which would introduce floating point and, worse, a domain error.

That domain point is the case to watch. If $U^2 - 2AS$ is **negative**, the car would have come to a stop before reaching the turn, so it enters at $v = 0$ and certainly succeeds. Taking $\sqrt{U^2 - 2AS}$ there is undefined, but the inequality form handles it without a branch: a negative left side is automatically $\leq V^2$. Sample case 1 is exactly this, with $1 - 2 = -1$.

Braking hardest is optimal because the goal is only to be *slow enough*; there is no reward for arriving fast, so the maximum deceleration gives the best chance. That is why $a = -A$ rather than something in between.

Sample case 2 is the failure: $4 - 2 = 2$ against $V^2 = 1$, so the car is still too fast. Case 3 has the same approach speed but a more forgiving limit, $V^2 = 4$, and passes.

With all values to $10^4$, $U^2$ and $2AS$ reach $10^8$ and $2 \times 10^8$ — inside 32 bits, though a C solution should be careful.

## Edge cases

- **A negative left side needs no special case.** The first row gives $u^2 - 2as = -1$, meaning the car stops before reaching the turn; the comparison $-1 \leq 1$ answers `Yes` correctly without a branch.
- **Exact equality is safe.** If braking brings the speed to precisely $V$, the turn is survivable, so the comparison is non-strict.
- **No square root is taken.** Comparing $u^2 - 2as$ against $v^2$ keeps everything in integers, where a float `sqrt` could land on the wrong side of an exact tie.
- **All of $U, V, A, S \geq 1$**, so there is always some braking over some distance — zero-distance and zero-deceleration cases cannot arise.
- **Values up to $10^4$** make $u^2$ up to $10^8$ and $2as$ up to $2 \cdot 10^8$: small, but both intermediates exceed any single input.
- **$T$ up to $10^5$** with constant work per case.

## Dry run

| $U$ | $V$ | $A$ | $S$ | $u^2 - 2as$ | $v^2$ | $\leq$? | output |
|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 1 | 1 | $-1$ | 1 | yes | `Yes` |
| 2 | 1 | 1 | 1 | 2 | 1 | no | `No` |
| 2 | 2 | 1 | 1 | 2 | 4 | yes | `Yes` |

Row 1 is the stops-early case; the formula handles it as an ordinary comparison.
