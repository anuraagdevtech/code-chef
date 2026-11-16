---
topic: Greedy
subtopic: Discount the shallowest active toll when a path exceeds budget
time: $O(N\log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Root the tree at the home city. Any root-to-city toll sum must be at most $K$. A discount at an ancestor helps every descendant route, so an amount discounted at a descendant can instead be discounted at a not-yet-fully-discounted ancestor at the same price without making any route worse.

Traverse with explicit enter and exit events, maintaining the current path toll and a min-heap of active vertices by depth. Whenever the path exceeds $K$, reduce the shallowest available toll until the excess vanishes. Fully discounted and inactive heap entries are discarded lazily. This applies the exchange argument whenever a new constraint first becomes binding and never removes unnecessary toll. Each unit discounted costs two; accumulate reductions and double at the end.

## Edge cases

- The starting city toll counts even when the destination is home.
- Coupons are reusable across days; a reduction is paid for only once.
- Leaving a DFS branch subtracts its remaining toll, including any discounts already applied.
- When no path exceeds budget, the answer is zero.

## Dry run

In sample one, home city 2 has toll 7 and budget 6. The first child of toll 4 forces five units off the home toll. Visiting the child of toll 6 forces two more off home. Seven total discounted units cost 14.
