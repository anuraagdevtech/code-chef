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

## Edge cases

- **Only matched pairs can be loaded**, since the two sides of the bar must be symmetric — so a weight appearing an odd number of times leaves one copy as dead weight.
- **Every available pair should be used**, as more weight is never worse: the goal is a *minimum* lift of $W$, so the check is against the maximum achievable load.
- **Using no weights at all is allowed**, so the rod alone may suffice — the first row needs $5$ grams and the rod already weighs $10$.
- **Exactly reaching $W$ counts** (the third row, where six $10$-gram plates plus a $40$-gram rod make precisely $100$).
- **Odd leftovers can be decisive.** The second row has a $100$ and a $90$ with no partners, so only the five $10$s contribute — two pairs, for $40$ — leaving the load at $90$ against a target of $100$.
- **Each pair adds $2w$**, not $w$, since one plate goes on each side.
- **$N$ up to $10^5$** with $T \leq 10$: a `Counter` and one pass over the distinct weights.

## Dry run

Second sample: target $100$, rod $50$, plates $100, 10, 10, 10, 10, 10, 90$.

| weight | copies | usable pairs | contribution $2w \lfloor c/2 \rfloor$ |
|---:|---:|---:|---:|
| 100 | 1 | 0 | 0 |
| 10 | 5 | 2 | 40 |
| 90 | 1 | 0 | 0 |

Total load $50 + 40 = 90 < 100$, so `NO`. The lone $100$-gram plate is unusable for want of a twin.
