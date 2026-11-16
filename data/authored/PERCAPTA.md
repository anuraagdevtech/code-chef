---
topic: Graphs
subtopic: Largest component among maximum-ratio provinces
time: $O(N+M)$ per test case
space: $O(N+M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The kingdom's income per capita is a population-weighted average of provincial ratios. It cannot exceed the maximum individual ratio, and it equals that maximum exactly when every chosen province has that ratio.

Find the maximum using integer cross products, mark all provinces tying it, and traverse the graph induced by those provinces. The largest connected component maximises the number of retained provinces while preserving the optimal ratio.

## Edge cases

- Compare ratios without floating-point division.
- Zero incomes are allowed.
- If several largest components tie, any one is valid.
- Abandoned provinces cannot be used as intermediate stops.

## Dry run

The sample ratios are `10/5=2`, `1/1=1`, and `2/1=2`. Provinces 1 and 3 are connected directly, so retain both.
