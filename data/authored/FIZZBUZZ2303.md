---
topic: Combinatorics
subtopic: Ordered pairs (permutations)
time: $O(1)$ per test case
space: $O(1)$
---
Chef picks a captain and a vice-captain from $N$ players. The two roles are **distinct**, so choosing Alice as captain and Bob as vice-captain is a different outcome from the reverse — the order matters.

There are $N$ ways to fill the captaincy and, with that player used up, $N - 1$ remaining for vice-captain:

$$N \cdot (N-1)$$

This is the permutation count $P(N, 2) = \frac{N!}{(N-2)!}$, not the combination count $\binom{N}{2} = \frac{N(N-1)}{2}$. Halving is the classic error here, and the sample pins it down: $N = 3$ gives $6$, not $3$. The division by $2$ in $\binom{N}{2}$ exists precisely to discard orderings, which is the wrong thing to do when the two slots mean different jobs.

The rule of thumb: ask whether swapping the two chosen items changes the answer. If it does, count permutations; if it does not, count combinations.

The team size of $11$ is scenery — only $N$, the shortlist, enters the formula. The constraint $N \geq 2$ guarantees at least one valid choice, so no empty case arises.

## Edge cases

- **Smallest squad** ($N = 2$): two arrangements — either player can captain while the other is vice-captain.
- **Order matters.** Captain and vice-captain are different roles, so the count is the ordered pair $N(N-1)$ and *not* the combination $\binom{N}{2} = N(N-1)/2$. Using the combination halves every answer.
- **One player cannot hold both roles**, which is why the second factor is $N - 1$ rather than $N$.
- **Largest input** ($N = 11$): $110$ arrangements.

## Dry run

| $N$ | captain choices | vice-captain choices | total $N(N-1)$ | output |
|---:|---:|---:|---:|---|
| 2 | 2 | 1 | 2 | `2` |
| 3 | 3 | 2 | 6 | `6` |

For $N = 3$ the six orderings are $(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)$ — the pairs $(1,2)$ and $(2,1)$ counting separately is exactly what makes this a permutation count.
