---
topic: Dynamic Programming
subtopic: Two arrays per count - subarray still open, or best so far
time: $O(N \cdot K)$ per test case
space: $O(K)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Process the array from left to right and keep, for every $j \le K$:

- `end[j]`: the best score when the $j$-th subarray ends exactly at the current element;
- `best[j]`: the best score using $j$ subarrays within the prefix processed so far.

For a new element $x$, the $j$-th subarray ending here either extends the $j$-th subarray that ended at the previous element, or starts fresh after the best arrangement of $j - 1$ subarrays in the earlier prefix; in both cases $x$ is added with weight $j$:

$$\text{end}[j] = \max(\text{end}[j],\; \text{best}[j-1]) + j \cdot x, \qquad \text{best}[j] = \max(\text{best}[j],\; \text{end}[j]).$$

Updating $j$ from $K$ down to 1 ensures that `best[j-1]` still refers to the prefix before the current element, so the subarrays stay disjoint. The answer is `best[K]`.

## Edge cases

- Exactly $K$ non-empty subarrays are required, so `best[K]` may be negative.
- Elements may be skipped between subarrays.
- Unreachable states use a large negative sentinel that never wins a maximum.
- The weights make the order of subarrays matter - later ones count more.

## Dry run

`A = [1, 2, -1, 3, 1]`, `K = 2`. Values of (`best[1]`, `best[2]`) after each element:

| element | end[1] | best[1] | end[2] | best[2] |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | - | - |
| 2 | 3 | 3 | 5 | 5 |
| -1 | 2 | 3 | 3 | 5 |
| 3 | 5 | 5 | 9 | 9 |
| 1 | 6 | 6 | 11 | 11 |

Answer 11: `[1, 2]` with weight 1 and `[3, 1]` with weight 2.
