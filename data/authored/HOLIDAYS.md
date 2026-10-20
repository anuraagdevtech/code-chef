---
topic: Greedy
subtopic: Take the largest items first
time: $O(N \log N)$ per test case
space: $O(N)$
---
Maximising holidays is the same as **minimising days worked** while still earning $W$. Since Ved may work on any subset of days, he should work the most lucrative ones: sort the earnings descending and take them until the running total reaches $W$.

The greedy is optimal by an exchange argument. Suppose an optimal schedule of $m$ days omits one of the $m$ highest-earning days in favour of a lower one; swapping them keeps the day count the same and cannot lower the total. Repeating this turns any optimal schedule into the greedy one, so the greedy uses no more days than any alternative.

Holidays are then $N$ minus the days worked.

The guarantee that working every day earns at least $W$ means the loop always terminates with the target met, so no "impossible" case arises.

Sample case 3 is the striking one: a single day earning $12$ covers the $8$ required, so Ved rests for $5$ of $6$ days. Sorting matters here — taking days in input order would start with $9$, also enough, but on other inputs it would take more days than necessary.

Sample case 2 needs every day: the earnings sum to exactly $15 = W$, leaving zero holidays. That is the boundary where the `>=` comparison must be inclusive.

Sample case 1 takes $6 + 3 + 3 = 12 \geq 10$ in three days, leaving two holidays — note it stops as soon as the threshold is crossed rather than matching $W$ exactly.
