# 114. Badminton Serves

> CodeChef problem code [`BADMINTON`](https://www.codechef.com/problems/BADMINTON) &middot; difficulty **869** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Counting even values in a range |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef is playing badminton today. The service rules of this singles game of badminton are as follows:
1. The player who starts the game serves from the **right** side of their court.
2. Whenever a player wins a point, they serve next.
3. If the server has won an **even** number of points during a game, then they will serve from the **right** side of the service court for the subsequent point.

Chef will be the player who begins the game.

Given the number of points $P$ obtained by Chef at the end of the game, please determine how many times Chef served from the **right** side of the court.

Please see the sample cases below for explained examples.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line containing one integer $P$, the points obtained by Chef.

**Output**

For each test case, output in a single line the number of times Chef served from the **right** side of the court.

## Constraints

- $1 \leq T \leq 10^3$
- $0 \leq P \leq 10^9$

## Sample

**Sample input**

```
4
2
9
53
746
```

**Sample output**

```
2
5
27
374
```

<details><summary>Explanation</summary>

**Test case $1$**: Chef obtained $2$ points at the end of the game. This means he served two times from the right side of the court, once when his score was $0$ and once again when his score was $2$.

**Test case $2$**: Chef obtained $9$ points at the end of the game. This means he served $5$ times from the right side of the court. The points when he had to serve from right were: $0,2,4,6,8$.

</details>

## Approach

Chef serves at the start of the game, and thereafter whenever he wins a point. So each of Chef's serves happens at a distinct score of his own: $0$ at the opening serve, then $1$ after his first point, then $2$, and so on up to $P$. He serves exactly once at each of the scores $0, 1, \ldots, P$.

Rule 3 says he serves from the **right** when his score is even. So the answer is the number of even integers in $[0, P]$:

$$\left\lfloor \frac{P}{2} \right\rfloor + 1$$

The $+1$ is there because the range starts at the even value $0$ — the opening serve counts, and it is from the right.

The reasoning that each score from $0$ to $P$ is served exactly once is the real content. It holds no matter how the opponent's points are interleaved: Chef may lose the serve repeatedly, but he regains it precisely when he scores, and that is the moment his count ticks up. The opponent's score never enters the formula.

Checking the samples: $P = 9$ gives $4 + 1 = 5$ (scores $0,2,4,6,8$), and $P = 746$ gives $373 + 1 = 374$. The case $P = 0$ is valid too — Chef serves once, from the right, giving $1$.

With $P$ up to $10^9$ a loop is out of the question, but the closed form is immediate.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        p = int(data[1 + i])
        # Chef serves once at each of his scores 0..p; even scores are right.
        out.append(str(p // 2 + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$P = 0$**: the answer is $1$, the serve made at a score of zero. The constraints allow $P = 0$, and the $+1$ is exactly what covers it — dropping it returns $0$.
- **$P$ even** ($P = 2$: scores $0$ and $2$): two serves.
- **$P$ odd** ($P = 9$: scores $0, 2, 4, 6, 8$): five serves, since $9$ itself is not even.
- **Largest input** ($P = 10^9$): $5 \times 10^8 + 1$.
- The count is of *even values in $[0, P]$ inclusive*, which is $\lfloor P/2 \rfloor + 1$ — the inclusive zero is what makes it a $+1$ rather than a plain halving.

## Dry run

| $P$ | even scores $0, 2, \ldots$ | count $P//2 + 1$ | output |
|---:|---|---:|---|
| 2 | $0, 2$ | 2 | `2` |
| 9 | $0, 2, 4, 6, 8$ | 5 | `5` |
| 53 | $0, 2, \ldots, 52$ | 27 | `27` |
| 746 | $0, 2, \ldots, 746$ | 374 | `374` |

> CodeChef tags: `Algorithms`, `Constructive`

---

Same problem in rating order (#114 of 486): [../../by-rating/114-BADMINTON.md](../../by-rating/114-BADMINTON.md)
