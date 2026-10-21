---
topic: Arrays
subtopic: Summing alternate positions
time: $O(1)$ per test case — ten fixed entries
space: $O(1)$
---
The ten outcomes interleave the two teams: positions $1, 3, 5, 7, 9$ belong to team 1 and positions $2, 4, 6, 8, 10$ to team 2. Since a goal is encoded as $1$ and a miss as $0$, each team's score is simply the sum of its own positions.

Python's slice stride does the deinterleaving in one step. With the list read zero-based, `a[0::2]` picks the odd-numbered shots (team 1) and `a[1::2]` the even-numbered ones (team 2).

The indexing base is the thing to be careful about. The statement numbers shots from $1$, so team 1 owns the **odd** labels — which land on the **even** zero-based indices. Getting this backwards swaps the teams, and sample case 2 would catch it: a lone goal in the final position belongs to team 2, so the answer is $2$.

Then a three-way comparison yields $1$, $2$, or $0$ for a draw. Note the unusual output encoding: $0$ means draw rather than "team 0", and sample case 1 — ten misses — is a $0$–$0$ draw.

Summing booleans directly works because the values are already $0$ and $1$; no conversion to goals is needed.

## Edge cases

- **A tie** (all zeros, or equal goals): the answer is `0`, a distinct third output.
- **The offset is the trap.** Shots are numbered from $1$, so team $1$ takes the odd-numbered shots — the *even* zero-based slots. The sample's second row puts a single goal in the last slot, which belongs to team $2$; getting the parity backwards reports `1` there.
- **One team wins every shot** (the fourth row: team $1$ takes $5$ to team $2$'s $4$): a narrow win on the alternating split.
- All ten shots are always present, so there is no partial-match handling.

## Dry run

| shots $A_1 \ldots A_{10}$ | team 1 (slots $1,3,5,7,9$) | team 2 (slots $2,4,6,8,10$) | output |
|---|---:|---:|---|
| all $0$ | 0 | 0 | `0` |
| $0\ldots0\,1$ | 0 | 1 | `2` |
| $1\,0\,1\,0\,0\ldots$ | 2 | 0 | `1` |
| $1\times9$ then $0$ | 5 | 4 | `1` |

Row 2's single goal lands on shot $10$, which is team $2$'s.
