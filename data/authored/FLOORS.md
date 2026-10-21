---
topic: Basic Math
subtopic: Mapping an index to its block
time: $O(1)$ per test case
space: $O(1)$
---
Rooms are grouped ten to a floor, with floor $i$ holding rooms $10(i-1)+1$ through $10i$. Inverting that gives the floor of room $r$:

$$\text{floor}(r) = \left\lfloor \frac{r - 1}{10} \right\rfloor + 1$$

and the answer is the absolute difference of the two floors.

The $-1$ and $+1$ are doing the work, and they are there because the numbering is **one-based**. Room $10$ must land on floor $1$ and room $11$ on floor $2$; the naive `r // 10 + 1` puts room $10$ on floor $2$ and breaks on every multiple of ten. Shifting to zero-based with $r - 1$, dividing, then shifting back is the general recipe for one-based block arithmetic, and it is the same manoeuvre used for the bus-seat problem.

Since only the *difference* of the two floors is wanted, the trailing $+1$ cancels and `(x - 1) // 10` would do just as well for both rooms. The code keeps it for readability — the helper genuinely returns a floor number.

The absolute value is needed because Chef may live above or below Chefina; sample case 3 goes downward, from floor $6$ to floor $3$.

Sample case 2 is the same-floor case: rooms $42$ and $50$ both sit on floor $5$, so the answer is $0$ despite the rooms differing by $8$. Sample case 4 is its neighbour — rooms $81$ and $80$ differ by just one yet straddle a floor boundary, giving $1$.

## Edge cases

- **Same floor, different rooms** ($42$ and $50$): the answer is $0$ even though the room numbers differ by $8$. The sample's second row.
- **Adjacent rooms across a floor boundary** ($80$ and $81$): one room apart but one *floor* apart. The sample's fourth row, and this is where the shift matters.
- **The $-1$ shift is essential.** Rooms are numbered from $1$, so room $10$ belongs to floor $1$ and room $11$ to floor $2$. A plain `room // 10 + 1` puts room $10$ on floor $2$, breaking every multiple of ten.
- **The extremes** ($1$ and $100$): floors $1$ and $10$, nine apart.
- $X \neq Y$ is guaranteed, but their floors may still coincide, so a zero answer is legitimate.

## Dry run

| $X$ | floor of $X$ | $Y$ | floor of $Y$ | difference | output |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | 100 | 10 | 9 | `9` |
| 42 | 5 | 50 | 5 | 0 | `0` |
| 53 | 6 | 30 | 3 | 3 | `3` |
| 81 | 9 | 80 | 8 | 1 | `1` |

Row 4 is the boundary pair: consecutive rooms, different floors.
