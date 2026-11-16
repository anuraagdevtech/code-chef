---
topic: Number Theory
subtopic: Sum of floors as a harmonic sum over multiples
time: $O(N + M \log M)$ per test case
space: $O(M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For a price $P$ the number of candies sold is $\sum_i \lfloor A_i / P \rfloor$. Rewrite one floor as a count of thresholds:

$$\Bigl\lfloor \frac{a}{P} \Bigr\rfloor = \#\{\, j \ge 1 : jP \le a \,\},$$

so the total is $\sum_{j \ge 1} \text{cnt}(jP)$, where $\text{cnt}(x)$ is the number of customers with budget at least $x$.

Build `at_least` as a suffix sum of the budget frequencies. Then the sales for price $P$ are the sum of `at_least` over the multiples of $P$ up to $M$, which takes $M / P$ steps; over all prices this is the harmonic sum $M (1 + 1/2 + \dots) = O(M \log M)$. Multiply by the bonus $C_P$ and keep the maximum.

## Edge cases

- The bonuses are not monotone, so every price has to be evaluated.
- A price above every budget sells nothing.
- The bonus can reach $10^6 \cdot$ (number of candies), exceeding 32 bits.
- Only the bonus matters, not the revenue.

## Dry run

`A = [3, 1, 4, 1, 5]`, `C = [1, 4, 5, 5, 8, 99]`.

Customers with budget at least $x$, for $x = 1 \dots 6$: `5 3 3 2 1 0`.

- $P = 1$: $5 + 3 + 3 + 2 + 1 = 14$ candies, bonus 14.
- $P = 2$: multiples 2, 4, 6 give $3 + 2 + 0 = 5$ candies, bonus $5 \cdot 4 = 20$.
- $P = 3$: $3 + 0 = 3$ candies, bonus 15. $P = 4$: 10. $P = 5$: 8. $P = 6$: 0.

Answer 20.
