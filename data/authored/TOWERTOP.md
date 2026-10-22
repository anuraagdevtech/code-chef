---
topic: Greedy
subtopic: Doubling to the first tower, then one per operation
time: $O(1)$ per test case
space: $O(1)$
---
Spending the whole inventory on one tower **doubles** it. If the tower has $h$ blocks and the inventory also holds $h$, adding all $h$ makes it $2h$ and the reward restores the inventory to $2h$. Starting from one block, operation $i$ leaves a tower of $2^{i-1}$ with $2^{i-1}$ in reserve, so the first tower of height $X$ needs

$$k = \min\{\,i : 2^{i-1} \geq X\,\}$$

operations — and the exact height $X$ is reachable at step $k$, because the inventory then holds $2^{k-2} \geq X - 2^{k-2}$, just enough to top up from $2^{k-2}$ to $X$.

The payoff is what the inventory looks like afterwards. Blocks spent plus the reward leave

$$2^{k-2} - (X - 2^{k-2}) + X = 2^{k-1} \;\geq\; X$$

so from then on **every operation builds a whole new tower**: spend $X$, get $X$ back, inventory unchanged. Hence

$$\text{answer} = \max(0,\ M - k + 1)$$

Doubling is optimal because the reward equals the tower's new size, so the inventory can never grow faster than by doubling, and the first tower cannot be finished sooner.

The samples trace this. For $X = 2$ we have $k = 2$: $M = 1$ gives $0$ (one operation only reaches height $1$), $M = 2$ gives $1$, and $M = 3$ gives $2$ — the third operation builds a second tower outright from the two banked blocks. For $X = 53$, $k = 7$ since $2^6 = 64 \geq 53$, so $M = 7$ yields exactly $1$: the tower grows $1, 2, 4, 8, 16, 32$ and then jumps to $53$.

## Edge cases

- **The inventory doubles while building the first tower.** Starting from one block, pouring everything into the same tower each turn gives heights $1, 2, 4, 8, \dots$ and refills the inventory to match — so reaching height $X$ takes $k = \lceil \log_2 X \rceil + 1$ operations.
- **After that, every operation yields a whole tower.** The inventory is then at least $X$, and spending $X$ blocks on a fresh tower refills it by $X$ — so it never drops below $X$ again.
- **Hence the answer is $M - k + 1$**: the first tower plus one per remaining operation.
- **Too few operations give $0$**, which the clamp handles — the first sample row has $M = 1$ against $k = 2$.
- **$X = 1$ makes $k = 1$**, since `(1-1).bit_length() + 1 = 1`: the very first operation already builds a tower of height $1$.
- **$X$ need not be a power of two.** For $X = 53$, seven operations reach height $64 \geq 53$, and the formula counts that as the one tower it is.
- **$M$ up to $10^{17}$** means the answer can be enormous, so no simulation is possible — but the arithmetic stays exact.

## Dry run

Fourth sample: $X = 53$, $M = 7$. Building one tower as fast as possible:

| operation | tower height after | inventory after |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 4 | 4 |
| 4 | 8 | 8 |
| 5 | 16 | 16 |
| 6 | 32 | 32 |
| 7 | 64 | 64 |

Seven operations produce exactly one tower of height at least $53$, so the output is `1`.
