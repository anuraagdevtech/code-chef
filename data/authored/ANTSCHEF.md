---
topic: Sorting
subtopic: Swap identities at collisions, then count meetings ray by ray
time: $O(S \log S)$ per test case, $S$ the total number of ants
space: $O(S)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
All ants walk towards $\mathsf{O}$ at the same speed, and ants that meet turn around. When two ants meet head-on and both reverse, the picture is the same as if they had passed through each other, so follow "ghosts" that keep going instead of the real ants - the set of meeting points is unchanged.

A ghost at distance $d$ reaches $\mathsf{O}$ at time $d$. What happens there depends on whether the distance is shared:

- If several ants (on any lines) have the same distance $d$, they all arrive together: one collision at $\mathsf{O}$, and each ghost turns back along the side it came from.
- If the distance is unique, the ghost walks through $\mathsf{O}$ and continues outward on the opposite side of its own line.

After that the ghost walks outward for ever, and every ant still walking inward on that same ray - same line, the relevant side, larger distance - meets it exactly once. Two outgoing ghosts never meet, and each off-centre collision is one outgoing-incoming meeting, so it is counted once.

So the answer is the number of shared distances, plus, for every ant, the number of ants on its line with a larger distance on the side it leaves along: its own side if its distance is shared, the opposite side otherwise. Sorting each line by distance and keeping the remaining counts per side gives these numbers in one pass.

## Edge cases

- A collision of many ants at $\mathsf{O}$ counts once.
- Ants on different lines can only meet at $\mathsf{O}$.
- Two ants on the same line at equal distances on opposite sides also meet at $\mathsf{O}$.
- The counts can be large when one line holds many ants: about $M^2 / 2$.

## Dry run

Line 1 has ants at $-2$ and $1$; line 2 has an ant at $2$.

Distance 2 is shared (line 1 and line 2): one collision at $\mathsf{O}$. Distance 1 is unique.

- The ant at $1$ (line 1) passes through $\mathsf{O}$ onto the negative side, where the ant at $-2$ is still coming in: 1 meeting (at $-1/2$).
- The ants at distance 2 turn back at $\mathsf{O}$; nobody farther out is left on their rays.

Answer $1 + 1 = 2$.
