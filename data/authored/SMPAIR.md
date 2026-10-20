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
