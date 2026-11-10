# Triplets (SUMQ)

[Problem statement](https://www.codechef.com/problems/SUMQ) · [Python solution](../../solutions/SUMQ.py)

## Approach

For a fixed middle value y, the valid triple sum factors into (sum of eligible A + countA*y)*(sum of eligible C + countC*y). Sort all arrays and advance two pointers while accumulating those eligible sums.

## Complexity

- Time: O(P log P+Q log Q+R log R).
- Space: O(P+Q+R).
