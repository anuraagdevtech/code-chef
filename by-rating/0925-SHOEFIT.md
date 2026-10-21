# 925 &middot; Shoe Fit

> CodeChef problem code [`SHOEFIT`](https://www.codechef.com/problems/SHOEFIT) &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Presence of both values in a small collection |
| **CodeChef tags** | `Special`, `Basic Programming Concepts`, `Algorithms`, `Case work`, `Conditional Statements`, `Brute Force` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/conditionals-case-work/SHOEFIT.md](../docs/conditionals-case-work/SHOEFIT.md)

## Question

You have three shoes of the same size lying around. Each shoe is either a left shoe (represented using $0$) or a right shoe (represented using $1$). Given $A$, $B$, $C$, representing the information for each shoe, find out whether you can go out now, wearing one left shoe and one right shoe.

**Input**

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, three integers $A$, $B$, $C$.

**Output**

For each test case, output in a single line the answer: $1$ if it's possible to go out with a pair of shoes and $0$ if not.

## Constraints

- $1 \leq T \leq 8$
- $0 \leq A, B, C \leq 1$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
0 0 0
0 1 1
1 0 1
```

**Sample output**

```
0
1
1
```

<details><summary>Explanation</summary>

**Test Case $1$:** Since there's no right shoe, it's not possible to go out with a pair of shoes.

**Test Case $2$:** It's possible to go out with a pair of shoes wearing the first and last shoes.

**Test Case $3$:** It's possible to go out with a pair of shoes wearing the first and second shoes.

</details>

## Approach

Three shoes, each a left ($0$) or a right ($1$). Going out needs **one of each**, so the question is whether both values appear among $A, B, C$.

The neat way to test this on $0/1$ values is to look at the sum $s = A + B + C$:

- $s = 0$ means all three are left shoes — no right shoe, so no pair.
- $s = 3$ means all three are right shoes — no left shoe, so no pair.
- $s = 1$ or $s = 2$ means a mix, so a pair exists.

Hence the answer is $1$ exactly when $0 < s < 3$.

The pigeonhole reasoning is worth seeing: with three items and two categories, having at least one of each is the same as *not* having all three in one category. Those are the only two bad cases, and both are detected by the sum hitting an extreme.

Equivalently, `len({a, b, c}) == 2` asks the question directly — a set of $0/1$ values has size $2$ precisely when both appear. Either formulation beats enumerating the eight possibilities.

Sample case 1 is all-left and fails; cases 2 and 3 each have a mix and succeed. Note that having *two* right shoes and one left is fine — only one pair is needed, and the spare is simply unused.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = sum(map(int, data[1 + 3 * i:4 + 3 * i]))
        # All-left (sum 0) or all-right (sum 3) are the only failures.
        out.append("1" if 0 < s < 3 else "0")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
