---
topic: Sets
subtopic: Smallest prefix covering a required set
time: $O(N)$ per test case
space: $O(1)$
---
The team solves problems in increasing order of difficulty, and $A$ already lists the problems in that order — $A_1$ is the easiest. So the problems solved after $m$ attempts are exactly $A_1, \ldots, A_m$, a **prefix** of the array.

The balloons wanted are those for problems $1$ through $7$, so the answer is the length of the shortest prefix containing all seven:

$$\min \{\, m : \{1,\ldots,7\} \subseteq \{A_1, \ldots, A_m\} \,\}$$

Scanning left to right and tracking how many of the seven have appeared gives this in one pass, stopping as soon as the count reaches $7$.

The ordering is the point. The team cannot cherry-pick the seven problems it wants — it must work through the difficulty order, picking up unwanted balloons along the way. So the answer is governed by the **latest position** among problems $1$ to $7$, not by the number of them.

Sample case 2 shows this starkly: the problems arrive in descending order, so problem $1$ is last at position $8$, and the team must solve all $8$ problems to collect $7$ balloons. Sample case 1 is the lucky case where the seven arrive first, giving exactly $7$ — which is also the minimum possible answer, since seven balloons need at least seven solves.

Sample case 3 needs $8$: problem $2$ does not appear until position $8$, even though problem $8$ was picked up at position $7$ as a side effect.

The constraint $N \geq 7$ with distinct values in $[1, N]$ guarantees all seven are present, so the scan always terminates.
