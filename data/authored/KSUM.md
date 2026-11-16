---
topic: Heaps
subtopic: K-way merge of the decreasing lists of sums per left endpoint
time: $O(N + K \log N)$
space: $O(N + K)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
All elements are positive, so for a fixed left end the subarray sum grows with the right end: the largest sum starting at $l$ is the one reaching the end of the array, the next largest stops one element earlier, and so on. That gives $N$ lists, each already sorted in decreasing order, and the task is to output the $K$ largest values of their union.

Merge them with a max-heap. Initially push, for every left end, the sum of the whole suffix. Each time the maximum is popped, output it and push the next element of the same list - the same left end with the right end moved one step left - if it is still non-empty. Sums come from prefix sums in $O(1)$.

The heap never holds more than $N$ entries and exactly $K$ pops are made.

## Edge cases

- Equal sums from different subarrays are all reported, each as its own entry.
- A list runs out when the subarray would become empty.
- $K$ can be far smaller than $N(N+1)/2$, which is why generating all sums is avoided.
- Python's heap is a min-heap, so sums are stored negated.

## Dry run

`A = [1, 3, 4]`, `K = 4`. Suffix sums by left end: 8, 7, 4.

- pop 8 (left 1); push `[1, 3] = 4`
- pop 7 (left 2); push `[3] = 3`
- pop 4 and then the other 4 - the subarrays `[1, 3]` and `[4]`

Output `8 7 4 4`.
