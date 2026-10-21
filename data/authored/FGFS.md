---
topic: Greedy
subtopic: Independent activity selection per compartment
time: $O(N \log N)$ per test case
space: $O(N)$
---
Each customer insists on one compartment, so the compartments never interact: the problem **decomposes** into $K$ independent instances, and only the compartments that actually appear matter — which is what makes $K$ up to $10^9$ harmless.

Within a compartment, a customer occupies the half-open interval $[s_i, f_i)$, and two customers are compatible when their intervals do not overlap. Maximising the count is the classic **activity-selection** problem, solved by sorting on finishing time and taking each interval whose start is at or after the last accepted finish:

$$\text{accept } i \iff s_i \geq f_{\text{last}}$$

The exchange argument: among any optimal solution's intervals, replacing the first by the globally earliest-finishing one keeps it feasible, since that one ends no later and so blocks no more of the future. Induction does the rest.

Half-open intervals are the detail to get right — a customer leaving at $f$ frees the compartment *at* $f$, so the comparison is $\geq$, not $>$. The second sample turns on it: in compartment $2$, the customer $[100,200)$ is followed by $[200,300)$, which fits exactly, while $[150,500)$ would collide.

Grouping by compartment with a dictionary and sorting each group gives $O(N \log N)$ overall. Note $N$ may be $0$, in which case the answer is $0$ and no groups exist.

The first sample has three customers in three different compartments, so all three dine. The second has one in compartment $1$ and three in compartment $2$, of which two are compatible — total $3$.
