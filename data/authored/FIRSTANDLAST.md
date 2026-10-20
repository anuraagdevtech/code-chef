---
topic: Arrays
subtopic: Cyclically adjacent pairs
time: $O(N)$ per test case
space: $O(1)$
---
The key observation is what a right rotation does to the *pair* $(A_1, A_N)$, not to the array as a whole.

Initially the first and last elements are $A_1$ and $A_N$ — which are **cyclically adjacent**, since the array wraps from $A_N$ back to $A_1$. After one right rotation the array is $[A_N, A_1, \ldots, A_{N-1}]$, whose ends are $A_N$ and $A_{N-1}$: adjacent again. Each rotation simply slides the split point by one.

So every reachable pair is a cyclically adjacent pair, and every such pair is reachable. The answer is

$$\max_{0 \leq i < N} \left( A_i + A_{(i+1) \bmod N} \right)$$

one pass, $O(N)$ time and $O(1)$ space. No rotation is ever performed — simulating all $N$ rotations would be $O(N^2)$ and far too slow at $N = 10^5$.

The wraparound term is essential and easy to drop. Sample case 2, $[5, 10, 15]$, has adjacent sums $15$ and $25$ from the interior pairs and $20$ from the wrapping pair $(15, 5)$; here the interior wins, but on an array like $[9, 1, 9]$ only the wrapping pair gives the maximum $18$.

Sample case 1 with $N = 2$ is a degenerate case worth checking: both elements are adjacent to each other in both directions, and the sum $13$ is the only possible answer.

Values reach $10^9$, so a pair sums to $2 \times 10^9$ — past the signed 32-bit limit, which a C solution would need to handle with a 64-bit type.
