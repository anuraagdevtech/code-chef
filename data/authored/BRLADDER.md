---
topic: Conditionals & Case Work
subtopic: Deriving an adjacency rule from an edge list
time: $O(1)$ per query
space: $O(1)$
---
The graph is infinite, so the answer has to come from a rule rather than from building anything. Read the three families of roads and work out what they mean for a pair $(a, b)$:

1. **Rungs** $2i+1 \leftrightarrow 2i+2$: the pairs $1$–$2$, $3$–$4$, $5$–$6$, … These differ by $1$, and the smaller endpoint is always **odd**.
2. **Odd rail** — consecutive odd numbers, differing by $2$.
3. **Even rail** — consecutive even numbers, also differing by $2$.

Families 2 and 3 together cover *every* pair differing by $2$, since two numbers two apart always share a parity. So the rule collapses to

$$|a - b| = 2, \quad\text{or}\quad |a - b| = 1 \text{ with } \min(a,b) \text{ odd}$$

The parity condition on the difference-of-one case is the whole problem. Not every adjacent pair is joined: $1$–$2$ and $3$–$4$ are rungs, but $2$–$3$ and $4$–$5$ are not. Sample cases 2 and 3 are placed side by side to make this exact point — $4$–$3$ is a road (smaller is $3$, odd) while $5$–$4$ is not (smaller is $4$, even).

Sample case 6 confirms the rule survives at the top of the range: $999999999$ is odd, so it is rung-joined to $1000000000$.

With coordinates to $10^9$ and $Q$ up to $1000$, only an $O(1)$ test per query is viable — which is exactly what reading the structure, rather than simulating it, buys. This graph is the infinite "ladder", and recognising the rungs-plus-rails shape is what makes the rule obvious.

## Edge cases

- **A difference of $1$ depends on the parity of the lower endpoint.** The sample has both sides one unit apart: $4, 3$ has the lower endpoint $3$ (odd) and answers `YES`, while $5, 4$ has $4$ (even) and answers `NO`. That parity is the whole subtlety, and ignoring it passes half the cases.
- **A difference of $2$ always works** — the sample shows it at both $1, 3$ and $10, 12$, so the rule is not about small values.
- **A difference of $3$ or more never works** ($1, 4$ and the far-apart last row).
- **Huge endpoints** ($999999999$ and $10^9$): the parity rule applies unchanged, and the sample includes exactly this pair.
- **$a \neq b$ is guaranteed**, so the difference is at least $1$ and there is no self-loop case.

## Dry run

| $a$ | $b$ | $|a-b|$ | lower endpoint | rule | output |
|---:|---:|---:|---:|---|---|
| 1 | 4 | 3 | — | too far | `NO` |
| 4 | 3 | 1 | 3 (odd) | rung | `YES` |
| 5 | 4 | 1 | 4 (even) | no rung | `NO` |
| 10 | 12 | 2 | — | rail | `YES` |
| 1 | 3 | 2 | — | rail | `YES` |
| 999999999 | 1000000000 | 1 | odd | rung | `YES` |
| 17 | 2384823 | large | — | too far | `NO` |

Rows 2 and 3 are the parity pair.
