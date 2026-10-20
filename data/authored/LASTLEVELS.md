---
topic: Basic Math
subtopic: Counting separators, not groups
time: $O(1)$ per test case
space: $O(1)$
---
Playing time is straightforward: $X$ levels at $Y$ minutes each gives $XY$. The interesting part is counting the breaks.

Chef rests after every third level, **except** that no break is taken once the game is finished. So the breaks fall *between* blocks of three levels rather than after each block — they are separators, not group markers. The number of complete three-level blocks that are followed by more play is

$$\left\lfloor \frac{X - 1}{3} \right\rfloor$$

and the total is

$$XY + Z \left\lfloor \frac{X - 1}{3} \right\rfloor$$

The $-1$ is the whole problem. The tempting $\lfloor X/3 \rfloor$ over-counts whenever $X$ is a multiple of three, because it charges a break after the final level with nothing left to play. Sample case 2 catches it exactly: $X = 3$ gives $\lfloor 3/3 \rfloor = 1$ break and an answer of $46$, where the expected answer is $36$ with no break at all.

Sample case 4 confirms the formula at scale: $24 \times 45 = 1080$ playing minutes plus $\lfloor 23/3 \rfloor = 7$ breaks at $15$ minutes, giving $1080 + 105 = 1185$.

The general shape — *$n$ items have $n - 1$ gaps between them* — recurs constantly, in joining strings with separators as much as in scheduling rests.
