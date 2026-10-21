# 641 &middot; Flip the cards

> CodeChef problem code [`FLIPCARDS`](https://www.codechef.com/problems/FLIPCARDS) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Choosing the cheaper of two targets |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/FLIPCARDS.md](../docs/basic-math/FLIPCARDS.md)

## Question

There are $N$ cards on a table, out of which $X$ cards are face-up and the remaining are face-down.

In one operation, we can do the following:
- Select any one card and flip it (i.e. if it was initially face-up, after the operation, it will be face-down and vice versa)

What is the minimum number of operations we must perform so that all the cards face in the same direction (i.e. either all are face-up or all are face-down)?

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $N$ and $X$ — the total number of cards and the number of cards which are initially face-up.

**Output**

For each test case, output the minimum number of cards you must flip so that all the cards face in the same direction.

## Constraints

- $1 \leq T \leq 5000$
- $2 \leq N \leq 100$
- $0 \leq X \leq N$

## Sample

**Sample input**

```
4
5 0
4 2
3 3
10 2
```

**Sample output**

```
0
2
0
2
```

<details><summary>Explanation</summary>

**Test Case 1:** All the cards are already facing down. Therefore we do not need to perform any operations.

**Test Case 2:** $2$ cards are facing up and $2$ cards are facing down. Therefore we can flip the $2$ cards which are initially facing down.

**Test Case 3:** All the cards are already facing up. Therefore we do not need to perform any operations.

**Test Case 4:** $2$ cards are facing up and $8$ cards are facing down. Therefore we can flip the $2$ cards which are initially facing up.

</details>

## Approach

There are $X$ face-up cards and $N - X$ face-down ones, and only two possible end states.

- To make everything **face-up**, flip the $N - X$ cards that are currently down.
- To make everything **face-down**, flip the $X$ cards that are currently up.

Each flip changes exactly one card, so each target costs precisely the number of cards not already in that state. The minimum is therefore

$$\min(X,\; N - X)$$

The insight is that both targets are always reachable and their costs are complements summing to $N$, so no search is needed — just take the cheaper. Note the problem does not insist on a particular final direction, only that all cards agree; if it had demanded "all face-up", the answer would be the single value $N - X$.

The extremes confirm the formula. When every card already points the same way the cost is zero, as in sample cases 1 ($X = 0$) and 3 ($X = N$). When the split is exactly even, as in case 2 with $N = 4, X = 2$, both targets cost the same $2$ and the `min` is indifferent.

The identity $\min(X, N - X)$ also says the answer never exceeds $\lfloor N/2 \rfloor$ — you are never worse off than flipping the smaller half.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Flip the up ones, or the down ones, whichever is cheaper.
        out.append(str(min(x, n - x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
