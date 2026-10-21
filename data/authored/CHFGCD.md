---
topic: Number Theory
subtopic: Case analysis on parity
time: $O(\log \min(X,Y))$ per test case
space: $O(1)$
---
The answer is always $0$, $1$ or $2$, and the reason is that **$2$ is a divisor we can always reach**: incrementing each odd value once makes both even, so

$$\text{answer} \leq [X \text{ odd}] + [Y \text{ odd}] \leq 2$$

That bound drives the whole case analysis.

- $\gcd(X,Y) > 1$ already: **$0$**.
- Otherwise the pair is coprime, so they are never both even. If exactly one is odd, adding $1$ to that one makes both even: **$1$**, and $0$ is impossible since they are coprime.
- If both are odd, two moves always suffice. One move can also work, but only if a single increment lands on a common factor — so test $\gcd(X+1, Y) > 1$ and $\gcd(X, Y+1) > 1$. If either holds the answer is **$1$**, else **$2$**.

Only those two one-move candidates need checking, because a single operation can do nothing else.

The both-odd case is where the answer genuinely splits. $X = 3, Y = 5$ needs one move: $Y + 1 = 6$ shares the factor $3$. But $X = Y = 1$ needs two — $\gcd(2,1)$ and $\gcd(1,2)$ are both $1$, and only $(2,2)$ works. More generally two consecutive odd numbers $2m{-}1, 2m{+}1$ often need both increments.

In the sample, $(4,16)$ has $\gcd = 4$, so $0$; $(4,55)$ is coprime with one odd member, so $1$ — and indeed $(4,56)$ shares $4$.

Each test is a couple of GCDs, which keeps $T = 10^5$ comfortable.

## Edge cases

- **Already sharing a factor** (the first row, $\gcd(4,16) = 4$) → $0$ operations, which must be tested first.
- **One of them even, coprime** → one operation: increment the odd one so both are even and share $2$. The second row turns $55$ into $56$ alongside $4$.
- **Both odd and coprime** → check whether a single increment suffices. Raising either one may create a shared odd factor, as with $3$ and $5$ where $\gcd(3, 6) = 3$.
- **The answer is never more than $2$.** Incrementing both makes both even, so $2$ always works — which is why the final branch needs no search.
- **$X = Y = 1$** is the smallest hard case: $\gcd(2,1) = \gcd(1,2) = 1$, so it costs the full $2$.
- **$X, Y$ up to $10^9$**: at most three gcd computations per case, each $O(\log)$.

## Dry run

| $X$ | $Y$ | $\gcd$ | parity | single increment helps? | output |
|---:|---:|---:|---|---|---:|
| 4 | 16 | 4 | — | — | `0` |
| 4 | 55 | 1 | one even | yes: $4, 56$ share $4$ | `1` |
| 3 | 5 | 1 | both odd | yes: $\gcd(3,6) = 3$ | `1` |
| 1 | 1 | 1 | both odd | no | `2` |

The last row needs $2, 2$, which share the factor $2$.
