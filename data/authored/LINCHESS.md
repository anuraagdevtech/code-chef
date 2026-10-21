---
topic: Number Theory
subtopic: Divisors as reachable positions
time: $O(N)$ per test case
space: $O(1)$
---
Player $i$ places a pawn on square $P_i$ and then advances by $P_i$ each move, so the squares they ever occupy are

$$P_i,\ 2P_i,\ 3P_i,\ \ldots$$

— exactly the positive multiples of $P_i$. So that player can reach Chef's square $K$ **if and only if $P_i$ divides $K$**.

When it does, reaching $K$ takes $\frac{K}{P_i} - 1$ moves, since the pawn starts already placed on $P_i$. That count shrinks as $P_i$ grows, so among the divisors of $K$ present in the list, the **largest** one wins. If none divides $K$, the answer is $-1$.

Recasting "can this player reach that square" as a divisibility test is the whole problem; without it one might try to simulate the moves, which is hopeless with $K$ up to $10^9$.

The output is the **starting square** $P_i$, not the number of moves — easy to misread, since the question is phrased around move counts.

Sample case 1 has $K = 6$ with candidates $\{4,3,2,8\}$. Both $3$ and $2$ divide $6$, needing $1$ and $2$ moves respectively, so the larger divisor $3$ is reported. Sample case 2 has $K = 7$, a prime, and none of $\{4,3,2,8\}$ divides it — note that $7$ itself does not appear, and the guarantee that all values are pairwise distinct means $P_i = K$ never happens anyway.

A single pass over the list suffices; no factorisation of $K$ is required, since the candidates are given.

## Edge cases

- **No player can capture** (the second row, where $K = 7$ is prime and $7$ is not among the $P_i$): print $-1$.
- **The output is the starting square, not the player's index** — the answer $3$ in the first row is the value $P_2$, not the position $2$.
- **Larger divisors are better.** A player starting at $P_i$ reaches $K$ after $K/P_i - 1$ moves, so the biggest divisor is the fastest; taking the smallest divisor reverses the answer.
- **$K$ itself is never in the list** ($K$ and all $P_i$ are pairwise distinct), so no player starts on Chef's square and every capture takes at least one move.
- **$P_i > K$ cannot divide $K$** and is dropped by the modulo test with no special case — the $8$ in both sample rows.
- **$P_i = 1$ divides everything** but is the slowest, so it is only ever the answer when nothing else divides $K$.

## Dry run

First sample: $K = 6$, players at $4, 3, 2, 8$.

| start $P_i$ | $6 \bmod P_i$ | divides? | moves $K/P_i - 1$ | best so far |
|---:|---:|:---:|---:|---:|
| 4 | 2 | no | — | $-1$ |
| 3 | 0 | yes | 1 | **3** |
| 2 | 0 | yes | 2 | 3 |
| 8 | 6 | no | — | 3 |

Output `3`: that player needs one move ($3 \to 6$), while the player at $2$ needs two.
