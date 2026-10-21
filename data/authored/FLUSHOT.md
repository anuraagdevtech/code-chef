---
topic: Binary Search
subtopic: Binary search on a real-valued answer
time: $O(N \log \frac{1}{\varepsilon})$ per test case
space: $O(N)$
---
Ask whether a given maximum movement $D$ suffices. Each person $i$ may end up anywhere in $[x_i - D,\ x_i + D]$, clipped below at $0$ since nobody may pass the receptionist, and consecutive people must sit at least $T$ apart.

That feasibility test is a **left-greedy sweep**: push each person as far left as the rules permit.

$$p_1 = \max(0,\ x_1 - D), \qquad p_i = \max(p_{i-1} + T,\ x_i - D)$$

and the arrangement fails the moment some $p_i$ exceeds $x_i + D$. Placing each person as early as possible is optimal because it leaves the most room for everyone after them — any feasible arrangement can be slid left to this one.

Since the people arrive in non-decreasing order, keeping them in that order is also optimal: swapping two would only widen the distance one of them must travel.

Feasibility is monotone in $D$ — more slack never hurts — so a **binary search on the real line** finds the threshold. About $100$ halvings take the interval well below the $10^{-4}$ the output needs.

Sample case 3 is the instructive one. Three people crowd near the receptionist at $0$, $0.5$ and $0.6$ while a fourth sits far off at $2.75$. The cramped trio must spread to $0$, $1$ and $2$, and it is the person at $0.6$ who moves furthest — $1.4$ — not the isolated one, who barely shifts.

The answer is printed to four decimal places, matching the published format.
