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
