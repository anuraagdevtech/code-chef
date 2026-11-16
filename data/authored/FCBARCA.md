---
topic: Combinatorics
subtopic: Closed form for walks returning to the starting player
time: $O(\log N+\log MOD)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $a_n$ be the number of length-$n$ passing sequences ending with Messi, and $b_n$ those ending with any other player. Since self-passes are forbidden, $a_{n+1}=b_n$ and $b_{n+1}=Ka_n+(K-1)b_n$, starting from $(a_0,b_0)=(1,0)$.

Solving these two recurrences gives $a_n=(K^n+K(-1)^n)/(K+1)$. Evaluate the power modulo $10^9+7$ and divide using the modular inverse of $K+1$. The denominator is nonzero modulo this prime because $K\le10$.

## Edge cases

- Intermediate passes may return to Messi many times.
- A player cannot pass to themselves.
- For one teammate, exactly the even pass counts return to Messi.

## Dry run

For `N=4,K=2`, the expression is `(2^4+2)/3=6`, matching the six winning plays.
