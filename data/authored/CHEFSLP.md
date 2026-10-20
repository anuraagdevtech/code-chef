---
topic: Basic Math
subtopic: Pairing limited by the scarcer side
time: $O(1)$ per test case
space: $O(1)$
---
Of the $N$ slippers, $L$ are left and the remaining $N - L$ are right. A sellable pair needs one of each, so the number of pairs is limited by whichever side is scarcer:

$$\text{pairs} = \min(L,\; N - L)$$

and the revenue is that count times $X$.

Taking the minimum is the whole idea — surplus slippers on the abundant side are unsellable, exactly as the spare left shoes were useless in the shoes problem. Sample case 4 shows it: $7$ left and $3$ right out of $10$ yields only $3$ pairs, stranding four left slippers.

Sample case 3 is the opposite imbalance, with $10$ left against $990$ right giving $10$ pairs — the small side binds, whichever side it happens to be, which is why `min` is used rather than assuming lefts are scarce.

Two degenerate inputs are inside the constraints and both work without special handling. $N = 0$ gives zero pairs, and $X = 0$ makes the revenue zero regardless of how many pairs exist — sample cases 1 and 2 respectively. Neither needs a guard, but it is worth noticing that a zero answer can arise for two quite different reasons.
