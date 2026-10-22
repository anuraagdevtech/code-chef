# 400. Gritty Grid

> [`GRITGRID`](https://www.codechef.com/problems/GRITGRID) &middot; difficulty **1691** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Checkerboard parity across alternating moves |
| **CodeChef tags** | `Algorithms`, `Observation` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Alice and Bob are trapped in a grid having $N$ rows and $M$ columns. Alice is currently at cell $(1, 1)$ and Bob is at cell $(N, M)$ and they both want to meet each other at any common cell. But they have some restrictions in the way they can move and meet:

A _step_ is defined as moving to an adjacent cell from the current cell that the person is in. So in a single step, if a person is at $(X, Y)$ they may move to any one of the following cells, provided that they are inside the grid's boundaries - $(X + 1, Y)$, $(X, Y + 1)$, $(X - 1, Y)$, $(X, Y - 1)$.

A _move_ for Alice is defined to be **exactly** $X$ steps. And a _move_ for Bob is defined to be **exactly** $Y$ steps.

They can only meet at the common cell after **Alice** has just completed her move i.e. they should not meet in the middle of anyone's move or at the end of Bob's move. The first time that they meet should be right after a move of Alice, and they stop moving after that.

Alice makes a move first, then Bob makes a move, and they alternate like this.

Alice and Bob want to know if it is possible to meet with these restrictions. Please help Alice and Bob by telling them whether they would be able to meet each other if they stick to these restrictions.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing four integers: $N$, $M$, $X$ and $Y$ denoting the number of rows, number of columns, number of steps in Alice's one move and the number of steps in Bob's one move respectively.

**Output**

For each test case, output in a single line $\texttt{YES}$ if they would be able to meet each other at a common cell, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N, M \leq 10^6$
- $1 \leq X, Y \leq 10^9$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
4
2 2 2 1
2 2 1 1
2 2 1 2
2 3 3 3
```

**Sample output**

```
Yes
No
Yes
Yes
```

<details><summary>Explanation</summary>

**Test case 1:** Alice is initially at $(1, 1)$, and Bob is at $(2, 2)$. In Alice's first _move_, she has to take $2$ _steps_ - she can choose to go from $(1, 1) \rightarrow (1, 2) \rightarrow (2, 2)$. And so at the end of Alice's first move, Alice and Bob meet, and they stop. So the answer is Yes.

**Test case 2:** Alice is initially at $(1, 1)$, and Bob is at $(2, 2)$. In Alice's first _move_, she has to take $1$ _step_ - she can choose to go from $(1, 1) \rightarrow (1, 2)$, or $(1, 1) \rightarrow (2, 1)$. Similarly for Bob. But you can check that no matter what they do, they can't coordinate in such a way that they meet only after Alice's move. So the answer is No.

**Test case 3:** Alice is initially at $(1, 1)$, and Bob is at $(2, 2)$. In Alice's first _move_, she has to take $1$ _step_ - she can choose to go from $(1, 1) \rightarrow (1, 2)$. Then in Bob's move, he has to take $2$ steps - he can choose to go from $(2, 2) \rightarrow (2, 1) \rightarrow (2, 2)$. Then in Alice's second move, she can choose to go from $(1, 2) \rightarrow (2, 2)$. And so at the end of Alice's second move, Alice and Bob meet, and they stop. So the answer is Yes.

**Test case 4:** Alice is initially at $(1, 1)$, and Bob is at $(2, 3)$. In Alice's first _move_, she has to take $3$ _steps_ - she can choose to go from $(1, 1) \rightarrow (1, 2) \rightarrow (1, 3) \rightarrow (2, 3)$. And so at the end of Alice's first move, Alice and Bob meet, and they stop. So the answer is Yes.

</details>

## Approach

Colour the grid like a checkerboard. Every step flips colour, so after Alice's $k$-th move her colour is $kX \bmod 2$ starting from $(1,1)$, and after Bob's $(k-1)$-th move his is $(N+M) + (k-1)Y \bmod 2$ starting from $(N,M)$. Meeting right after Alice's $k$-th move requires equal colours:

$$kX \;\equiv\; (N+M) + (k-1)Y \pmod 2$$

Distance is never the obstacle. With $N, M \geq 2$ every cell has a neighbour, so either walker can burn two steps going back and forth, and for large enough $k$ the step budget covers the whole grid. So parity is the *only* constraint, and the question is whether some $k \geq 1$ satisfies the congruence.

Reading it mod $2$ with $x = X \bmod 2$ and $y = Y \bmod 2$:

- $x \neq y$: the left side's dependence on $k$ survives, so one of the two parities of $k$ works. Always `Yes`.
- $x = y$: the $k$ terms combine to a constant — $0$ when both are even, $1$ when both are odd — so the answer is `Yes` exactly when $N + M$ matches that constant, i.e. when $N + M \equiv X \pmod 2$.

The samples are all on a tiny grid, which is where parity is starkest. $2\,2\,1\,1$ fails because both move lengths are odd while $N+M = 4$ is even — Alice is always on her starting colour after an odd-length move pair, and Bob is always on the opposite one. Changing Alice's move to $2$ steps, or Bob's to $2$, makes the parities differ and the answer flips to `Yes`. And $2\,3\,3\,3$ has both odd with $N+M = 5$ odd, which matches.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m, x, y = (int(data[1 + 4 * i]), int(data[2 + 4 * i]),
                      int(data[3 + 4 * i]), int(data[4 + 4 * i]))
        # Equal move parities fix the colour gap; unequal ones let k choose it.
        ok = x % 2 != y % 2 or (n + m) % 2 == x % 2
        out.append("Yes" if ok else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The grid is a checkerboard and each step flips colour**, so Alice's colour after $k$ moves shifts by $kX$ and Bob's by $(k-1)Y$ — they can only share a cell when those parities agree.
- **Equal move parities fix the gap.** If $X \equiv Y$, then $kX - (k-1)Y \equiv X \pmod 2$ for every $k$, so meeting requires $(N+M) \equiv X \pmod 2$ and no choice of $k$ can help.
- **Unequal move parities let $k$ choose the colour.** If $X \not\equiv Y$ the expression is $k + Y \pmod 2$, so some $k$ always works and the answer is `Yes` regardless of the grid.
- **They must meet right after Alice's move**, which is why Bob has made $k-1$ moves and not $k$ — the asymmetry is what puts $Y$ in the odd-parity branch.
- **Steps may be wasted**, since $N, M \geq 2$ always leaves a neighbour to bounce off, so distance is never an obstacle and only parity matters.
- **$X$ and $Y$ reach $10^9$** while only their parities are used.
- **The second sample row is the sole `No`**: both moves odd, and $(N+M)$ even against an odd $X$.

## Dry run

| $N$ | $M$ | $X$ | $Y$ | parities | condition | output |
|---:|---:|---:|---:|---|---|---|
| 2 | 2 | 2 | 1 | differ | $k$ is free | `Yes` |
| 2 | 2 | 1 | 1 | same | $(N{+}M) \bmod 2 = 0 \neq 1$ | `No` |
| 2 | 2 | 1 | 2 | differ | $k$ is free | `Yes` |
| 2 | 3 | 3 | 3 | same | $(N{+}M) \bmod 2 = 1 = 1$ ✓ | `Yes` |

In the second row Alice always lands on a colour Bob has just left.

---

Same problem grouped by topic: [../docs/basic-math/GRITGRID.md](../docs/basic-math/GRITGRID.md)
