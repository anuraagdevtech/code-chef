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
