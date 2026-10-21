# 212. Count Substrings

> [`CSUB`](https://www.codechef.com/problems/CSUB) &middot; difficulty **1330** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Counting pairs from a tally |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Given a string **S** consisting of only **1s** and **0s**, find the number of substrings which start and end both in **1**.

In this problem, a substring is defined as a sequence of continuous characters **S_i, S_i+1, ..., S_j** where **1 ≤ i ≤ j ≤ N**.

**Input**

First line contains **T**, the number of testcases. Each testcase consists of **N**(the length of string) in one line and string in second line.

**Output**

For each testcase, print the required answer in one line.

**Constraints**

- **1** ≤ **T** ≤ **10^5**

- **1** ≤ **N** ≤ **10^5**

- Sum of  **N ** over all testcases ≤ **10^5**

## Constraints

- 1 ≤ T ≤ 10^5
- 1 ≤ N ≤ 10^5
- Sum of  N  over all testcases ≤ 10^5

## Sample

**Sample input**

```
2
4
1111
5
10001
```

**Sample output**

```
10
3
```

<details><summary>Explanation</summary>

**Test case $1$:** All substrings of this string start and end with `1`. The substrings are $\{ 1, 1, 1, 1, 11, 11, 11, 111, 111, 1111 \}$. The total count of these substrings is $10$.

**Test case $2$:** Three substrings of this string start and end with `1`. These are $\{1, 1, 10001\}$.

</details>

## Approach

A substring that starts and ends with `1` is determined entirely by **which two `1`s** sit at its ends — everything between them is carried along automatically. So the characters in the middle are irrelevant, and only the count of `1`s matters.

If there are $c$ ones, a valid substring is a choice of a start and an end from among them, with the start no later than the end. That is $\binom{c}{2}$ choices of two distinct positions, plus $c$ single-character substrings where both ends coincide:

$$\binom{c}{2} + c = \frac{c(c+1)}{2}$$

Including the single-character case is the detail to get right. The problem defines a substring with $i \leq j$, so a lone `1` counts. Sample case 2, `10001`, has $c = 2$ and the answer $3$ — the two single `1`s plus the whole string — rather than the $1$ a strict-pairs reading would give.

Sample case 1, `1111`, gives $4 \cdot 5 / 2 = 10$, which is every pair of positions including the degenerate ones.

Counting the `1`s is $O(N)$ and the arithmetic is $O(1)$; enumerating substrings directly would be $O(N^2)$ and far too slow at $N = 10^5$.

The result reaches about $5 \times 10^9$ when every character is a `1`, which **overflows a signed 32-bit integer** — worth noting for a C solution, though Python is unbothered.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        # data[pos] is N, which Python does not need.
        s = data[pos + 1]
        pos += 2
        c = s.count(b"1")
        # Choose any two 1s as the ends, plus the single-character cases.
        out.append(str(c * (c + 1) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Length-one substrings count**, which is why the formula is $c(c+1)/2$ and not $\binom{c}{2}$: each single `1` is itself a substring beginning and ending with `1`.
- **No `1`s at all** → $0$, which the formula gives with no special case.
- **The positions of the `1`s are irrelevant**, only how many there are: `10001` and `11000` both answer $3$.
- **A single `1`** → exactly $1$.
- **$c$ up to $10^5$** puts $c^2$ near $10^{10}$, past 32-bit signed.
- **$N$ is supplied but unused** in Python, so its token must still be consumed or the next case's string is misread.

## Dry run

| $S$ | count of `1` | $c(c+1)/2$ | substrings |
|---|---:|---:|---|
| `1111` | 4 | `10` | all $\binom{4}{2} = 6$ pairs plus $4$ singles |
| `10001` | 2 | `3` | `1`, `1`, `10001` |

---

Same problem grouped by topic: [../docs/combinatorics/CSUB.md](../docs/combinatorics/CSUB.md)
