[&larr; 364. Construct Array](364-CONSTRRAY.md) &middot; [Index](README.md) &middot; [366. Stamps 100 &rarr;](366-S100.md)

# 365. Zebra Crossing

> [`ZEBRA`](https://www.codechef.com/problems/ZEBRA) &middot; difficulty **1626** &middot; time limit **0.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Earliest hops, then one long final leap |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

**Read problems statements in [Russian](https://www.codechef.com/download/translated/COOK133/russian/ZEBRA.pdf) and [Bengali](https://www.codechef.com/download/translated/COOK133/bengali/ZEBRA.pdf).**
There's a zebra crossing appearing in the middle of nowhere with $N$ blocks in it. The colors of the zebra crossing is represented by a binary string $S$, where $S_i$ is `1` if the $i$-th block from the left is white, and `0` if the block is black.

Chef really wants to play with the zebra crossing. Although the given zebra crossing might not have alternate black and white blocks, Chef wants to follow the alternating white-black color pattern while crossing it.

Initially, Chef stands at block $1$. Chef has to jump **exactly** $K$ times, and in each jump he has to move forward and jump to a different color than that previously occupied by Chef. More formally, suppose that Chef is currently at block $i$ and wants to jump to block $j$ then following conditions should hold:

- $i < j$
- $S_i \neq S_j$

Output the farthest block Chef can reach with exactly $K$ jumps. If Chef cannot jump exactly $K$ times, output `-1`.

**Input**

- The first line contains an integer $T$ denoting the number of test cases. The $T$ test cases then follow.
- The first line of each test case contains two integers $N$ and $K$.
- The second line of each test case consists of a binary string of length $N$ denoting the color of blocks of the zebra crossing.

**Output**

For each test case, output the farthest block Chef can reach with exactly $K$ jumps, or `-1` in case Chef cannot jump exactly $K$ times.

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^3$
- $1 \leq K \leq N$
- Sum of $N$ over all test cases does not exceed $5 \cdot 10^5$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
6 2
100101
5 1
10111
6 1
000000
```

**Sample output**

```
6
2
-1
```

<details><summary>Explanation</summary>

- For the first test case, Chef can jump in the following order: $1 \rightarrow 5 \rightarrow 6$.

- For the second test case, Chef can jump in the following order: $1 \rightarrow 2$.

- For the third test case, Chef cannot make any jumps.

</details>

## Approach

Colours must alternate, so after $j$ jumps Chef stands on colour $S_1 \oplus (j \bmod 2)$ — the required colour at every step is fixed in advance and does not depend on the route.

That makes the greedy clean: take the **first $K-1$ jumps as early as possible**, then make the last jump as far as possible. Landing earlier is never worse, because the set of legal landing spots for a later jump is a suffix of the blocks, and a suffix only grows as the current position moves left. So

- for $j = 1, \ldots, K-1$: move to the smallest index beyond the current one with the required colour;
- for the last jump: move to the **largest** index beyond the current one with the required colour.

If any step finds no such index, exactly $K$ jumps are impossible and the answer is $-1$. Note the problem insists on *exactly* $K$ jumps, so stopping early is not allowed even when Chef has already gone far.

The samples cover the three behaviours. In `100101` with $K = 2$, Chef starts on white at block $1$, hops minimally to the black block $2$, then leaps to the last white block, $6$. In `10111` with $K = 1$ the single jump must land on black, and the only black block is $2$ — so the answer is $2$ even though blocks $3, 4, 5$ lie further on. And `000000` offers no colour change at all, so even one jump is impossible.

Greedily minimising the early jumps is what makes the one-leap-at-the-end optimal; doing it the other way round — jumping far immediately — would strand Chef with no room left.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        s = data[pos + 2]
        pos += 3
        # First index after i whose colour differs: the end of i's own run.
        nxt = [n] * n
        for i in range(n - 2, -1, -1):
            nxt[i] = i + 1 if s[i] != s[i + 1] else nxt[i + 1]
        last = {s[n - 1]: n - 1}
        for i in range(n - 2, -1, -1):
            last.setdefault(s[i], i)

        at = 0
        for _ in range(k - 1):            # land as early as possible
            at = nxt[at]
            if at == n:
                break
        if at == n:
            out.append("-1")
            continue
        far = last.get(s[at] ^ 1, -1)     # then leap as far as possible
        out.append(str(far + 1) if far > at else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The first $K-1$ jumps should land as early as possible**, which keeps the most blocks in reach for the ones that follow — and the earliest legal landing from block $i$ is the end of $i$'s own colour run.
- **The final jump should go as far as possible**, to the *last* block of the opposite colour. Splitting the strategy this way is the whole solution: greedy-early for all but the last jump, greedy-far for the last.
- **Running out of blocks mid-way gives $-1$** (the `at == n` break), which is how an all-one-colour crossing fails.
- **A single colour throughout** (the third row, all zeros) admits no jump at all, so even $K = 1$ answers $-1$.
- **Exactly $K$ jumps are required**, not at most $K$ — so a crossing that allows fewer is a failure, not a partial success.
- **The run-end table is built right to left**, with `nxt[i] = i + 1` when the colours differ and inherited otherwise, which gives every start its earliest landing in one pass.
- **The last-occurrence map is also built right to left** with `setdefault`, so each colour records its final position.
- **$S_i \neq S_j$ is the only colour rule**, so the alternation follows automatically from jumping to a different colour each time.

## Dry run

First sample: $N = 6$, $K = 2$, $S = $ `100101`.

| step | at block | colour | action |
|---|---:|---|---|
| start | 1 | white | — |
| jump 1 (early) | 2 | black | earliest differing block |
| jump 2 (far) | 6 | white | last white block |

Output `6`. Jumping far on the first move instead would land on block $4$ or $6$ and leave no legal second jump to a black block beyond.

---

Same problem grouped by topic: [../docs/greedy/ZEBRA.md](../docs/greedy/ZEBRA.md)
