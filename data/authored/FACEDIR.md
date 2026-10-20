---
topic: Number Theory
subtopic: Cyclic state via modulo
time: $O(1)$ per test case
space: $O(1)$
---
Turning $90°$ clockwise four times returns Chef to where he started, so the heading depends only on $X \bmod 4$. Listing the directions in clockwise order from the starting point:

$$[\text{North},\ \text{East},\ \text{South},\ \text{West}]$$

the answer is the entry at index `x % 4`.

Two things make the table correct. It must be written in **clockwise** order, matching the direction of rotation — anticlockwise would reverse the middle two entries. And it must **start at the initial heading**, North, so that index $0$ (no rotation) is right; starting the list elsewhere would rotate every answer.

This is the same cycle-collapsing idea as the Mario transformation problem, with period $4$ instead of $3$. Simulating $X$ steps would pass at $X \leq 1000$, but the modulo is $O(1)$ and would still work if $X$ reached $10^{18}$.

Checking the samples: $X = 1$ gives East, $X = 3$ gives West, and $X = 6$ reduces to $6 \bmod 4 = 2$, giving South — a full rotation plus two quarter turns.
