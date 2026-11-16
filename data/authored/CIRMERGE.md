---
topic: Dynamic Programming
subtopic: Interval merging on the doubled circle with Knuth optimisation
time: $O(N^2)$ per test case
space: $O(N^2)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
On a line this is the classic stone-merging DP: the last merge joins a left block and a right block, so

$$\text{cost}(i, j) = \min_{i \le k < j} \bigl(\text{cost}(i, k) + \text{cost}(k+1, j)\bigr) + \text{sum}(i, j).$$

On a circle, the $N - 1$ merges use $N - 1$ of the $N$ adjacencies, so some adjacency is never merged across; cutting the circle there gives a line. Write the array twice and solve the linear problem for every interval of length up to $N$ in the doubled array; the answer is the best interval of length exactly $N$.

The plain DP is cubic. The weights are positive, so the cost function satisfies the quadrangle inequality and the optimal split point is monotone: $\text{opt}(i, j-1) \le \text{opt}(i, j) \le \text{opt}(i+1, j)$. Restricting the search for $k$ to that range (Knuth's optimisation) makes the total work quadratic.

## Edge cases

- $N = 1$: no merge, penalty 0.
- $N = 2$: a single merge costing the total.
- Only intervals up to length $N$ are needed in the doubled array.
- Penalties can exceed 32 bits.

## Dry run

`A = [10, 10, 1]`, doubled `10 10 1 10 10 1`.

Length-2 costs: `20, 11, 11, 20, 11`. Length 3:

- `[10, 10, 1]`: $\min(0 + 11,\; 20 + 0) + 21 = 32$
- `[10, 1, 10]`: $\min(0 + 11,\; 11 + 0) + 21 = 32$
- `[1, 10, 10]`: $\min(0 + 20,\; 11 + 0) + 21 = 32$

Answer 32.
