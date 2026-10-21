---
topic: Constructive
subtopic: Multiplicity bounds for a bitonic arrangement
time: $O(N \log N)$ per test case
space: $O(N)$
---
The target shape is a single peak: $a_1 < \cdots < a_p > a_{p+1} > \cdots > a_N$. Both arms are **strictly** monotone, so each arm uses any value at most once, and the peak belongs to both arms. That pins down feasibility entirely:

- every value occurs **at most twice** — once on the way up, once on the way down;
- the **maximum** occurs **exactly once** — it must be the peak, since every other position is strictly below its neighbour toward the peak.

Those two conditions are also sufficient, and the construction reads straight off them. Sort the distinct values ascending to form the ascending arm; then let the descending arm be the values with multiplicity two, in descending order:

$$[\,v_1,\, v_2,\, \ldots,\, v_m,\ \underbrace{\ldots}_{\text{doubled values, descending}}\,]$$

The ascending arm is strictly increasing because the $v_i$ are distinct, and the descending arm is strictly decreasing for the same reason. The join is strict because the maximum $v_m$ is unique, so the first element of the descending arm is strictly below it — which is exactly why the "maximum occurs once" condition is needed and not merely convenient.

The samples cover each failure mode. $[1,10,10,10,20,15]$ fails on multiplicity three. $[1,2,3,3]$ has all counts at most two but the maximum $3$ doubled, so no legal peak exists. $[1,1,2,2,3]$ satisfies both and yields `1 2 3 2 1`.

Note the first two samples are the identical input printed twice, with the expected outputs `1 2 3 4` and `4 3 2 1` — both valid, since $p$ may be $N$ (an empty descending arm) or $1$ (an empty ascending arm). Our construction always produces the former shape when every value is distinct.
