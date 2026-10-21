# 049. Chess Ratings

> [`C_RATING`](https://www.codechef.com/problems/C_RATING) &middot; difficulty **651** &middot; time limit **1.5s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ceiling division with a clamp |
| **CodeChef tags** | `Mathematics` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Alice has recently started playing Chess. Her current rating is $X$. She noticed that when she wins a game, her rating increases by $8$ points.

Can you help Alice in finding out the **minimum** number of games she needs to win in order to make her rating greater than or equal to $Y$?

**Input**

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two integers $X$ and $Y$, as described in the problem statement.

**Output**

For each test case, output the **minimum** number of games that Alice needs to win in order to make her rating greater than or equal to $Y$.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq X \leq Y \leq 10^4$

## Sample

**Sample input**

```
4
10 10
10 17
10 18
10 19
```

**Sample output**

```
0
1
1
2
```

<details><summary>Explanation</summary>

**Test case $1$:** Since Alice's current rating $X$ is already equal to her desired rating $Y$, she doesn't need to win any game.

**Test case $2$:** Alice's current rating is $10$. After winning $1$ game, her rating will become $10+8=18$, which is greater than her desired rating of $17$. Thus, she has to win at least $1$ game.

**Test case $3$:** Alice's current rating is $10$. After winning $1$ game, her rating will become $10+8=18$, which is equal to her desired rating of $18$. Thus, she has to win at least $1$ game.

**Test case $4$:** Alice's current rating is $10$. After winning $1$ game, her rating will become $18$, which is less than her desired rating of $19$. She will need to win one more game in order to make her rating $26$, which is greater than $19$. Thus, she has to win at least $2$ games.

</details>

## Approach

Each win adds $8$ rating, so after $w$ wins Alice sits at $X + 8w$. She needs this to reach $Y$:

$$X + 8w \geq Y \quad\Longleftrightarrow\quad w \geq \frac{Y - X}{8}$$

Since $w$ must be a whole number of games, the answer is the ceiling of that bound:

$$w = \left\lceil \frac{Y - X}{8} \right\rceil$$

computed in integers as `(gap + 7) // 8`.

The constraints promise $X \leq Y$, so the gap is never negative — but writing `max(0, y - x)` costs nothing and makes the intent explicit. Sample case 1 is the zero-gap case: Alice is already at the target, so no wins are needed.

The three cases $Y = 17, 18, 19$ against $X = 10$ are a precise test of the ceiling. A gap of $7$ needs $1$ game (overshooting to $18$), a gap of exactly $8$ also needs $1$ (landing precisely on $18$), and a gap of $9$ tips over into $2$. A floor division would answer $0, 1, 1$ and fail the first and third.

Note that "greater than or **equal** to $Y$" is what lets the exact-multiple case stay at one game rather than two.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        gap = max(0, y - x)
        # Each win is worth 8 rating, and a partial win is not a thing.
        out.append(str((gap + 7) // 8))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/basic-math/C_RATING.md](../docs/basic-math/C_RATING.md)
