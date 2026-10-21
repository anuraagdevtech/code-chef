# 608 &middot; Minimum Cars required

> CodeChef problem code [`MINCARS`](https://www.codechef.com/problems/MINCARS) &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ceiling division |
| **CodeChef tags** | `Mathematics`, `Basic Math`, `Integer Division`, `Arithmetic` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/MINCARS.md](../docs/basic-math/MINCARS.md)

## Question

A single car can accommodate at most $4$ people.

$N$ friends want to go to a restaurant for a party. Find the **minimum** number of cars required to accommodate all the friends.

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer $N$ - denoting the number of friends.

**Output**

For each test case, output the minimum number of cars required to accommodate all the friends.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 1000$

## Sample

**Sample input**

```
4
4
2
7
98
```

**Sample output**

```
1
1
2
25
```

<details><summary>Explanation</summary>

**Test Case $1$:** There are only $4$ friends and a single car can accommodate $4$ people. Thus, only $1$ car is required.

**Test Case $2$:** There are only $2$ friends and a single car can accommodate $4$ people. Thus, only $1$ car is required

**Test Case $3$:** There are $7$ friends and $2$ cars can accommodate $8$ people. Thus, $2$ cars are required.

</details>

## Approach

A car seats at most $4$ people and $N$ friends must all travel, so the leftover group of fewer than four still needs a car of its own:

$$\left\lceil \frac{N}{4} \right\rceil$$

computed in integers as `(n + 3) // 4`.

This is the third ceiling-division problem in the set — after the subscriptions and the pizzas — and the repetition is deliberate. The recognisable signature is *"items have a fixed capacity, everyone must be served, partial units round up"*. Contrast it with the CRED-coins problem, where the leftover was simply wasted and the division floored instead. Deciding which way the remainder pushes is the entire decision.

The identity $\lceil n/k \rceil = \lfloor (n + k - 1)/k \rfloor$ keeps everything in integer arithmetic, so there is no float and no `math.ceil`.

Sample case 4 is a good check that the formula does not overshoot on a clean division's neighbour: $N = 98$ gives $(98 + 3)//4 = 25$ cars, carrying $100$ seats for $98$ people, while $N = 4$ gives exactly $1$ rather than $2$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Everyone must travel, so a partial carload still needs a whole car.
        out.append(str((n + 3) // 4))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
