---
topic: Greedy
subtopic: Walk the path backwards, keeping the group size needed for the rest
time: $O((B + C) \log (B + C))$ per test case
space: $O(B + C)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let `need` be the smallest group that can complete the remaining part of the path from the current point; at the destination it is 1 (Chef himself must arrive). Sort dishes and clans by position and process them from the far end back to the start.

- A dish that must be eaten by $y$ people: those $y$ stay behind, so before the dish the group must be $y$ larger: `need += y`.
- A clan at this point with threshold $q$ and $r$ members: arriving with $g \ge q$ people gives $g + r$ afterwards. To have `need` after the clan we can either ignore the clan and arrive with `need`, or arrive with $\max(q, \text{need} - r)$ and recruit. So `need = min(need, max(q, need - r))`.

Each step is the exact inverse of "what group size before this point guarantees the required size after it", so the value at the start is the answer. Binary search on the starting size with a forward simulation would work as well; the backward pass avoids it.

## Edge cases

- No clans: the answer is 1 plus the sum of all dish requirements.
- A clan whose threshold exceeds the current need is never worth joining - the `min` keeps the old value.
- Recruits can make the requirement before a clan much smaller than after it, but never below the threshold.
- Positions of dishes and clans are distinct, so the sort order is unambiguous.

## Dry run

Third sample: dishes at 2 (3 people) and 8 (5 people); clans at 1 ($q=2, r=1$), 4 ($q=3, r=2$), 9 ($q=1, r=1$).

Backwards from `need = 1`:

- clan at 9: $\min(1, \max(1, 0)) = 1$
- dish at 8: $1 + 5 = 6$
- clan at 4: $\min(6, \max(3, 4)) = 4$
- dish at 2: $4 + 3 = 7$
- clan at 1: $\min(7, \max(2, 6)) = 6$

Answer 6.
