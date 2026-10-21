# 1735 &middot; Penalty Shoot-Out II

> CodeChef problem code [`PSHOT`](https://www.codechef.com/problems/PSHOT) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Simulation |
| **Technique** | Best and worst completions of a prefix |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **CodeChef top tag** | `Ad Hoc` |
| **CodeChef category** | easy |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/simulation/PSHOT.md](../docs/simulation/PSHOT.md)

## Question

Teams $A$ and $B$ are having a penalty shoot-out to decide the winner of their football match. Each team gets to take a shot $N$ times, and the team with the higher number of scored goals at the end wins. If the number of goals scored during the shoot-out by each team turns out to be the same even after all $2N$ shots, then they stop and agree that the result is a draw.

The two teams take shots alternately — team $A$ shoots first, then team $B$ shoots, then team $A$ and so on until team $B$ takes its $N$-th shot (at which point each team has taken exactly $N$ shots). Even though all $2N$ shots are taken, the result of the shoot-out is often known earlier — e.g. if team $A$ has already scored $N-1$ goals and team $B$ has missed at least two shots, team $A$ is definitely the winner.

For each shot, you know whether it was a goal or a miss. You need to find the earliest moment when the winner is known — the smallest $s$ ($0 \le s \le 2N$) such that after $s$ shots, the result of the shoot-out (whether team $A$ won, team $B$ won or the match is drawn) would be known even if we did not know the results of the remaining $2N-s$ shots.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains a string $S$ with length $2 \cdot N$, where for each valid $i$, the $i$-th character is '0' if the $i$-th shot was a miss or '1' if it was a goal.

### Output
For each test case, print a single line containing one integer — the smallest $s$ such that after $s$ shots, the result of the shoot-out is known.

### Constraints
- $1 \le T \le 10^5$
- $1 \le N \le 10^5$
- $S$ contains only characters '0' and '1'
- the sum of $N$ over all test cases does not exceed $10^6$

## Constraints

- $1 \le T \le 10^5$
- $1 \le N \le 10^5$
- $S$ contains only characters '0' and '1'
- the sum of $N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
2
3
101011
3
100001
```

**Sample output**

```
4
6
```

<details><summary>Explanation</summary>

**Example case 1:** After four shots, team $A$ has scored $2$ goals and team $B$ has scored $0$ goals. Whatever happens afterwards, team $A$ is guaranteed to win, since even if team $B$ scored their last (and only) goal and team $A$ did not score their last goal, team $A$ would still win by $1$ goal.

**Example case 2:** Team $A$ scores the first goal and after that, neither team scores any goals until the last shot. Up till then, there is always a possibility that the match could end in a draw if team $B$ scored a goal with its last shot, or in the victory of team $A$ if it was a miss. We can only guarantee the result after the last shot.

</details>

## Approach

After $s$ shots, team $A$ has taken $\lceil s/2 \rceil$ and team $B$ has taken $\lfloor s/2 \rfloor$, so their remaining shots are known. The result is decided at $s$ exactly when every completion of the remaining shots gives the same winner, which is a check against the two extreme completions:

- $A$ has already won if it beats $B$'s best possible finish: $g_A > g_B + (N - \lfloor s/2 \rfloor)$;
- $B$ has already won if it beats $A$'s best possible finish: $g_B > g_A + (N - \lceil s/2 \rceil)$.

A **draw** is never decided early, because a single remaining shot could break the tie — so if neither inequality ever fires, the answer is the full $2N$.

Both inequalities are strict, which matters: equality means the trailing team can still level, and a level score is a different outcome from a win.

So one left-to-right sweep over the string, updating the two goal counts and testing the two conditions, finds the smallest such $s$ in linear time.

The samples show both endings. For `101011` with $N = 3$: after four shots $A$ leads $2$–$0$ with one shot each left, and $0 + 1 < 2$, so $A$ has clinched it at $s = 4$. For `100001` the scores stay within reach of each other throughout — after five shots $A$ leads $1$–$0$ with $B$ holding one shot, which is exactly enough to draw — so the result is only known at $s = 6$, and it is a draw.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        ga = gb = 0
        answer = 2 * n
        for k, c in enumerate(s, 1):
            if c == 0x31:
                if k % 2:
                    ga += 1
                else:
                    gb += 1
            # Compare against the opponent's best possible finish.
            if ga > gb + (n - k // 2) or gb > ga + (n - (k + 1) // 2):
                answer = k
                break
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
