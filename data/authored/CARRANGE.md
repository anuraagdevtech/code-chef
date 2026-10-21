---
topic: Basic Math
subtopic: Reading an off-by-one from the statement
time: $O(1)$ per test case
space: $O(1)$
---
The base economy $M$ already accounts for the driver, so only the **extra** passengers reduce it. With $P$ people in the car there are $P - 1$ extras, each costing $1$ km/l:

$$\text{economy} = M - (P - 1) = M - P + 1$$

and the distance is that economy multiplied by the fuel available:

$$V \cdot (M - P + 1)$$

The whole problem is the $-1$. Reading the penalty as $P$ rather than $P - 1$ gives a plausible-looking formula that fails every sample, and the statement goes out of its way to warn about it — both by defining the base case as "only the driver" and by the closing note that the $P$ people *include* the driver.

Sample case 2 is the one that isolates it: a single occupant means no extras at all, so the economy is the full $M = 6$ and the answer is $60$. A formula using $M - P$ would give $50$.

Sample case 1 shows the penalty biting hardest: five people drop a $10$ km/l car to $6$ km/l, giving $120$ km from $20$ litres.

The constraints keep the economy positive — $M \geq 6$ while $P \leq 5$, so $M - P + 1 \geq 2$ — meaning no clamping is needed and the distance is never zero or negative.

## Edge cases

- **$P = 1$** (just the driver): the answer is $V \cdot M$, the full mileage. The $+1$ in $M - P + 1$ is what makes this come out right — without it the row gives $50$ instead of $60$.
- **The driver is already priced into $M$**, so only the $P - 1$ extra passengers reduce the range. That off-by-one is the entire problem, and it is read from the statement rather than derived.
- **$P \leq 5$ while $M \geq 6$**, so $M - P + 1 \geq 2$ and the answer is always positive — there is no clamp to worry about.
- **Largest input** ($V = 100$, $M = 56$, $P = 1$): $5600$.

## Dry run

| $P$ | $M$ | $V$ | effective mileage $M - P + 1$ | range $V \cdot {\cdot}$ | output |
|---:|---:|---:|---:|---:|---|
| 5 | 10 | 20 | 6 | 120 | `120` |
| 1 | 6 | 10 | 6 | 60 | `60` |
| 4 | 6 | 1 | 3 | 3 | `3` |

Row 2 is the driver-only case that pins the $+1$.
