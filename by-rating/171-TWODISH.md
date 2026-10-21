# 171. Two Dishes

> [`TWODISH`](https://www.codechef.com/problems/TWODISH) &middot; difficulty **1140** &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Bottleneck across shared and exclusive resources |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef will have $N$ guests in his house today. He wants to serve at least one dish to each of the $N$ guests. Chef can make two types of dishes. He needs one fruit and one vegetable to make the first type of dish and one vegetable and one fish to make the second type of dish. Now Chef has $A$ fruits, $B$ vegetables, and $C$ fishes in his house. Can he prepare at least $N$ dishes in total?

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, four integers $N, A, B, C$.

**Output**

For each test case, print "YES" if Chef can prepare at least $N$ dishes, otherwise print "NO". Print the output without quotes.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, A, B, C \leq 100$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
4
2 1 2 1
3 2 2 2
4 2 6 3
3 1 3 1
```

**Sample output**

```
YES
NO
YES
NO
```

<details><summary>Explanation</summary>

**Test case $1$**: Chef prepares one dish of the first type using one fruit and one vegetable and another dish of the second type using one vegetable and one fish.

**Test case $2$**: Chef prepares two dishes of the first type using two fruit and two vegetable. Now all the vegetables are exhausted, hence he can't prepare any other dishes.

**Test case $3$**: Chef can prepare a total of $5$ dishes, two dishes of the first type and three dishes of the second type.

</details>

## Approach

Both dish types consume **one vegetable** each; they differ only in the second ingredient, a fruit or a fish. That asymmetry is the whole problem.

Two limits apply:

- **Vegetables are shared.** Every dish needs one, so at most $B$ dishes can be made however the types are mixed.
- **Fruits and fish are interchangeable in aggregate.** Each dish needs exactly one of them, and Chef may freely choose which type to cook, so together they support at most $A + C$ dishes.

The maximum is therefore

$$\min(B,\ A + C)$$

and Chef succeeds when that reaches $N$.

Recognising that $A$ and $C$ **add** rather than each capping separately is the key step. Chef is not forced into a fixed ratio of the two dish types, so a shortage of fruit is covered by fish. Sample case 3 shows it: $A = 2$ and $C = 3$ give $5$ possible second ingredients, comfortably covering $N = 4$, with vegetables at $6$ not binding.

Sample case 2 is vegetable-bound: $A + C = 4$ would allow four dishes, but only $2$ vegetables exist, so just $2$ are possible against a required $3$.

Sample case 4 is the mirror case, bound by $A + C = 2$ while vegetables are plentiful at $3$. Dropping either term of the `min` fails one of these two.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, a, b, c = map(int, data[1 + 4 * i:5 + 4 * i])
        # Every dish takes one vegetable plus either a fruit or a fish.
        out.append("YES" if min(b, a + c) >= n else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/greedy/TWODISH.md](../docs/greedy/TWODISH.md)
