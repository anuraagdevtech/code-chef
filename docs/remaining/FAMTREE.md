# Family Tree (FAMTREE)

[Problem statement](https://www.codechef.com/problems/FAMTREE) · [Python solution](../../solutions/FAMTREE.py)

## Approach

Unlike INOI1601, this problem asks for the absolute wealth difference between an ancestor and descendant. Carry both the smallest and largest ancestor wealth during an iterative traversal and compare each with the current member.

## Complexity

- Time: O(N).
- Space: O(N).

[Official explanation of both subtree extremes](https://discuss.codechef.com/t/famtree-editorial/18864).
