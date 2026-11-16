---
topic: Constructive
subtopic: Only two obstructions - K = N, and a parity clash
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
If $K = N$ every operation raises all elements together, so nothing relative ever changes: the array must already be a palindrome.

If $K < N$, two operations that differ in a single index have the net effect "add 1 to $i$" versus "add 1 to $j$". Combining such pairs on top of a large common number of operations lets us move single units around freely, so any target of non-negative increments is reachable as long as the total number of increments is a multiple of $K$ (and large enough). To make the array a palindrome we need increments that equalise each mirrored pair; adding the same amount to both members of a pair, or to the middle element, adjusts the total without breaking the palindrome.

- $N$ odd: the middle element absorbs any amount, so the total can be fixed to a multiple of $K$.
- $N$ even: the final sum is even, because it is twice the sum of one half. If $K$ is odd the parity of the sum can be changed by one more operation, so it is fine; if $K$ is even the parity of the sum never changes, and the initial sum has to be even.

So for $K < N$ the answer is No only when $N$ and $K$ are even and the sum is odd.

## Edge cases

- $K = N$ depends on the actual values; all other cases depend only on parities.
- $N = 1$ forces $K = 1 = N$, and a single element is a palindrome.
- $K = 1$ with $N > 1$ is always Yes.
- The increments needed can be large, but the question is only about existence.

## Dry run

- `N = 4, K = 2, A = [1, 2, 3, 3]`: both even and the sum 9 is odd - NO.
- `N = 6, K = 2, A = [4, 5, 5, 4, 6, 4]`: both even and the sum 28 is even - YES.
- `N = 5, K = 3`: $N$ is odd - YES whatever the values.
