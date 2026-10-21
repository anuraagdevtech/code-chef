---
topic: Basic Math
subtopic: Floor division
time: $O(1)$ per test case
space: $O(1)$
---
Chef earns $X$ coins per bill and pays $Y$ bills, so he ends up with $X \cdot Y$ coins. Each bag costs $100$ coins, and coins cannot be split across a partial purchase, so the number of bags is the floor:

$$\left\lfloor \frac{X \cdot Y}{100} \right\rfloor$$

This is the mirror image of a ceiling-division problem: here the leftover coins are simply wasted rather than forcing an extra unit, so we round **down**. Recognising which way a remainder should push is the whole skill being drilled — "how many whole things can I afford" floors, "how many containers do I need" ceils.

Python's `//` is exactly floor division on non-negative integers, so `x * y // 100` is the entire computation. Avoid `int(x * y / 100)`, which routes through a float and would start misbehaving on larger inputs.

Sample case 2 shows the rounding clearly: $20 \times 4 = 80$ coins, which is not enough for even one bag, so the answer is $0$.

## Edge cases

- **Fewer than $100$ coins earned** ($X = 20$, $Y = 4$ gives $80$): no bag is affordable, so the answer is $0$. The sample includes this.
- **Exactly $100$** ($X = Y = 10$): one bag, with nothing left over.
- **Not a multiple of $100$** ($199$ coins): one bag — the division floors, it does not round, so $199$ must not become $2$.
- **Largest input** ($X = Y = 1000$): $10^6$ coins and $10000$ bags.
- The product is computed before dividing, so no precision is lost; dividing first would floor twice.

## Dry run

| $X$ | $Y$ | coins $XY$ | $//\,100$ | output |
|---:|---:|---:|---:|---|
| 10 | 10 | 100 | 1 | `1` |
| 20 | 4 | 80 | 0 | `0` |
| 70 | 7 | 490 | 4 | `4` |

The last row shows the floor discarding $90$ spare coins.
