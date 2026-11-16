---
topic: Geometry
subtopic: Precomputed nearest finish, then all pairs in both visiting orders
time: $O(N \cdot M + (N + M) \cdot K)$ per test case
space: $O(N + M + K)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A run is start $\to$ first visited point $\to$ second visited point $\to$ finish, where the two middle points come one from each of the first two sets, in either order.

Once the last middle point is fixed, the finish point should simply be the one nearest to it. So precompute, for every point of the first two sets, its distance from ShareChat and its distance to the nearest point of the third set. Then enumerate every pair $(A_i, C_j)$ and take

$$|A_i C_j| + \min(\text{start}(A_i) + \text{end}(C_j),\; \text{start}(C_j) + \text{end}(A_i)).$$

The sum of $N \cdot M$ over tests is small enough for the quadratic enumeration.

## Edge cases

- Both visiting orders must be tried; the cheaper one depends on the geometry.
- Points may coincide with each other or with ShareChat, giving zero-length legs.
- The answer is a real number; ten decimals are printed and an error of $10^{-6}$ is tolerated.
- `math.hypot` avoids overflow and loss of precision in the squared distance.

## Dry run

Start $(0,0)$, first set $\{(1,0)\}$, second set $\{(2,0)\}$, finish set $\{(3,0)\}$.

Distances from the start: 1 and 2. Distances to the nearest finish: 2 and 1. The pair is 1 apart, so the two orders cost $1 + (1 + 1) = 3$ and $1 + (2 + 2) = 5$.

Answer `3.0000000000`.
