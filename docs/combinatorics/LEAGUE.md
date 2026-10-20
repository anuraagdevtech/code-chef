# 122. Farmers League

> CodeChef problem code [`LEAGUE`](https://www.codechef.com/problems/LEAGUE) &middot; difficulty **883** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Extremal construction in a round robin |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

A football league of $N$ teams is taking place, where each team plays other teams once in [single round robin](https://en.wikipedia.org/wiki/Round-robin_tournament) fashion. A team gets $3$ points for winning a game and $0$ for losing (assume that no games end in a draw/tie). What is the **maximum** possible difference of points between the winning team and the second-placed team?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing a single integer $N$.

**Output**

For each test case, output in a single line the maximum difference of points between first and second place.

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^9$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
4
2
3
4
9
```

**Sample output**

```
3
3
6
12
```

<details><summary>Explanation</summary>

**Test case $1$:** There will only be one match played between the two teams, therefore one team wins by $3$ points.

**Test case $2$:** Let the three teams be A, B, C. If team A wins both the games against team B and team C, then team A will win by $3$ points since one of team B and team C will win the game between them.

**Test case $3$:** Let the four teams be A, B, C, D. One possibility is for A to win all its games, and then B beats C, C beats D, D beats B. This way, the winner has $9$ points and second place has $3$ points, making a difference of $6$.

**Test case $4$:** It can be shown that it's not possible to achieve a difference higher than $12$ when $9$ teams play. One way of achieving this is for the winner to score $24$ points and second place to score $12$.

</details>

## Approach

To maximise the gap, push the winner as high as possible and the runner-up as low as possible.

**The winner** can take every one of its $N - 1$ games, for $3(N-1)$ points. Nothing constrains this.

**The runner-up** is the best of the remaining $N - 1$ teams, and here is the constraint that makes the problem interesting: those teams still play each other, and every game produces a winner. Among themselves they contest $\binom{N-1}{2}$ games, so they share $N-1 \choose 2$ wins between $N - 1$ teams. By the pigeonhole principle the best of them has at least

$$\left\lceil \frac{\binom{N-1}{2}}{N-1} \right\rceil = \left\lceil \frac{N-2}{2} \right\rceil$$

wins, and that bound is achievable by spreading the results as evenly as possible. So the runner-up can be held to $3\left\lceil \frac{N-2}{2} \right\rceil$ points and no lower.

The difference simplifies neatly:

$$3(N-1) - 3\left\lceil \frac{N-2}{2} \right\rceil = 3 \left\lfloor \frac{N}{2} \right\rfloor$$

so the whole answer is `3 * (n // 2)`.

The pigeonhole step is the part worth dwelling on. The instinct is to say the runner-up could lose everything and score $0$ — but that is impossible once $N \geq 3$, because the non-winning teams must distribute wins among themselves. Sample case 3 shows it: with $N = 4$ the answer is $6$, not $9$, because the other three teams play three games and someone must win at least one.

Sample case 1 is the exception where the instinct holds: with $N = 2$ the loser really does score $0$, and $3 \lfloor 2/2 \rfloor = 3$.

With $N$ up to $10^9$ and $T$ up to $10^5$, only a closed form is viable.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Winner takes 3(n-1); the rest must share wins among themselves, so
        # the runner-up cannot be held below 3*ceil((n-2)/2). This simplifies.
        out.append(str(3 * (n // 2)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
