# A Plus B Again! (TAAPLUSB)

[Problem statement](https://www.codechef.com/problems/TAAPLUSB) · [Python solution](../../solutions/TAAPLUSB.py)

## Approach

If p_i is the probability of a carry after digit i, then p_i=0.45+0.1*p_(i-1), with p_0=0. Summing the resulting geometric series gives N/2-(1-10^(-N))/18. Output sufficient decimal precision.

## Complexity

- Time: O(1).
- Space: O(1).
