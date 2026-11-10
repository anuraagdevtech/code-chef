# Chef and Hamming Distance of arrays (CHEFHAM)

[Problem statement](https://www.codechef.com/problems/CHEFHAM) · [Python solution](../../solutions/CHEFHAM.py)

## Approach

Sort indices by value and cyclically shift their values by the largest frequency. This separates equal-value blocks as far as possible. The unavoidable number of matches is max(0,2*maxFrequency-N), so the resulting Hamming distance is optimal.

## Complexity

- Time: O(N log N).
- Space: O(N).
