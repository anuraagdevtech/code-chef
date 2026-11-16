---
topic: Simulation
subtopic: One simulated step, then distance to the nearest seed and parity
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
After the first second the picture becomes regular. Every old 1 turns into 0, and a position is 1 exactly when it was 0 and had a neighbouring 1. Call these positions the seeds. If there are none (all zeros, or all ones), the string is all zeros from then on.

From this moment each seed behaves like a source that sends a front outwards one cell per second while the cells behind the front alternate between 1 and 0. A cell at distance $d$ from its nearest seed is first reached $d$ seconds later and from then on is 1 every second step. Fronts coming from two different seeds agree in parity wherever they meet, or meet between two adjacent cells, so taking the nearest seed is enough.

So with $k = K - 1$ seconds remaining after the first one, cell $i$ is 1 exactly when $d_i \le k$ and $k - d_i$ is even. The distances come from one left-to-right and one right-to-left pass.

## Edge cases

- No seed after the first second: the answer is all zeros.
- $K$ is up to $10^9$; nothing is simulated beyond the first step.
- $K = 1$ gives exactly the seed string ($d = 0$, $k = 0$).
- A string of length 1 containing `1` becomes `0` and stays there.

## Dry run

`S = 10001`, `K = 2`.

After one second the seeds are the zeros next to a one: positions 2 and 4, i.e. `01010`. One second remains, $k = 1$.

Distances to the nearest seed: `1 0 1 0 1`. A cell is 1 when $d \le 1$ and $1 - d$ is even, i.e. $d = 1$: positions 1, 3, 5.

Answer `10101`.
