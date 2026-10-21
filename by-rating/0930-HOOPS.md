# 930 &middot; Hoop Jump

> CodeChef problem code [`HOOPS`](https://www.codechef.com/problems/HOOPS) &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Where two converging sequences meet |
| **CodeChef category** | main |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/HOOPS.md](../docs/basic-math/HOOPS.md)

## Question

You and your friend are playing a game with hoops. There are $N$ hoops (where $N$ is odd) in a row. You jump into hoop $1$, and your friend jumps into hoop $N$. Then you jump into hoop $2$, and after that, your friend jumps into hoop $N-1$, and so on.

The process ends when someone cannot make the next jump because the hoop is occupied by the other person. Find the last hoop that will be jumped into.

### Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, a single integer $N$.

### Output
For each testcase, output in a single line the answer to the problem.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq N \lt 2\cdot 10^5$
- $N$ is odd

### Subtasks
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \lt 2\cdot 10^5$
- $N$ is odd

## Sample

**Sample input**

```
2
1
3
```

**Sample output**

```
1
2
```

<details><summary>Explanation</summary>

**Test Case $1$:** Since there is only $1$ hoop, that's the only one to be jumped into.

**Test Case $2$:** The first player jumps into hoop $1$. The second player jumps into hoop $3$ and finally the first player jumps into hoop $2$. Then the second player cannot make another jump, so the process stops.

</details>

## Approach

You occupy hoops $1, 2, 3, \ldots$ from the left while your friend takes $N, N-1, N-2, \ldots$ from the right. The two sequences march toward each other and the game stops the moment one of you finds the next hoop already taken.

Since $N$ is odd, the two sequences meet exactly at the middle hoop

$$\frac{N+1}{2}$$

and because **you** jump first, you are the one who claims it. Your friend then has nowhere to go, so that middle hoop is the last one jumped into.

Tracing $N = 5$: you take $1$, friend takes $5$, you take $2$, friend takes $4$, you take $3$ — and now the friend's next target would be $3$, already yours. The answer is $3 = (5+1)/2$.

The oddness of $N$ is what makes this clean. With an even $N$ the two sequences would pass each other without landing on a shared hoop, and the stopping condition would need more care — so the constraint is load-bearing, not decoration.

Sample case 1 is the degenerate $N = 1$: you jump into the only hoop and your friend is immediately stuck, giving $1$. The formula handles it without a special case.

In integers this is `(n + 1) // 2`, and with $T$ up to $10^5$ the bulk read matters more than the arithmetic.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # n is odd, so the two sequences meet at the middle hoop, which the
        # first player reaches first.
        out.append(str((n + 1) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
