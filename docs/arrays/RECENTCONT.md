# 89. Recent contest problems

> CodeChef problem code [`RECENTCONT`](https://www.codechef.com/problems/RECENTCONT) &middot; difficulty **793** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Counting two categories in one pass |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

*CodeChef recently revamped its [practice page](https://www.codechef.com/practice) to make it easier for users to identify the next problems they should solve by introducing some new features:*
- *Recent Contest Problems - Contains only problems from the last 2 contests*
- *Separate Un-Attempted,  Attempted, and All tabs*
- *Problem Difficulty Rating - The Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience*
- *Popular Topics and Tags*

Chef has been participating regularly in rated contests but missed the last two contests due to his college exams. He now wants to solve them and so he visits the practice page to view these [problems](https://www.codechef.com/practice/recent).

Given a list of $N$ contest codes, where each contest code is either `START38` or `LTIME108`, help Chef count how many problems were featured in each of the contests.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of two lines of input.
- First line of input contains the total count of problems that appeared in the two recent contests - $N$.
- Second line of input contains the list of $N$ contest codes. Each code is either `START38` or `LTIME108`, to which each problem belongs.

**Output**

For each test case, output two integers in a single new line - the first integer should be the number of problems in `START38`, and the second integer should be the number of problems in `LTIME108`.

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 1000$
- Each of the contest codes will be either `START38` or `LTIME108`.

## Sample

**Sample input**

```
4
3
START38 LTIME108 START38
4
LTIME108 LTIME108 LTIME108 START38
2
LTIME108 LTIME108
6
START38 LTIME108 LTIME108 LTIME108 START38 LTIME108
```

**Sample output**

```
2 1
1 3
0 2
2 4
```

<details><summary>Explanation</summary>

**Test case $1$:** There are $2$ `START38`s in the input, which means that there were $2$ problems in `START38`. Similarly, there was $1$ problem in `LTIME108`.

**Test case $2$:** There is $1$ `START38` in the input, which means that there was $1$ problem in `START38`. Similarly, there were $3$ problems in `LTIME108`.

**Test case $3$:** There are no `START38`s in the input, which means that were $0$ problems in `START38`. Similarly, there were $2$ problems in `LTIME108`.

**Test case $4$:** There are $2$ `START38`s in the input, which means that there were $2$ problems in `START38`. Similarly, there were $4$ problems in `LTIME108`.

</details>

## Approach

Every code is one of exactly two values, so counting one of them determines the other. Count the `START38` entries as $s$; the `LTIME108` count is then $N - s$, with no second scan and no dictionary.

That complement trick is the point of the problem. It is the same idea as counting evens and deriving the odds in the Mahasena problem: when a set is partitioned into two classes, one counter plus the total is enough.

For a general partition into many categories, `collections.Counter` would be the tool — but here it would allocate a dictionary per test case to hold two keys, and the answer still has to be emitted in a fixed order with zeros present. Sample case 3 has no `START38` at all and must print `0 2`, which a Counter-based solution gets wrong if it iterates over observed keys rather than the known pair.

Output order is fixed by the statement: `START38` count first, then `LTIME108`, regardless of which appears first in the input. Sample case 2 leads with `LTIME108` three times yet still prints `1 3`.

The codes are compared as whole tokens. Matching on a prefix such as `S` would work for these two particular strings but is the kind of shortcut that breaks the moment a third contest code appears.

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
        codes = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # Only two categories exist, so one count determines the other.
        start = codes.count(b"START38")
        out.append(f"{start} {n - start}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Data Structures`
