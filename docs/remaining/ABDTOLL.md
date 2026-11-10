# Abdullah and Toll Discounts (ABDTOLL)

[Problem statement](https://www.codechef.com/problems/ABDTOLL) · [Python solution](../../solutions/ABDTOLL.py)

## Approach

In postorder, keep the largest remaining root-to-leaf toll below each node. If adding this node exceeds K, reduce this node's toll by as much of the excess as possible. Earlier shared discounts dominate separate discounts below, while any excess already removed below was unavoidable even with zero ancestor tolls.

## Complexity

- Time: O(N).
- Space: O(N).
