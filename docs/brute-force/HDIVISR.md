# 110. Highest Divisor

> CodeChef problem code [`HDIVISR`](https://www.codechef.com/problems/HDIVISR) &middot; difficulty **860** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Brute Force |
| **Technique** | Searching a small range downward |
| **Time** | $O(1)$ — at most 10 divisibility tests |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

You are given an integer $N$. Find the largest integer between $1$ and $10$ (inclusive) which divides $N$.

**Input**
The first and only line of the input contains a single integer $N$.

**Output**
Print a single line containing one integer ― the largest divisor of $N$ between $1$ and $10$.

**Constraints**
- $2 \leq N \leq 1,000$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $2 \leq N \leq 1,000$

## Sample

**Sample 1 input**

```
91
```

**Sample 1 output**

```
7
```

<details><summary>Explanation</summary>

The divisors of $91$ are $1, 7, 13, 91$, out of which only $1$ and $7$ are in the range $[1, 10]$. Therefore, the answer is $\max(1, 7) = 7$.

</details>

**Sample 2 input**

```
24
```

**Sample 2 output**

```
8
```

<details><summary>Explanation</summary>

The divisors of $24$ are $1, 2, 3, 4, 6, 8, 12, 24$, out of which $1, 2, 3, 4, 6, 8$ are in the range $[1, 10]$. Therefore, the answer is $\max(1, 2, 3, 4, 6, 8) = 8$.

</details>

## Approach

Find the largest $d$ in $[1, 10]$ dividing $N$. The search space has ten elements, so simply try them from $10$ downward and return the first that divides:

```python
next(d for d in range(10, 0, -1) if n % d == 0)
```

Counting **down** is what makes this correct with an early exit — the first hit is already the largest. Counting up would require scanning all ten and remembering the best, which is no slower here but is the version that invites an off-by-one.

The search can never fail, because $d = 1$ divides every integer. So no fallback or sentinel is needed, and `next` is safe without a default.

It is worth noticing that this is *not* the same as "the largest proper divisor capped at 10", nor does it have anything to do with the greatest common divisor of $N$ with anything. Sample case $N = 91 = 7 \times 13$ answers $7$: the divisors of $91$ are $1, 7, 13, 91$, and $7$ is the largest that fits inside the range.

For a range this small, brute force is not a compromise — it is the right answer. Factorising $N$ first would be more work for no benefit, and would still need a pass to pick the largest factor under $10$.

There is **no $T$**: the input is a single integer.

## Solution (Python)

```python
import sys


def main() -> None:
    # Single integer, no test-case count.
    n = int(sys.stdin.buffer.read().split()[0])
    # Counting down means the first divisor found is the largest; d = 1 always
    # succeeds, so the search cannot come up empty.
    print(next(d for d in range(10, 0, -1) if n % d == 0))


main()
```

## Complexity

- **Time:** $O(1)$ — at most 10 divisibility tests
- **Space:** $O(1)$

> CodeChef tags: `Algorithms`
