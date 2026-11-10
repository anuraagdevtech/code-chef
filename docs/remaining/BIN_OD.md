# Binod (BIN_OD)

[Problem statement](https://www.codechef.com/problems/BIN_OD) · [Python solution](../../solutions/BIN_OD.py)

## Approach

Group queries by the requested bit and construct one bit-prefix array at a time. If the two ranges have x and y set bits and lengths a,b, their XOR-set pair count is x*(b-y)+y*(a-x). Reusing the prefix array avoids storing sixty full arrays.

## Complexity

- Time: O(60N+Q).
- Space: O(N+Q).
