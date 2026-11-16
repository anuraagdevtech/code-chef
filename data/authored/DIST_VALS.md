---
topic: Stacks
subtopic: Largest and second largest of a subarray are neighbours on a monotonic stack
time: $O(N)$ expected per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Take a subarray and let $u, v$ be its largest and second largest elements. Everything between their positions is no larger than the smaller of the two, so the subarray that starts at one of them and ends at the other has the same beauty. The distinct beauties are therefore the differences over pairs of positions such that all elements strictly between them are at most the smaller endpoint.

Those pairs are exactly what a monotonic stack produces. Keep a stack of values that is strictly decreasing from bottom to top. When a new value $x$ arrives:

- every stack element $\le x$ is popped; it sees $x$ as the first element to its right that is at least as large, giving the pair with difference $x -$ (popped);
- the element left on top, if any, is larger than $x$ and is the nearest larger element to the left of $x$, giving the pair with difference (top) $- x$.

Collect the differences in a set and print its size.

## Edge cases

- Equal neighbours give beauty 0; equal values are popped, which records it.
- $N = 2$ has exactly one subarray.
- Each element is pushed and popped once, so the number of candidate pairs is at most $2N$.
- Only distinct values of beauty are counted.

## Dry run

`A = [8, 1, 7, 2]`.

- 8: push. Stack `8`.
- 1: top 8 is larger: record $8 - 1 = 7$. Stack `8 1`.
- 7: pop 1, record $7 - 1 = 6$; top 8 is larger: record $8 - 7 = 1$. Stack `8 7`.
- 2: top 7 is larger: record $7 - 2 = 5$. Stack `8 7 2`.

Distinct beauties `{7, 6, 1, 5}`: answer 4.
