---
topic: Combinatorics
subtopic: Multinomial over sixes, fours and the rest, with a prefix of binomials for wickets
time: $O(B_{\max} + T \cdot B)$
space: $O(B_{\max})$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Fix the number of sixes $s$. Then the fours are forced: $f = (R - 6s) / 4$ must be a non-negative integer. The remaining $n = B - s - f$ balls score nothing and each is either a dot ball or a wicket, with at most $L$ wickets.

The balls are ordered, so the number of ways is

$$\frac{B!}{s! \, f! \, n!} \cdot \sum_{w=0}^{\min(L, n)} \binom{n}{w}.$$

Factorials and inverse factorials modulo $10^9 + 7$ give the multinomial; the inner sum depends only on $(n, L)$ with $L \le 9$, so it is tabulated once for every $n$ as a running prefix of binomials. Sum over all feasible $s$.

## Edge cases

- Odd $R$ or $R > 6B$ is impossible: answer 0.
- $R = 0$ is valid - every ball is a dot or a wicket.
- When $L$ exceeds the number of non-scoring balls, the prefix simply stops growing at $n$.
- The batting order is fixed, so wickets are indistinguishable apart from the ball they fall on.

## Dry run

`R = 6, B = 2, L = 9`.

- $s = 0$: $f = 6/4$ is not an integer - skip.
- $s = 1$: $f = 0$, $n = 1$. Arrangements $2! / (1! \, 0! \, 1!) = 2$; the one non-scoring ball is a dot or a wicket, $\binom{1}{0} + \binom{1}{1} = 2$.

Answer $2 \cdot 2 = 4$: `60`, `6W`, `06`, `W6`.
