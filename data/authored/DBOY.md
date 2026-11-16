---
topic: Dynamic Programming
subtopic: Unbounded minimum-coin DP for each exact round trip
time: $O(KU+N)$ per test case for $U=2\max H$ and $K$ distinct fuel amounts
space: $O(U+N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A delivery to distance $H_i$ needs exactly $2H_i$ litres, and fuel cannot be shared between orders under the stated exact-trip policy. Each station is an unlimited coin denomination: using it fills exactly its offered amount once.

Compute the minimum number of fills for every fuel total up to the largest round-trip distance using unbounded coin-change DP. Process each distinct denomination with totals in ascending order, allowing repeated use. Sum the optimal fill counts for all orders.

## Edge cases

- Use the round-trip distance, not the one-way distance.
- Duplicate station capacities do not create new options.
- An exact fill is required; overshooting is not allowed.
- The input guarantees each requested total is reachable.

## Dry run

For distances `[1,2,3,4]` and capacities `[1,4,5,3]`, round-trip totals `[2,4,6,8]` need `[2,1,2,2]` fills, summing to seven.
