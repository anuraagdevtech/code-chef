# 1483 &middot; Alternating Divisibility

> CodeChef problem code [`ALTERNATEDIV`](https://www.codechef.com/problems/ALTERNATEDIV) &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Pairing k with 2k |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc`, `Observation` |
| **CodeChef top tag** | `Ad Hoc` |
| **CodeChef category** | easy |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/constructive/ALTERNATEDIV.md](../docs/constructive/ALTERNATEDIV.md)

## Question

JJ challenges the Chef to construct an array $A$ of length $N$ such that the following conditions hold:
- $A_i$ divides $A_{i + 1}$ when $i$ is odd and $1 \le i \le N - 1$
- $A_i$ does not divide $A_{i + 1}$ when $i$ is even and $1 \le i \le N - 1$
- $1 \le A_i \le 2 \cdot N$
- All $A_i$ are pairwise **distinct**

Can you help Chef complete JJ's challenge?

If multiple arrays satisfying the above conditions exist print any one of them.

It is guaranteed that under the given constraints, at least one array satisfying the above conditions exists.

**Input**

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer $N$ - the length of the array $A$ to be constructed.

**Output**

For each test case, output a single line containing $N$ space-separated integers, denoting the elements of the array $A$ you constructed.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $5 \cdot 10^5$.

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
4
1
6
```

**Sample output**

```
1 3 2 4
2
1 5 6 12 3 9
```

<details><summary>Explanation</summary>

**Test case-1:** $[1, 3, 2, 4]$ is a valid array because:
- $A_1 = 1$ divides $A_2 = 3$.
- $A_2 = 3$ does not divide $A_3 = 2$.
- $A_3 = 2$ divides $A_4 = 4$.

**Test case-3:** $[1, 5, 6, 12, 3, 9]$ is a valid array because:
- $A_1 = 1$ divides $A_2 = 5$.
- $A_2 = 5$ does not divide $A_3 = 6$.
- $A_3 = 6$ divides $A_4 = 12$.
- $A_4 = 12$ does not divide $A_5 = 3$.
- $A_5 = 3$ divides $A_6 = 9$.

</details>

## Approach

The conditions alternate: positions $(1,2), (3,4), (5,6), \ldots$ must divide, and the links between those pairs — positions $(2,3), (4,5), \ldots$ — must **not**.

So treat the array as consecutive pairs and make each pair a multiple relation. The clean choice is to put an **odd** number at each odd position and its **double** at the even position after it:

$$A_{2j-1} = 2j-1, \qquad A_{2j} = 2(2j-1) = 4j-2$$

giving $1, 2,\ 3, 6,\ 5, 10,\ 7, 14, \ldots$

Each required divisibility holds by construction. Each required **non**-divisibility holds too: the link runs from $A_{2j} = 4j-2$ to $A_{2j+1} = 2j+1$, and for $j \geq 2$ the first exceeds the second, so it cannot divide it; for $j = 1$ it is $2 \nmid 3$.

Distinctness falls out from parity: the odd positions hold odd numbers, while the even positions hold numbers of the form $4j-2$, all $\equiv 2 \pmod 4$. The two families never collide, and within each family the values strictly increase.

The bound is satisfied with room to spare. The largest value used is $N$ when $N$ is odd, and $2N - 2$ when $N$ is even — both within $2N$.

Odd $N$ simply ends on a lone odd number with no partner, which is fine since the final element has no condition after it. $N = 1$ emits a single value.

**Any valid array is accepted**, so this is judged by a checker — the sample prints `1 3 2 4` for $N = 4$ where this construction gives `1 2 3 6`, both legitimate.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Odd positions take odd values, even positions take their doubles.
        a = []
        for j in range(1, n // 2 + 1):
            a.append(2 * j - 1)
            a.append(4 * j - 2)
        if n % 2:
            a.append(n)                  # a lone odd tail has no condition
        out.append(" ".join(map(str, a)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
