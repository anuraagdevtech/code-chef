# 1200 &middot; Chef and Linear Chess

> CodeChef problem code [`LINCHESS`](https://www.codechef.com/problems/LINCHESS) &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Divisors as reachable positions |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Basic Math`, `Sorting` |
| **CodeChef category** | easy |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/number-theory/LINCHESS.md](../docs/number-theory/LINCHESS.md)

## Question

Chef wants to play a game of *linear chess* on a one-dimensional board ― an infinite row of squares numbered by positive integers. In this game, he has a pawn, which is initially at a square $K$. There are also $N$ other people (numbered $1$ through $N$); Chef can choose one of them to play against. For each valid $i$, the $i$-th player would play in the following way:
- Take a pawn and place it on a square $P_i$.
- Repeat the following move any number of times: move the pawn from its current square $P_i$ squares forward, i.e. from a square $s$, this player's pawn is moved to the square $s+P_i$.
- If this player moves their pawn to the square with Chef's pawn, then Chef's pawn is *captured* and he loses the game.

Unfortunately, Chef cannot move his pawn during the game, making him an easy target for other players. Given the starting positions of all $N+1$ players, find a player who can capture Chef's pawn in the smallest number of moves or determine that no player can capture his pawn.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $P_1, P_2, \ldots, P_N$.

### Output
For each test case, print a single line containing one integer ― the starting square of one player that can beat Chef in the smallest number of turns, or $-1$ if no player can beat him.

If there are multiple solutions, you may find any one.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 1,000$
- $1 \le K \le 10^9$
- $1 \le P_i \le 10^9$ for each valid $i$
- $K, P_1, P_2, \ldots, P_N$ are pairwise distinct

### Subtasks
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 1,000$
- $1 \le K \le 10^9$
- $1 \le P_i \le 10^9$ for each valid $i$
- $K, P_1, P_2, \ldots, P_N$ are pairwise distinct

## Sample

**Sample input**

```
2
4 6
4 3 2 8
4 7
4 3 2 8
```

**Sample output**

```
3
-1
```

<details><summary>Explanation</summary>

**Example case 1:** The player who starts at the position $2$ can move to square $4$ and then to square $6$. The player who starts at the position $3$ can move to square $6$. The player at position $2$ can capture Chef's pawn in $2$ turns, whereas the player at position $3$ can capture Chef's pawn in $1$ turn. Therefore, the answer is $3$.

**Example case 2:** No player can capture Chef's pawn.

</details>

## Approach

Player $i$ places a pawn on square $P_i$ and then advances by $P_i$ each move, so the squares they ever occupy are

$$P_i,\ 2P_i,\ 3P_i,\ \ldots$$

— exactly the positive multiples of $P_i$. So that player can reach Chef's square $K$ **if and only if $P_i$ divides $K$**.

When it does, reaching $K$ takes $\frac{K}{P_i} - 1$ moves, since the pawn starts already placed on $P_i$. That count shrinks as $P_i$ grows, so among the divisors of $K$ present in the list, the **largest** one wins. If none divides $K$, the answer is $-1$.

Recasting "can this player reach that square" as a divisibility test is the whole problem; without it one might try to simulate the moves, which is hopeless with $K$ up to $10^9$.

The output is the **starting square** $P_i$, not the number of moves — easy to misread, since the question is phrased around move counts.

Sample case 1 has $K = 6$ with candidates $\{4,3,2,8\}$. Both $3$ and $2$ divide $6$, needing $1$ and $2$ moves respectively, so the larger divisor $3$ is reported. Sample case 2 has $K = 7$, a prime, and none of $\{4,3,2,8\}$ divides it — note that $7$ itself does not appear, and the guarantee that all values are pairwise distinct means $P_i = K$ never happens anyway.

A single pass over the list suffices; no factorisation of $K$ is required, since the candidates are given.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        best = -1
        for v in data[pos + 2:pos + 2 + n]:
            p = int(v)
            # A player lands on the multiples of their own step size.
            # Larger divisors need fewer moves.
            if k % p == 0 and p > best:
                best = p
        pos += 2 + n
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
