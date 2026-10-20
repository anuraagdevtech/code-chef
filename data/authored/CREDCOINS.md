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
