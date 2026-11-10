# Robot Game (TR2)

[Problem statement](https://www.codechef.com/problems/TR2) · [Python solution](../../solutions/TR2.py)

## Approach

Insert every root-to-vertex L/R path into one shared trie and count how many maps contain it. Record the greatest path depth for each exact map count, then take suffix maxima to answer all at-least-K requirements.

## Complexity

- Time: O(total map vertices+number of maps).
- Space: O(total map vertices).
