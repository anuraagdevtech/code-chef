[&larr; 641. Mahesh and his lost array](641-ANUMLA.md) &middot; [Index](README.md) &middot; [643. Yet Another Crossover Episode &rarr;](643-DIANE.md)

# 642. String Operations

> [`STROPERS`](https://www.codechef.com/problems/STROPERS) &middot; difficulty **2220** &middot; time limit **2.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | A complete invariant - length, ones, and zeros seen after an odd number of ones |
| **CodeChef tags** | `Data Structures`, `Sets`, `Algorithms`, `Constructive`, `Unordered Sets`, `ad-hoc`, `Observation` |
| **Complexity class** | Quadratic $O(n^2)$ |
| **Time** | $O(N^2)$ per test case |
| **Space** | $O(N^2)$ for the set of classes |

## Question

Two strings $A$ and $B$ are *equivalent* (denoted by $A \sim B$) if they have the same lengths and $A$ can be transformed into $B$ by performing the following operation zero or more times: choose a substring of $A$ which contains '1' an even number of times and reverse this substring.

You are given a binary string $S$. Find the number of different equivalence classes of the substrings of this string. In other words, find the smallest possible size of a set $\mathcal{C}$ of binary strings with the following property: for each non-empty string $R$ which is a substring of $S$ (including $S$ itself), there is a string $X \in \mathcal{C}$ such that $R \sim X$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$ with length $N$.

**Output**
For each test case, print a single line containing one integer ― the number of equivalence classes among the substrings of the given string.

**Constraints**
- $1 \le T \le 10$
- $1 \le N \le 1,000$
- $S$ contains only characters '0' and '1'

**Subtasks**
**Subtask #1 (10 points):** $N \le 10$

**Subtask #2 (90 points):** original constraints

## Constraints

- $1 \le T \le 10$
- $1 \le N \le 1,000$
- $S$ contains only characters '0' and '1'

## Sample

**Sample input**

```
10
00000
10001
10101
01111
11001
01101
10110
10010
10111
11001
```

**Sample output**

```
5
11
8
9
12
10
10
11
11
12
```

## Approach

Describe a binary string by the zeros between its ones: with $m$ ones there are $m + 1$ gaps. Call a zero *odd* if an odd number of ones precede it.

Reversing a substring that contains an even number of ones keeps three things fixed: the length, the number of ones, and the number of odd zeros. Inside the reversed part the parity of "ones before me" is preserved for every zero, because the part contains an even number of ones in total.

Conversely these three numbers determine the class. Reversing a substring that starts just after some zeros, spans exactly two ones and ends before some zeros moves zeros between two gaps of the same parity, and reversing a block of zeros with nothing else is trivial; with such moves any distribution of the zeros over the even gaps and over the odd gaps can be reached. So two strings are equivalent exactly when (length, ones, odd zeros) agree.

Enumerate all substrings by fixing the left end and extending the right end, updating the three numbers in $O(1)$, and count the distinct triples.

## Solution

```python
import sys


def solve(tokens):
    text = next(tokens).decode()
    n = len(text)
    seen = set()
    base = n + 1
    for left in range(n):
        ones = odd_zeros = 0
        for right in range(left, n):
            if text[right] == '1':
                ones += 1
            elif ones & 1:
                odd_zeros += 1
            seen.add(((right - left + 1) * base + ones) * base + odd_zeros)
    return str(len(seen))


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- A string with no ones has no odd zeros; its class is determined by its length.
- Different substrings with the same triple are counted once.
- The triple is packed into one integer to keep the set compact.
- The total length over the test cases allows the quadratic enumeration.

## Dry run

`S = 101`.

| substring | length | ones | odd zeros |
|---|---:|---:|---:|
| `1` (twice) | 1 | 1 | 0 |
| `0` | 1 | 0 | 0 |
| `10` | 2 | 1 | 1 |
| `01` | 2 | 1 | 0 |
| `101` | 3 | 2 | 1 |

Five distinct triples, so the answer is 5.

---

Same problem grouped by topic: [../docs/strings/STROPERS.md](../docs/strings/STROPERS.md)
