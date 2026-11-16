---
topic: Combinatorics
subtopic: Fibonacci convolution in closed form with fast doubling
time: $O(\log N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $w(d)$ be the number of ways to cover a distance $d$ with forward steps of 1 and 2; $w(d) = F_{d+1}$. A walk with exactly one wrong step is: walk forward from 0 to some point $p$ with $1 \le p \le N-1$ (not at home, and not at the restaurant, where she stops), step back by $s \in \{1, 2\}$, then walk forward from $p - s$ to $N$. The backward step may go below 0. So

$$\text{answer} = \sum_{p=1}^{N-1} w(p) \cdot \bigl(w(N - p + 1) + w(N - p + 2)\bigr).$$

For $N = 3$ this is $1 \cdot (3 + 5) + 2 \cdot (2 + 3) = 18$.

Both parts are convolutions of the Fibonacci sequence with itself, and $\sum_{i=0}^{m} F_i F_{m-i} = (m L_m - F_m) / 5$ with $L_m$ the Lucas numbers. The code evaluates the two full convolutions with this identity and subtracts the few boundary terms that correspond to $p = 0$ and $p = N$. The handful of Fibonacci numbers around index $N$ come from fast doubling, and the division by 5 is a modular inverse.

## Edge cases

- $N$ is far too large for a loop over positions - only the closed form is evaluated.
- The backward step from position 1 by two units lands on $-1$, which is allowed.
- $N = 1$ leaves no place for a wrong step and the formula gives 0.
- Intermediate values can be negative before the final reduction modulo $10^9 + 7$.

## Dry run

`N = 3`, with $w = 1, 1, 2, 3, 5$ for distances $0 \dots 4$.

- $p = 1$: one way to get there; back to 0 or $-1$, then 3 or 4 units forward: $1 \cdot (3 + 5) = 8$.
- $p = 2$: two ways; back to 1 or 0, then 2 or 3 units forward: $2 \cdot (2 + 3) = 10$.

Answer 18.
