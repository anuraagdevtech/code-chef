---
topic: Arrays
subtopic: Consecutive differences as a window
time: $O(N)$ per test case
space: $O(1)$
---
Student $i$ starts when student $i-1$ must be finished, so their slot runs from $A_{i-1}$ to $A_i$, with $A_0 = 0$ for the first student. The window available to student $i$ is therefore the **consecutive difference**

$$A_i - A_{i-1}$$

and they succeed when $B_i \leq A_i - A_{i-1}$. Counting the successes is one pass.

The crucial point is that the slots are **fixed in advance**, not consumed dynamically. A student who runs out of time simply fails; they do not eat into the next student's window, and a student who finishes early does not donate the slack forward. So each student is judged independently against their own gap, and no running clock needs maintaining.

Sample case 1 makes this concrete. Windows are $1, 9, 5$ against requirements $1, 10, 3$. The second student fails, needing $10$ but having $9$ — and the third student is **unaffected**, succeeding with $3 \leq 5$. A simulation that advanced a shared clock past the overrun would wrongly fail the third as well.

Sample case 2 has uniform windows of $10$ against $15, 5, 20$, so only the middle student manages.

Seeding with $A_0 = 0$ is what lets the first student be handled by the same expression as the rest, rather than as a special case. With $N$ up to $10^4$ and values to $10^9$, nothing is at risk numerically, and the single pass is well within limits.
