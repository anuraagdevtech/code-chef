---
topic: Number Theory
subtopic: Dirichlet hyperbola count of divisible ordered pairs
time: $O(\sqrt N+\log N)$ per test case
space: $O(1)$ auxiliary
complexity_note: Auxiliary space excludes the buffered input and output.
---
The condition $gcd(A,B)=B$ is equivalent to $B$ dividing $A$. For fixed $B$, there are $\lfloor N/B\rfloor$ choices of $A$, so favourable ordered pairs total $S=\sum_{b=1}^N\lfloor N/b\rfloor$.

Count lattice points $ab\le N$ by symmetry around $a=b$. With $r=\lfloor\sqrt N\rfloor$, the count is $S=2\sum_{i=1}^r\lfloor N/i\rfloor-r^2$. The subtraction removes the square counted twice. Reduce $S/N^2$ by its GCD.

## Edge cases

- The two choices are independent and ordered, giving denominator $N^2$.
- Include pairs with equal entries.
- Use an exact integer square root.

## Dry run

For `N=3`, favourable pairs number `3+1+1=5`, out of nine ordered pairs. The irreducible probability is `5/9`.
