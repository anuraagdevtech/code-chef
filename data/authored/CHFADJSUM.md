---
topic: Greedy
subtopic: Keeping the heaviest elements apart
time: $O(N)$ per test case
space: $O(1)$
---
$Z$ is the largest sum any pair can make, so adjacent sums are automatically $\leq Z$ and the question is purely whether the pairs achieving **exactly** $Z$ can be kept non-adjacent. Writing $b_1 \geq b_2$ for the two largest values, a pair sums to $Z = b_1 + b_2$ only if its values are precisely $b_1$ and $b_2$.

That splits into two cases.

**The maximum is repeated** ($b_1 = b_2 = m$, occurring $p$ times). The bad pairs are two copies of $m$ side by side, so the $p$ copies must be mutually non-adjacent. Separating $p$ items among $N$ positions is possible exactly when

$$p \leq \left\lceil \frac{N}{2} \right\rceil$$

Sample case 1, $[3,4,4]$, has $p = 2$ against $\lceil 3/2 \rceil = 2$ — just enough, via $4\;3\;4$. Sample case 3, $[2,2]$, has $p = 2$ against $\lceil 2/2 \rceil = 1$, so `NO`.

**The maximum is unique.** Then $b_1$ occurs once and the bad pairs are $b_1$ beside any copy of $b_2$. Placing $b_1$ at an **end** leaves it a single neighbour, which only needs to be some element strictly below $b_2$. So the answer is `YES` exactly when such an element exists — that is, when the count $q$ of $b_2$-valued elements satisfies $N \geq q + 2$.

Sample case 4, $[1,2]$, has $q = 1$ and $N = 2 < 3$, so the $2$ is forced beside the $1$ — `NO`. Sample case 2, $[1,2,3,4]$, has $q = 1$ and $N = 4$, so $4\;1\;3\;2$ works.

Note $N = 2$ always fails under either branch, since the only arrangement puts the top two together.
