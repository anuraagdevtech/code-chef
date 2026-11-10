# Shortest Path in Binary Trees (BINTREE)

[Problem statement](https://www.codechef.com/problems/BINTREE) · [Python solution](../../solutions/BINTREE.py)

## Approach

Repeatedly replace the larger label by its parent, floor(label/2), until the labels agree. This walks exactly the two branches to their lowest common ancestor.

## Complexity

- Time: O(log max label).
- Space: O(1).
