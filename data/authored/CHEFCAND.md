---
topic: Basic Math
subtopic: Clamping before a ceiling division
time: $O(1)$ per test case
space: $O(1)$
---
Chef needs one candy per child, so he needs $N$ candies and already holds $X$. The shortfall is $N - X$, and packets contain exactly $4$ candies, so the number of packets is

$$\left\lceil \frac{N - X}{4} \right\rceil$$

The trap is that $X$ may **exceed** $N$ — Chef can already have more candies than children. Sample case 2 ($N = 10$, $X = 100$) is exactly that, and the answer must be $0$. A bare ceiling division would produce a negative number there, so the shortfall has to be clamped at zero first:

$$\text{need} = \max(0,\; N - X)$$

Only then is the ceiling applied, as `(need + 3) // 4`.

The clamp and the ceiling must happen in that order. Applying `(n - x + 3) // 4` directly looks like a shortcut but is wrong whenever $X > N$: with $N = 10, X = 100$ it gives $(-90 + 3) // 4 = -22$, because Python's `//` floors toward negative infinity rather than truncating toward zero. Guarding the subtraction is what keeps the identity valid.

Walking the samples: $20, 12$ needs $8$ candies and so $2$ packets; $10, 9$ needs $1$ candy, which still costs a whole packet; $20, 9$ needs $11$, giving $3$ packets with one candy spare.

## Edge cases

- **Chef already has enough** ($N = 10$ children, $X = 100$ candies): the shortfall is negative, so the answer is $0$ packets. **The clamp is essential** — without `max(0, ...)` the expression $(-90 + 3) // 4$ evaluates to $-22$ in Python, because floor division rounds negatives *down*, and the answer would be badly wrong rather than merely off by one.
- **Exactly enough** ($N = X$): shortfall $0$, so $0$ packets.
- **Shortfall not a multiple of $4$** ($N = 10$, $X = 9$: one candy short): one whole packet.
- **Shortfall an exact multiple** ($N = 20$, $X = 12$: eight short): two packets, and the $+3$ must not make it three.

## Dry run

| $N$ | $X$ | shortfall $N - X$ | clamped | $(\text{need}+3)//4$ | output |
|---:|---:|---:|---:|---:|---|
| 20 | 12 | 8 | 8 | 2 | `2` |
| 10 | 100 | $-90$ | 0 | 0 | `0` |
| 10 | 9 | 1 | 1 | 1 | `1` |
| 20 | 9 | 11 | 11 | 3 | `3` |

Row 2 is the one the clamp exists for.
