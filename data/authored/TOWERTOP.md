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
