---
topic: Greedy
subtopic: Keep the largest feasible prefix after sorting
time: $O(N\log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Suppose $k$ people remain. Their final wealth is at least the largest initial wealth among them, so they require at least $k$ times that maximum coins. The entire town has only $S$ coins.

For any fixed $k$, keeping the $k$ poorest people minimises that maximum to sorted $A_{k-1}$. If $kA_{k-1}\le S$, the departing people can donate exactly the deficits and take the excess away. This condition is both necessary and sufficient. Maximise feasible $k$ and return $N-k$.

## Edge cases

- Everyone can remain if all amounts are equal.
- At least one person can always remain.
- Donors may retain excess coins; exact divisibility of the town total is unnecessary.

## Dry run

For `[5,1,4]`, sorted amounts are `[1,4,5]`, total `10`. Keeping all three needs `15`, but keeping two needs `8`, so one monk suffices.
