# 043. Police and Thief

> [`POLTHIEF`](https://www.codechef.com/problems/POLTHIEF) &middot; difficulty **639** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Relative speed |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef discovered that his secret recipe has been stolen. He immediately informs the police of the theft.

It is known that the policeman and thief move on the number line. You are given that:
- The initial location of the policeman on the number line is $X$ and his speed is $2$ units per second.
- The initial location of the thief on the number line is $Y$ and his speed is $1$ unit per second.

Find the **minimum** time (in seconds) in which the policeman can catch the thief. Note that, the policeman catches the thief as soon as their locations become equal and the thief will try to evade the policeman for as long as possible.

**Input**

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $X$ and $Y$, as described in the problem statement.

**Output**

For each test case, output in a single line the minimum time taken by the policeman to catch the thief.

## Constraints

- $1 \leq T \leq 1000$
- $-10^5 \leq X, Y \leq 10^5$

## Sample

**Sample input**

```
3
1 3
2 1
1 1
```

**Sample output**

```
2
1
0
```

<details><summary>Explanation</summary>

**Test case $1$**: The initial locations of the policeman and thief are $1$ and $3$ respectively. The minimum time taken by the policeman to catch the thief is $2$ seconds, and this happens when both the policeman and the thief move towards the right.

**Test case $2$**: The initial location of the policeman and thief are $2$ and $1$ respectively. The minimum time taken by the policeman to catch the thief is $1$ second, and this happens when both the policeman and the thief move towards the left.

**Test case $3$**: The initial locations of the policeman and thief are $1$ and $1$ respectively. Because the police is already present at the location of thief, the time taken by police to catch the thief is $0$ seconds.

</details>

## Approach

The policeman starts at $X$ moving at $2$ units per second; the thief starts at $Y$ moving at $1$. The thief runs directly away, so the gap between them shrinks at the **relative speed**

$$2 - 1 = 1 \text{ unit per second}$$

The initial gap is $|X - Y|$, so the capture time is

$$\frac{|X - Y|}{1} = |X - Y|$$

The answer is simply the absolute difference.

Two things make this cleaner than it first looks. The absolute value handles both directions at once — the thief may start to the left or the right, and the coordinates may be negative, since $X, Y \in [-10^5, 10^5]$. Writing `x - y` without `abs` would return a negative time for half the inputs.

And the phrase "the thief will try to evade for as long as possible" is what fixes the relative speed at $1$ rather than $3$. If the thief ran *toward* the policeman the gap would close at $2 + 1 = 3$ and the time would be a third as long; fleeing is the thief's best play, so the worst case for the policeman is the answer. Reading the adversarial clause as a maximisation is the real content here.

The case $X = Y$ needs no special handling: the gap is zero and the answer is $0$, as sample case 3 shows.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Fleeing thief closes the gap at 2 - 1 = 1 unit per second.
        out.append(str(abs(x - y)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Already in the same place** ($X = Y$): zero seconds, so the answer can legitimately be $0$. The sample's third row covers it.
- **Negative coordinates** are allowed ($-10^5 \leq X, Y$), so the gap must be taken as an absolute value; subtracting in a fixed order gives a negative time for half the inputs.
- **Widest separation** ($X = -10^5$, $Y = 10^5$): $2 \times 10^5$ seconds.
- **The closing speed is $1$**, not $2$: the thief flees at $1$ while the policeman runs at $2$, so the gap shrinks by $2 - 1 = 1$ per second and the answer is the raw distance, not half of it.

## Dry run

| $X$ | $Y$ | gap $|X - Y|$ | closing speed | output |
|---:|---:|---:|---:|---|
| 1 | 3 | 2 | 1 per second | `2` |
| 2 | 1 | 1 | 1 per second | `1` |
| 1 | 1 | 0 | — | `0` |

Row 2 has the gap the other way round, which the absolute value absorbs.

---

Same problem grouped by topic: [../docs/basic-math/POLTHIEF.md](../docs/basic-math/POLTHIEF.md)
