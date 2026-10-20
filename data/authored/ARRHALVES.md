---
topic: Arrays
subtopic: Minimum adjacent swaps to gather a set
time: $O(N)$ per test case
space: $O(N)$
---
Since $P$ is a permutation of $1 \ldots 2N$, "max of the first half below min of the second half" can only mean the first half holds exactly $\{1, \ldots, N\}$ and the second holds $\{N+1, \ldots, 2N\}$. **Their order within each half is irrelevant.**

So the task is: move the $N$ small values into the first $N$ positions, using adjacent swaps, as cheaply as possible.

The classic result applies. If the small values currently sit at positions $p_1 < p_2 < \cdots < p_N$ (zero-indexed), the minimum number of adjacent swaps to gather them into the first $N$ slots is

$$\sum_{i=0}^{N-1} (p_i - i)$$

The reasoning: the relative order of the small values never needs to change — swapping two of them is wasted work — so the $i$-th small value from the left is destined for slot $i$, and each must step past exactly the large values standing before it. The sum counts precisely those crossings.

That subtraction of $i$ is what prevents double-counting. Summing the raw positions would also charge each small value for the small values ahead of it, which it never has to cross.

Sample case 3 is the worst case: $[6,5,4,3,2,1]$ has its small values at positions $3,4,5$, giving $(3-0)+(4-1)+(5-2) = 9$. Sample case 2 is already good at $0$ cost. Sample case 1, $[3,2,1,4]$ with $N=2$, has small values at $1$ and $2$, giving $1 + 1 = 2$ — note the result is already good without sorting either half.

The answer can reach about $N^2 \approx 10^{10}$, which **overflows 32 bits** — Python is fine, but a C solution needs a 64-bit accumulator.
