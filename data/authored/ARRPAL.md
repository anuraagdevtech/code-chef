---
topic: Arrays
subtopic: Prefix increments force a non-increasing profile
time: $O(N)$ per test case
space: $O(1)$
---
Let $d_j$ be how many operations cover index $j$. Since every operation covers a **prefix**, an operation covering $j$ also covers everything before it, so

$$d_1 \geq d_2 \geq \cdots \geq d_N \geq 0$$

and the total number of operations is $d_1$ — every operation covers index $1$.

The final array is $A_j + d_j$, and the palindrome requirement pairs $j$ with $N+1-j$:

$$d_j - d_{N+1-j} = A_{N+1-j} - A_j =: \delta_j$$

Two conditions follow, and both are necessary.

**Each $\delta_j \geq 0$.** Because $j < N+1-j$ and $d$ is non-increasing, the left side cannot be negative. So the mirror element must already be at least as large — sample case 2, $[5,4,3,2,1]$, fails immediately with $\delta_1 = 1 - 5 < 0$.

**The $\delta_j$ must themselves be non-increasing.** Expanding $\delta_j - \delta_{j+1} = (d_j - d_{j+1}) + (d_{N-j} - d_{N+1-j})$ shows it is a sum of two non-negative terms.

When both hold, the construction is immediate: set $d_j = \delta_j$ on the first half and $d_j = 0$ on the second. That is non-increasing and satisfies every pairing, so the answer is

$$d_1 = \delta_1 = A_N - A_1$$

Sample case 3, $[1,2,3,4]$, has $\delta = (3, 1)$ — non-negative and non-increasing — giving $3$. Sample case 1 is already a palindrome with $\delta = (0,0)$, so zero operations.
