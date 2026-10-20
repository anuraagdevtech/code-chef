---
topic: Basic Math
subtopic: Floor division by a composite unit
time: $O(1)$ per test case
space: $O(1)$
---
A bucket holds $Y$ litres and one bath takes exactly $2$ buckets, so a single person consumes $2Y$ litres. The geyser holds $X$ litres, so the number of complete baths is

$$\left\lfloor \frac{X}{2Y} \right\rfloor$$

The rounding direction is the crux. A bath needs *exactly* two buckets — a person cannot bathe with one and a half — so any remaining water is simply unused and the division **floors**. This is the opposite of the cars and pizzas problems, where every person had to be served and partial units rounded up. The phrase to look for is "maximum number that can be served from a fixed supply", which always floors.

The other half of the trick is forming the right unit. The divisor is $2Y$, not $Y$: it is tempting to compute the number of buckets `x // y` and then halve it, which happens to give the same answer here but is an extra step and reads less directly. Dividing by the per-person cost in one go is both clearer and immune to a stray rounding between the two divisions.

Sample cases 1 and 4 are the ones that punish a wrong direction: $10$ litres against a $12$-litre bath, and $30$ against $80$, both yield $0$ people rather than $1$.
