# 333. Gravity Guy

> [`GRGUY`](https://www.codechef.com/problems/GRGUY) &middot; difficulty **1568** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Two-state DP with a zero-cost move |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(n)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef likes to play games a lot. Gravity Guy is one such interesting game.

"*Gravity Guy is an arcade side-scrolling game in which the player controls Gravity Guy by tapping the screen to switch gravity. The objective in this game is to run as far as possible while avoiding being trapped by obstacles, falling, or flying off the screen. If hit by obstacles, the game is over.*"

Chef is so addicted to this game that each night he dreams of himself being in the game as Gravity Guy. He has two lanes in front of him represented by two strings of equal length named as **L_1** and **L_2**. Each of the two lanes consists of some clean blocks represented by **'.'** and some dirty blocks represented by **'#'**.

Chef can start running from the beginning of any of the two lanes and cannot step over any dirty block **( '#' )** encountered during his journey. He has to complete his journey by reaching the end block of any of the two lanes.

Chef can use the following jumps to reach his destination. Considering chef is at **x^th** block of some lane.

- He can jump to **x+1^th** block of the same lane.

- He can switch gravity quickly and jump to **x^th** block of the other lane.

- He can switch gravity and jump to **x+1^th** block of the other lane.

You have to tell him whether he can reach his destination or not. If it is possible for him to reach his destination, then Chef is interested in knowing the minimum number of gravity switches required to reach the destination.

**Input**

First line of input contains a single integer **T** denoting the number of test cases. Each test case consists of **2** lines. First line of each test case contains a string denoting lane **L_1**. Second line of each test case contains a string denoting lane **L_2**.

**Output**

For each test case, print **"Yes"** (without quotes) in the first line if Chef is able to reach the destination followed by a line containing an integer denoting minimum number of gravity switches required to reach to the destination. Print a single line containing the word **"No"** (without quotes) otherwise.

**Constraints**

- **1 ≤ T ≤ 10^5**

- **1 ≤ |L_1| ≤ 2 × 10^5**, where **|S|** denotes the length of string **S**

- **|L_1| = |L_2|**

**Subtasks**

**Subtask 1 (25 points)**

- Sum of **|L_1|** over all test cases in one file it at most **200**.

- Only "Yes"/"No" response will be evaluated.

**Subtask 2 (25 points)**

- Sum of **|L_1|** over all test cases in one file it at most **200**.

**Subtask 3 (25 points)**

- Sum of **|L_1|** over all test cases in one file it at most **10^6**.

- Only "Yes"/"No" response will be evaluated.

**Subtask 4 (25 points)**

- Sum of **|L_1|** over all test cases in one file it at most **10^6**.

## Constraints

- 1 ≤ T ≤ 10^5
- 1 ≤ |L_1| ≤ 2 × 10^5, where |S| denotes the length of string S
- |L_1| = |L_2|

## Sample

**Sample input**

```
3
#...#
.###.
#.#.#.
.#.#.#
#...
#...
```

**Sample output**

```
Yes
2
Yes
5
No
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef will start his journey from $L_2$. He switches gravity and jumps to $L_1$. He continues on $L_1$ till block $4$ and then again switch gravity and jump to block $5$ of $L_2$. Therefore, he requires total $2$ gravity switches to reach the destination.

**Test case $2$:** Chef will start his journey from $L_2$. He switches gravity and jumps to second block of $L_1$. He switches gravity and jumps to third block of $L_2$. He switches gravity and jumps to fourth block of $L_1$. He switches gravity and jumps to fifth block of $L_2$. He switches gravity and jumps to sixth block of $L_1$. Therefore, he requires total $5$ gravity switches to reach the destination.

**Test case $3$:** Chef cannot start his journey as starting block of both the lanes $L_1$ and $L_2$ are dirty and he cannot step over them.

</details>

## Approach

With only two lanes the state is tiny — (lane, column) — and the cost model is what makes it interesting: advancing within a lane is **free**, while the two gravity-switching moves cost $1$. Minimising switches is therefore a shortest path on a graph with $0$- and $1$-weight edges.

Because every move either advances the column or stays in it, a left-to-right DP over columns is a valid order. Let $f[\ell][x]$ be the fewest switches to stand on lane $\ell$, column $x$. At each column, in order:

1. **Settle the free-standing switch:** $f[1-\ell][x] \leftarrow f[\ell][x] + 1$ if that cell is clean. Doing this once in each direction is enough — switching twice in the same column only wastes two moves.
2. **Push forward:** to $(\ell, x{+}1)$ at no cost and to $(1-\ell, x{+}1)$ at cost $1$, in each case only onto a clean block.

Chef may start on either lane and finish on either, so initialise both lanes at column $1$ (whichever are clean) and answer with the minimum over both lanes at column $n$. Unreachable means `No`.

Only two values per column are ever live, so the sweep runs in constant space — worth having with $|L|$ up to $2 \times 10^5$ and $T$ up to $10^5$.

The samples show the range. In `#...#` / `.###.` the blocked ends force a start on lane 2 and a finish on lane 2, with a crossing out and back: $2$ switches. The alternating `#.#.#.` / `.#.#.#` leaves no choice at all — every step must change lane, giving $5$. And two identical lanes starting with `#` block both entrances, so the answer is `No` before any move is considered.

## Solution

```python
import sys

INF = float("inf")
CLEAN = 0x2E       # '.'


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        top, bot = data[1 + 2 * i], data[2 + 2 * i]
        n = len(top)
        a = 0 if top[0] == CLEAN else INF
        b = 0 if bot[0] == CLEAN else INF
        for x in range(n):
            if x:
                prev_a, prev_b = a, b
                # Arrive by advancing (free) or by switching lanes (cost 1).
                a = min(prev_a, prev_b + 1) if top[x] == CLEAN else INF
                b = min(prev_b, prev_a + 1) if bot[x] == CLEAN else INF
            # A switch inside the column; once each way is enough.
            if top[x] == CLEAN and b + 1 < a:
                a = b + 1
            if bot[x] == CLEAN and a + 1 < b:
                b = a + 1
        best = a if a < b else b
        out.append("No" if best == INF else f"Yes\n{best}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Advancing is free and switching lanes costs one**, so the DP tracks the cheapest way to stand in each lane at each column — two states, rolled forward.
- **A switch within the same column must be allowed**, which is the second pair of updates: the guy can flip gravity and then advance, so arriving in one lane lets him reach the other at $+1$ in that same column. Without it the second sample is unsolvable.
- **One in-column switch each way is enough**, since switching twice returns to the start at a strictly higher cost.
- **Obstacles make a state unreachable**, marked `INF` — and `INF` must never be treated as $0$, or the path would tunnel through walls.
- **Both lanes blocked at the start** (the third sample, with `#` atop `#`) → `No` immediately, and the sentinel propagates it to the end.
- **The answer is the better of the two lanes at the last column**, since finishing in either is acceptable.
- **The output is two lines on success** — `Yes` then the count — and one line on failure.
- **Sum of lengths up to $2 \times 10^5$** with $T$ up to $10^5$, so the state is two scalars rather than arrays.

## Dry run

First sample: top `#...#`, bottom `.###.`

| column | top reachable at | bottom reachable at |
|---:|---|---|
| 0 | blocked | **0** |
| 1 | $0 + 1 = 1$ (switch) | blocked |
| 2 | 1 | blocked |
| 3 | 1 | blocked |
| 4 | blocked | $1 + 1 = $ **2** (switch) |

Output `Yes` then `2`: one switch down at column 1 and one back up at column 4.

---

Same problem grouped by topic: [../docs/dynamic-programming/GRGUY.md](../docs/dynamic-programming/GRGUY.md)
