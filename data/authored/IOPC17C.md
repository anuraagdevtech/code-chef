---
topic: Sorting
subtopic: The second largest distinct value is the answer
time: $O(N)$ per test case
space: $O(1)$
---
The whole problem collapses once you notice that **$a \bmod b = a$ whenever $a < b$**. So taking $b$ to be the maximum and $a$ the largest value strictly below it already achieves the second largest distinct value $s$.

And nothing beats it. Fix any pair $(a, b)$:

- $a < b$: the result is $a$, and the largest such $a$ is $s$.
- $a \geq b$: the result is $a \bmod b \leq b - 1$. If $b = \max$ then $a = \max$ too, so the result is $0$. Otherwise $b \leq s$, so the result is at most $s - 1$.

Hence $\max_{i,j} A_i \bmod A_j = s$ exactly, with $0$ when all elements are equal (then no $a < b$ exists and every $a \bmod b$ is $0$). Note $i = j$ is allowed, which contributes only $0$ and changes nothing.

This matters because the natural algorithm is much heavier: for each candidate divisor $b$, scan the multiples $2b, 3b, \ldots$ and look up the largest array element just below each, which costs about $V \log V$ with $V = 10^6$. That work is entirely unnecessary here — the $a < b$ case dominates every remainder.

So one pass tracking the largest and second largest **distinct** values is enough. The distinctness is the detail to get right: duplicates of the maximum must not be mistaken for a second value, or the answer would wrongly become $\max$.

The sample $[1, 2]$ gives $1$: indeed $1 \bmod 2 = 1$, while $2 \bmod 1 = 0$.

## Edge cases

- **The answer is the second largest *distinct* value.** Taking $A_i \bmod \max$ gives $A_i$ itself for anything below the maximum, and no pair can do better: $A_i \bmod A_j < A_j$, so beating the runner-up would require $A_j$ to be the maximum, and then the result is at most the runner-up.
- **A duplicate maximum is not a runner-up.** With $A = [5, 5]$ the answer is $0$, since $5 \bmod 5 = 0$ — which is why the scan tracks distinct values and rejects $v = \text{top}$.
- **All elements equal** → $0$, which the initialiser gives since `second` stays at $0$.
- **$N = 1$** → the only pair is $i = j$, giving $0$.
- **$i$ and $j$ may be equal** by the statement, but that always yields $0$ and never helps.
- **The strict double comparison `second < v < top`** is what keeps a repeated runner-up from being promoted to `top` or being missed.
- **$A_i \geq 1$**, so no modulo by zero can arise.

## Dry run

| array | largest | second distinct | best $A_i \bmod A_j$ |
|---|---:|---:|---:|
| $1, 2$ | 2 | 1 | `1` (from $1 \bmod 2$) |
| $5, 5$ | 5 | — | `0` |
| $3, 7, 7, 4$ | 7 | 4 | `4` (from $4 \bmod 7$) |

The sample is the first row; the others show the duplicate-maximum trap.
