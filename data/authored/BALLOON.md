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

## Edge cases

- **Problems numbered above $7$ are irrelevant and must not advance the count.** The second and third rows both contain an $8$, and the third also a $9$; counting them as progress gives the wrong index.
- **The answer can be $N$** (the first row, where the last of the seven arrives on the final problem).
- **All of $1, \dots, 7$ are guaranteed present**, because $N \geq 7$ and the $A_i$ are distinct values in $[1, N]$ — so the loop always finds the seventh and the fallback `answer = n` is a formality.
- **Duplicates are impossible**, so each needed problem is counted exactly once and the set never re-adds.
- **$T$ up to $10{,}500$** with $N \leq 15$: the work is dominated by reading input, so the scan should break as soon as the seventh is seen.

## Dry run

Third sample: $7, 4, 3, 5, 6, 1, 8, 2, 9$.

| position | problem | needed? | distinct needed seen |
|---:|---:|:---:|---:|
| 1 | 7 | yes | 1 |
| 2 | 4 | yes | 2 |
| 3 | 3 | yes | 3 |
| 4 | 5 | yes | 4 |
| 5 | 6 | yes | 5 |
| 6 | 1 | yes | 6 |
| 7 | 8 | **no** | 6 |
| 8 | 2 | yes | **7** |

Output `8`. Problem $8$ at position $7$ contributes nothing.
