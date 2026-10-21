# 042. Watching Movies at 2x

> [`MOVIE2X`](https://www.codechef.com/problems/MOVIE2X) &middot; difficulty **628** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Rate and time |
| **CodeChef tags** | `Mathematics`, `Basic Math`, `Arithmetic` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ |
| **Space** | $O(1)$ |

## Question

Chef started watching a movie that runs for a total of $X$ minutes.

Chef has decided to watch the first $Y$ minutes of the movie at **twice** the usual speed as he was warned by his friends that the movie gets interesting only after the first $Y$ minutes.

How long will Chef spend watching the movie in **total**?

**Note:** It is guaranteed that $Y$ is **even**.

**Input**

- The first line contains two space separated integers $X, Y$ - as per the problem statement.

**Output**

- Print in a single line, an integer denoting the total number of minutes that Chef spends in watching the movie.

## Constraints

- $1 \leq X, Y \leq 1000$
- $Y$ is an even integer.

**Subtasks**

**Subtask #1 (100 points):** original constraints

## Sample

**Sample 1 input**

```
100 20
```

**Sample 1 output**

```
90
```

<details><summary>Explanation</summary>

For the first $Y = 20$ minutes, Chef watches at twice the usual speed, so the total amount of time spent to watch this portion of the movie is $\frac{Y}{2} = 10$ minutes.

For the remaining $X - Y = 80$ minutes, Chef watches at the usual speed, so it takes him $80$ minutes to watch the remaining portion of the movie.

In total, Chef spends $10 + 80 = 90$ minutes watching the entire movie.

</details>

**Sample 2 input**

```
50 24
```

**Sample 2 output**

```
38
```

<details><summary>Explanation</summary>

For the first $Y = 24$ minutes, Chef watches at twice the usual speed, so the total amount of time spent to watch this portion of the movie is $\frac{Y}{2} = 12$ minutes.

For the remaining $X - Y = 26$ minutes, Chef watches at the usual speed, so it takes him $26$ minutes to watch the remaining portion of the movie.

In total, Chef spends $12 + 26 = 38$ minutes watching the entire movie.

</details>

## Approach

The movie is $X$ minutes long. Chef watches the first $Y$ minutes of *content* at double speed and the remaining $X - Y$ minutes at normal speed.

Playing $Y$ minutes of footage at twice the speed takes $Y/2$ minutes of real time; the rest takes $X - Y$ minutes unchanged. So the time spent is

$$\frac{Y}{2} + (X - Y) \;=\; X - \frac{Y}{2}$$

The simplified right-hand form says it plainly: double speed saves exactly half of the fast-forwarded stretch.

The guarantee that $Y$ is **even** is what keeps the answer an integer, so `y // 2` is exact and no rounding rule is needed. Without that promise the problem would have to say whether to round up or down.

The distinction between *footage* and *real time* is the thing to keep straight. $Y$ measures content, not viewing time, so the saving is $Y/2$ rather than $Y$. Sample: $X = 100$, $Y = 20$ gives $10 + 80 = 90$.

As with The Three Topics, there is **no $T$ on the first line** — the input is a single line holding $X$ and $Y$, so this is one test case only.

## Solution

```python
import sys


def main() -> None:
    # Single test case: one line with X and Y, no leading T.
    x, y = map(int, sys.stdin.buffer.read().split()[:2])
    # y minutes of footage at 2x costs y // 2 minutes of real time.
    print(y // 2 + (x - y))


main()
```

## Edge cases

- **The whole movie at double speed** ($Y = X$): the answer is $X/2$, e.g. $X = Y = 100$ gives $50$.
- **$Y$ is guaranteed even**, so $Y/2$ is exact and there is no rounding decision. Were $Y$ odd the problem would have to state how a half minute is handled.
- **Smallest $Y$** is $2$, not $0$, so there is always some footage watched at $2\times$.
- The formula assumes $Y \leq X$ — you cannot fast-forward more footage than the film contains — which the problem's setup implies.
- **Input shape**: one line with $X$ and $Y$, no leading test-case count.

## Dry run

Sample 1: $X = 100$, $Y = 20$.

| part | footage | real time |
|---|---:|---:|
| at $2\times$ | $20$ min | $10$ min |
| at normal speed | $80$ min | $80$ min |
| **total** | $100$ min | **$90$ min** |

Output `90`. Sample 2 ($X = 50$, $Y = 24$) gives $12 + 26 = 38$.

---

Same problem grouped by topic: [../docs/basic-math/MOVIE2X.md](../docs/basic-math/MOVIE2X.md)
