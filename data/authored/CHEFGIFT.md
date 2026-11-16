---
topic: Dynamic Programming
subtopic: Shortest transfer costs followed by stage DP
time: $O(M^3+NM^2)$ per test case
space: $O(MN+M^2)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Switching roads between two toll stages may use intermediate roads. Run Floyd-Warshall on the transfer-price matrix to obtain the cheapest cost for each ordered pair of roads.

Initially the caravan may use any road, so its cost at the first stage is simply that road's first toll. For each later stage, let $dp[j]$ be the cheapest cost after paying that toll on road $j$. Compute $next[j]=toll[j][stage]+\min_i(dp[i]+transfer[i][j])$. The cheapest final cost is the minimum of the last DP row. Subtract it from the initial money, or return minus one if the tolls are unaffordable.

## Edge cases

- Transfer prices need not be symmetric or satisfy the triangle inequality.
- Staying on the same road costs zero.
- Spending the entire budget on tolls leaves a valid caravan budget of zero.

## Dry run

In sample one, taking road 3 for all five booths costs `16+1+1+1+1=20`. The minimum toll budget is 20, leaving `40-20=20` for the caravan.
