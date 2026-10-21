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

## Edge cases

- **The first student's slot starts at time $0$**, so the running marker must be initialised to $0$ rather than to $A_1$ — otherwise the first slot comes out as length zero.
- **Slots are fixed, so an overrun does not eat into the next one.** In the second sample the first student needs $15$ against a $10$-unit slot and fails, yet the second student still gets a full $10$ units. The marker advances to $A_i$ whether or not the student finished.
- **Exactly enough time** ($B_i$ equal to the slot length): counts as done, so the comparison is non-strict — the first sample's opening row turns on it.
- **$A$ is strictly increasing** by the constraints, so every slot has positive length.

## Dry run

First sample, $A = 1, 10, 15$ and $B = 1, 10, 3$:

| $i$ | slot $A_i - \text{prev}$ | $B_i$ | fits? |
|---:|---:|---:|:---:|
| 1 | $1 - 0 = 1$ | 1 | yes |
| 2 | $10 - 1 = 9$ | 10 | no |
| 3 | $15 - 10 = 5$ | 3 | yes |

Two finish, so `2`. The second sample gives slots $10, 10, 10$ against $15, 5, 20$ — only the middle one fits, so `1`.
