# 143. Two vs Ten

> CodeChef problem code [`TWOVSTEN`](https://www.codechef.com/problems/TWOVSTEN) &middot; difficulty **936** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Which prime factors an operation can supply |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef Two and Chef Ten are playing a game with a number $X$. In one turn, they can multiply $X$ by $2$. The goal of the game is to make $X$ divisible by $10$.

Help the Chefs find the smallest number of turns necessary to win the game (it may be possible to win in zero turns) or determine that it is impossible.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer denoting the initial value of $X$.

### Output
For each test case, print a single line containing one integer — the minimum required number of turns or $-1$ if there is no way to win the game.

### Constraints
- $1 \le T \le 1000$
- $0 \le X \le 10^9$

### Subtasks
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \le T \le 1000$
- $0 \le X \le 10^9$

## Sample

**Sample input**

```
3
10
25
1
```

**Sample output**

```
0
1
-1
```

## Approach

Divisibility by $10$ means divisibility by both $2$ and $5$, since $10 = 2 \times 5$. Multiplying by $2$ can supply as many factors of $2$ as wanted — but it can **never** supply a factor of $5$.

So the factor of $5$ must already be present in $X$. That splits the problem into three cases:

- $X \equiv 0 \pmod{10}$ — already done, $0$ turns.
- $X \equiv 5 \pmod{10}$ — divisible by $5$ but odd. One multiplication makes it even, hence divisible by $10$: $1$ turn.
- otherwise — $X$ has no factor of $5$, and doubling never creates one: impossible, $-1$.

Thinking in terms of **which prime factors the operation can introduce** is the move that makes this immediate. Without it, one might search over numbers of doublings and never be sure when to give up.

Note that a single doubling always suffices in the second case; there is no input needing two or more. That is because any multiple of $5$ is either already even (so $\equiv 0 \bmod 10$) or becomes even after one doubling.

The edge case is $X = 0$, which the constraints admit. Zero is divisible by everything, including $10$, so `0 % 10 == 0` correctly yields $0$ turns with no special handling.

Sample case 3 ($X = 1$) is the impossible case, and case 2 ($X = 25$) the one-turn case giving $50$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # Doubling supplies factors of 2 but never a factor of 5.
        if x % 10 == 0:
            out.append("0")
        elif x % 5 == 0:
            out.append("1")
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`
