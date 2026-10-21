---
topic: Prefix Sums
subtopic: Alternating hits balance two totals
time: $O(N)$ per test case
space: $O(N)$
---
A ball launched from an empty cell strikes walls **alternately**: one on the side it was pushed toward, then one on the other side, and so on, each strike removing exactly one unit of height. It leaves the array the moment it travels toward a side with nothing left.

So only the **total wall height on each side** matters. Let $L$ and $R$ be the sums to the left and right of the starting index.

Pushed right, the strikes land R, L, R, L, …. For every wall to be destroyed, the alternation must consume both totals exactly:

- $R = L$ — the strikes pair off perfectly, and after the final left strike the ball turns right into an empty array;
- $R = L + 1$ — one extra right strike leads the sequence, and after it the ball turns left into nothing.

Any other relationship strands height on one side. So pushing right succeeds exactly when $R - L \in \{0, 1\}$, and by symmetry pushing left succeeds when $L - R \in \{0, 1\}$.

Counting per empty cell: both directions work when $L = R$ (contributing $2$), exactly one works when the totals differ by one, and nothing works otherwise.

Prefix sums give $L$ and $R$ for every index in one pass.

Sample case 2, $[1,1,0,1,1]$, has the only gap perfectly balanced at $L = R = 2$, so both pushes work — answer $2$. Sample case 3's second gap has $L = 11$ against $R = 0$ and contributes nothing, while the first gap differs by exactly one and contributes a single way.

Heights reach $10^9$ with $N$ up to $10^5$, so the side totals reach $10^{14}$ — **64-bit** territory outside Python.
