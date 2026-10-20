---
topic: Sorting
subtopic: Choosing extremes for a product
time: $O(N \log N)$ per test case
space: $O(N)$
---
Maximise $(A_i - A_j) \cdot A_k$ over three pairwise distinct indices. Every $A_i$ is **at least $1$**, which is what makes the answer a clean choice of extremes.

Since all values are positive, the product is largest when both factors are. The difference is maximised by taking $A_i$ as the largest value and $A_j$ as the smallest. That leaves $A_k$ to be the largest value still available, which after sorting is the **second** largest. So with $a$ sorted ascending:

$$(a_{n-1} - a_0) \cdot a_{n-2}$$

The natural worry is whether sacrificing some difference to free up the maximum for $A_k$ could do better — using $a_{n-2}$ and $a_0$ for the difference while $A_k = a_{n-1}$. Comparing the two:

$$(a_{n-1} - a_0)\,a_{n-2} - (a_{n-2} - a_0)\,a_{n-1} = a_0\,(a_{n-1} - a_{n-2}) \geq 0$$

so the first is always at least as good. Positivity of $a_0$ is exactly what decides it; with zeros or negatives allowed the comparison could flip and the problem would be considerably harder.

The triplet is **ordered** and the indices distinct, so the three chosen positions are genuinely different — guaranteed since $N \geq 3$.

Sample case 2, $[3,4,4,1,2]$, sorts to $[1,2,3,4,4]$: $(4-1) \cdot 4 = 12$. Note the two $4$s occupy separate indices, so using one as $A_i$ and the other as $A_k$ is legal — which is why duplicates need no special handling.
