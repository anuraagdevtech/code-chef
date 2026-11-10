# Palpal Strings (PALPALS)

[Problem statement](https://www.codechef.com/problems/PALPALS) · [Python solution](../../solutions/PALPALS.py)

## Approach

Each odd-frequency character needs a palindrome center supported by one pair. Every unused pair can form a palindrome of length two. Consequently rearrangement is possible exactly when the number of available pairs is at least the number of odd counts.

## Complexity

- Time: O(length).
- Space: O(26).
