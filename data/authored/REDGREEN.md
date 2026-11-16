---
topic: Combinatorics
subtopic: Count (grid, path) pairs path by path
time: $O(N + M)$ precomputation, $O(\log (N M))$ per test case
space: $O(N + M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The sum of scores over all grids is the number of pairs (colouring, path) in which the path is balanced. Count it from the side of the paths.

There are $\binom{N + M - 2}{N - 1}$ monotone paths, and each visits exactly $L = N + M - 1$ cells. For a fixed path, the colourings in which it is balanced choose which $L / 2$ of its cells are red, $\binom{L}{L/2}$ ways, and colour the remaining $N M - L$ cells freely, $2^{N M - L}$ ways. The count is the same for every path, so

$$\text{answer} = \binom{N + M - 2}{N - 1} \cdot \binom{L}{L/2} \cdot 2^{N M - L}.$$

If $L$ is odd no path can be balanced and the answer is 0.

## Edge cases

- $N + M$ even means an odd path length: answer 0.
- A $1 \times M$ grid has a single path covering every cell.
- The exponent $N M - L$ can be about $10^6$; modular exponentiation handles it.
- The modulus here is $998244353$.

## Dry run

`2 x 3` grid: $L = 4$.

Paths: $\binom{3}{1} = 3$. Balanced colourings of one path: $\binom{4}{2} = 6$. Free cells: $6 - 4 = 2$, so $2^2 = 4$.

Answer $3 \cdot 6 \cdot 4 = 72$.
