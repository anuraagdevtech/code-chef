[&larr; 485. Flip the Prefix](485-PREFIXFLIP.md) &middot; [Index](README.md) &middot; [487. Racing &rarr;](487-RACINGEN.md)

# 486. Optimal Denomination

> [`MINNOTES`](https://www.codechef.com/problems/MINNOTES) &middot; difficulty **1759** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Prefix and suffix GCD after one removal |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Algorithms`, `Simple Algos`, `GCD`, `Prefix Sum`, `Suffix Sum` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log V)$ per test case |
| **Space** | $O(N)$ |

## Question

You are the owner of a big company. You are so rich, that the government has allowed you to print as many notes as you want of any single value that you like. You also have peculiar behavioral traits and you often do things that look weird to a third person.

You have $N$ employees, where the $i$-th employee has salary $A_i$. You want to pay them using a denomination that you create. You are also eco-friendly and wish to save paper. So, you wish to pay them using as few notes as possible. Find out the minimum number of notes required if you can alter the salary of at most one employee to any **positive integer** that you like, and choose the positive integer value that each note is worth (called its denomination).

Each employee must receive the exact value of his/her salary and no more.

**Subtasks**
**Subtask #1 (100 points):** Original constraints

**Input**

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ integers $A_1, A_2, \ldots, A_N$, where $A_i$ is the salary of the $i$-th employee.

**Output**

For each test case, output in a single line the answer to the problem.

## Constraints

- $1 \leq T \leq 12\cdot 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases is at most $10^6$.

## Sample

**Sample input**

```
3
3
1 2 3
3
8 4 2
2
2 2
```

**Sample output**

```
4
4
2
```

<details><summary>Explanation</summary>

**Test Case $1$:** We can change the salary of the third person to $1$ and use $1$ as the denomination. So in total we need $\frac{1}{1} + \frac{2}{1} + \frac{1}{1}$ = $1 + 2 + 1$ = $4$ notes.

**Test Case $2$:** We can change the salary of the first person to $2$ and use $2$ as the denomination. So in total we need $1 + 2 + 1$ = $4$ notes.

**Test Case $3$:** We can use $2$ as the denomination and we need not change the salary of any person. So in total we need $1 + 1$ = $2$ notes.

</details>

## Approach

If employee $i$ is changed, every other salary must be divisible by the denomination. Its largest possible value is the GCD $g$ of those other salaries. Set the changed salary to $g$, which needs one note. The exact cost is $(S-A_i)/g+1$; no smaller denomination improves it.

Prefix and suffix GCDs give $g$ for every removed employee in constant many GCD calls. Minimise this cost. For one employee, choose their existing salary as the denomination and pay one note.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        if n == 1:
            out.append('1')
            continue
        prefix = [0] * (n+1)
        suffix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = gcd(prefix[i], a[i])
        for i in range(n-1, -1, -1):
            suffix[i] = gcd(suffix[i+1], a[i])
        total = sum(a)
        out.append(str(min((total-v)//gcd(prefix[i], suffix[i+1])+1 for i,v in enumerate(a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- $N=1$ must bypass the GCD of an empty array.
- The changed salary must be positive: it costs one note, not zero.
- Equal salaries already need exactly $N$ notes.

## Dry run

For salaries `[1,2,3]`, excluding `3` leaves GCD `1`. Replace `3` by `1`, requiring `1+2+1=4` notes.

---

Same problem grouped by topic: [../docs/number-theory/MINNOTES.md](../docs/number-theory/MINNOTES.md)
