# 23. Nearest Exit

> CodeChef problem code [`NEARESTEXIT`](https://www.codechef.com/problems/NEARESTEXIT) &middot; difficulty **585** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Comparing distances to two endpoints |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

There are two exits in a bus with $100$ seats:
- First exit is located beside seat number $1$.
- Second exit is located beside seat number $100$.

Seats are arranged in a straight line from $1$ to $100$ with equal spacing between any $2$ adjacent seats.

A passenger prefers to choose the nearest exit while leaving the bus.

Determine the exit taken by passenger sitting on seat $X$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists a single integer $X$, denoting the seat number.

**Output**

For each test case, output `LEFT` if the passenger chooses the exit beside seat $1$, `RIGHT` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `LEFT`, `lEft`, `left`, and `lEFT` will all be treated as identical).

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$

## Sample

**Sample input**

```
6
1
50
100
30
51
73
```

**Sample output**

```
LEFT
LEFT
RIGHT
LEFT
RIGHT
RIGHT
```

<details><summary>Explanation</summary>

**Test case $1$:** The exit is located beside seat $1$. Hence, the passenger can take this exit without moving to any other seat.

**Test case $2$:** To take exit at seat $1$, the passenger needs to move $49$ seats. However, to take the exit at seat $100$, the passenger needs to move $50$ seats. Thus, exit at seat $1$ is closer.

**Test case $3$:** The exit is located beside seat $100$. Hence, the passenger can take this exit without moving to any other seat.

**Test case $4$:** To take exit at seat $1$, the passenger needs to move $29$ seats. However, to take the exit at seat $100$, the passenger needs to move $70$ seats. Thus, exit at seat $1$ is closer.

</details>

## Approach

Seats run $1$ to $100$ with equal spacing, so from seat $X$ the distance to the left exit (beside seat $1$) is $X - 1$ and the distance to the right exit (beside seat $100$) is $100 - X$.

The passenger takes the left exit when it is no further away:

$$X - 1 \leq 100 - X \quad\Longleftrightarrow\quad 2X \leq 101 \quad\Longleftrightarrow\quad X \leq 50.5$$

Since $X$ is an integer this is simply $X \leq 50$. The midpoint falls *between* seats $50$ and $51$, so there is no genuine tie to resolve — every seat is strictly closer to one exit than the other, and the problem's silence about ties is therefore harmless.

Two details are easy to get wrong. The distances are $X - 1$ and $100 - X$, not $X$ and $100 - X$; the exits sit *beside* the end seats, so the passenger in seat $1$ has distance zero. And the cutoff is $50$, not $49$ or $51$ — the samples pin both sides down, with $X = 50$ answering `LEFT` and $X = 51$ answering `RIGHT`.

Writing the test as `x <= 50` is clearest, though `2 * x <= 101` is equivalent and shows the derivation.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # dist left = x - 1, dist right = 100 - x; left wins iff x <= 50.
        out.append("LEFT" if x <= 50 else "RIGHT")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$X = 50$ and $X = 51$** straddle the midpoint and both appear in the sample: at $50$ the distances are $49$ left and $50$ right, so `LEFT`; at $51$ they are $50$ and $49$, so `RIGHT`.
- **$X = 1$**: already at the left exit, distance $0$, so `LEFT`.
- **$X = 100$**: already at the right exit, so `RIGHT`.
- **No tie is possible.** The two distances are $X - 1$ and $100 - X$, which always sum to $99$ — an odd number, so they can never be equal. That is why the problem needs no third answer, and why the test collapses to the single comparison $X \leq 50$.

## Dry run

| $X$ | left $X-1$ | right $100-X$ | nearer | output |
|---:|---:|---:|---|---|
| 1 | 0 | 99 | left | `LEFT` |
| 50 | 49 | 50 | left | `LEFT` |
| 100 | 99 | 0 | right | `RIGHT` |
| 30 | 29 | 70 | left | `LEFT` |
| 51 | 50 | 49 | right | `RIGHT` |
| 73 | 72 | 27 | right | `RIGHT` |

Rows 2 and 5 are the two sides of the midpoint, one unit apart.

---

Same problem in rating order (#30 of 486): [../../by-rating/030-NEARESTEXIT.md](../../by-rating/030-NEARESTEXIT.md)
