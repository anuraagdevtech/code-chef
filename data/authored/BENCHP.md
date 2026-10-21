---
topic: Greedy
subtopic: Frequency pairing for a symmetric load
time: $O(N)$ per test case
space: $O(N)$
---
Symmetry means the multiset of plates on the left equals the multiset on the right, so every plate used must be **matched by an identical twin**. A weight occurring $c$ times therefore contributes at most $\lfloor c/2 \rfloor$ matched pairs, and each pair adds $2w$ to the bar.

There is no trade-off to optimise: using more weight is never harmful, since the goal is only to reach $W$. So the maximum achievable load is

$$W_r + 2\sum_{w} \left\lfloor \frac{c_w}{2} \right\rfloor \cdot w$$

and the answer is `YES` exactly when that reaches $W$. The floor is where the odd leftovers vanish — a lone plate is dead weight, because putting it on one side would unbalance the bar.

The rod alone may already suffice, which is why no plates are required: sample 1 has $W_r = 10 \geq W = 5$, so the two $2$s are irrelevant.

Sample 2 is the odd-leftover trap. The plates are $100, 10 \times 5, 90$, and only the $10$s pair up — twice, since the fifth is stranded — so the best load is $50 + 2(2 \cdot 10) = 90$, short of $100$. Naively summing all plates would give $230$ and the wrong answer: the heavy $100$ and $90$ are unusable precisely because each is unique.

Sample 3 is the exact boundary: six $10$s give three pairs, so $40 + 60 = 100$ meets $W = 100$ — the requirement is *at least* $W$, so equality passes.
