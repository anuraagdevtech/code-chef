---
topic: Combinatorics
subtopic: Pruefer codes and the coefficient of a power of an exponential generating function
time: $O(N)$ for $K = 1$; otherwise $O(N \log K)$ plus $O(\log N)$ levels of big-integer convolutions
space: $O(N)$ coefficients plus the big-integer workspace
complexity_note: Auxiliary space excludes the buffered input and output.
---
In a Pruefer code a vertex of degree $d$ appears exactly $d - 1$ times, and every sequence of length $N - 2$ is the code of exactly one tree. Summing $\prod d_i^K$ over all trees is therefore a sum over sequences, which by the multinomial theorem equals

$$(N-2)! \cdot [x^{N-2}] \; F(x)^N, \qquad F(x) = \sum_{c \ge 0} (c+1)^K \frac{x^c}{c!},$$

and the expectation divides this by the number of trees, $N^{N-2}$.

For $K = 1$, $F(x) = (1 + x) e^x$, so $F^N = (1+x)^N e^{Nx}$ and the coefficient is a single sum whose consecutive terms have a simple ratio: $\sum_j \binom{N}{j} \frac{(N-2)!}{(N-2-j)!} N^{-j}$, evaluated in $O(N)$.

For general $K$, let $G = F^N$. Differentiating gives $G' = N \frac{F'}{F} G$, i.e. $k \, g_k = \sum_{j} h_j \, g_{k-1-j}$ with $h = N F'/F$. The series $1/F$ comes from Newton iteration, and the recurrence - each coefficient depends on all earlier ones - is solved by divide and conquer, convolving the finished left half into the right half. Polynomial products are done exactly by packing coefficients into one big Python integer with enough bits per slot (Kronecker substitution).

## Edge cases

- $N = 2$: the only tree has both degrees 1 and the answer is 1.
- The modulus is 998244353, and $N^{N-2}$ is inverted with Fermat's little theorem.
- $K = 1$ has to take the linear path - it is where the largest $N$ occurs.
- The packing width must hold a full convolution sum, otherwise coefficients would carry into each other.

## Dry run

`N = 3, K = 1`. The sum over $j = 0, 1$:

- $j = 0$: 1
- $j = 1$: $\binom{3}{1} \cdot \frac{1!}{0!} \cdot \frac{1}{3} = 1$

Answer 2. Check: the three labelled trees on 3 vertices are paths with degree product $1 \cdot 2 \cdot 1 = 2$ each.
