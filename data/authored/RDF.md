---
topic: Probability
subtopic: Expectation by layers with a running prefix average, cut off after 70 steps
time: $O(70 \cdot \max N + T)$
space: $O(\max N + T)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $E_k(n)$ be the expected result of $k$ steps starting from $n$. One step replaces $n$ by a uniform value in $[0, n)$, so

$$E_0(n) = n, \qquad E_k(n) = \frac{1}{n} \sum_{j=0}^{n-1} E_{k-1}(j), \qquad E_k(0) = 0.$$

A running sum over $j$ turns a whole layer into one linear pass. Each step at least halves the expectation ($E_1(n) = (n-1)/2$), so after 70 steps it is below $N / 2^{70}$, far under the required precision; such queries are answered with 0 and layers beyond 69 are never built.

The queries are grouped by $k$ and answered offline while the layers are generated up to the largest $N$ in the input.

## Edge cases

- $K = 0$ returns $N$ itself.
- `random(0) = 0`, so $E_k(0) = 0$ and the division by $n$ only happens for $n \ge 1$.
- Huge $K$ must not drive the loop - the cut-off keeps the work bounded.
- Answers are floats; ten decimals are printed.

## Dry run

`RDF(4, 2)`.

Layer 0: $E_0 = 0, 1, 2, 3, 4$. Layer 1: $E_1(n) = (n-1)/2$, giving $0, 0, 0.5, 1, 1.5$.

Layer 2: $E_2(4) = (E_1(0) + E_1(1) + E_1(2) + E_1(3)) / 4 = (0 + 0 + 0.5 + 1) / 4 = 0.375$.
