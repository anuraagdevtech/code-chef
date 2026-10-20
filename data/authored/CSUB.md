---
topic: Combinatorics
subtopic: Counting pairs from a tally
time: $O(N)$ per test case
space: $O(1)$
---
A substring that starts and ends with `1` is determined entirely by **which two `1`s** sit at its ends — everything between them is carried along automatically. So the characters in the middle are irrelevant, and only the count of `1`s matters.

If there are $c$ ones, a valid substring is a choice of a start and an end from among them, with the start no later than the end. That is $\binom{c}{2}$ choices of two distinct positions, plus $c$ single-character substrings where both ends coincide:

$$\binom{c}{2} + c = \frac{c(c+1)}{2}$$

Including the single-character case is the detail to get right. The problem defines a substring with $i \leq j$, so a lone `1` counts. Sample case 2, `10001`, has $c = 2$ and the answer $3$ — the two single `1`s plus the whole string — rather than the $1$ a strict-pairs reading would give.

Sample case 1, `1111`, gives $4 \cdot 5 / 2 = 10$, which is every pair of positions including the degenerate ones.

Counting the `1`s is $O(N)$ and the arithmetic is $O(1)$; enumerating substrings directly would be $O(N^2)$ and far too slow at $N = 10^5$.

The result reaches about $5 \times 10^9$ when every character is a `1`, which **overflows a signed 32-bit integer** — worth noting for a C solution, though Python is unbothered.
