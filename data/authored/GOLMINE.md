---
topic: Game Theory
subtopic: Every mine is split in proportion to the mining speeds
time: $O(N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
In mine $i$ Chef digs $G_i / A_i$ gold per day and Chefu $G_i / B_i$. If both work in the same mine until it is empty, Chef ends up with the fraction

$$\frac{1/A_i}{1/A_i + 1/B_i} = \frac{B_i}{A_i + B_i}$$

of its gold, i.e. $G_i B_i / (A_i + B_i)$, and Chefu with the rest.

The claim is that under optimal play this is exactly what happens in every mine. Either miner can guarantee his proportional share of each mine simply by always working where the opponent works; so neither can be pushed below the proportional total. Since the two totals add up to all the gold, neither can get more either. The answer is the sum of the proportional shares.

## Edge cases

- The answer is real-valued; an absolute or relative error of $10^{-6}$ is accepted.
- Chefu's total is computed as (all gold) $-$ (Chef's total), so the two always add up exactly.
- Equal speeds split every mine evenly.
- The order in which mines are worked does not matter for the result.

## Dry run

One mine with `G = 30, A = 2, B = 1`: Chef is half as fast as Chefu, so he gets $30 \cdot 1 / (2 + 1) = 10$ and Chefu gets 20.

Three mines `(10,1,1) (20,2,2) (30,3,3)`: equal speeds everywhere, so each miner gets $5 + 10 + 15 = 30$.
