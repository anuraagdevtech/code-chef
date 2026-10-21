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
