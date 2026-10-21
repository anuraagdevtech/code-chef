---
topic: Basic Math
subtopic: Working backwards from a deadline
time: $O(1)$ per test case
space: $O(1)$
---
The bullet covers $X$ pixels per unit time and the goomba is $Y$ pixels away, so the bullet is in flight for

$$\text{flight} = \frac{Y}{X}$$

The guarantee that **$X$ divides $Y$** is what makes this an exact integer, so `y // x` is safe and no rounding rule is needed.

If Mario fires at time $t$, the hit lands at $t + \text{flight}$. The requirement is that the hit happen at least $Z$ from now, so

$$t + \frac{Y}{X} \geq Z \quad\Longleftrightarrow\quad t \geq Z - \frac{Y}{X}$$

and the smallest such $t$ is that bound — except that Mario cannot fire in the past. Clamping gives

$$t = \max\left(0,\; Z - \frac{Y}{X}\right)$$

The clamp is the case worth noticing, and sample 2 is built on it: with flight time $4/2 = 2$ and a deadline of only $Z = 1$, the bullet already arrives later than required if fired immediately, so the answer is $0$ rather than $-1$.

Reading "at least $Z$" as a *lower* bound on the arrival time is what makes this a delay rather than a hurry; Mario waits so the bullet does not arrive too early.

## Edge cases

- **The bullet cannot arrive in time even if fired immediately** ($X = 2$, $Y = 4$, $Z = 1$: a flight of $2$ against a deadline of $1$): the wait would be negative, so the clamp returns $0$. The sample's second row is this case.
- **Exact arrival** (flight time equal to $Z$): the wait is $0$ — fire at once.
- **$X$ divides $Y$ is guaranteed**, so the flight time $Y/X$ is an exact integer and no rounding decision arises.
- Firing early is not allowed, so a negative wait is meaningless rather than useful, which is why it clamps to zero instead of being reported.

## Dry run

| $X$ (speed) | $Y$ (distance) | $Z$ (deadline) | flight $Y/X$ | wait $Z - {\cdot}$ | output |
|---:|---:|---:|---:|---:|---|
| 3 | 3 | 5 | 1 | 4 | `4` |
| 2 | 4 | 1 | 2 | $-1 \to 0$ | `0` |
| 3 | 12 | 8 | 4 | 4 | `4` |

Row 2 is the clamped case.
