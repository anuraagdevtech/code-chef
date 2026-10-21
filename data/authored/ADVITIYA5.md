---
topic: Constructive
subtopic: Parity blocks and the number of switches
time: $O(N)$ per test case
space: $O(N)$
---
$P_i + P_{i+1}$ is odd exactly when the two have **different parity**. So reading the permutation as a string of O's and E's, the answer counts the positions where that string changes — and a string with $b$ maximal blocks has exactly $b - 1$ changes.

So the task is to arrange $\lceil N/2 \rceil$ odd numbers and $\lfloor N/2 \rfloor$ even numbers into exactly

$$b = K + 1$$

alternating blocks. Starting with an odd block, that needs $\lceil b/2 \rceil$ odd blocks and $\lfloor b/2 \rfloor$ even blocks — and both fit, since $b \leq N$ gives $\lceil b/2 \rceil \leq \lceil N/2 \rceil$ and likewise for the evens. So starting with odds always works and no case analysis is needed.

The leftovers go into the **first** block of each parity: give every block one number, then dump the surplus odds into the first odd block and the surplus evens into the first even block. Padding a block never creates a new change, since the block's parity is unchanged.

The constraint $K \geq 1$ guarantees $b \geq 2$, so there is at least one even block to receive the evens — with $b = 1$ there would be nowhere to put them.

For $N = 4, K = 2$ this builds three blocks: odds $[1]$, evens $[2,4]$, odds $[3]$, giving `1 2 4 3` with changes at positions $1$ and $3$. The published sample, `4 3 1 2`, has a different block structure with the same count — **any valid permutation is accepted**, so this is judged by a checker.
