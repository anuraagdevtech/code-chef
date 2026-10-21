# 040. Discus Throw

> [`DISCUS`](https://www.codechef.com/problems/DISCUS) &middot; difficulty **622** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Maximum of a fixed set |
| **CodeChef tags** | `Basic Programming Concepts`, `Conditional Statements`, `Inbuilt functions` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

In discus throw, a player is given $3$ throws and the throw with the **longest distance** is regarded as their final score.

You are given the distances for all $3$ throws of a player. Determine the final score of the player.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, three integers $A, B,$ and $C$ denoting the distances in each throw.

**Output**

For each test case, output the final score of the player.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq A,B,C \leq 100$

## Sample

**Sample input**

```
3
10 15 8
32 32 32
82 45 54
```

**Sample output**

```
15
32
82
```

<details><summary>Explanation</summary>

**Test Case $1$:** The longest distance is achieved in the second throw, which is equal to $15$ units. Thus, the answer is $15$.

**Test Case $2$:** In all throws, the distance is $32$ units. Thus, the final score is $32$.

**Test Case $3$:** The longest distance is achieved in the first throw which is equal to $82$ units. Thus, the answer is $82$.

</details>

## Approach

The final score is the longest of the three throws, so the answer is $\max(A, B, C)$ — a single built-in call.

Python's `max` takes any number of positional arguments, so `max(a, b, c)` works directly without building a list. Writing a manual chain of comparisons would also work but invites the usual mistakes: forgetting to seed the running maximum with the first value, or initialising it to $0$, which is safe here only because all distances are at least $1$. Seeding from the data rather than from a magic constant is the habit that survives into problems where negatives are allowed.

Ties need no special handling. The maximum of equal values is that value, so sample case 2 with three throws of $32$ simply returns $32$. Nothing in the problem distinguishes *which* throw produced the best distance, only its length.

The $O(1)$ bound is because the count of throws is fixed at three; for $n$ throws this would be the usual $O(n)$ single-pass scan.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = map(int, data[1 + 3 * i:4 + 3 * i])
        # The best of three throws is the score.
        out.append(str(max(a, b, c)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **All three throws equal** ($32, 32, 32$): the maximum is that value; ties need no special handling.
- **The best throw in each position** — the sample has it in the middle ($10, 15, 8$) and the first ($82, 45, 54$), so a solution that only compares two of the three fails somewhere.
- **All at the minimum** ($1, 1, 1$): answer $1$; there is no "no valid throw" case, since every throw counts.
- Only the single best attempt scores, so the other two are discarded rather than summed or averaged.

## Dry run

| $A$ | $B$ | $C$ | best | output |
|---:|---:|---:|---:|---|
| 10 | 15 | 8 | 15 | `15` |
| 32 | 32 | 32 | 32 | `32` |
| 82 | 45 | 54 | 82 | `82` |

---

Same problem grouped by topic: [../docs/basic-math/DISCUS.md](../docs/basic-math/DISCUS.md)
