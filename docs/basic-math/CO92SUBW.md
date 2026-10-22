# 265. Chef Goes to the Cinema

> CodeChef problem code [`CO92SUBW`](https://www.codechef.com/problems/CO92SUBW) &middot; difficulty **1493** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Triangular numbers and a local search |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Chef lives in Chefcity. Chefcity can be represented as a straight line with Chef's house at point 0 on this line. There is an infinite number of subway stations in Chefcity, numbered by positive integers. The first station is located at point 1 and for each **i** ≥ 1, the distance between stations **i** and **i+1** is equal to **i+1**. (Station **i+1** is always located at a higher coordinate than station **i**, i.e., the subway stations are located at points 1, 3, 6, 10, 15 etc.)

Subway trains in Chefcity allow Chef to move between any pair of adjacent stations in one minute, regardless of the distance between them. Chef can also move by walking; his walking speed is one unit of distance in one minute. Chef can enter or exit the subway at any station.

Chef has decided to go to the cinema. The only cinema in Chefcity is located at point **X**. (Note that the cinema can be placed at the same point as a subway station.) Help Chef determine the minimum possible time required to get to the cinema from his house.

**Input**

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first and only line of each test case contains a single integer **X**.

**Output**

For each test case, print a single line containing one integer - the minimum possible travel time.

**Constraints**

- 1 ≤ **T** ≤ 200

- 1 ≤ **X** ≤ 10^9

## Constraints

- 1 ≤ T ≤ 200
- 1 ≤ X ≤ 10^9

## Sample

**Sample input**

```
4
1
2
3
9
```

**Sample output**

```
1
2
2
5
```

<details><summary>Explanation</summary>

**Example case 4:** Chef will walk from **x** = 0 to **x** = 1 in one minute, then he will enter the subway and move from station 1 (at **x** = 1) to station 2 (at **x** = 3) in one minute, then from station 2 to station 3 (at **x** = 6) in one minute, from station 3 to station 4 (at **x** = 10) in one minute, and finally, he will walk from **x** = 10 to **x** = 9 in one minute, which makes the total travel time 5 minutes.

</details>

## Approach

Station $k$ sits at the triangular number $T_k = \frac{k(k+1)}{2}$, since the gaps are $1, 2, 3, \ldots$

Reaching station $k$ is cheap: walk one unit to station $1$ (one minute), then ride $k-1$ hops (one minute each), for **$k$ minutes total** regardless of how far away it is. From there, walk the remaining $|X - T_k|$ units. So the cost of using station $k$ is

$$k + |X - T_k|$$

and pure walking costs $X$. The answer is the minimum.

Scanning every $k$ would cost about $\sqrt{2X} \approx 45{,}000$ steps, which is affordable but unnecessary. The function is **unimodal**: while $T_k < X$ the cost is $k + X - T_k$, and each step adds $1$ to $k$ while subtracting $k+1 \geq 2$ from the walk, so it strictly decreases; once $T_k > X$ it strictly increases. So only the two stations bracketing $X$ matter, found by inverting the triangular formula with $\texttt{isqrt}$.

Sample $X = 9$ shows the key behaviour: station $4$ sits at $10$, **past** the cinema, yet riding there (4 minutes) and walking back one unit beats stopping at station $3$ at point $6$ and walking three units. Overshooting is often optimal, because riding is flat-rate while walking is not.

Sample $X = 2$ ties at $2$ — walk the whole way, or ride to station $1$ and walk one more.

Using `math.isqrt` rather than a float square root keeps the station index exact at $X = 10^9$.

## Solution (Python)

```python
import math
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        best = x                               # walk the whole way
        # Largest k with k(k+1)/2 <= x, from inverting the triangular formula.
        k0 = (math.isqrt(8 * x + 1) - 1) // 2
        # Cost is unimodal in k, so only the stations bracketing x matter.
        for k in range(max(1, k0 - 1), k0 + 3):
            best = min(best, k + abs(x - k * (k + 1) // 2))
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Walking the whole way is a candidate**, which is what `best = x` represents — it is the $k = 0$ case, and for $X = 1$ and $X = 2$ it ties or wins.
- **The cost is unimodal in $k$**, since riding further adds one minute per station while the walk shrinks by an ever-growing amount and then grows again — so only the stations bracketing $X$ matter, not a full scan.
- **Overshooting can beat undershooting.** At $X = 9$ the nearest station below is $6$ (cost $3 + 3 = 6$) but station $4$ at $10$ costs $4 + 1 = 5$ — so the window must include stations past $X$, which is why the loop runs to $k_0 + 2$.
- **`isqrt` must be exact.** Inverting $k(k+1)/2 \leq X$ gives $k_0 = \lfloor (\sqrt{8X+1} - 1)/2 \rfloor$, and a float `sqrt` at $X = 10^9$ can land one off and shift the window.
- **The window is widened by one on each side** rather than trusted exactly, which costs nothing and absorbs any off-by-one in the inversion.
- **$X$ up to $10^9$** puts $k_0$ near $44{,}720$, so the closed-form inversion is essential — scanning stations would be $10^4$ per case but computing them all would not scale.

## Dry run

$X = 9$. Stations sit at $1, 3, 6, 10, 15, \dots$

| $k$ | station at $k(k+1)/2$ | ride cost | walk $|9 - T_k|$ | total |
|---:|---:|---:|---:|---:|
| 0 | 0 (home) | 0 | 9 | 9 |
| 2 | 3 | 2 | 6 | 8 |
| 3 | 6 | 3 | 3 | 6 |
| 4 | 10 | 4 | 1 | **5** |
| 5 | 15 | 5 | 6 | 11 |

Output `5`: ride four stations past the target, then walk back one unit.

> CodeChef tags: `Mathematics`, `Algorithms`, `Constructive`

---

Same problem in rating order (#290 of 486): [../../by-rating/290-CO92SUBW.md](../../by-rating/290-CO92SUBW.md)
