[&larr; 118. Counting Pretty Numbers](NUM239.md) &middot; [Index](../../README.md) &middot; [132. Problem &rarr;](PR0BLEM.md)

# 121. Find the Direction

> CodeChef problem code [`FACEDIR`](https://www.codechef.com/problems/FACEDIR) &middot; difficulty **880** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Cyclic state via modulo |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef is currently facing the north direction. Each second he rotates exactly $90$ degrees in clockwise direction. Find the direction in which Chef is facing after exactly $X$ seconds.

$\textbf{Note}:$ There are only 4 directions: North, East, South, West (in clockwise order).

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single integer $X$.

**Output**

For each testcase, output the direction in which Chef is facing after exactly $X$ seconds.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 1000$

## Sample

**Sample input**

```
3
1
3
6
```

**Sample output**

```
East
West
South
```

<details><summary>Explanation</summary>

Chef is facing North in the starting.

**Test Case $1$:** After $1$ second he turns $90$ degrees clockwise and now faces the east direction.

**Test Case $2$:**
Direction after $1$ second- east

Direction after $2$ seconds- south

Direction after $3$ seconds- west

</details>

## Approach

Turning $90°$ clockwise four times returns Chef to where he started, so the heading depends only on $X \bmod 4$. Listing the directions in clockwise order from the starting point:

$$[\text{North},\ \text{East},\ \text{South},\ \text{West}]$$

the answer is the entry at index `x % 4`.

Two things make the table correct. It must be written in **clockwise** order, matching the direction of rotation — anticlockwise would reverse the middle two entries. And it must **start at the initial heading**, North, so that index $0$ (no rotation) is right; starting the list elsewhere would rotate every answer.

This is the same cycle-collapsing idea as the Mario transformation problem, with period $4$ instead of $3$. Simulating $X$ steps would pass at $X \leq 1000$, but the modulo is $O(1)$ and would still work if $X$ reached $10^{18}$.

Checking the samples: $X = 1$ gives East, $X = 3$ gives West, and $X = 6$ reduces to $6 \bmod 4 = 2$, giving South — a full rotation plus two quarter turns.

## Solution (Python)

```python
import sys

# Clockwise from the starting heading, so index 0 is the initial direction.
DIRS = ("North", "East", "South", "West")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = [DIRS[int(data[1 + i]) % 4] for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$X$ a multiple of $4$** ($X = 4$, $X = 8$): back to the starting heading, `North`.
- **The first three turns** ($X = 1, 2, 3$): `East`, `South`, `West` in order.
- **Largest input** ($X = 1000$): $1000 \bmod 4 = 0$, so `North` — no need to step through a thousand turns.
- The period is exactly $4$, so only $X \bmod 4$ matters; the table's index $0$ must be the *initial* direction for that to line up.

## Dry run

Table, clockwise from the start: $0$ `North`, $1$ `East`, $2$ `South`, $3$ `West`.

| $X$ | $X \bmod 4$ | output |
|---:|---:|---|
| 1 | 1 | `East` |
| 3 | 3 | `West` |
| 6 | 2 | `South` |

> CodeChef tags: `Basic Programming Concepts`, `Mathematics`, `Algorithms`

---

Same problem in rating order (#122 of 486): [../../by-rating/122-FACEDIR.md](../../by-rating/122-FACEDIR.md)
