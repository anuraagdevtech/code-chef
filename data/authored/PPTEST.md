---
topic: Dynamic Programming
subtopic: 0-1 knapsack with total test value
time: $O(NW)$ per test case
space: $O(W)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Learning question $i$ once earns $C_iP_i$ points across all tests and consumes $T_i$ minutes. This is a 0-1 knapsack item. For every question, update time capacities in descending order, ensuring the question cannot be learned more than once. The capacity-$W$ entry stores the best score achievable within the available time.

## Edge cases

- Multiply test count by points per test.
- Skipping every question is allowed.
- Descending capacity updates prevent reusing one question.

## Dry run

The first and third sample questions use six minutes and earn `1*2+3*3=11` points, better than studying only the second question.
