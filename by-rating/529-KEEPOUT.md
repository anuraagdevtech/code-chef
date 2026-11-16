[&larr; 528. Forest Gathering](528-FORESTGA.md) &middot; [Index](README.md) &middot; [530. A-E Hash Function &rarr;](530-AEHASH.md)

# 529. Ultimate Fencing

> [`KEEPOUT`](https://www.codechef.com/problems/KEEPOUT) &middot; difficulty **1830** &middot; time limit **2s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Undo the insertions on a linked list of sorted posts |
| **CodeChef tags** | `binary-search` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

You've recently come into possession of a rather nice piece of land, on which you'd like to build a house.
Unfortunately, one side of this land borders a forest, and you really don't want any dangerous animals showing up at your doorstep. Naturally, you decide to build a fence to keep them out.
Building a fence requires you to place fence posts first.

The border can be thought of as a segment of length $M$ on the $x$-axis, with its endpoints at $x = 0$ and $x = M$. Initially, there are posts only at these two endpoints.

You will place $N$ posts at **distinct** points along this border, one at a time. The $i$-th of them will be placed at point $x = A_i$.
After each post is placed, you'd like to know: what's the longest *empty* segment (i.e, a segment without any posts) along the border?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of fence posts and the length of the border.
    - The second line will contain $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the positions at which the posts are placed, in order.

**Output**

For each test case, output $N$ space-separated integers on a new line. The $i$-th of them should denote the length of the longest empty segment after the first $i$ posts have been placed.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $N \lt M$
- $2 \leq M \leq 10^9$
- $1 \leq A_i \lt M$
- All the $A_i$ values are **distinct**.
- The sum of $N$ across all tests won't exceed $2\cdot 10^5$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
3
2 5
2 4
4 5
4 3 2 1
4 25
10 12 5 19
```

**Sample output**

```
3 2
4 3 2 1
15 13 13 7
```

<details><summary>Explanation</summary>

**Test case $1$:** The posts are placed as follows:
- Initially, the posts are at $[0, 5]$.
- The first post is placed at $x = 2$. The posts are at positions $[0, 2, 5]$.
The largest empty segment is between points $2$ and $5$, with a length of $3$.
- The second post is placed at $x = 4$. The posts are at positions $[0, 2, 4, 5]$.
The largest empty segment is of length $2$, between $2$ and $4$ (and also between $0$ and $2$).

**Test case $2$:** The posts are placed as follows:
- The first one is at $x = 4$, so the posts are at $[0, 4, 5]$. The longest empty segment is between $0$ and $4$, of length $4$.
- The second post is at $x = 3$, so the posts are at $[0, 3, 4, 5]$. The longest empty segment is between $0$ and $3$, of length $3$.
- The third post is at $x = 2$. The longest empty segment is between $0$ and $2$, of length $2$.
- The fourth post is at $x = 1$. The longest empty segment is of length $1$.

</details>

## Approach

Inserting a post splits a gap, and tracking the maximum gap under splits needs a heap or a sorted structure. Removing a post is much easier: it merges its two neighbouring gaps into one, so the maximum can only grow and is updated with a single comparison.

So start from the final picture: sort all posts together with the endpoints 0 and $M$, link them into a doubly linked list by sorted index and compute the largest gap. Then walk through the posts in reverse order of insertion: first record the current maximum as the answer for that prefix, then remove the post - its neighbours are read from the list in $O(1)$, the merged gap is compared with the maximum, and the two neighbours are linked to each other.

Reverse the recorded answers before printing.

## Solution

```python
import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    posts = [next(tokens) for _ in range(n)]
    points = [0] + sorted(posts) + [m]
    index_of = {post: i for i, post in enumerate(points)}
    left = [i - 1 for i in range(n + 2)]
    right = [i + 1 for i in range(n + 2)]
    best = max((points[i + 1] - points[i] for i in range(n + 1)))
    out = []
    for post in reversed(posts):
        out.append(best)
        i = index_of[post]
        l, r = (left[i], right[i])
        best = max(best, points[r] - points[l])
        right[l] = r
        left[r] = l
    return ' '.join(map(str, reversed(out)))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- The answer for the first $i$ posts is recorded before post $i$ is removed.
- The endpoints 0 and $M$ are never removed.
- Positions are distinct, so the position-to-index map is well defined.
- The only superlinear step is the initial sort.

## Dry run

`M = 25`, posts in order `10, 12, 5, 19`. Sorted points `0 5 10 12 19 25`, gaps `5 5 2 7 6`, maximum 7.

- record 7; remove 19: gap $25 - 12 = 13$, maximum 13
- record 13; remove 5: gap $10 - 0 = 10$, maximum 13
- record 13; remove 12: gap $25 - 10 = 15$, maximum 15
- record 15; remove 10

Reversed: `15 13 13 7`.

---

Same problem grouped by topic: [../docs/arrays/KEEPOUT.md](../docs/arrays/KEEPOUT.md)
