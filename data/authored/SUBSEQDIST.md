---
topic: Combinatorics
subtopic: Operations as bits of a distinguishing code
time: $O(N)$ per test case
space: $O(N)$
---
After $k$ operations with increments $X_1, \ldots, X_k$, element $i$ has become

$$A_i + \sum_{j \in S_i} X_j$$

where $S_i \subseteq \{1, \ldots, k\}$ records which operations included it. So the operations act as **$k$ bits of a code** assigned to each element.

Two elements that started equal can only be separated if their codes differ, so a value occurring $m$ times needs $m$ distinct codes:

$$2^k \geq m \quad\Longleftrightarrow\quad k \geq \lceil \log_2 m \rceil$$

and the binding case is the largest multiplicity. That bound is achievable: pick the $X_j$ wildly separated (say $X_j = 10^{18} \cdot 4^{\,j}$), so distinct codes give distinct sums and elements from different original values never collide. Hence

$$\text{answer} = \lceil \log_2 (\max_v \mathrm{cnt}_v) \rceil$$

computed as `(m - 1).bit_length()`.

The key realisation is that one operation can fix *many* duplicate groups at once, since the chosen subsequence is arbitrary — so the answer depends only on the worst group, not on how many groups there are. The second sample shows this: $[1,3,2,1,2,2]$ has a pair of $1$s and a triple of $2$s, and the same two operations resolve both, giving $2$ rather than $1 + 2$.

The other samples: three equal elements need $2$ operations since $2^1 < 3$; two pairs need only $1$; and an already-distinct array needs none.
