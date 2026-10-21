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

## Edge cases

- **The obvious alternative is never better.** Using the second-largest in the difference and the largest as the multiplier gives $(a_{n-1} - a_1) \cdot a_n$, and the chosen form beats it by $a_1 (a_n - a_{n-1}) \geq 0$ — non-negative because every value is positive. The third row shows the gap concretely: $126$ against $92$.
- **All values positive is essential.** With negatives the largest product could come from quite different positions, and this two-line argument collapses.
- **$N = 3$** (the first row): the three elements are forced, and the multiplier is simply the middle one.
- **Duplicates at the top** (the second row, two $4$s): the maximum and second-maximum are equal, which sorted indices handle without a tie-break.
- **All values equal** → the difference is $0$ and so is the answer.
- **Products reach $10^6 \times 10^6 = 10^{12}$**, past 32-bit signed.

## Dry run

Third sample: $23, 17, 21, 18, 19$ sorted to $17, 18, 19, 21, 23$.

| choice | difference | multiplier | product |
|---|---:|---:|---:|
| max $-$ min, times second-max | $23 - 17 = 6$ | 21 | **126** |
| second-max $-$ min, times max | $21 - 17 = 4$ | 23 | 92 |

Output `126`, and the margin is $a_1(a_n - a_{n-1}) = 17 \cdot 2 = 34$.
