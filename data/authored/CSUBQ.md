---
topic: Trees
subtopic: Segment tree counting all-good subarrays, used at two thresholds
time: $O((N + Q) \log N)$
space: $O(N)$ in packed arrays
complexity_note: Auxiliary space excludes the buffered input and output.
---
The maximum of a subarray lies in $[L, R]$ exactly when all elements are $\le R$ but not all are $\le L - 1$. So

$$\text{answer} = \#\{\text{subarrays with all elements} \le R\} - \#\{\text{subarrays with all elements} \le L - 1\}.$$

Each of the two counts is a classic segment-tree monoid. Mark an element good if it is within the threshold. A node stores its length, the length of its good prefix, the length of its good suffix and the number of all-good subarrays inside it. Merging two children adds their counts plus (good suffix of the left) $\times$ (good prefix of the right) for the subarrays crossing the middle; the prefix extends into the right child only if the left child is entirely good, and symmetrically for the suffix.

A point update recomputes one leaf-to-root path for both thresholds; a range query combines the $O(\log N)$ covering nodes from the left and from the right, keeping the order of the pieces.

## Edge cases

- All elements start at 0, which is good for both thresholds when $L \ge 1$, so the trees start fully good.
- The merge is not commutative; left-side and right-side partial results are accumulated separately.
- Counts are about $N^2 / 2$, so 64-bit storage is used.
- An update that leaves the element's status unchanged is still processed safely.

## Dry run

`N = 5, L = 1, R = 10`.

After `A = [2, 0, 0, 0, 0]`, query `[1, 5]`: all five elements are $\le 10$, giving $5 \cdot 6 / 2 = 15$ subarrays. Elements $\le 0$ are positions 2-5, a run of 4, giving $4 \cdot 5 / 2 = 10$.

Answer $15 - 10 = 5$ - the subarrays that contain position 1.
