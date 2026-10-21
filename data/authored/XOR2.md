---
topic: Bit Manipulation
subtopic: The total XOR is invariant
time: $O(N)$ per test case
space: $O(1)$
---
Each operation XORs the **same** $X$ into two neighbouring elements. In the XOR of the whole array those two contributions cancel, since $X \oplus X = 0$. So

$$A_1 \oplus A_2 \oplus \cdots \oplus A_N \;\text{ is invariant}$$

no matter how many operations are applied.

Now look at the target. If every element ends up equal to some $v$, the total XOR of the final array is $v$ when $N$ is **odd** (the copies cancel in pairs, leaving one) and $0$ when $N$ is **even** (they cancel completely).

- **$N$ odd.** The invariant imposes no obstruction — whatever the starting total $S$ is, the target value $v = S$ is consistent, and the operations are flexible enough to reach it. So the answer is always `YES`.
- **$N$ even.** The final total must be $0$, so the starting total must be $0$ too. The answer is `YES` exactly when $S = 0$.

Sample case 1, $[3,2,2,3]$, has even length and total $3 \oplus 2 \oplus 2 \oplus 3 = 0$ — `YES`. Sample case 2 has even length but total $1$, so no sequence of operations can ever fix it — `NO` regardless of effort.

Sample case 3, $[1,2,4]$, is odd-length and so succeeds even though its elements look entirely unrelated; the target is simply $1 \oplus 2 \oplus 4 = 7$.

Finding the conserved quantity is the whole solution — it decides both directions at once, and the answer is a single XOR fold plus a parity check.
