---
topic: Strings
subtopic: Runs of zeros classified by their bounding charges
time: $O(N)$ per test case
space: $O(1)$
---
Charges never move or change, so the only cells in play are the maximal runs of `0`. Each run fills in from whichever ends have a charge next to them, and the outcome depends only on those two bounding characters.

- **No bounding charge at all** (the whole string is zeros): nothing ever happens, so all $N$ cells stay neutral.
- **Bounded on one side only** (the run touches an end of the string): the charge marches in one cell per second and eventually fills the run — $0$ neutral.
- **Both bounds the same sign**: the run fills from both sides with the same charge — $0$ neutral.
- **Both bounds opposite**: the two fronts advance one cell per second and meet in the middle. A run of length $L$ ends with $\lfloor L/2 \rfloor$ cells of each sign, and when $L$ is **odd** the centre cell receives both charges on the same second, so it stays neutral forever.

$$\text{answer} = \sum_{\text{runs bounded by opposite signs}} (L \bmod 2)$$

The odd/even distinction is the whole problem. For `+0-` the single zero has both neighbours charged from the start and never resolves. For `+00-` the two cells are claimed one each. For `+000-` the fronts take cells $1$ and $3$, then stall on cell $2$, which is permanently caught between a `+` and a `-`.

The samples: `00` has no charges, so both cells stay neutral. `-+0` has its run bounded only on the left, so it fills. `00+-00` has two one-sided runs, both of which fill. And `0-0+000-` has a one-sided run plus two opposite-bounded runs of lengths $1$ and $3$, both odd, giving $2$.

## Edge cases

- **Two charged neighbours of the same sign still charge the cell**, but **opposite** signs leave it neutral — that single rule is what lets anything survive at all.
- **So a run of zeros survives only when squeezed between opposite charges, and then only its centre**, which exists exactly when the run has odd length. Both fronts advance one cell per second and meet at the middle cell, which receives a `+` and a `-` simultaneously.
- **An even run between opposite charges is fully consumed**, since the two fronts pass each other between cells with nothing left in the middle.
- **A run bounded on one side only is fully charged**, which is why the leading and trailing runs never contribute — the third sample's `00+-00` answers $0$ despite having four zeros.
- **A run between same-sign charges is fully charged** too, so the bounding signs must be compared, not merely counted.
- **An all-zero string never changes**, so every character stays neutral and the answer is $N$ — checked up front.
- **The trailing run is deliberately not counted** after the loop, since it has no closing charge.

## Dry run

Fourth sample: $S = $ `0-0+000-`.

| run of zeros | left charge | right charge | opposite? | length | survivors |
|---|---|---|:---:|---:|---:|
| position 1 | none | `-` | — | 1 | 0 |
| position 3 | `-` | `+` | yes | 1 (odd) | **1** |
| positions 5–7 | `+` | `-` | yes | 3 (odd) | **1** |

Output `2`. After infinite time the string is `--0++0--`, with the two centres left neutral.
