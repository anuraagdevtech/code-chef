---
topic: Sorting
subtopic: Sorted split maximising a product of two sums
time: $O(N \log N)$ per test case
space: $O(N)$
---
Defense points are $1000 - A_i$, so a soldier is valuable on attack exactly when $A_i$ is large and valuable on defense exactly when $A_i$ is small. That means the optimal assignment, **for any fixed number $k$ of attackers**, puts the $k$ largest $A_i$ on attack:

$$\text{atk}(k) = \sum_{i<k} A_{(i)}, \qquad \text{def}(k) = 1000(N-k) - \Bigl(\textstyle\sum_i A_i - \text{atk}(k)\Bigr)$$

with $A$ sorted descending. Both halves of the product improve under the same ordering — the attack sum wants the big values and the defense sum wants the rest to be small — so there is no tension and the split is always a prefix of the sorted array.

That leaves only $N+1$ candidates, scanned with a running prefix sum:

$$\text{answer} = \max_{0 \leq k \leq N}\ \text{atk}(k) \cdot \text{def}(k)$$

The product is not monotone in $k$, so every split has to be tried: the attack sum rises while the defense sum falls, and with $A_i < 1000$ the balance point depends on the values. Note $k = 0$ and $k = N$ both give a product of $0$, so the optimum is always interior — an army of all attackers has no defense at all.

The samples bear this out. Three soldiers at $500$ each tie at $k = 1$ and $k = 2$ with $500 \cdot 1000 = 500000$. For $[800,500,300,100]$ the best is $k = 2$: $1300 \cdot 1600 = 2080000$, beating $k=1$'s $1680000$. And for $[800,700,300,200]$, $k = 2$ gives the perfectly balanced $1500 \cdot 1500$.

## Edge cases

- **Sorting descending by attack makes every optimal split a prefix.** The attackers should be the soldiers with the highest attack points — which, since defense is $1000 - A_i$, are also the ones with the lowest defense — so trying each prefix size covers every candidate.
- **The defense value is $1000(n-k) - (\text{total} - \text{attack})$**, not a stored sum: each defender contributes $1000 - A_i$, so the group's value is $1000$ per defender minus their attack points.
- **Both extremes must be allowed**, so $k$ ranges over $0 \dots n$ — and both give a rating of $0$, which is why they are never optimal but still need including for correctness.
- **A balanced split is usually best**, since the rating is a product: the third sample peaks at $k = 2$ with $1300 \times 1600$.
- **Equal attack values** (the first two rows) make several splits tie, which the running maximum handles.
- **$0 < A_i < 1000$ strictly**, so no soldier has zero attack or zero defense.
- **$N \leq 1000$ with $\sum N \leq 2000$**, so the linear scan over split points is trivially affordable.

## Dry run

Third sample: $A = 100, 800, 300, 500$, sorted descending to $800, 500, 300, 100$ with a total of $1700$.

| $k$ | attack value | defenders | defense value | rating |
|---:|---:|---:|---:|---:|
| 0 | 0 | 4 | $4000 - 1700 = 2300$ | 0 |
| 1 | 800 | 3 | $3000 - 900 = 2100$ | 1680000 |
| 2 | 1300 | 2 | $2000 - 400 = 1600$ | **2080000** |
| 3 | 1600 | 1 | $1000 - 100 = 900$ | 1440000 |
| 4 | 1700 | 0 | 0 | 0 |

Output `2080000`.
