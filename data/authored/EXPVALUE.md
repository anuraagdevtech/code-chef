---
topic: Probability
subtopic: Carry the mean and the second moment through independent increments
time: $O(N)$
space: $O(1)$ besides the output
complexity_note: Auxiliary space excludes the buffered input and output.
---
Turn $i$ adds $w_i = P^{-(i-1)}$ with probability $\tfrac12$, independently of the past. If $S$ is the score so far and $X$ the new increment,

$$E[(S + X)^2] = E[S^2] + 2\,E[S]\,E[X] + E[X^2] = E[S^2] + E[S] \cdot w + \frac{w^2}{2},$$

using independence, $E[X] = w/2$ and $E[X^2] = w^2/2$. Also $E[S + X] = E[S] + w/2$.

So keep two numbers, the mean and the second moment, update them in that order for each turn, and print the second moment after every turn. All values are fractions modulo $998244353$: $1/2$ and $1/P$ are modular inverses, and $w$ is multiplied by $1/P$ each turn.

## Edge cases

- The second moment must be updated before the mean, since it uses the old mean.
- $F(1)$ is always $1/2$.
- Only one modular inverse of $P$ is needed; powers follow by multiplication.
- The output has $N$ values on one line.

## Dry run

`N = 2, P = 2`.

- Turn 1, $w = 1$: second moment $0 + 0 \cdot 1 + \tfrac12 = \tfrac12$; mean $\tfrac12$.
- Turn 2, $w = \tfrac12$: second moment $\tfrac12 + \tfrac12 \cdot \tfrac12 + \tfrac18 = \tfrac78$.

$1/2$ and $7/8$ modulo $998244353$ are `499122177` and `124780545`.
