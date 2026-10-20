---
topic: Greedy
subtopic: Choosing between mutually exclusive groups
time: $O(1)$ per test case
space: $O(1)$
---
Region $B$ conflicts with both $A$ and $C$, while $A$ and $C$ have no quarrel with each other. So any peaceful guest list is one of two shapes:

- invite $B$ alone, seating $P_B$ people;
- invite $A$ and $C$ together, seating $P_A + P_C$.

Those are the only maximal options, so the answer is

$$\max(P_B,\; P_A + P_C)$$

The key observation is that $A$ and $C$ are **not** in conflict, so there is never a reason to invite just one of them — taking both is free. That collapses what looks like a subset-selection problem over three groups into a choice between two candidates. Inviting nobody, or only $A$, are both dominated.

Sample case 2 is the case where $B$ wins: $P_B = 5$ beats $P_A + P_C = 3$. The other two samples favour the $A+C$ coalition. A solution that always picked $A + C$, or always picked the single largest region, would fail one of these.

This is the smallest instance of the **maximum weight independent set** problem on a graph — here a path $A - B - C$, where the two independent sets worth considering are $\{B\}$ and $\{A, C\}$. On larger graphs that problem is genuinely hard, but on a three-vertex path the enumeration is immediate.
