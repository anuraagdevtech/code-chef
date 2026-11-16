[&larr; 635. Valid String](635-VSTRING.md) &middot; [Index](README.md) &middot; [637. Partition It &rarr;](637-PARPERM.md)

# 636. Chef and insomnia

> [`CHINSM`](https://www.codechef.com/problems/CHINSM) &middot; difficulty **2197** &middot; time limit **2s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Sliding window whose left end jumps past the latest bad partner |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Integer Factorisation`, `Algorithms`, `Constructive`, `Queries`, `Divisors`, `ad-hoc`, `Range Minimum Queries` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(V \log V + N \cdot \tau(V))$, $V$ the largest value |
| **Space** | $O(V \log V)$ for the divisor lists |

## Question

Chef sometimes suffers from insomnia. During sleepless nights, he often plays this game: He creates an array **A** of **N** integers and also decides one integer **K**. After that, he tries to count the number of non-empty contiguous subsequences (subsegments) of **A**, such that there are no bad pairs of integers in this subsegment. A pair **(x, y)** of integers is called bad if **x** is situated to the left of **y** in the array and **x mod y = K**. Finally, before going to sleep, Chef wrote down the answer on a sheet of paper. Sadly, he has forgotten it this morning and want your help regarding that.

**Input**

- The first line contains two integers - **N** and **K**.

- Second line contains **N** integers - **A_1**, **A_2** ... **A_N** - separated by spaces, denoting the array **A**.

**Output**

A single line containing an integer - the answer to the problem.

**Constraints**

- 1 ≤ **N**, **A_i** ≤ 10^5

- 0 ≤ **K** ≤ 10^5

**Subtasks**

- Subtask 1: **N** ≤ 100 (15 points)

- Subtask 2: **N** ≤ 1000 (15 points)

- Subtask 3: **K** = 0 (10 points)

- Subtask 4: Original constraints (60 points)

## Constraints

- 1 ≤ N, A_i ≤ 10^5
- 0 ≤ K ≤ 10^5

## Sample

**Sample input**

```
3 2
5 3 1
```

**Sample output**

```
4
```

## Approach

Count subsegments by their right end: for each $i$, find the smallest left end such that the segment contains no bad pair; all later left ends are fine too, so $i$ contributes $i - \text{left} + 1$. The left end only moves right.

When a new element $y = A_i$ arrives, the new bad pairs are those with $y$ on the right: earlier $x$ with $x \bmod y = K$. This needs $y > K$, and then either $x = K$, or $x > K$ and $y$ divides $x - K$. The window has to start after the latest such $x$.

So maintain `last[d]`: the latest index of an element $x > K$ such that $d$ divides $x - K$ (only for $d > K$), and separately the latest index of an element equal to $K$. On arrival of $y > K$ move the left end past both. After counting, register the new element itself: if it equals $K$ update the special index, and if it exceeds $K$ set `last[d] = i` for every divisor $d > K$ of $y - K$. Divisor lists for all needed numbers are built with a harmonic sieve.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    n = next(tokens)
    remainder = next(tokens)
    values = [next(tokens) for _ in range(n)]
    limit = max(values)
    divisors = [[] for _ in range(max(1, limit - remainder + 1))]
    for divisor in range(remainder + 1, limit - remainder + 1):
        for v in range(divisor, limit - remainder + 1, divisor):
            divisors[v].append(divisor)
    last = [-1] * (limit + 1)
    special = -1
    left = 0
    total = 0
    for i, value in enumerate(values):
        if value > remainder:
            left = max(left, last[value] + 1, special + 1)
        total += i - left + 1
        if value == remainder:
            special = i
        elif value > remainder:
            for divisor in divisors[value - remainder]:
                last[divisor] = i
    print(total)


if __name__ == "__main__":
    main()
```

## Edge cases

- An element $y \le K$ can never be the right member of a bad pair.
- $x = K$ pairs with every later $y > K$, which is why it is tracked separately.
- Only divisors larger than $K$ are stored - smaller ones can never be a valid $y$.
- The number of subsegments can reach about $N^2 / 2$.

## Dry run

`A = [5, 3, 1]`, `K = 2`.

- $i = 1$, value 5: window `[1, 1]`, count 1. Register: $5 - 2 = 3$ has the divisor 3 (> 2), so `last[3] = 1`.
- $i = 2$, value 3: `last[3] = 1`, so the window must start at 2 (indeed $5 \bmod 3 = 2$). Count 1.
- $i = 3$, value 1: not larger than $K$, window stays `[2, 3]`. Count 2.

Answer 4.

---

Same problem grouped by topic: [../docs/number-theory/CHINSM.md](../docs/number-theory/CHINSM.md)
