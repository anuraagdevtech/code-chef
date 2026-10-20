---
topic: Basic Math
subtopic: Ceiling division
time: $O(1)$ per test case
space: $O(1)$
---
$N$ friends each want $X$ slices, so the group needs $N \cdot X$ slices in total. A pizza yields $4$ slices and pizzas are only sold whole, so the number to order is

$$\left\lceil \frac{N \cdot X}{4} \right\rceil$$

Leftover slices are fine; being short by even one is not. That asymmetry is what forces a **ceiling** here, in contrast to the floor used when spending a fixed budget.

As with the subscriptions problem, compute the ceiling in integers using

$$\left\lceil \frac{n}{k} \right\rceil = \left\lfloor \frac{n + k - 1}{k} \right\rfloor$$

so the expression is `(n * x + 3) // 4`. A useful sanity check is that the formula must return the exact quotient when the division is clean and never overshoot: with $N \cdot X = 12$ it gives $(12 + 3) // 4 = 3$, not $4$.

Sample case 3 is the clean-division case ($4 \times 3 = 12$ slices, exactly $3$ pizzas) and case 1 is the ragged one ($1 \times 5 = 5$ slices, needing $2$ pizzas and wasting $3$ slices).
