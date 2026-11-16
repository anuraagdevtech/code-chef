---
topic: Combinatorics
subtopic: Per-bit signed coefficients from a three-term recurrence, grouped by bit count
time: $O(30 \cdot N + Q)$
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Handle each bit separately. If $c$ of the $N$ numbers have bit $b$, a subsequence contributes $2^b$ exactly when it contains an odd number of those $c$ elements. Let $f_k$ be (number of size-$k$ subsets with an even count) minus (number with an odd count); then the number with an odd count is $(\binom{N}{k} - f_k) / 2$.

$f_k$ is the coefficient of $z^k$ in $F(z) = (1 - z)^c (1 + z)^{N - c}$. Taking the logarithmic derivative, $(1 - z^2) F' = \bigl((N - 2c) - N z\bigr) F$, and comparing coefficients gives

$$(k + 1) f_{k+1} = (N - 2c) f_k - (N - k + 1) f_{k-1}, \qquad f_0 = 1,\; f_1 = N - 2c,$$

so all $f_k$ follow in linear time without any convolution.

The recurrence depends on the bit only through $c$, so bits with the same count are merged by adding their weights $2^b$; there are at most 30 groups. Accumulate, for every size $k$, the total contribution of subsequences of exactly that size, then take prefix sums over $k$ so that a query $M$ is a single lookup.

## Edge cases

- A bit present in no element contributes nothing and is skipped.
- $M$ may equal $N$; the recurrence is not advanced past $k = N$.
- Division by 2 and by $k + 1$ are modular inverses modulo $998244353$.
- For $k = 1$ the odd count is simply $c$, so the answer for $M = 1$ is the sum of the array.

## Dry run

`A = [1, 3, 5, 2]`: bit 0 occurs 3 times, bit 1 twice, bit 2 once.

For $k = 1$: $f_1 = N - 2c$, so the odd count is $(4 - (4 - 2c)) / 2 = c$. Contribution $1 \cdot 3 + 2 \cdot 2 + 4 \cdot 1 = 11$, the answer for $M = 1$.

For $k = 2$: $f_2 = ((N - 2c) f_1 - N f_0) / 2$ gives $0, -2, 0$ for $c = 3, 2, 1$, so the odd counts are $(6 - f_2)/2 = 3, 4, 3$ and the contribution is $3 + 8 + 12 = 23$. The answer for $M = 2$ is $11 + 23 = 34$.
