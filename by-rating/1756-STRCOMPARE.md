# 1756 &middot; Compare those strings

> CodeChef problem code [`STRCOMPARE`](https://www.codechef.com/problems/STRCOMPARE) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Suffix comparison answered by one backward pass |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `Constructive`, `String`, `ad-hoc` |
| **CodeChef top tag** | `Ad Hoc` |
| **CodeChef category** | easy |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/strings/STRCOMPARE.md](../docs/strings/STRCOMPARE.md)

## Question

Chef has two strings $A$ and $B$ consisting of lowercase alphabets, each of length $N$. Help Chef in finding the number of indices $i$ $(1 \leq i \leq N)$ such that $A[i \dots N] \lt B[i \dots N]$.

- $S[i \dots N]$ denotes the suffix of string $S$ starting at index $i$, i.e. $S_iS_{i+1}$ $\dots$ $S_{N}$.
- String $S \lt$ String $T$ denotes that $S$ is lexicographically smaller than $T$. If two strings $S$ and $T$ have the same length $N$, we say that $S$ is lexicographically smaller than $T$ if there exists an index $i(1 \le i \le N)$ such that $S_1 = T_1,$ $S_2 = T_2, \ldots, S_{i-1} = T_{i-1}$ and $S_i \lt T_i$. For example, "$abc$" is lexicographically smaller than "$acd$", "$abe$", but not smaller than "$abc$", "$aac$".

**Input**

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- The first line of each test case contains $N$, denoting the length of the strings $A$ and $B$.
- The second line of each test case contains the string $A$.
- The third line of each test case contains the string $B$.

**Output**

For each test case, print a single line containing one integer -  the number of indices $i$ such that $A[i \dots N] \lt B[i\dots N]$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^6$
- The sum of $N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
2
2
ab
bb
3
aaa
aab
```

**Sample output**

```
1
3
```

<details><summary>Explanation</summary>

**Test Case $1$**:
- For $i = 1$, $A[1 \dots 2] = $ "$ab$", $B[1 \dots 2] = $ "$bb$" and lexicographically, "$ab$" $\lt$ "$bb$".
- For $i = 2$, $A[2 \dots 2] =$ "$b$", $B[2 \dots 2] = $ "$b$" and lexicographically, "$b$" $=$ "$b$".

**Test Case $2$**: For each $i \in \{1 , 2, 3\}$, $A[i \dots 3] \lt B[i \dots 3]$.

</details>

## Approach

The two suffixes $A[i..N]$ and $B[i..N]$ have the same length, so the comparison is settled by the **first position where they differ**. That makes the answers chain backwards:

$$\mathrm{less}[i] = \begin{cases} [\,A_i < B_i\,] & A_i \neq B_i \\ \mathrm{less}[i+1] & A_i = B_i \end{cases}$$

with $\mathrm{less}[N+1] = \text{false}$, since two empty suffixes are equal rather than strictly ordered. So a single right-to-left sweep decides every index in $O(1)$, and the answer is the number of true entries.

The recurrence is the whole algorithm — there is no need for suffix arrays, hashing, or any comparison beyond one character per index, which matters with $\sum N$ up to $10^6$.

Note the `false` base case: a tie all the way to the end means the suffixes are equal, and equality does not count as "less than". That is why the shorter sample answers are what they are.

For $A = \texttt{ab}$ and $B = \texttt{bb}$: position $2$ has `b` against `b`, so it inherits `false` from the empty suffix; position $1$ has `a < b`, so it is true. Answer $1$.

For $A = \texttt{aaa}$ and $B = \texttt{aab}$: position $3$ has `a < b`, true; positions $2$ and $1$ tie and inherit that truth. All three indices qualify, giving $3$ — the single difference at the very end propagates all the way left.

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
        a, b = data[pos + 1], data[pos + 2]
        pos += 3
        # Equal suffixes do not count, so the chain starts false.
        less = False
        total = 0
        for i in range(n - 1, -1, -1):
            if a[i] != b[i]:
                less = a[i] < b[i]
            total += less
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
