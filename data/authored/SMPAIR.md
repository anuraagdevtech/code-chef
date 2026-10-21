---
topic: Sorting
subtopic: The two smallest elements
time: $O(N)$ per test case
space: $O(1)$
---
The smallest sum $a_i + a_j$ over distinct indices is simply the sum of the **two smallest values** in the array. Any other pair replaces one of them with something at least as large.

Two ways to get them. Sorting and taking the first two is $O(N \log N)$ and reads clearly. Better, a single pass tracking the smallest and second-smallest is $O(N)$ — and with the hardest subtask allowing $N = 10^5$ across $T = 10$ cases, plus $T = 10^5$ cases of $N = 2$, the linear version is the one that comfortably fits both shapes. Python's `heapq.nsmallest(2, a)` does it in one pass without a full sort.

The constraint $i < j$ means two **distinct positions**, not two distinct values. So an array like $[3, 3]$ answers $6$: the two entries are separate elements even though they are equal. A solution deduplicating the values first would break on that, and it is the most likely bug here.

The guarantee $N \geq 2$ means a valid pair always exists, so no empty case needs handling.

Sample: $[5, 1, 3, 4]$ has smallest $1$ and second smallest $3$, giving $4$. Note the two need not be adjacent in the input.

With $a_i$ up to $10^6$ the sum stays small; the subtask table in the constraints is really a hint about which complexities will pass, and only the $O(N)$ or $O(N \log N)$ approaches clear all four.

## Edge cases

- **Equal values are a valid pair**, because the problem asks for two distinct *positions*, not two distinct values — $[2, 2]$ answers $4$.
- **$N = 2$**: the only pair, which the $13$- and $16$-point subtasks hammer at $T = 10^5$.
- **`nsmallest(2, …)` is linear**, not $O(N \log N)$, which matters for the $40$-point subtask at $N = 10^5$ while keeping the per-case overhead tiny for the $T = 10^5$ subtasks.
- **The subtasks have very different shapes** — many tiny cases versus a few large ones — so both the per-case cost and the per-element cost have to stay low, hence a single buffered read for the whole file.
- **$a_i$ up to $10^6$**, so the sum reaches $2 \cdot 10^6$ and fits anywhere.
- **The two smallest need not be adjacent** in the input, so a scan comparing neighbours is wrong; the sample's $1$ and $3$ sit either side of a larger value.

## Dry run

Input $5, 1, 3, 4$.

| rank | value |
|---|---:|
| smallest | 1 |
| second smallest | 3 |

Output `4`. The $5$ and $4$ are never considered.
