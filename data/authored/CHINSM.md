---
topic: Number Theory
subtopic: Sliding window whose left end jumps past the latest bad partner
time: $O(V \log V + N \cdot \tau(V))$, $V$ the largest value
space: $O(V \log V)$ for the divisor lists
complexity_note: Auxiliary space excludes the buffered input and output.
---
Count subsegments by their right end: for each $i$, find the smallest left end such that the segment contains no bad pair; all later left ends are fine too, so $i$ contributes $i - \text{left} + 1$. The left end only moves right.

When a new element $y = A_i$ arrives, the new bad pairs are those with $y$ on the right: earlier $x$ with $x \bmod y = K$. This needs $y > K$, and then either $x = K$, or $x > K$ and $y$ divides $x - K$. The window has to start after the latest such $x$.

So maintain `last[d]`: the latest index of an element $x > K$ such that $d$ divides $x - K$ (only for $d > K$), and separately the latest index of an element equal to $K$. On arrival of $y > K$ move the left end past both. After counting, register the new element itself: if it equals $K$ update the special index, and if it exceeds $K$ set `last[d] = i` for every divisor $d > K$ of $y - K$. Divisor lists for all needed numbers are built with a harmonic sieve.

## Edge cases

- An element $y \le K$ can never be the right member of a bad pair.
- $x = K$ pairs with every later $y > K$, which is why it is tracked separately.
- Only divisors larger than $K$ are stored - smaller ones can never be a valid $y$.
- The number of subsegments can reach about $N^2 / 2$.

## Dry run

`A = [5, 3, 1]`, `K = 2`.

- $i = 1$, value 5: window `[1, 1]`, count 1. Register: $5 - 2 = 3$ has the divisor 3 (> 2), so `last[3] = 1`.
- $i = 2$, value 3: `last[3] = 1`, so the window must start at 2 (indeed $5 \bmod 3 = 2$). Count 1.
- $i = 3$, value 1: not larger than $K$, window stays `[2, 3]`. Count 2.

Answer 4.
