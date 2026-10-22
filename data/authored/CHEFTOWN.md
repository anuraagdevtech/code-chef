---
topic: Arrays
subtopic: Sliding-window maximum and minimum with deques
time: $O(N)$
space: $O(N)$
---
The heights are a **permutation** of $1 \ldots N$, and that single fact replaces the whole sorting-and-comparing definition. A window of length $W$ therefore holds $W$ *distinct* values, and $W$ distinct integers are consecutive exactly when their span is $W - 1$:

$$\max - \min = W - 1$$

($\geq W-1$ always holds for $W$ distinct integers, and equality forces every value in $[\min, \max]$ to be present.) So the task is: slide a window of length $W$ and count the positions where its span is $W - 1$.

Both window extremes come from **monotonic deques**. For the maximum, hold indices whose values are strictly decreasing: before pushing index $i$, pop from the back every index whose value is $\leq H_i$, since a smaller value that is also older can never be the maximum again. Pop from the front once it falls out of the window. The minimum is the mirror image, with an increasing deque. Each index enters and leaves each deque once, so the sweep is linear rather than the $O(N \log N)$ a heap or balanced tree would cost — which matters at $N = 4 \times 10^5$.

Note the input format is unusual for CodeChef: there is **no leading $T$**, just $N$ and $W$ followed by the heights.

In the sample $N = 2$ and $W = 1$. Every single-element window trivially has span $0 = W - 1$, so both positions count and the answer is $2$. The degenerate $W = 1$ case needs no special handling — the formula covers it.

## Edge cases

- **$H$ is a permutation, so every window holds distinct heights** — which means a window of length $W$ has consecutive values exactly when its maximum minus its minimum equals $W - 1$. No sorting or counting is needed.
- **Both a sliding maximum and a sliding minimum are required**, each maintained by a monotone deque so that every window is answered in amortised constant time.
- **The deques hold indices, not values**, so the expiry check can compare against the window's left edge.
- **Expiry must be checked after pushing**, and only the front can expire — which is why a single `if` suffices rather than a loop.
- **Windows before the array is full are skipped**, hence the early continue until the left edge reaches $0$.
- **$W = 1$ makes every window interesting**, since the maximum and minimum coincide and $W - 1 = 0$ — the first sample counts both positions.
- **$W = N$ leaves one window**, which is interesting precisely because $H$ is a permutation of $1 \dots N$.
- **There is no test-case count**, and $N$ reaches $4 \cdot 10^5$, so the deque approach is what keeps it linear.

## Dry run

Second sample: $H = 1, 2, 3, 4$ with $W = 2$.

| window | maximum | minimum | difference | interesting? |
|---|---:|---:|---:|:---:|
| $1, 2$ | 2 | 1 | 1 | yes |
| $2, 3$ | 3 | 2 | 1 | yes |
| $3, 4$ | 4 | 3 | 1 | yes |

Output `3`.
