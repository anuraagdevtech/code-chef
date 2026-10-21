# 650 &middot; Mario and Bullet

> CodeChef problem code [`BULLET`](https://www.codechef.com/problems/BULLET) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Working backwards from a deadline |
| **CodeChef tags** | `Special`, `Mathematics`, `Physics`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/BULLET.md](../docs/basic-math/BULLET.md)

## Question

Mario's bullet moves at $X$ pixels per frame. He wishes to shoot a goomba standing $Y$ pixels away from him. The goomba does not move.

Find the **minimum** time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after **at least** $Z$ seconds from now.

**Input**

- The first line of input will contain an integer $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing three space-separated integers $X, Y,$ and $Z$.

**Output**

For each test case, output in a single line the **minimum** time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after **at least** $Z$ seconds from now.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y, Z \leq 100$
- $X$ divides $Y$

## Sample

**Sample input**

```
3
3 3 5
2 4 1
3 12 8
```

**Sample output**

```
4
0
4
```

<details><summary>Explanation</summary>

**Test case $1$:** The speed of the bullet is $3$ pixels per frame and the goomba is $3$ pixels away from Mario. Thus, it would take $1$ second for the bullet to reach the goomba. Mario wants the bullet to reach goomba after at least $5$ seconds. So, he should fire the bullet after $4$ seconds.

**Test case $2$:** The speed of the bullet is $2$ pixels per frame and the goomba is $4$ pixels away from Mario. Thus, it would take $2$ seconds for the bullet to reach the goomba. Mario wants the bullet to reach the goomba after at least $1$ second. So, he should fire the bullet after $0$ seconds. Note that, this is the minimum time after which he can shoot a bullet.

**Test case $3$:** The speed of the bullet is $3$ pixels per frame and the goomba is $12$ pixels away from Mario. Thus, it would take $4$ seconds for the bullet to reach the goomba. Mario wants the bullet to reach goomba after at least $8$ seconds. So, he should fire the bullet after $4$ seconds.

</details>

## Approach

The bullet covers $X$ pixels per unit time and the goomba is $Y$ pixels away, so the bullet is in flight for

$$\text{flight} = \frac{Y}{X}$$

The guarantee that **$X$ divides $Y$** is what makes this an exact integer, so `y // x` is safe and no rounding rule is needed.

If Mario fires at time $t$, the hit lands at $t + \text{flight}$. The requirement is that the hit happen at least $Z$ from now, so

$$t + \frac{Y}{X} \geq Z \quad\Longleftrightarrow\quad t \geq Z - \frac{Y}{X}$$

and the smallest such $t$ is that bound — except that Mario cannot fire in the past. Clamping gives

$$t = \max\left(0,\; Z - \frac{Y}{X}\right)$$

The clamp is the case worth noticing, and sample 2 is built on it: with flight time $4/2 = 2$ and a deadline of only $Z = 1$, the bullet already arrives later than required if fired immediately, so the answer is $0$ rather than $-1$.

Reading "at least $Z$" as a *lower* bound on the arrival time is what makes this a delay rather than a hurry; Mario waits so the bullet does not arrive too early.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        # x divides y, so the flight time is exact. Mario cannot fire early.
        out.append(str(max(0, z - y // x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
