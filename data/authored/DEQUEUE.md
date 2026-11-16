---
topic: Arrays
subtopic: Keep the longest middle part that does not swallow all copies of any value
time: $O(N + M)$ per test case
space: $O(N + M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Popping from the two ends leaves a contiguous middle part (possibly empty). The popped elements contain every value from 1 to $N$ exactly when the middle part does *not* contain all occurrences of any value. Minimising the number of pops is the same as maximising the length of such a middle part.

"Does not contain all occurrences of any value" is preserved when the window shrinks, so two pointers work: extend the right end by one element; if the window now holds every occurrence of that element's value, move the left end forward until one occurrence of it has left the window. (No other value can be violated - only the count of the new element grew.) Track the longest window seen; the answer is $M$ minus its length.

## Edge cases

- If every value occurs exactly once, the middle part must be empty and everything is popped.
- The middle part may be empty even otherwise.
- Popping only from one end is covered - the window may touch either end of the queue.
- Values are shifted to 0-based for indexing.

## Dry run

`Q = [1, 1, 1, 3, 2, 2]`, $N = 3$. Totals: value 1 three times, value 2 twice, value 3 once.

The middle part cannot contain the 3 at all, at most two of the 1s and at most one of the 2s. The longest such window is `1 1` (length 2).

Answer $6 - 2 = 4$.
