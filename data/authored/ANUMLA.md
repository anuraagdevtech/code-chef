---
topic: Greedy
subtopic: Smallest unexplained subset sum is the next element
time: $O(N \cdot 2^N)$ per test case
space: $O(2^N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Sort the $2^N$ subset sums and keep them as a multiset. Remove one 0 for the empty subset.

All elements are positive, so the smallest sum that is not yet explained by the elements found so far must be a single new element: any subset using two or more undiscovered elements, or an undiscovered element together with known ones, has a larger sum. Take it as the next element $x$. Every already known subset sum $s$ now also produces $s + x$; remove all of those from the multiset and append them to the list of known sums.

Repeat until $N$ elements are found. Scanning the sorted list once and skipping values whose multiplicity has dropped to zero yields the elements in non-decreasing order, which is the required output order.

## Edge cases

- Duplicate elements are handled by multiplicities - the Counter never goes negative on valid input.
- $N = 1$: the sums are `0` and the element.
- The list of known sums doubles each time, for $2^N$ in total.
- The output must be sorted in non-decreasing order.

## Dry run

Sums `0 1 1 2`, $N = 2$. After removing the empty subset the multiset is `{1, 1, 2}`; known sums `[0]`.

- Smallest remaining is 1: element 1. New sums `[1]`; multiset `{1, 2}`; known `[0, 1]`.
- Smallest remaining is 1: element 1. New sums `[1, 2]`; multiset empty.

Output `1 1`.
