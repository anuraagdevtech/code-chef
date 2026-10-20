---
topic: Number Theory
subtopic: Block index parity via modulo
time: $O(1)$ per test case
space: $O(1)$
---
The scores themselves are a distraction. Serving rotates on a fixed schedule that depends only on **how many points have been played**, not on who won them. That total is

$$n = P + Q$$

Serves come in blocks of two: serves $1,2$ belong to Alice, serves $3,4$ to Bob, serves $5,6$ to Alice again. The next serve to be played is serve number $n + 1$, which sits in block

$$\left\lfloor \frac{n}{2} \right\rfloor$$

counting blocks from zero. Alice owns the even-numbered blocks and Bob the odd ones, so the server is Alice when $\lfloor n/2 \rfloor$ is even and Bob otherwise.

Two steps, each easy to get subtly wrong. Dividing by $2$ collapses each pair of serves into one block; taking that result modulo $2$ asks whose turn the block is. Doing only one of them — testing `n % 2` or `n % 4` directly — gets half the cases right and looks plausible.

Equivalently the whole thing is `(n // 2) % 2`, which is just bit $1$ of $n$. Working through the samples: $n = 0$ gives block $0$, Alice; $n = 2$ gives block $1$, Bob; $n = 4$ gives block $2$, Alice; $n = 11$ gives block $5$, Bob.

Note $P = Q = 0$ is a valid input — the match has not started and Alice serves first.
