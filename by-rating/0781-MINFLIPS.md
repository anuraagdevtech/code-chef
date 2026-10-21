# 781 &middot; Minimum number of Flips

> CodeChef problem code [`MINFLIPS`](https://www.codechef.com/problems/MINFLIPS) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Feasibility by parity, then distance to the target count |
| **CodeChef tags** | `Mathematics`, `Basic Programming Concepts`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/arrays/MINFLIPS.md](../docs/arrays/MINFLIPS.md)

## Question

Chef has an array $A$ of length $N$ consisting of $1$ and $-1$ only.

In one operation, Chef can choose any index $i$ $(1\le i \le N)$ and multiply the element $A_i$ by $-1$.

Find the **minimum** number of operations required to make the sum of the array equal to $0$. Output `-1` if the sum of the array cannot be made $0$.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case consists of a single integer $N$ denoting the length of the array.
- Second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

**Output**

For each test case, output the minimum number of operations to make the sum of the array equal to $0$. Output `-1` if it is not possible to make the sum equal to $0$.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 1000$
- $A_i = 1$ or $A_i = -1$

## Sample

**Sample input**

```
4
4
1 1 1 1
5
1 -1 1 -1 1
6
1 -1 -1 1 1 1
2
1 -1
```

**Sample output**

```
2
-1
1
0
```

<details><summary>Explanation</summary>

**Test case $1$:** The minimum number of operations required is $2$. In the first operation, change $A_3$ from $1$ to $-1$. Similarly, in the second operation, change $A_4$ from $1$ to $-1$. Thus, the sum of the final array is $1+1-1-1=0$.

**Test case $2$:** It can be proven that the sum of the array cannot be made equal to zero by making any number of operations.

**Test case $3$:** We can change $A_1$ from $1$ to $-1$ in one operation. Thus, the sum of the array becomes $-1-1-1+1+1+1=0$.

**Test case $4$:** The sum of the array is already zero. Thus we do not need to make any operations.

</details>

## Approach

The array holds only $+1$ and $-1$. If $p$ of them are $+1$ and $m$ are $-1$, the sum is $p - m$, so a sum of zero requires $p = m = N/2$.

**Feasibility first.** That is only possible when $N$ is even. For odd $N$ the sum of an odd number of odd values is odd and can never be zero, so the answer is $-1$ — sample case 2, with $N = 5$.

**Then the cost.** Each flip turns a $+1$ into a $-1$ or the reverse, changing $p$ by exactly one. Starting at $p$ and needing $N/2$, the minimum number of flips is

$$\left|\,p - \frac{N}{2}\,\right|$$

Every flip moves $p$ one step toward the target, and no flip moves it more, so this bound is both necessary and achievable — flip the surplus majority elements and stop.

The absolute value covers both directions: there may be too many $+1$s or too many $-1$s. Sample case 1 has $p = 4$ against a target of $2$, needing $2$ flips; sample case 3 has $p = 4$ against a target of $3$, needing $1$.

Sample case 4 is already balanced, giving $0$ — the formula handles it without a special case.

A neat equivalent is $|{\rm sum}|/2$, since the sum is $2p - N$; dividing the imbalance by two gives the same count, because each flip shifts the sum by $2$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        vals = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        if n % 2:
            out.append("-1")          # an odd count can never sum to zero
            continue
        plus = sum(1 for v in vals if v == b"1")
        # Each flip moves the +1 count by exactly one.
        out.append(str(abs(plus - n // 2)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
