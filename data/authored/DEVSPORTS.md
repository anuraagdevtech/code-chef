---
topic: Basic Math
subtopic: Remaining budget against a total cost
time: $O(1)$ per test case
space: $O(1)$
---
Devendra started with $Z$ and has already spent $Y$, so he has $Z - Y$ left. He wants each of the three sports at least once, costing $A + B + C$ in total. He can manage when

$$Z - Y \geq A + B + C$$

The phrase "at least once" might suggest something more involved, but since prices are fixed and there is no discount for repeats, trying each exactly once is the cheapest way to try each at least once. So the minimum spend is simply the sum, and no optimisation is needed.

The comparison is inclusive: spending his remaining money down to exactly zero still counts. Sample case 3 is precisely this, with $10000$ remaining against a total of $10000$, giving `YES`. A strict `>` would fail it.

Sample case 1 is the near miss — $3000$ left against $3200$ of sports — and shows that the already-spent $Y$ must be subtracted first. Comparing $Z$ against the total instead would wrongly pass every case here, since $Z \geq 10^4$ while the three sports cost at most $15000$ but usually far less.

All quantities are small integers, so there is nothing to watch for numerically; the whole problem is reading the five values in the right order, $Z, Y, A, B, C$.
