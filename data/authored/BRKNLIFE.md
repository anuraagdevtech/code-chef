---
topic: Greedy
subtopic: Avoid advancing the subsequence matcher at question marks
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Scan $S$ while greedily matching the longest possible prefix of $A$. A fixed character advances the matcher only when it equals the next required character. At a question mark, choose a letter different from that next required character.

Keeping the matched prefix as short as possible dominates every other choice: a smaller matched prefix cannot make completing $A$ easier. Thus if even this scan completes $A$, every replacement fails. Otherwise its constructed string is valid.

## Edge cases

- A subsequence need not be contiguous.
- A fixed occurrence of all of $A$ already makes the task impossible.
- The replacement alphabet is only `a` through `e`.

## Dry run

For `S=?ab?`, `A=ba`, choose `a` at the first question mark. The fixed `b` matches the first target letter; choose `b` at the end to avoid matching `a`. Result `aabb` avoids `ba`.
