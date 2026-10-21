---
topic: Arrays
subtopic: Group total with a per-group adjustment
time: $O(\sum E_i)$ per test case
space: $O(1)$
---
Each episode length $L_{i,j}$ already includes the intro. Chef watches the intro only in the **first** episode of each season, skipping it in the other $E_i - 1$. So for season $i$ he saves $Q_i$ minutes $E_i - 1$ times:

$$\text{total} = \sum_i \left( \sum_j L_{i,j} \;-\; Q_i \cdot (E_i - 1) \right)$$

The $E_i - 1$ is the crux. Subtracting $Q_i \cdot E_i$ would strip the intro from the first episode too, which Chef does watch; subtracting nothing ignores the skipping entirely. It is the same *n items, n−1 gaps* shape as the gaming-breaks and tournament problems — here, the first episode of each season is the one that does not get the adjustment.

A season with a single episode saves nothing, since $E_i - 1 = 0$. Sample season 1 is exactly that, contributing its full $2$ minutes. Season 2 sums to $3 + 4 = 7$ and saves one intro of $2$, giving $5$, for a total of $7$.

The input layout is the other hazard: the intro durations arrive on **one line for all seasons**, before any episode data, and each season's line then begins with its own $E_i$ before the lengths. Reading the whole stream as flat tokens and advancing a cursor by $E_i + 1$ per season handles the ragged rows cleanly.

The guarantee $Q_i < L_{i,j}$ means no episode is shorter than its intro, so the per-episode contribution never goes negative.

## Edge cases

- **The intro is watched once per season, not once overall.** It changes slightly each season, so he sits through it in each season's first episode and skips it in the other $E_i - 1$ — hence a per-season subtraction of $Q_i (E_i - 1)$.
- **A one-episode season subtracts nothing**, since $E_i - 1 = 0$. The second sample's whole second case is five such seasons, and its answer is the raw sum.
- **$Q_i < L_{i,j}$ is guaranteed**, so no episode is shorter than its own intro and the total can never go negative.
- **$Q$ is read as a block of $S$ values before the seasons**, so the input is not interleaved — reading a $Q_i$ alongside each season desynchronises everything.
- **Each season's length list is preceded by its own $E_i$**, so the stride varies and the position must be advanced per season.
- **Sum of all $E_i \leq 10^5$** per case with $T \leq 5$, and lengths up to $10^5$ make the total around $10^{10}$ — past 32-bit.

## Dry run

First sample: $S = 2$, intros $Q = 1, 2$.

| season | episodes | raw total | intro skips | subtracted | net |
|---:|---|---:|---:|---:|---:|
| 1 | $2$ | 2 | 0 | 0 | 2 |
| 2 | $3, 4$ | 7 | 1 | $2 \times 1 = 2$ | 5 |

Output `7`. Season 2's second episode skips its two-minute intro.
