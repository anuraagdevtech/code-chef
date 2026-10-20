# 226. String Game 

> CodeChef problem code [`STRAME`](https://www.codechef.com/problems/STRAME) &middot; difficulty **1413** &middot; time limit **4.5s**

| | |
|---|---|
| **Topic** | Game Theory |
| **Technique** | Counting the forced number of moves |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Zlatan and Ramos are playing a game on a **binary** string $S$ of length $N$.
Zlatan and Ramos make alternating moves with Zlatan going first.

In one move, a player will:

- Select an index $i$ $(1 \leq i < N)$ such that $S_i \neq S_{i+1}$ and delete both $S_i$ and $S_{i+1}$ from the string $S$. Note that $N$ gets reduced by $2$ when both characters are deleted. If a player cannot select any such index $i$, he loses the game.

Determine the winner of the game if both players play optimally.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the length of the binary string.
    - The next line contains a binary string $S$ of length $N$.

**Output**

For each test case, if Zlatan will win the game, output `Zlatan`. Otherwise, output `Ramos`.

You can output each letter of the string in uppercase or lowercase. For example, `Ramos`, `ramos`, `RAMOS`, and `rAmOS` are all considered same.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$.
- $S$ consists of $0$ and $1$ only.
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

## Sample

**Sample input**

```
5
1
0
2
11
2
10
3
111
3
101
```

**Sample output**

```
Ramos
Ramos
Zlatan
Ramos
Zlatan
```

<details><summary>Explanation</summary>

**Test case $1$:** Zlatan goes first and has no move to make. Thus, Ramos wins.

**Test case $2$:** Zlatan goes first and has no move to make. Thus, Ramos wins.

**Test case $3$:** Zlatan goes first and selects $i=1$ where $S_1\neq S_2$. Thus, he removes $S_1$ and $S_2$.
Since the string is empty now, Ramos has no move to make and Zlatan wins.

**Test case $4$:** Zlatan goes first and has no move to make. Thus, Ramos wins.

**Test case $5$:** Zlatan goes first and selects $i=1$ where $S_1\neq S_2$. Thus, he removes $S_1$ and $S_2$.
Since the string only has length $1$ now, Ramos has no move to make and Zlatan wins.

</details>

## Approach

Every move deletes one `0` and one `1`, because the chosen pair must differ. So each move reduces both counts by exactly one, and the total number of moves is fixed no matter how either player plays.

The game ends when one character runs out, so the move count is

$$\min(c_0,\ c_1)$$

Crucially, a move is **always available while both characters remain**: a string containing both a `0` and a `1` must have them adjacent somewhere, since scanning from a `0` to a `1` has to cross a boundary. So play never stalls early.

With the move count forced, the winner is pure parity. Zlatan moves first, so he makes moves $1, 3, 5, \ldots$ and wins exactly when $\min(c_0, c_1)$ is **odd**; otherwise Ramos makes the last move and Zlatan is the one left unable to play.

"Both play optimally" turns out to be vacuous here — there are no choices that matter. Recognising that a game is *move-count-determined* is the whole insight, and it saves any search over strategies.

The samples sweep the small cases: `0` and `11` offer no move at all (count $0$, even) so Zlatan loses immediately; `10` gives exactly one move; `101` has $c_0 = 1$ and $c_1 = 2$, so one move, and Zlatan wins. `111` has no `0` at all.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1]
        pos += 2
        zeros = s.count(b"0")
        # Every move removes one of each, and one is always available while
        # both remain, so the move count is forced.
        moves = min(zeros, n - zeros)
        out.append("Zlatan" if moves % 2 else "Ramos")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Algorithms`
