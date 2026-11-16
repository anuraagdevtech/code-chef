[&larr; 494. Cybalphabit](494-CAB.md) &middot; [Index](README.md) &middot; [496. Triplets &rarr;](496-SUMQ.md)

# 495. Broken Life

> [`BRKNLIFE`](https://www.codechef.com/problems/BRKNLIFE) &middot; difficulty **1772** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Avoid advancing the subsequence matcher at question marks |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `String`, `Greedy` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given two strings $S$ and $A$ of lengths $N$ and $M$ respectively.
- String $S$ contains characters from the set $\texttt{\{?, a, b, c, d, e\}}$.
- String $A$ contains characters from the set $\texttt{\{a, b, c, d, e\}}$.

Let $S'$ denote the string formed by replacing **all** the $\texttt{?}$ in $S$ using the characters from the set $\texttt{\{a, b, c, d, e\}}$.
Construct $S'$ such that $A$ is **not** a [subsequence](https://en.wikipedia.org/wiki/Subsequence) of $S'$.

If multiple such $S'$ exist, output any. If no such $S'$ exists, print $-1$.

**Input**

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $M$ - the lengths of strings $S$ and $A$ respectively.
- The second line of each test case contains string $S$.
- The third line of each test case contains string $A$.

**Output**

For each test case, output any valid string $S'$. If no such string exists, print $-1$.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N,M \leq 10^5$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.
- Sum of $M$ over all test cases does not exceed $3 \cdot 10^5$.

## Sample

**Sample input**

```
2
4 2
?ab?
ba
4 2
a??b
ab
```

**Sample output**

```
aabe
-1
```

<details><summary>Explanation</summary>

**Test case $1$:** Replace the $\texttt{?}$ at indices $1$ and $4$ using characters $\texttt{a}$ and $\texttt{e}$ respectively. Both the characters belong to the set $\texttt{\{a, b, c, d, e\}}$.
The string $S' = \texttt{aabe}$. Note that no subsequence of $S'$ is equal to $\texttt{ba}$.

**Test case $2$:** There is no possible value of $S'$ such that $\texttt{ab}$ is not a subsequence of $S'$.

</details>

## Approach

Scan $S$ while greedily matching the longest possible prefix of $A$. A fixed character advances the matcher only when it equals the next required character. At a question mark, choose a letter different from that next required character.

Keeping the matched prefix as short as possible dominates every other choice: a smaller matched prefix cannot make completing $A$ easier. Thus if even this scan completes $A$, every replacement fails. Otherwise its constructed string is valid.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, m = int(next(tokens)), int(next(tokens))
        s = next(tokens).decode()
        a = next(tokens).decode()
        matched = 0
        result = []
        for char in s:
            if char == '?':
                char = 'b' if matched < m and a[matched] == 'a' else 'a'
            result.append(char)
            if matched < m and char == a[matched]:
                matched += 1
        out.append(''.join(result) if matched < m else '-1')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- A subsequence need not be contiguous.
- A fixed occurrence of all of $A$ already makes the task impossible.
- The replacement alphabet is only `a` through `e`.

## Dry run

For `S=?ab?`, `A=ba`, choose `a` at the first question mark. The fixed `b` matches the first target letter; choose `b` at the end to avoid matching `a`. Result `aabb` avoids `ba`.

---

Same problem grouped by topic: [../docs/greedy/BRKNLIFE.md](../docs/greedy/BRKNLIFE.md)
