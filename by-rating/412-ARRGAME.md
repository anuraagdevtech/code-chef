# 412. Game on a Strip

> [`ARRGAME`](https://www.codechef.com/problems/ARRGAME) &middot; difficulty **1705** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Game Theory |
| **Technique** | Largest free run against the runner-up |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Tzuyu gave Nayeon a strip of $N$ cells (numbered $1$ through $N$) for her birthday. This strip is described by a sequence $A_1, A_2, \ldots, A_N$, where for each valid $i$, the $i$-th cell is blocked if $A_i = 1$ or free if $A_i = 0$. Tzuyu and Nayeon are going to use it to play a game with the following rules:

- The players alternate turns; Nayeon plays first.
- Initially, both players are outside of the strip. However, note that afterwards during the game, their positions are always different.
- In each turn, the current player should choose a free cell and move there. Afterwards, this cell becomes blocked and the players cannot move to it again.
- If it is the current player's first turn, she may move to any free cell.
- Otherwise, she may only move to one of the left and right adjacent cells, i.e. from a cell $c$, the current player may only move to the cell $c-1$ or $c+1$ (if it is free).
- If a player is unable to move to a free cell during her turn, this player loses the game.

Nayeon and Tzuyu are very smart, so they both play optimally. Since it is Nayeon's birthday, she wants to know if she can beat Tzuyu. Find out who wins.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**
For each test case, print a single line containing the string `"Yes"` if Nayeon wins the game or `"No"` if Tzuyu wins (without quotes).

**Constraints**
- $1 \le T \le 40,000$
- $2 \le N \le 3\cdot 10^5$
- $0 \le A_i \le 1$ for each valid $i$
- $A_1 = A_N = 1$
- the sum of $N$ over all test cases does not exceed $10^6$

**Subtasks**
**Subtask #1 (50 points):** $A_i = 0$ for each $i$ ($2 \le i \le N-1$)

**Subtask #2 (50 points):** original constraints

## Constraints

- $1 \le T \le 40,000$
- $2 \le N \le 3\cdot 10^5$
- $0 \le A_i \le 1$ for each valid $i$
- $A_1 = A_N = 1$
- the sum of $N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
4
7
1 1 0 0 0 1 1
8
1 0 1 1 1 0 0 1
4
1 1 0 1
4
1 1 1 1
```

**Sample output**

```
Yes
No
Yes
No
```

<details><summary>Explanation</summary>

**Example case 1:** Since both Nayeon and Tzuyu play optimally, Nayeon can start e.g. by moving to cell $4$, which then becomes blocked. Tzuyu has to pick either the cell $3$ or the cell $5$, which also becomes blocked. Nayeon is then left with only one empty cell next to cell $4$ (the one Tzuyu did not pick); after she moves there, Tzuyu is unable to move, so she loses the game.

**Example case 2:** Regardless of what cell Nayeon moves to at the start, Tzuyu will always be able to beat her.

</details>

## Approach

The blocked ends split the strip into maximal runs of free cells, and because a player's second and later moves must be to an adjacent cell, each player stays inside the run she entered and walks in one direction until stuck.

Suppose Nayeon enters a run of length $L$ with $a$ free cells to her left and $b$ to her right ($a + b = L - 1$). Tzuyu has two replies:

- **Contest the same run.** She steps in next to Nayeon on the larger side, so Nayeon can only walk the smaller side, making $1 + \min(a,b)$ moves while Tzuyu makes $\max(a,b)$. Nayeon needs $1 + \min > \max$, which is possible only with $a = b$, i.e. **$L$ odd**, taking the exact middle.
- **Take another run.** Entering a run of length $L'$ at its end gives her $L'$ moves, while Nayeon, unopposed from the middle, makes $1 + \frac{L-1}{2} = \frac{L+1}{2}$.

Since Nayeon commits her cell first, she must survive both replies, so her run must be odd *and* satisfy $\frac{L+1}{2} > L'$ for every other run. Only the longest run can qualify — any shorter one is beaten by the longest. With $M$ the largest run length and $M_2$ the second largest ($0$ if there is only one run):

$$\text{Nayeon wins} \iff M \text{ odd and } \frac{M+1}{2} > M_2$$

This matches an exhaustive search over all strips up to length $12$. Note how sharp it is: $[1,3]$ wins but $[2,3]$ loses, and $[2,5]$ wins but $[3,5]$ loses — a runner-up of exactly $\frac{M+1}{2}$ is enough for Tzuyu to draw level, and level means Nayeon runs out first.

The samples: one run of $3$ wins; runs $\{1,2\}$ lose on parity; a single cell wins trivially since Tzuyu has nowhere to go; and a fully blocked strip loses at once.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        best = second = 0
        run = 0
        for i in range(n):
            if data[pos + 1 + i] == b"0":
                run += 1
                continue
            if run > best:
                best, second = run, best
            elif run > second:
                second = run
            run = 0
        if run > best:
            best, second = run, best
        elif run > second:
            second = run
        pos += 1 + n
        # Odd longest run, and its half must outgrow the runner-up.
        out.append("Yes" if best % 2 and (best + 1) // 2 > second else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/game-theory/ARRGAME.md](../docs/game-theory/ARRGAME.md)
