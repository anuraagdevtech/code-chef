# 70. Too many items

> CodeChef problem code [`POLYBAGS`](https://www.codechef.com/problems/POLYBAGS) &middot; difficulty **738** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ceiling division |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef bought $N$ items from a shop. Although it is hard to carry all these items in hand, so Chef has to buy some polybags to store these items.

$1$ polybag can contain at most $10$ items. What is the minimum number of polybags needed by Chef?

**Input**

- The first line will contain an integer $T$ - number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer $N$ - the number of items bought by Chef.

**Output**

For each test case, output the minimum number of polybags required.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$

## Sample

**Sample input**

```
3
20
24
99
```

**Sample output**

```
2
3
10
```

<details><summary>Explanation</summary>

**Test case-1:**  Chef will require $2$ polybags. Chef can fit $10$ items in the first and second polybag each.

**Test case-2:**  Chef will require $3$ polybags. Chef can fit $10$ items in the first and second polybag each and fit the remaining $4$ items in the third polybag.

</details>

## Approach

A polybag holds at most $10$ items and every item must be carried, so the count rounds up:

$$\left\lceil \frac{N}{10} \right\rceil$$

written in integers as `(n + 9) // 10`.

This is the same capacity-and-ceiling shape as the cars, pizzas and subscriptions problems, and the signature is identical: a fixed container size, nothing may be left behind, so a partial container still costs a whole unit.

The samples cover both sides of the rounding. $N = 20$ divides exactly and needs $2$ bags, with the formula giving $(20+9)//10 = 2$ rather than overshooting to $3$ — the usual thing to check when using the $+k-1$ trick. $N = 24$ is ragged and needs $3$, the last bag holding only $4$ items. $N = 99$ needs $10$, one short of a clean $100$.

Keeping the arithmetic in integers avoids `math.ceil(n / 10)`, which converts to a float first and would start misbehaving for very large $N$ — not a risk at $N \leq 1000$, but the integer form costs nothing and always holds.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Every item must be carried, so a part-full bag still counts.
        out.append(str((n + 9) // 10))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`
