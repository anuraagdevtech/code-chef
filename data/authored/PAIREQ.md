---
topic: Arrays
subtopic: Keep the most frequent value
time: $O(N)$ per test case
space: $O(N)$
---
Each operation overwrites one element with the value of another, so it fixes **exactly one** mismatched element per move. The final common value must be one already present in the array, since the operation only ever copies existing values.

To minimise moves, choose the value that is already most common and overwrite everything else:

$$N - \max_v (\text{count of } v)$$

The lower bound is clear — every element not already equal to the target needs its own operation — and the construction matches it, so the bound is tight. Choosing any less frequent value would only leave more elements to fix.

`collections.Counter(...).most_common(1)` gives the modal frequency in one pass.

Sample case 1, $[1,2,3]$, has every value unique, so the mode count is $1$ and two operations are needed. Sample case 3, $[2,2,1,1]$, has a tie at frequency $2$; either value works and the answer is $2$ — ties need no tie-breaking, since only the count enters the formula.

Sample case 2 is already uniform, needing $0$ operations, which the formula gives without a special case.

The requirement that $i \neq j$ never binds, because $N \geq 2$ guarantees a second index exists to copy from. If the array were a single element it would already be uniform anyway.
