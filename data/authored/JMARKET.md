---
topic: Greedy
subtopic: Cheapest choice under a diversity constraint
time: $O(1)$ per test case
space: $O(1)$
---
Without the diversity rule, Janmansh would buy $X$ of the cheapest fruit. The rule forces **at least two different kinds**, so exactly one unit must be sacrificed to a second variety — and that sacrifice should be as cheap as possible.

Sort the three prices to get $a \leq b \leq c$. Buy $X - 1$ of the cheapest and $1$ of the second cheapest:

$$(X-1)\,a + b$$

Two greedy decisions sit behind this. First, the constraint is satisfied by exactly **two** kinds — bringing in a third would only replace a unit of $a$ with something at least as expensive, never cheaper. Second, among the non-cheapest options the second cheapest $b$ is the best filler, so the surcharge over the unconstrained cost is exactly $b - a$, the smallest possible.

The constraint $X \geq 2$ guarantees there are at least two fruits to buy, so $X - 1 \geq 1$ and the arrangement is always feasible.

Sample case 1 shows the surcharge vanishing when prices tie: all three fruits cost $1$, so $b - a = 0$ and the answer is simply $2$. A solution that always added a premium would get this wrong.

Sample case 2 sorts $[4,3,2]$ into $[2,3,4]$, giving $2 \cdot 2 + 3 = 7$ — two of the cheapest plus one of the next. Buying three of the cheapest would cost $6$ but is disallowed.

## Edge cases

- **All prices equal** ($1,1,1$): the answer is simply $X$ times the price, since the diversity requirement costs nothing.
- **$X = 2$** (the minimum): one of the cheapest and one of the second cheapest.
- **Exactly one unit must be a different kind**, which is the whole constraint. Buying all $X$ at the cheapest price would give $6$ on the second row instead of $7$.
- **The odd unit should be the *second* cheapest**, not the dearest: sorting and taking `lo` and `mid` is what makes it minimal.
- **Largest input** ($X = 1000$ with prices up to $100$): under $10^5$.

## Dry run

| $X$ | prices | sorted | $(X-1) \times \text{lo}$ | $+\,\text{mid}$ | output |
|---:|---|---|---:|---:|---|
| 2 | $1,1,1$ | $1,1,1$ | 1 | 2 | `2` |
| 3 | $4,3,2$ | $2,3,4$ | 4 | 7 | `7` |

Row 2 pays $3$ for the mandatory second kind rather than another $2$.
