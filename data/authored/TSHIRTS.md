---
topic: Dynamic Programming
subtopic: Bitmask over people, processing the 100 shirts one at a time
time: $O(100 \cdot 2^N \cdot N)$ per test case
space: $O(2^N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
There are at most 10 people but 100 shirt ids, so the state is the set of people who already have a shirt, and the shirts are the items processed one by one.

`ways[mask]` is the number of ways to dress exactly the people in `mask` using the shirts considered so far. For the next shirt id either nobody wears it, or exactly one person who owns it and is not yet dressed wears it: `ways[mask | bit] += ways[mask]`. Iterating the masks in decreasing order guarantees that a shirt is not handed out twice within the same step, since the target mask is always larger than the source.

The answer is `ways[full mask]`. Each line of the input lists one person's shirts and has variable length, so the input is read line by line.

## Edge cases

- A shirt nobody owns changes nothing.
- A person with a single shirt forces that shirt, which the DP handles naturally.
- If two people only own the same single shirt the answer is 0.
- Results are modulo $10^9 + 7$.

## Dry run

Two people with shirts `{3, 5}` and `{8, 100}`. Masks are written as (person 2, person 1).

- shirt 3: `01` gets 1 way.
- shirt 5: `01` gets one more: 2 ways.
- shirt 8: from `00` to `10` (1 way), from `01` to `11` (2 ways).
- shirt 100: from `00` to `10` (now 2), from `01` to `11` (now 4).

Answer 4.
