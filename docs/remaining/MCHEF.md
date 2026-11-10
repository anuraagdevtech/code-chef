# MCHEF

Sweep judge intervals with a minimum-cost heap. Only negative dishes help. Keep at most floor(K/cost) best gains of each cost, then run 0/1 knapsack.

Complexity: O((N+M) log(N+M) + K² log K) time and O(N+M+K) space.
