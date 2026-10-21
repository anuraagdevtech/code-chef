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
