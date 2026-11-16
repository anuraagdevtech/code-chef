[&larr; 553. Chef and Strings](553-STRQ.md) &middot; [Index](README.md) &middot; [555. Root the Tree &rarr;](555-ROOTTREE.md)

# 554. Appy Loves One

> [`HMAPPY1`](https://www.codechef.com/problems/HMAPPY1) &middot; difficulty **1932** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | All rotations answered at once with a sliding-window maximum over runs |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + Q)$ |
| **Space** | $O(N)$ |

## Question

Chef has a sequence $A_1, A_2, \ldots, A_N$; each element of this sequence is either $0$ or $1$. Appy gave him a string $S$ with length $Q$ describing a sequence of queries. There are two types of queries:
- '!': right-shift the sequence $A$, i.e. replace $A$ by another sequence $B_1, B_2, \ldots, B_N$ satisfying $B_{i+1} = A_i$ for each valid $i$ and $B_1 = A_N$
- '?': find the length of the longest contiguous subsequence of $A$ with length $\le K$ such that each element of this subsequence is equal to $1$

Answer all queries of the second type.

**Input**
- The first line of the input contains three space-separated integers $N$, $Q$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains a string with length $Q$ describing queries. Each character of this string is either '?', denoting a query of the second type, or '!', denoting a query of the first type.

**Output**
For each query of the second type, print a single line containing one integer — the length of the longest required subsequence.

**Constraints**
- $1 \le K \le N \le 10^5$
- $1 \le Q \le 3 \cdot 10^5$
- $0 \le A_i \le 1$ for each valid $i$
- $S$ contains only characters '?' and '!'

**Subtasks**
**Subtask #1 (30 points):**
- $1 \le N \le 10^3$
- $1 \le Q \le 3 \cdot 10^3$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le K \le N \le 10^5$
- $1 \le Q \le 3 \cdot 10^5$
- $0 \le A_i \le 1$ for each valid $i$
- $S$ contains only characters '?' and '!'

## Sample

**Sample input**

```
5 5 3
1 1 0 1 1
?!?!?
```

**Sample output**

```
2
3
3
```

<details><summary>Explanation</summary>

- In the first query, there are two longest contiguous subsequences containing only $1$-s: $A_1, A_2$ and $A_4, A_5$. Each has length $2$.
- After the second query, the sequence $A$ is $[1, 1, 1, 0, 1]$.
- In the third query, the longest contiguous subsequence containing only $1$-s is $A_1, A_2, A_3$.
- After the fourth query, $A = [1, 1, 1, 1, 0]$.
- In the fifth query, the longest contiguous subsequence containing only $1$-s is $A_1, A_2, A_3, A_4$ with length $4$. However, we only want subsequences with lengths $\le K$. One of the longest such subsequences is $A_2, A_3, A_4$, with length $3$.

</details>

## Approach

A right shift only moves the starting point of a circular array, so there are just $N$ different arrays. Double the array; the array after $s$ shifts is the window of length $N$ starting at position $(-s) \bmod N$. Precompute the longest run of ones for every window and answer each `?` with a lookup, capped at $K$.

For every position store the length of the run of ones ending there. Inside a window, the longest run is the maximum of these values, except that a run reaching back past the left edge of the window has to be clipped to the part inside. Keep a deque of (position, run length) with decreasing lengths, as in the sliding-window maximum. Run lengths ending later inside the same run are larger, so only the front entry can be clipped; while its clipped value is no better than the next entry, drop it.

## Solution

```python
import sys
from collections import deque


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n, q, k = (int(next(tokens)) for _ in range(3))
    bits = [int(next(tokens)) for _ in range(n)]
    queries = next(tokens)
    bits += bits
    starts = [0] * len(bits)
    run = 0
    for i, x in enumerate(bits):
        run = run + 1 if x else 0
        starts[i] = i - run + 1
    window = deque()
    answers = []
    for i, x in enumerate(bits):
        length = i - starts[i] + 1 if x else 0
        while window and window[-1][1] <= length:
            window.pop()
        window.append((i, length))
        left = i - n + 1
        while window and window[0][0] < left:
            window.popleft()
        if left >= 0:
            while len(window) > 1 and min(window[0][1], window[0][0] - left + 1) <= window[1][1]:
                window.popleft()
            answers.append(min(k, window[0][1], window[0][0] - left + 1))
    start = 0
    out = []
    for ch in queries:
        if ch == 33:
            start = (start - 1) % n
        else:
            out.append(str(answers[start]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- The answer is capped at $K$, and also at $N$ when the array is all ones (the clipping takes care of that).
- An all-zero array answers 0.
- Shifts are counted modulo $N$, so a long string of `!` costs nothing extra.
- The query string is read as bytes: 33 is `!`.

## Dry run

`A = [1, 1, 0, 1, 1]`, `K = 3`, queries `?!?!?`.

Doubled array `1 1 0 1 1 1 1 0 1 1`; longest run inside each window of length 5 by start: start 0 gives 2, start 4 gives 3 (`1 1 1 0 1`), start 3 gives 4 (`1 1 1 1 0`).

- `?` with 0 shifts: start 0, answer $\min(3, 2) = 2$.
- after one `!`: start 4, answer 3.
- after two: start 3, answer $\min(3, 4) = 3$.

---

Same problem grouped by topic: [../docs/arrays/HMAPPY1.md](../docs/arrays/HMAPPY1.md)
