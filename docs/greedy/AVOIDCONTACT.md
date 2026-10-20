# 131. Avoid Contact

> CodeChef problem code [`AVOIDCONTACT`](https://www.codechef.com/problems/AVOIDCONTACT) &middot; difficulty **907** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Packing with separation constraints |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

A hostel has $N$ rooms in a straight line. It has to accommodate $X$ people. Unfortunately, out of these $X$ people, $Y$ of them are infected with chickenpox. Due to safety norms, the following precaution must be taken:

- No person should occupy a room directly adjacent to a room occupied by a chickenpox-infected person. In particular, two chickenpox-infected people **cannot** occupy adjacent rooms.

For example, if room $4$ has a chickenpox-infected person, then nobody should occupy rooms $3$ and $5$. Similarly, if room $1$ has a chickenpox-infected person then nobody should occupy room $2$.

What's the **minimum** value of $N$ for which all the people can be accommodated in the hostel, following the above condition?

**Input**

- The first line of input contains a single integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $X$ and $Y$ — the total number of people and the number of chickenpox-infected people.

**Output**

For each test case, output on a new line a single integer — the **minimum** value of $N$ for which all the people can be accommodated in the hostel.

## Constraints

- $1 \leq T \leq 200$
- $1 \leq X \leq 1000$
- $0 \leq Y \leq X$

## Sample

**Sample input**

```
3
4 0
5 3
3 3
```

**Sample output**

```
4
8
5
```

<details><summary>Explanation</summary>

Note: Below, $C$ represents a room occupied by a chickenpox-infected person, $N$ represents a room occupied by an uninfected person, and $\_$ represents an empty room.

**Test case $1$**: One of the possible ways to accommodate the people in $4$ rooms is:

$N$ $N$ $N$ $N$

**Test case $2$**: One of the possible ways to accommodate the people in $8$ rooms is:

$C$ $\_$ $C$ $\_$ $N$ $N$ $\_$ $C$

**Test case $3$**: One of the possible ways to accommodate the people in $5$ rooms is:

$C$ $\_$ $C$ $\_$ $C$

</details>

## Approach

Healthy people may sit next to each other, so the $X - Y$ healthy residents pack into one contiguous block of $X - Y$ rooms. Infected people are the constraint: each needs an empty room on every side that touches anyone.

The tightest arrangement puts the healthy block at one end and then alternates:

$$\underbrace{\text{H H} \cdots \text{H}}_{X-Y}\ \_\ \text{I}\ \_\ \text{I}\ \_\ \cdots\ \text{I}$$

Each infected person costs two rooms — one empty separator plus their own — except that the very last one needs no separator after it, and the first needs none before it if nothing precedes.

**With healthy people present** ($X > Y$): the block occupies $X - Y$ rooms, then each of the $Y$ infected adds a gap and a room, for $X - Y + 2Y = X + Y$ rooms total.

**With no healthy people** ($X = Y$): the pattern is `I _ I _ ... I`, which is $2Y - 1$ rooms — one fewer, because the leading gap is unnecessary.

Both collapse into

$$N = X + Y - [X = Y]$$

Sample case 2 ($X=5, Y=3$) gives $8$: two healthy rooms plus three gap-and-room pairs. Sample case 3 ($X=Y=3$) gives $5$, and is exactly the case the $-1$ exists for. Sample case 1 has $Y = 0$ and reduces to $X$.

The greedy is optimal because every infected person forces at least one empty room between them and the next occupant, and the construction achieves that bound with no slack.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Healthy pack together; each infected costs a gap plus a room, except
        # that with nobody healthy the leading gap is not needed.
        out.append(str(x + y - (1 if x == y else 0)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Algorithms`, `Constructive`, `Observation`
