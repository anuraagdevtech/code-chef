---
topic: Basic Math
subtopic: Ceiling division
time: $O(1)$ per test case
space: $O(1)$
---
A car seats at most $4$ people and $N$ friends must all travel, so the leftover group of fewer than four still needs a car of its own:

$$\left\lceil \frac{N}{4} \right\rceil$$

computed in integers as `(n + 3) // 4`.

This is the third ceiling-division problem in the set — after the subscriptions and the pizzas — and the repetition is deliberate. The recognisable signature is *"items have a fixed capacity, everyone must be served, partial units round up"*. Contrast it with the CRED-coins problem, where the leftover was simply wasted and the division floored instead. Deciding which way the remainder pushes is the entire decision.

The identity $\lceil n/k \rceil = \lfloor (n + k - 1)/k \rfloor$ keeps everything in integer arithmetic, so there is no float and no `math.ceil`.

Sample case 4 is a good check that the formula does not overshoot on a clean division's neighbour: $N = 98$ gives $(98 + 3)//4 = 25$ cars, carrying $100$ seats for $98$ people, while $N = 4$ gives exactly $1$ rather than $2$.
