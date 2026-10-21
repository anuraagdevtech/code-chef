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

## Edge cases

- **The very first serve** ($0$&ndash;$0$): block $0$, so Alice.
- **The switch after two points**: a total of $1$ is still block $0$ (Alice), a total of $2$ is block $1$ (Bob). The sample's second row sits just past the change.
- **Only the total matters**, not how it splits: $0$&ndash;$2$, $1$&ndash;$1$ and $2$&ndash;$0$ all give block $1$, so Bob serves in all three.
- **Largest total** ($10 + 10 = 20$): block $10$, which is even, so Alice.
- Dividing by two to get the block index and then testing *its* parity is the whole trick; testing the parity of the total itself gives a different, wrong pattern.

## Dry run

| $P$ | $Q$ | total | block $\lfloor \text{total}/2 \rfloor$ | block parity | output |
|---:|---:|---:|---:|---|---|
| 0 | 0 | 0 | 0 | even | `Alice` |
| 0 | 2 | 2 | 1 | odd | `Bob` |
| 2 | 2 | 4 | 2 | even | `Alice` |
| 4 | 7 | 11 | 5 | odd | `Bob` |

Row 4 has an odd total, which still lands inside block $5$.
