---
topic: Number Theory
subtopic: A riffle is multiplication by two modulo N - 1
time: $O(N + \log K)$ per test case
space: $O(N)$ for the output
complexity_note: Auxiliary space excludes the buffered input and output.
---
Use 0-based positions. After one riffle, position $i$ in the first half holds the old element from position $2i$, and position $N/2 + i$ holds the old element from position $2i + 1$. Both cases are described by one formula: position $i < N - 1$ reads from position $2i \bmod (N - 1)$, and the last position reads from itself.

Applying this $K$ times, position $i$ ends up reading from position $i \cdot 2^K \bmod (N - 1)$ of the original arrangement. The original arrangement is the identity, so the answer at 0-based position $i$ is

$$(i \cdot 2^K \bmod (N - 1)) + 1 \quad (i < N - 1), \qquad N \text{ at the last position}.$$

$2^K \bmod (N - 1)$ is one modular exponentiation.

## Edge cases

- $N = 2$: the modulus is 1, everything maps to position 0, and the permutation stays `1 2`.
- $K$ up to $10^9$ is no problem for fast exponentiation.
- The first and the last element never move.
- The riffle has a period dividing the order of 2 modulo $N - 1$, but it is not needed.

## Dry run

`N = 8, K = 2`: $2^2 \bmod 7 = 4$.

Positions $0 \dots 6$ read from $0, 4, 1, 5, 2, 6, 3$, giving the values `1 5 2 6 3 7 4`, and the last position holds 8.

Output `1 5 2 6 3 7 4 8`.
