# 433. XOR Equal

> [`PALINT`](https://www.codechef.com/problems/PALINT) &middot; difficulty **1731** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | XOR pairs values into two-element orbits |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Mathematics`, `Frequency Arrays`, `Bit Manipulation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given an array $A$ consisting of $N$ integers and an integer $X$. Your goal is to have as many equal integers as possible in the array. To achieve this goal, you can do the following operation:
- Choose an index $i$ $(1 \leq i \leq N)$  and set $A_i = A_i \oplus X$,  where $\oplus$ denotes the [bitwise xor operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Find the maximum number of equal integers you can have in the final array and the minimum number of operations to obtain these many equal integers.

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- Each test case contains two lines of input.
- The first line of each test case contains two space-separated integers $N, X$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

**Output**

For each test case, print a single line containing two space-separated integers - first, the maximum number of equal integers in the final array and second, the minimum number of operations to achieve these many equal integers.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $0 \leq X \leq 10^9$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases does not exceed $5 \cdot 10^5$.

**Subtasks**

**Subtask #1 (100 points):** Original constraints

## Sample

**Sample input**

```
3
3 2
1 2 3
5 100
1 2 3 4 5
4 1
2 2 6 6
```

**Sample output**

```
2 1
1 0
2 0
```

<details><summary>Explanation</summary>

**Test case $1$:** One way to obtain $2$ equal integers is to set $A_1 = A_1 \oplus 2 $ $\; = 1 \oplus 2 = 3$. So the array becomes $[3, 2, 3]$. There is no way to obtain $3$ equal integers in the final array.

**Test case $2$:** There is no way to obtain more than one equal integer.

</details>

## Approach

XOR with a fixed $X$ is an involution, so each element can only ever hold one of two values, $a$ or $a \oplus X$. The values therefore split into **orbits** $\{a,\, a \oplus X\}$, and elements in different orbits can never be made equal.

So for a target value $v$, every element already equal to $v$ stays put and every element equal to $v \oplus X$ needs exactly one operation:

$$\text{count}(v) = \mathrm{cnt}[v] + \mathrm{cnt}[v \oplus X], \qquad \text{ops}(v) = \mathrm{cnt}[v \oplus X]$$

Both $v$ and $v \oplus X$ give the same count, so per orbit the best is

$$\text{count} = \mathrm{cnt}[a] + \mathrm{cnt}[a \oplus X], \qquad \text{ops} = \min\bigl(\mathrm{cnt}[a],\ \mathrm{cnt}[a \oplus X]\bigr)$$

— flip whichever side is smaller. Scanning the distinct values and taking the largest count, breaking ties by fewest operations, answers both questions at once.

The case $X = 0$ needs care: then $a \oplus X = a$ and the formula would double-count. With $X = 0$ no operation changes anything, so the answer is the largest frequency with $0$ operations.

The samples show each situation. $A = [1,2,3]$ with $X = 2$ has the orbit $\{1,3\}$ containing two elements, so two can be made equal with one flip. $A = [1,\ldots,5]$ with $X = 100$ has every orbit partner outside the array, so nothing can be merged: `1 0`. And $A = [2,2,6,6]$ with $X = 1$ has orbits $\{2,3\}$ and $\{6,7\}$ with the partners absent, so the best is the two existing twos at no cost.

## Solution

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        count = Counter(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        if x == 0:
            out.append(f"{max(count.values())} 0")
            continue
        best = (0, 0)
        for a, c in count.items():
            other = count.get(a ^ x, 0)
            # Either side of the orbit can be the target; flip the smaller one.
            cand = (c + other, -min(c, other))
            if cand > best:
                best = cand
        out.append(f"{best[0]} {-best[1]}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/bit-manipulation/PALINT.md](../docs/bit-manipulation/PALINT.md)
