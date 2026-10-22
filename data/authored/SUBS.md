---
topic: Sorting
subtopic: Sliding a fixed-size window
time: $O(N \log N)$ per test case
space: $O(N)$
---
The spread of a chosen set depends only on its largest and smallest members, so the middle elements are free. That means an optimal choice of $K$ elements can always be taken **contiguous in sorted order**: if two chosen values have an unchosen value between them, swapping it in never widens the spread.

So sort the array and slide a window of width $K$, taking the best:

$$\min_{0 \leq i \leq N-K} \bigl(A_{i+K-1} - A_i\bigr)$$

Sorting dominates at $O(N \log N)$; the sweep itself is linear with no extra storage.

The contiguity argument is what makes this cheap. Without it one might consider $\binom{N}{K}$ subsets, which is hopeless at $N = 10^5$.

Sample case 1, $[1,2,4,7]$ with $K = 3$, has windows $[1,2,4]$ spanning $3$ and $[2,4,7]$ spanning $5$ — so $3$. Note the best window is **not** the one containing the two closest elements in isolation; it is the tightest run of three.

Sample case 3, $[1,5,44,20,40]$ with $K = 4$, sorts to $[1,5,20,40,44]$ with both windows spanning $39$ — a tie, which needs no special handling.

Duplicates give a span of $0$ and are handled naturally. When $K = N$ there is a single window, the whole array, and when $K = 1$ every window has width $0$.

## Edge cases

- **An optimal choice is contiguous once sorted.** If two chosen elements straddle an unchosen one, swapping it in can only shrink the spread — so sliding a window of size $K$ over the sorted array covers every candidate.
- **The spread of a window is its last element minus its first**, since the array is sorted — no per-window maximum or minimum is needed.
- **$K = N$ leaves one window**, giving the full spread of the array.
- **$K = 1$ gives $0$**, as a single element has no spread.
- **Duplicates can give $0$** when $K$ of them coincide, which the window finds without a special case.
- **The window count is $N - K + 1$**, which is at least $1$ since $K \leq N$ is guaranteed.
- **$A_i$ may be $0$**, and the values reach $10^9$, so the spread fits comfortably.
- **Sum of $N$ up to $2 \cdot 10^6$**: one sort per case and one linear sweep.

## Dry run

Third sample: $A = 1, 5, 44, 20, 40$ sorted to $1, 5, 20, 40, 44$, with $K = 4$.

| window | spread |
|---|---:|
| $1, 5, 20, 40$ | $40 - 1 = 39$ |
| $5, 20, 40, 44$ | $44 - 5 = 39$ |

Both tie, so the answer is `39`.
