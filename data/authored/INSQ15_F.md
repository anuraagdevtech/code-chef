---
topic: Graphs
subtopic: Dijkstra on city and current travel mode
time: $O((N+R)\log N)$ overall
space: $O(N+R)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Use two states for each city: uphill mode and downhill mode. Switching mode at city $u$ costs $C_u$. A road can be traversed at zero additional cost in uphill mode when the next height is no smaller, and in downhill mode when it is no greater. Equal heights permit either mode.

Initialising either mode at city 1 costs $C_1$, as required by the statement. Run Dijkstra on these implicit state transitions and take the smaller destination-state distance.

## Edge cases

- Initial mode selection must be paid for.
- Equal-height roads preserve either mode.
- A disconnected destination returns minus one.
- A more expensive path in road length may still have lower mode-switch cost.

## Dry run

For the statement sample, path `1-4-5-6` chooses uphill at city 1 for one unit, stays uphill to city 5, then switches downhill for one unit. Total cost is 2.
