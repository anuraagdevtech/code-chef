---
topic: Simulation
subtopic: Best and worst completions of a prefix
time: $O(N)$ per test case
space: $O(1)$
---
After $s$ shots, team $A$ has taken $\lceil s/2 \rceil$ and team $B$ has taken $\lfloor s/2 \rfloor$, so their remaining shots are known. The result is decided at $s$ exactly when every completion of the remaining shots gives the same winner, which is a check against the two extreme completions:

- $A$ has already won if it beats $B$'s best possible finish: $g_A > g_B + (N - \lfloor s/2 \rfloor)$;
- $B$ has already won if it beats $A$'s best possible finish: $g_B > g_A + (N - \lceil s/2 \rceil)$.

A **draw** is never decided early, because a single remaining shot could break the tie — so if neither inequality ever fires, the answer is the full $2N$.

Both inequalities are strict, which matters: equality means the trailing team can still level, and a level score is a different outcome from a win.

So one left-to-right sweep over the string, updating the two goal counts and testing the two conditions, finds the smallest such $s$ in linear time.

The samples show both endings. For `101011` with $N = 3$: after four shots $A$ leads $2$–$0$ with one shot each left, and $0 + 1 < 2$, so $A$ has clinched it at $s = 4$. For `100001` the scores stay within reach of each other throughout — after five shots $A$ leads $1$–$0$ with $B$ holding one shot, which is exactly enough to draw — so the result is only known at $s = 6$, and it is a draw.
