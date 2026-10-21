---
topic: Greedy
subtopic: Batching purchases of the cheapest net-cost sweet
time: $O(N \log N)$ per test case
space: $O(N)$
---
Each purchase of sweet $i$ needs $A_i$ in hand but burns only $A_i - B_i$ net. So two numbers matter per sweet: the **affordability** $A_i$ and the **burn rate** $n_i = A_i - B_i \geq 1$.

At any moment the affordable sweets are those with $A_i \leq R$, and among them the right choice is the smallest burn rate — buying a cheaper-to-burn sweet now never costs a purchase later. And crucially, once that sweet becomes unaffordable, the affordable set has shrunk, so the best available burn rate can only get **worse**. So the current best is worth exhausting completely before reconsidering.

Sort by $A$ and take prefix minima of $n$: the affordable set is a prefix, and its best burn rate and that sweet's price $a$ are then immediate. Buying it $k$ times keeps $R - (t-1)n \geq a$ through $t = k$, so

$$k = \left\lfloor \frac{R - a}{n} \right\rfloor + 1$$

After that batch $R < a$, so the prefix strictly shrinks and the loop runs at most $N$ times — a per-purchase simulation would run up to $R = 10^9$ times.

The third sample shows the batching and the switch. With $R = 10$ and prices $4,4,5,5$ at burn rates $3,2,1,3$, the best burn rate is $1$ (price $5$), bought six times down to $R = 4$. That price is now unaffordable, so the prefix drops to the two sweets priced $4$, whose best burn rate is $2$, giving one more purchase and $7$ in total.

Note the last purchase of a batch may leave less than its own price in hand — the cashback arrives after the sale, so only the *first* $A_i$ has to be covered up front.
