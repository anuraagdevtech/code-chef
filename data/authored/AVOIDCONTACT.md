---
topic: Greedy
subtopic: Packing with separation constraints
time: $O(1)$ per test case
space: $O(1)$
---
Healthy people may sit next to each other, so the $X - Y$ healthy residents pack into one contiguous block of $X - Y$ rooms. Infected people are the constraint: each needs an empty room on every side that touches anyone.

The tightest arrangement puts the healthy block at one end and then alternates:

$$\underbrace{\text{H H} \cdots \text{H}}_{X-Y}\ \_\ \text{I}\ \_\ \text{I}\ \_\ \cdots\ \text{I}$$

Each infected person costs two rooms — one empty separator plus their own — except that the very last one needs no separator after it, and the first needs none before it if nothing precedes.

**With healthy people present** ($X > Y$): the block occupies $X - Y$ rooms, then each of the $Y$ infected adds a gap and a room, for $X - Y + 2Y = X + Y$ rooms total.

**With no healthy people** ($X = Y$): the pattern is `I _ I _ ... I`, which is $2Y - 1$ rooms — one fewer, because the leading gap is unnecessary.

Both collapse into

$$N = X + Y - [X = Y]$$

Sample case 2 ($X=5, Y=3$) gives $8$: two healthy rooms plus three gap-and-room pairs. Sample case 3 ($X=Y=3$) gives $5$, and is exactly the case the $-1$ exists for. Sample case 1 has $Y = 0$ and reduces to $X$.

The greedy is optimal because every infected person forces at least one empty room between them and the next occupant, and the construction achieves that bound with no slack.

## Edge cases

- **Nobody infected** ($Y = 0$): no separation is needed, so the answer is just $X$. The first sample row.
- **Everybody infected** ($X = Y$): the $-1$ fires, giving $2X - 1$ rather than $2X$, because with no healthy group present one leading gap is unnecessary. The third sample row ($3, 3$) gives $5$ and is the only case that exercises the correction.
- **A mix** ($5, 3$): $X + Y$ with no correction.
- The $-1$ triggers on exactly one condition, so the formula is $X + Y$ everywhere else — which makes that single sample row the whole test of the special case.

## Dry run

| $X$ | $Y$ | $X + Y$ | $X = Y$? | correction | output |
|---:|---:|---:|:---:|---:|---|
| 4 | 0 | 4 | no | 0 | `4` |
| 5 | 3 | 8 | no | 0 | `8` |
| 3 | 3 | 6 | yes | $-1$ | `5` |
