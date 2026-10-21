# 932 &middot; No Time to Wait

> CodeChef problem code [`NOTIME`](https://www.codechef.com/problems/NOTIME) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Existence check over a list |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Basic Math`, `Brute Force`, `Implementation` |
| **CodeChef category** | school |
| **Time** | $O(N)$ |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/arrays/NOTIME.md](../docs/arrays/NOTIME.md)

## Question

Only $x$ hours are left for the March Long Challenge and Chef is only left with the last problem unsolved. However, he is sure that he cannot solve the problem in the remaining time. From experience, he figures out that he needs exactly $H$ hours to solve the problem.

Now Chef finally decides to use his special power which he has gained through years of intense yoga. He can travel back in time when he concentrates. Specifically, his power allows him to travel to $N$ different time zones, which are $T_1, T_2, \ldots, T_N$ hours respectively behind his current time.

Find out whether Chef can use one of the available time zones to solve the problem and submit it before the contest ends.

### Input
- The first line of the input contains three space-separated integers $N$, $H$ and $x$.
- The second line contains $N$ space-separated integers $T_1, T_2, \ldots, T_N$.

### Output
Print a single line containing the string `"YES"` if Chef can solve the problem on time or `"NO"` if he cannot.

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq N \leq 100$
- $1 \leq x \lt H \leq 100$
- $1 \leq T_i \leq 100$ for each valid $i$

### Subtasks
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \leq N \leq 100$
- $1 \leq x \lt H \leq 100$
- $1 \leq T_i \leq 100$ for each valid $i$

## Sample

**Sample 1 input**

```
2 5 3
1 2
```

**Sample 1 output**

```
YES
```

<details><summary>Explanation</summary>

Chef already has $3$ hours left. He can go to the $2$-nd time zone, which is $2$ hours back in time. Then he has a total of $3 + 2 = 5$ hours, which is sufficient to solve the problem.

</details>

**Sample 2 input**

```
2 6 3
1 2
```

**Sample 2 output**

```
NO
```

<details><summary>Explanation</summary>

If Chef goes to the $1$-st time zone, he will have $3 + 1 = 4$ hours, which is insufficient to solve the problem.

If he goes to the $2$-nd time zone, he will have $3 + 2 = 5$ hours, which is also insufficient to solve the problem.

Since none of the time travel options can be used to gain sufficient time to solve the problem, Chef is incapable of solving it.

</details>

## Approach

Chef has $x$ hours left and needs $H$. Travelling back $T_i$ hours buys him $T_i$ extra hours, so in time zone $i$ he effectively has $x + T_i$. He succeeds if **some** zone gives him enough:

$$\exists i : \; x + T_i \geq H$$

In Python that is `any(x + t >= h for t in zones)`, which short-circuits on the first success and needs no extra storage.

Since only existence matters, there is nothing to optimise — no need to find the largest $T_i$ or to sort. Comparing against $\max(T)$ would also be correct and is equivalent, but `any` states the question directly.

The comparison is inclusive: arriving with exactly enough time counts. The sample is built on that boundary — $x = 3$, $H = 5$, and the best zone offers $T = 2$, giving precisely $5$ hours, so the answer is `YES`. A strict `>` would fail it.

The constraint $x < H$ guarantees Chef genuinely cannot finish without travelling, so the answer is never trivially yes.

Note the input shape: there is **no $T$ test-case count**. The first line holds three values $N, H, x$ — in that order, with the hours needed before the hours remaining — and the second line holds the $N$ time zones. Reading the first number as a test-case count is the likely misstep here.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    # Single test case: first line is N, H, x (not a test-case count).
    n, h, x = int(data[0]), int(data[1]), int(data[2])
    zones = data[3:3 + n]
    # Travelling back t hours leaves Chef with x + t; exactly enough counts.
    print("YES" if any(x + int(t) >= h for t in zones) else "NO")


main()
```

## Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$
